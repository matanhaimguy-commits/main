import type { Business } from '../config/schema';
import type { CommentDecision } from '../ai/agent';
import {
  clearOptOut,
  countRecentSends,
  findContact,
  insertComment,
  insertMessage,
  isOurMessage,
  markDelivered,
  markInbound,
  markOutbound,
  markRead,
  pauseAi,
  recordAiRun,
  recordTap,
  setFollows,
  setOptedOut,
  setProfile,
  updateComment,
  upsertContact,
  type Contact,
} from '../db/repo';
import { isAllowedRecipient, screenComment } from '../logic/comments';
import { decodePayload, findFunnel, selectCommentFunnel, selectMessageFunnel, type SkipReason } from '../logic/funnels';
import { normalize } from '../logic/text';
import { parseWebhook, type CommentEvent, type MessageEvent, type MetaEvent, type PostbackEvent, type ReceiptEvent } from '../meta/webhook';
import type { Deps } from './deps';
import { runDeliver, runOpenerAsDm, runOpenerFromComment } from './funnel';
import { delivered, hideComment, sendDm, sendPrivateReply, sendPublicReply } from './send';

// Meta's own Page Inbox / Business Suite app. Echoes carrying it were typed by a person.
export const PAGE_INBOX_APP_ID = '263902037430900';

const STOP_WORDS = new Set(['stop', 'unsubscribe', 'הסר', 'הסרה', 'הסירו', 'תסירו']);

/**
 * Processes one stored webhook payload. Every step is idempotent (sends are keyed in the
 * ledger, messages by mid, comments by id), so re-processing after a crash is safe.
 */
export async function processPayload(deps: Deps, payload: unknown): Promise<void> {
  for (const ev of parseWebhook(payload as Record<string, unknown>, deps.now())) {
    await processEvent(deps, ev);
  }
}

export async function processEvent(deps: Deps, ev: MetaEvent): Promise<void> {
  const b = deps.registry.byAccount(ev.platform, ev.accountId);
  if (!b) {
    deps.log.warn('webhook for an account no business config claims', { platform: ev.platform, account: ev.accountId });
    return;
  }
  switch (ev.type) {
    case 'comment':
      return handleComment(deps, b, ev);
    case 'message':
      return ev.isEcho ? handleEcho(deps, b, ev) : handleMessage(deps, b, ev);
    case 'postback':
      return handlePostback(deps, b, ev);
    case 'delivery':
    case 'read':
      return handleReceipt(deps, b, ev);
  }
}

export function shouldAiReply(deps: Deps, b: Business, c: Contact): boolean {
  return (
    !!deps.ai &&
    b.enabled &&
    b.ai.enabled &&
    b.ai.dm_replies &&
    !c.opted_out &&
    !(c.ai_paused_until && c.ai_paused_until > deps.now()) &&
    isAllowedRecipient(b, { id: c.external_id, username: c.username ?? undefined })
  );
}

function aiCommentsOn(deps: Deps, b: Business): boolean {
  return !!deps.ai && b.ai.enabled && (b.ai.comment_replies || b.ai.comment_dms || b.ai.hide_spam);
}

// ---- comments ----------------------------------------------------------------

async function handleComment(deps: Deps, b: Business, ev: CommentEvent) {
  const screen = screenComment(ev, b, deps.now());
  if (screen === 'not_new') return; // edits and removals are not new comments

  let outcome: 'funnel' | 'ai' | 'skipped' = 'skipped';
  let reason: SkipReason | undefined = screen;
  let funnel = undefined;
  if (!b.enabled) {
    reason = 'business_disabled';
  } else if (!screen) {
    const decision = selectCommentFunnel(b.funnels, { platform: ev.platform, postId: ev.postId, text: ev.text });
    const allowed = isAllowedRecipient(b, { id: ev.authorId, username: ev.authorName });
    funnel = decision.funnel;
    if (decision.kind === 'matched') {
      reason = allowed ? undefined : 'not_a_tester';
      outcome = allowed ? 'funnel' : 'skipped';
    } else {
      reason = decision.reason;
      // No funnel owns it: the AI may answer questions and buying intent.
      if (allowed && (reason === 'keyword_not_matched' || reason === 'no_funnel_for_post') && aiCommentsOn(deps, b)) {
        outcome = 'ai';
      }
    }
  }

  const inserted = await insertComment(deps.sql, {
    business: b.slug,
    platform: ev.platform,
    comment_id: ev.commentId,
    post_id: ev.postId,
    parent_id: ev.parentId,
    author_id: ev.authorId,
    author_name: ev.authorName,
    text: ev.text,
    commented_at: ev.createdAt,
    outcome,
    skip_reason: reason,
    funnel_id: funnel?.id,
  });
  deps.log.info('comment', { business: b.slug, platform: ev.platform, comment: ev.commentId, outcome, reason, funnel: funnel?.id, duplicate: !inserted });

  if (outcome === 'funnel' && funnel) {
    await runOpenerFromComment(deps, b, funnel, ev);
  } else if (outcome === 'ai') {
    let existing: CommentDecision | undefined;
    if (!inserted) {
      const [row] = await deps.sql<{ ai_decision: CommentDecision | null }[]>`
        SELECT ai_decision FROM comments WHERE platform = ${ev.platform} AND comment_id = ${ev.commentId}`;
      existing = row?.ai_decision ?? undefined;
    }
    await runCommentAi(deps, b, ev, existing);
  }
}

async function runCommentAi(deps: Deps, b: Business, ev: CommentEvent, existing?: CommentDecision) {
  let decision = existing;
  if (!decision) {
    try {
      const r = await deps.ai!.triageComment({ business: b, platform: ev.platform, text: ev.text, authorName: ev.authorName });
      decision = r.decision;
      await recordAiRun(deps.sql, { business: b.slug, kind: 'comment', ...usageFields(r.usage) });
      await updateComment(deps.sql, ev.platform, ev.commentId, { outcome: 'ai', ai_intent: decision.intent, ai_decision: decision });
    } catch (err) {
      deps.log.error('comment triage failed', { business: b.slug, comment: ev.commentId, err });
      await recordAiRun(deps.sql, { business: b.slug, kind: 'comment', error: (err as Error).message });
      await updateComment(deps.sql, ev.platform, ev.commentId, { outcome: 'skipped', skip_reason: 'ai_error' });
      return;
    }
  }

  if (decision.hide && b.ai.hide_spam) await hideComment(deps, b, ev);
  if (decision.intent === 'spam') return;

  let dmFailed = false;
  const dmIntent = ['question', 'pricing', 'buying_intent'].includes(decision.intent);
  if (decision.send_dm && decision.dm_text && b.ai.comment_dms && dmIntent) {
    const { outcome } = await sendPrivateReply(deps, b, ev, { text: decision.dm_text }, {
      source: 'ai',
      step: 'comment_dm',
      contactSource: 'comment:ai',
    });
    dmFailed = !delivered(outcome);
  }
  if (decision.public_reply && b.ai.comment_replies && !dmFailed) {
    const today = await countRecentSends(deps.sql, { business: b.slug, kind: 'public_reply', sinceHours: 24 });
    if (today < b.ai.max_public_replies_per_day) await sendPublicReply(deps, b, ev, decision.public_reply, 'ai_public');
  }
  if (decision.alert_owner) {
    await deps.alert({
      key: `comment:${ev.commentId}`,
      text: `💬 ${b.name} (${ev.platform}): ${decision.intent} comment from ${ev.authorName ?? 'someone'}:\n"${ev.text}"\n${decision.reason}`,
    });
  }
}

// ---- messages ----------------------------------------------------------------

function describeInbound(ev: MessageEvent): string {
  const parts: string[] = [];
  if (ev.storyReply) parts.push('[Replied to our story]');
  for (const a of ev.attachments) {
    if (a.type === 'story_mention') parts.push('[Mentioned us in their story]');
    else if (a.type === 'ig_reel' || a.type === 'reel') parts.push('[Shared a reel]');
    else if (a.type === 'ig_post' || a.type === 'share') parts.push('[Shared a post]');
    else parts.push(`[Sent ${a.type === 'image' ? 'a photo' : a.type === 'audio' ? 'a voice message' : a.type === 'video' ? 'a video' : `an attachment (${a.type})`}]`);
  }
  if (ev.text) parts.push(ev.text);
  return parts.join(' ') || '[Sent something we cannot read]';
}

/** Fetches name/username once, so the testers list and the AI can use them. */
async function ensureProfile(deps: Deps, b: Business, contact: Contact): Promise<Contact> {
  if (contact.username || contact.name) return contact;
  const api = deps.metaFor(b);
  if (!api) return contact;
  try {
    if (contact.platform === 'instagram') {
      const p = await api.getUserProfile(contact.external_id, ['name', 'username', 'is_user_follow_business']);
      await setProfile(deps.sql, contact.id, { username: p.username as string | undefined, name: p.name as string | undefined });
      if (typeof p.is_user_follow_business === 'boolean') await setFollows(deps.sql, contact.id, p.is_user_follow_business);
      return { ...contact, username: (p.username as string) ?? null, name: (p.name as string) ?? null };
    }
    const p = await api.getUserProfile(contact.external_id, ['first_name', 'last_name']);
    const name = [p.first_name, p.last_name].filter(Boolean).join(' ') || undefined;
    await setProfile(deps.sql, contact.id, { name });
    return { ...contact, name: name ?? null };
  } catch (err) {
    deps.log.info('profile lookup failed', { business: b.slug, contact: contact.id, err });
    return contact;
  }
}

async function handleMessage(deps: Deps, b: Business, ev: MessageEvent) {
  if (ev.senderId === ev.accountId || ev.isDeleted) return;
  let contact = await upsertContact(deps.sql, { business: b.slug, platform: ev.platform, externalId: ev.senderId });
  await insertMessage(deps.sql, {
    contactId: contact.id,
    direction: 'in',
    source: 'user',
    mid: ev.mid,
    text: describeInbound(ev),
    payload: { attachments: ev.attachments, story: ev.storyReply, quick_reply: ev.quickReplyPayload },
    at: ev.timestamp,
  });
  const now = deps.now();
  // Another app (e.g. ManyChat) owns this thread: record it, don't answer.
  if (ev.standby || !b.enabled) return markInbound(deps.sql, contact.id, now, null);
  contact = await ensureProfile(deps, b, contact);
  const allowed = isAllowedRecipient(b, { id: contact.external_id, username: contact.username ?? undefined });

  if (ev.text && STOP_WORDS.has(normalize(ev.text))) {
    await markInbound(deps.sql, contact.id, now, null);
    await setOptedOut(deps.sql, contact.id);
    if (allowed) {
      const hebrew = /\p{Script=Hebrew}/u.test(ev.text);
      await sendDm(
        deps,
        b,
        contact,
        { text: hebrew ? 'קיבלנו 🙏 לא נשלח לך יותר הודעות אוטומטיות.' : "Got it 🙏 You won't get any more automated messages from us." },
        { key: `optout:${ev.mid}`, source: 'system', step: 'optout' },
      );
    }
    return;
  }
  if (contact.opted_out && ev.text) {
    // They wrote to us again after opting out: they want to talk.
    await clearOptOut(deps.sql, contact.id);
    contact = { ...contact, opted_out: false };
  }

  const quick = decodePayload(ev.quickReplyPayload);
  if (quick) {
    await markInbound(deps.sql, contact.id, now, null);
    return runFunnelPayload(deps, b, contact, quick.funnelId, quick.step, ev.mid, allowed);
  }

  if (ev.text && allowed) {
    const decision = selectMessageFunnel(b.funnels, {
      platform: ev.platform,
      trigger: ev.storyReply ? 'story_reply' : 'dm_keyword',
      text: ev.text,
    });
    if (decision.kind === 'matched') {
      await markInbound(deps.sql, contact.id, now, null);
      await runOpenerAsDm(deps, b, decision.funnel, contact, ev.mid);
      return;
    }
  }

  const due = shouldAiReply(deps, b, contact) ? new Date(now.getTime() + b.ai.reply_delay_seconds * 1000) : null;
  await markInbound(deps.sql, contact.id, now, due);
}

async function runFunnelPayload(
  deps: Deps,
  b: Business,
  contact: Contact,
  funnelId: string,
  step: 'deliver' | 'gate',
  triggerKey: string,
  allowed: boolean,
) {
  const funnel = findFunnel(b.funnels, funnelId);
  await recordTap(deps.sql, { business: b.slug, contactId: contact.id, funnelId, payload: `${funnelId}:${step}` });
  if (!funnel) {
    deps.log.warn('button tap for a funnel that no longer exists', { business: b.slug, funnel: funnelId });
    return;
  }
  if (!allowed) return;
  await runDeliver(deps, b, funnel, contact, triggerKey, step);
}

async function handlePostback(deps: Deps, b: Business, ev: PostbackEvent) {
  let contact = await upsertContact(deps.sql, { business: b.slug, platform: ev.platform, externalId: ev.senderId });
  const triggerKey = ev.mid ?? `${ev.senderId}:${ev.timestamp.getTime()}`;
  await insertMessage(deps.sql, {
    contactId: contact.id,
    direction: 'in',
    source: 'user',
    mid: ev.mid ?? `postback:${triggerKey}`,
    text: `[Tapped the button "${ev.title ?? ev.payload}"]`,
    at: ev.timestamp,
  });
  const now = deps.now();
  if (!b.enabled) return markInbound(deps.sql, contact.id, now, null);
  contact = await ensureProfile(deps, b, contact);
  const allowed = isAllowedRecipient(b, { id: contact.external_id, username: contact.username ?? undefined });

  const payload = decodePayload(ev.payload);
  if (payload) {
    // The tap counts as the person messaging us: the 24h window is open from here.
    await markInbound(deps.sql, contact.id, now, null);
    return runFunnelPayload(deps, b, contact, payload.funnelId, payload.step, triggerKey, allowed);
  }
  // Get Started, ice breakers or a menu: let the AI answer.
  await recordTap(deps.sql, { business: b.slug, contactId: contact.id, payload: ev.payload });
  const due = shouldAiReply(deps, b, contact) ? new Date(now.getTime() + b.ai.reply_delay_seconds * 1000) : null;
  await markInbound(deps.sql, contact.id, now, due);
}

/**
 * An echo is a message sent from the business side. If this app sent it, ignore it. Anything
 * else is a person on the team (Page Inbox, Business Suite, the Instagram app) or another tool,
 * so the AI steps back for a while instead of talking over them.
 */
async function handleEcho(deps: Deps, b: Business, ev: MessageEvent) {
  const userId = ev.recipientId;
  if (!userId || userId === ev.accountId) return;
  const appId = deps.env.META_APP_ID;
  if (appId && ev.appId === appId) return;
  if (await isOurMessage(deps.sql, ev.mid)) return;
  // A send still in flight to this person: its echo can beat our ledger update.
  const [inflight] = await deps.sql`
    SELECT 1 FROM sends WHERE business = ${b.slug} AND recipient_id = ${userId} AND status = 'pending'
      AND created_at > now() - interval '2 minutes' LIMIT 1`;
  if (inflight) return;

  const contact = await upsertContact(deps.sql, { business: b.slug, platform: ev.platform, externalId: userId });
  await insertMessage(deps.sql, {
    contactId: contact.id,
    direction: 'out',
    source: 'human',
    mid: ev.mid,
    text: describeInbound({ ...ev, storyReply: undefined }),
    at: ev.timestamp,
  });
  await markOutbound(deps.sql, contact.id, ev.timestamp);
  if (b.ai.pause_hours_after_human > 0) {
    const until = new Date(deps.now().getTime() + b.ai.pause_hours_after_human * 3_600_000);
    const who = !ev.appId || ev.appId === PAGE_INBOX_APP_ID ? 'a team member replied' : `another app (${ev.appId}) replied`;
    await pauseAi(deps.sql, contact.id, until, who);
    deps.log.info('AI paused for conversation', { business: b.slug, contact: contact.id, until, who });
  }
}

async function handleReceipt(deps: Deps, b: Business, ev: ReceiptEvent) {
  const contact = await findContact(deps.sql, b.slug, ev.platform, ev.senderId);
  if (!contact) return;
  if (ev.type === 'delivery') await markDelivered(deps.sql, contact.id, ev.mids, ev.watermark);
  else await markRead(deps.sql, contact.id, ev.mids, ev.watermark);
}

export function usageFields(u: { model: string; inputTokens: number; outputTokens: number; cacheReadTokens: number; stopReason: string | null }) {
  return {
    model: u.model,
    inputTokens: u.inputTokens,
    outputTokens: u.outputTokens,
    cacheReadTokens: u.cacheReadTokens,
    stopReason: u.stopReason,
  };
}
