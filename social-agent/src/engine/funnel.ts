import type { Business, Funnel } from '../config/schema.js';
import { setFollows, setProfile, type Contact } from '../db/repo.js';
import { encodePayload } from '../logic/funnels.js';
import { pickVariant } from '../logic/text.js';
import type { OutboundMessage } from '../meta/messages.js';
import type { CommentEvent } from '../meta/webhook.js';
import type { Deps } from './deps.js';
import { delivered, sendDm, sendPrivateReply, sendPublicReply, type SendOutcome } from './send.js';

export function resolveLink(b: Business, ref: string): string {
  return b.links.find((l) => l.id === ref)?.url ?? ref;
}

export function openerMessage(b: Business, f: Funnel): OutboundMessage {
  if (f.opener.mode === 'link') {
    return { text: f.opener.text, button: { title: f.opener.button, url: resolveLink(b, f.deliver.link) } };
  }
  return { text: f.opener.text, button: { title: f.opener.button, payload: encodePayload({ funnelId: f.id, step: 'deliver' }) } };
}

/** Step 1 from a comment: the private reply, then (only if it went out) the public reply. */
export async function runOpenerFromComment(deps: Deps, b: Business, f: Funnel, comment: CommentEvent): Promise<SendOutcome> {
  const { outcome } = await sendPrivateReply(deps, b, comment, openerMessage(b, f), {
    source: 'funnel',
    funnelId: f.id,
    step: 'opener',
    contactSource: `funnel:${f.id}`,
  });
  // A public "check your DMs" is only true if the DM went out. If another tool already used
  // this comment's private reply, it has posted its own public reply.
  const publicText = pickVariant(f.public_replies, comment.commentId);
  if (publicText && delivered(outcome)) await sendPublicReply(deps, b, comment, publicText, 'public', f.id);
  return outcome;
}

/** Step 1 from a story reply or DM keyword: the person messaged us, so this is a normal DM. */
export function runOpenerAsDm(deps: Deps, b: Business, f: Funnel, contact: Contact, triggerMid: string) {
  return sendDm(deps, b, contact, openerMessage(b, f), {
    key: `funnel:${f.id}:opener:${triggerMid}`,
    source: 'funnel',
    funnelId: f.id,
    step: 'opener',
  });
}

/**
 * Instagram only shares follow status after the person has messaged you or tapped a button,
 * and it lags 10-30 seconds behind a fresh follow. So: check after the tap, and when they tap
 * "I followed", re-check a few times before telling them it didn't work.
 */
async function checkFollows(deps: Deps, b: Business, contact: Contact, attempts: number): Promise<boolean | undefined> {
  const api = deps.metaFor(b);
  if (!api) return deps.isLive(b) ? undefined : true;
  for (let i = 0; i < attempts; i++) {
    try {
      const p = await api.getUserProfile(contact.external_id, ['is_user_follow_business', 'username', 'name']);
      const follows = p.is_user_follow_business === true;
      await setFollows(deps.sql, contact.id, follows);
      if (p.username || p.name) await setProfile(deps.sql, contact.id, { username: p.username as string, name: p.name as string });
      if (follows) return true;
    } catch (err) {
      deps.log.warn('follow check failed; delivering anyway', { business: b.slug, contact: contact.id, err });
      return undefined;
    }
    if (i < attempts - 1) await deps.sleep(5_000);
  }
  return false;
}

/** Step 2, when the opener's button is tapped: optional follow gate, then the link, then the conversation opener. */
export async function runDeliver(
  deps: Deps,
  b: Business,
  f: Funnel,
  contact: Contact,
  triggerKey: string,
  step: 'deliver' | 'gate',
): Promise<void> {
  if (f.follow_gate?.enabled && contact.platform === 'instagram') {
    const follows = await checkFollows(deps, b, contact, step === 'gate' ? 3 : 1);
    if (follows === false) {
      await sendDm(
        deps,
        b,
        contact,
        { text: f.follow_gate.text, button: { title: f.follow_gate.button, payload: encodePayload({ funnelId: f.id, step: 'gate' }) } },
        { key: `funnel:${f.id}:gate:${triggerKey}`, source: 'funnel', funnelId: f.id, step: 'gate' },
      );
      return;
    }
  }
  const outcome = await sendDm(
    deps,
    b,
    contact,
    { text: f.deliver.text, button: { title: f.deliver.button, url: resolveLink(b, f.deliver.link) } },
    { key: `funnel:${f.id}:deliver:${triggerKey}`, source: 'funnel', funnelId: f.id, step: 'deliver' },
  );
  if (delivered(outcome) && f.after) {
    await sendDm(deps, b, contact, { text: f.after }, { key: `funnel:${f.id}:after:${triggerKey}`, source: 'funnel', funnelId: f.id, step: 'after' });
  }
}
