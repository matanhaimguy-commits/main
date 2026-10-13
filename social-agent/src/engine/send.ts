import { randomBytes } from 'node:crypto';
import type { Business } from '../config/schema.js';
import {
  attachLinkToSend,
  claimSend,
  completeSend,
  createLink,
  insertMessage,
  linkSendToContact,
  markOutbound,
  pauseSending,
  sendingPausedUntil,
  updateComment,
  upsertContact,
  type Contact,
  type MessageRow,
  type SendClaim,
} from '../db/repo.js';
import { MetaApiError, type MetaApi } from '../meta/client.js';
import { describeMessage, toMetaMessage, type OutboundMessage } from '../meta/messages.js';
import type { CommentEvent } from '../meta/webhook.js';
import type { Deps } from './deps.js';

export type SendOutcome =
  | { status: 'sent'; sendId: number; messageId?: string; recipientId?: string }
  | { status: 'dry_run'; sendId: number }
  | { status: 'failed' | 'unknown'; sendId: number; category: string; error: string }
  | { status: 'blocked'; sendId: number; reason: string }
  | { status: 'duplicate' };

export const delivered = (o: SendOutcome): o is Extract<SendOutcome, { status: 'sent' | 'dry_run' }> =>
  o.status === 'sent' || o.status === 'dry_run';

/**
 * The only path to Meta's send APIs.
 * 1. Claim the idempotency key in the ledger BEFORE calling Meta. A key can be claimed once,
 *    ever, so a crash, a webhook redelivery or a second worker can never send twice.
 * 2. Make exactly one call. Never retry: a duplicate DM to a real person is worse than a
 *    failure in the log. A timeout is recorded as "unknown" and left alone.
 */
export async function performSend(
  deps: Deps,
  b: Business,
  claim: Omit<SendClaim, 'business'>,
  call: (api: MetaApi) => Promise<{ message_id?: string; recipient_id?: string; id?: string }>,
): Promise<SendOutcome> {
  const { sql, log } = deps;
  const sendId = await claimSend(sql, { ...claim, business: b.slug });
  if (sendId === undefined) {
    log.info('send skipped: already attempted', { business: b.slug, key: claim.key });
    return { status: 'duplicate' };
  }
  if (!deps.isLive(b)) {
    await completeSend(sql, sendId, { status: 'dry_run' });
    log.info('DRY RUN: would send', { business: b.slug, kind: claim.kind, key: claim.key, request: claim.request });
    return { status: 'dry_run', sendId };
  }
  const pausedUntil = await sendingPausedUntil(sql, b.slug);
  if (pausedUntil) {
    const reason = `sending paused until ${pausedUntil.toISOString()}`;
    await completeSend(sql, sendId, { status: 'skipped', errorMessage: reason });
    return { status: 'blocked', sendId, reason };
  }
  const api = b.meta.page_id ? deps.metaFor(b) : undefined;
  if (!api) {
    const error = b.meta.page_id ? 'no access token for this Page (connect it in /admin/connect)' : 'no Facebook Page connected';
    await completeSend(sql, sendId, { status: 'failed', errorMessage: error });
    await deps.alert({ key: `token-missing:${b.slug}`, text: `⚠️ ${b.name}: ${error}. Nothing can be sent.` });
    return { status: 'failed', sendId, category: 'token', error };
  }

  try {
    const res = await call(api);
    await completeSend(sql, sendId, { status: 'sent', messageId: res.message_id ?? res.id, recipientId: res.recipient_id });
    return { status: 'sent', sendId, messageId: res.message_id ?? res.id, recipientId: res.recipient_id };
  } catch (err) {
    if (err instanceof MetaApiError) {
      const category = err.category;
      await completeSend(sql, sendId, {
        status: 'failed',
        errorCode: err.code,
        errorSubcode: err.subcode,
        errorMessage: `${category}: ${err.message}`,
      });
      log.warn('send failed', { business: b.slug, key: claim.key, category, code: err.code, subcode: err.subcode, error: err.message });
      await alertForFailure(deps, b, category, err);
      return { status: 'failed', sendId, category, error: err.message };
    }
    const error = (err as Error).message;
    await completeSend(sql, sendId, { status: 'unknown', errorMessage: `outcome unknown, not retried: ${error}` });
    log.error('send outcome unknown', { business: b.slug, key: claim.key, error });
    await deps.alert({
      key: `send-unknown:${b.slug}`,
      text: `⚠️ ${b.name}: a send to Meta timed out or the connection dropped (${error}). It may or may not have arrived. It was NOT retried. Check the sends ledger.`,
      cooldownMinutes: 30,
    });
    return { status: 'unknown', sendId, category: 'network', error };
  }
}

async function alertForFailure(deps: Deps, b: Business, category: string, err: MetaApiError) {
  const detail = `(${err.code ?? '?'}${err.subcode ? `/${err.subcode}` : ''}: ${err.message})`;
  switch (category) {
    case 'token':
      return deps.alert({
        key: `token:${b.slug}`,
        text: `🚨 ${b.name}: Meta rejected the Page access token ${detail}. All sends will fail until you mint a new token.`,
      });
    case 'spam_block': {
      const until = new Date(deps.now().getTime() + 24 * 3_600_000);
      await pauseSending(deps.sql, b.slug, until, `Meta spam block ${detail}`);
      return deps.alert({
        key: `spam:${b.slug}`,
        text: `🚨 ${b.name}: Meta flagged our messages as spam ${detail}. All sending is paused for 24 hours. Review keywords and message copy.`,
      });
    }
    case 'permission':
      return deps.alert({ key: `perm:${b.slug}`, text: `⚠️ ${b.name}: permission error from Meta ${detail}. Check app review / permissions.` });
    case 'rate_limit':
      return deps.alert({ key: `rate:${b.slug}`, text: `⚠️ ${b.name}: Meta rate limit hit ${detail}.`, cooldownMinutes: 120 });
    case 'unknown':
    case 'invalid_request':
      return deps.alert({ key: `sendfail:${b.slug}:${err.code}`, text: `⚠️ ${b.name}: send failed ${detail}.`, cooldownMinutes: 120 });
    default:
      // already_replied, comment_ineligible, outside_window, user_unavailable, thread_owner:
      // expected, harmless, and visible in the ledger.
      return;
  }
}

/** Swaps button URLs for /r/<token> redirects when click tracking is on for this business. */
async function trackLinks(
  deps: Deps,
  b: Business,
  msg: OutboundMessage,
  ctx: { contactId?: number; funnelId?: string },
): Promise<{ msg: OutboundMessage; token?: string }> {
  const base = deps.env.PUBLIC_URL?.replace(/\/$/, '');
  if (!b.track_clicks || !base || !msg.button || !('url' in msg.button)) return { msg };
  const token = randomBytes(9).toString('base64url');
  await createLink(deps.sql, { token, business: b.slug, contactId: ctx.contactId, funnelId: ctx.funnelId, url: msg.button.url });
  return { msg: { ...msg, button: { ...msg.button, url: `${base}/r/${token}` } }, token };
}

export interface DmMeta {
  key: string;
  source: Extract<MessageRow['source'], 'funnel' | 'ai' | 'system'>;
  funnelId?: string;
  step: string;
}

/** A normal DM to someone inside the 24h window. */
export async function sendDm(deps: Deps, b: Business, contact: Contact, original: OutboundMessage, meta: DmMeta): Promise<SendOutcome> {
  const { msg, token } = await trackLinks(deps, b, original, { contactId: contact.id, funnelId: meta.funnelId });
  const payload = toMetaMessage(msg, contact.platform);
  const outcome = await performSend(
    deps,
    b,
    {
      platform: contact.platform,
      kind: 'message',
      key: meta.key,
      funnelId: meta.funnelId,
      step: meta.step,
      contactId: contact.id,
      recipientId: contact.external_id,
      request: payload,
    },
    (api) => api.sendMessage({ pageId: b.meta.page_id!, recipient: { id: contact.external_id }, message: payload }),
  );
  if (delivered(outcome)) {
    const mid = outcome.status === 'sent' && outcome.messageId ? outcome.messageId : `dry:${outcome.sendId}`;
    await insertMessage(deps.sql, {
      contactId: contact.id,
      direction: 'out',
      source: meta.source,
      mid,
      text: describeMessage(original),
      sendId: outcome.sendId,
      at: deps.now(),
    });
    await markOutbound(deps.sql, contact.id, deps.now());
    if (token) await attachLinkToSend(deps.sql, token, outcome.sendId);
  }
  return outcome;
}

/**
 * The private reply to a comment: one per comment, ever, across every app. On success Meta
 * returns the person's messaging ID, which becomes the contact.
 */
export async function sendPrivateReply(
  deps: Deps,
  b: Business,
  comment: CommentEvent,
  original: OutboundMessage,
  meta: Omit<DmMeta, 'key'> & { contactSource: string },
): Promise<{ outcome: SendOutcome; contact?: Contact }> {
  const { msg, token } = await trackLinks(deps, b, original, { funnelId: meta.funnelId });
  const payload = toMetaMessage(msg, comment.platform);
  const outcome = await performSend(
    deps,
    b,
    {
      platform: comment.platform,
      kind: 'private_reply',
      key: `private_reply:${comment.platform}:${comment.commentId}`,
      funnelId: meta.funnelId,
      step: meta.step,
      commentId: comment.commentId,
      request: payload,
    },
    (api) => api.sendMessage({ pageId: b.meta.page_id!, recipient: { comment_id: comment.commentId }, message: payload }),
  );
  if (!delivered(outcome)) return { outcome };

  const externalId = (outcome.status === 'sent' && outcome.recipientId) || comment.authorId;
  if (!externalId) return { outcome };
  const contact = await upsertContact(deps.sql, {
    business: b.slug,
    platform: comment.platform,
    externalId,
    username: comment.platform === 'instagram' ? comment.authorName : undefined,
    name: comment.platform === 'facebook' ? comment.authorName : undefined,
    source: meta.contactSource,
  });
  await linkSendToContact(deps.sql, outcome.sendId, contact.id);
  await updateComment(deps.sql, comment.platform, comment.commentId, { contact_id: contact.id });
  await insertMessage(deps.sql, {
    contactId: contact.id,
    direction: 'in',
    source: 'comment',
    mid: `comment:${comment.commentId}`,
    text: comment.text,
    payload: { post_id: comment.postId },
    at: comment.createdAt,
  });
  const mid = outcome.status === 'sent' && outcome.messageId ? outcome.messageId : `dry:${outcome.sendId}`;
  await insertMessage(deps.sql, {
    contactId: contact.id,
    direction: 'out',
    source: meta.source,
    mid,
    text: describeMessage(original),
    sendId: outcome.sendId,
    at: deps.now(),
  });
  await markOutbound(deps.sql, contact.id, deps.now());
  if (token) await attachLinkToSend(deps.sql, token, outcome.sendId);
  return { outcome, contact };
}

export function sendPublicReply(deps: Deps, b: Business, comment: CommentEvent, text: string, step: string, funnelId?: string) {
  return performSend(
    deps,
    b,
    {
      platform: comment.platform,
      kind: 'public_reply',
      key: `public_reply:${comment.platform}:${comment.commentId}`,
      funnelId,
      step,
      commentId: comment.commentId,
      request: { message: text },
    },
    (api) => api.replyToComment(comment.platform, comment.commentId, text),
  );
}

export function hideComment(deps: Deps, b: Business, comment: CommentEvent) {
  return performSend(
    deps,
    b,
    {
      platform: comment.platform,
      kind: 'hide_comment',
      key: `hide:${comment.platform}:${comment.commentId}`,
      commentId: comment.commentId,
      request: { hide: true },
    },
    async (api) => {
      await api.hideComment(comment.platform, comment.commentId, true);
      return {};
    },
  );
}
