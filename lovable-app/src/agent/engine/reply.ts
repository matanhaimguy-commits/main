import type { ReplyResult } from '../ai/agent';
import type { Business } from '../config/schema';
import {
  countRecentSends,
  finishReply,
  lastInboundMessageId,
  pauseAi,
  recentMessages,
  recordAiRun,
  sendExists,
  setFollowupFor,
  setOptedOut,
  updateLead,
  type Contact,
} from '../db/repo';
import type { Deps } from './deps';
import { shouldAiReply, usageFields } from './process';
import { sendDm } from './send';

const HANDOFF_PAUSE_DAYS = 30;

/** Answers a contact whose debounced reply is due. Called with the contact's reply lease held. */
export async function runReply(deps: Deps, contact: Contact): Promise<void> {
  const startedAt = deps.now();
  try {
    const b = deps.registry.bySlug(contact.business);
    if (!b || !deps.ai || !shouldAiReply(deps, b, contact)) return;

    const lastIn = await lastInboundMessageId(deps.sql, contact.id);
    if (!lastIn) return;
    // One AI answer per inbound message, ever: a crash or a second worker cannot double-answer.
    const key = `ai:${contact.id}:${lastIn}`;
    if (await sendExists(deps.sql, key)) return;

    const today = await countRecentSends(deps.sql, { business: b.slug, contactId: contact.id, step: 'ai', sinceHours: 24 });
    if (today >= b.ai.max_replies_per_contact_per_day) {
      await deps.alert({
        key: `cap:${contact.id}`,
        text: `⚠️ ${b.name}: daily AI reply cap reached for ${who(contact)}. The AI is quiet in that thread until tomorrow.`,
        cooldownMinutes: 720,
      });
      return;
    }

    const transcript = await recentMessages(deps.sql, contact.id, 40);
    if (transcript[transcript.length - 1]?.direction !== 'in') return; // someone already answered

    let result: ReplyResult;
    try {
      result = await deps.ai.reply({ business: b, contact, transcript, mode: 'reply', now: deps.now() });
      await recordAiRun(deps.sql, { business: b.slug, contactId: contact.id, kind: 'reply', ...usageFields(result.usage) });
    } catch (err) {
      deps.log.error('AI reply failed', { business: b.slug, contact: contact.id, err });
      await recordAiRun(deps.sql, { business: b.slug, contactId: contact.id, kind: 'reply', error: (err as Error).message });
      await deps.alert({
        key: `ai-error:${b.slug}`,
        text: `⚠️ ${b.name}: the AI could not answer ${who(contact)} (${(err as Error).message}). Reply manually.`,
        cooldownMinutes: 30,
      });
      return;
    }
    await applyResult(deps, b, contact, result, { key, step: 'ai' });
  } finally {
    await finishReply(deps.sql, contact.id, startedAt);
  }
}

export async function applyResult(
  deps: Deps,
  b: Business,
  contact: Contact,
  result: ReplyResult,
  meta: { key: string; step: 'ai' | 'followup' },
) {
  if (result.text) {
    const link = result.linkId ? b.links.find((l) => l.id === result.linkId) : undefined;
    await sendDm(
      deps,
      b,
      contact,
      { text: result.text, button: link ? { title: link.title, url: link.url } : undefined },
      { key: meta.key, source: 'ai', step: meta.step },
    );
  }
  if (Object.keys(result.lead).length > 0) await updateLead(deps.sql, contact.id, result.lead);
  if (result.optOut) await setOptedOut(deps.sql, contact.id);

  const stage = result.lead.stage;
  if (stage && stage !== contact.stage && (stage === 'hot' || stage === 'booked' || stage === 'won')) {
    const lead = { ...contact, ...Object.fromEntries(Object.entries(result.lead).filter(([, v]) => v)) };
    await deps.alert({
      key: `stage:${contact.id}:${stage}`,
      text: `🔥 ${b.name}: ${who(lead)} is now ${stage.toUpperCase()} (${contact.platform}).${lead.interest ? `\nWants: ${lead.interest}` : ''}${lead.phone ? `\nPhone: ${lead.phone}` : ''}${lead.email ? `\nEmail: ${lead.email}` : ''}`,
      cooldownMinutes: 24 * 60,
    });
  }
  if (result.handoff) {
    const until = new Date(deps.now().getTime() + HANDOFF_PAUSE_DAYS * 86_400_000);
    await pauseAi(deps.sql, contact.id, until, `handoff: ${result.handoff.reason}`);
    await deps.alert({
      key: `handoff:${contact.id}`,
      text: `${result.handoff.urgent ? '🚨' : '🙋'} ${b.name}: ${who(contact)} needs a person (${contact.platform}).\nWhy: ${result.handoff.reason}\n${result.handoff.summary}\nThe AI is paused in this thread; resume it from the admin page.`,
      cooldownMinutes: 60,
    });
  }
}

function who(c: Pick<Contact, 'name' | 'username' | 'external_id'>): string {
  return c.name ?? (c.username ? `@${c.username}` : `user ${c.external_id}`);
}

/**
 * One gentle follow-up when a warm lead goes quiet, sent only inside Meta's 24h window
 * (we stop at 23h) and at most once per message from them.
 */
export async function runFollowups(deps: Deps): Promise<number> {
  const candidates = await deps.sql<Contact[]>`
    SELECT * FROM contacts
    WHERE NOT opted_out AND NOT needs_reply
      AND stage IN ('engaged', 'qualified', 'hot')
      AND last_inbound_at > now() - interval '23 hours'
      AND last_outbound_at > last_inbound_at
      AND (followup_for IS NULL OR followup_for <> last_inbound_at)
      AND (ai_paused_until IS NULL OR ai_paused_until < now())
      AND (reply_lock_until IS NULL OR reply_lock_until < now())
      -- A person on the team spoke last: the thread is theirs, no automated nudge.
      AND NOT EXISTS (
        SELECT 1 FROM messages m
        WHERE m.contact_id = contacts.id AND m.source = 'human' AND m.created_at >= contacts.last_inbound_at)
    ORDER BY last_outbound_at LIMIT 20`;
  let sent = 0;
  for (const contact of candidates) {
    const b = deps.registry.bySlug(contact.business);
    if (!b || !deps.ai || !b.ai.followup.enabled || !shouldAiReply(deps, b, contact)) continue;
    const quietHours = (deps.now().getTime() - contact.last_outbound_at!.getTime()) / 3_600_000;
    if (quietHours < b.ai.followup.after_hours) continue;

    const [claimed] = await deps.sql`
      UPDATE contacts SET reply_lock_until = now() + interval '3 minutes'
      WHERE id = ${contact.id} AND (reply_lock_until IS NULL OR reply_lock_until < now()) RETURNING id`;
    if (!claimed) continue;
    const inboundAt = contact.last_inbound_at!;
    try {
      const key = `followup:${contact.id}:${inboundAt.toISOString()}`;
      if (await sendExists(deps.sql, key)) continue;
      const transcript = await recentMessages(deps.sql, contact.id, 40);
      const result = await deps.ai.reply({ business: b, contact, transcript, mode: 'followup', now: deps.now() });
      await recordAiRun(deps.sql, { business: b.slug, contactId: contact.id, kind: 'followup', ...usageFields(result.usage) });
      await applyResult(deps, b, contact, result, { key, step: 'followup' });
      if (result.text) sent++;
    } catch (err) {
      deps.log.error('follow-up failed', { business: b.slug, contact: contact.id, err });
      await recordAiRun(deps.sql, { business: b.slug, contactId: contact.id, kind: 'followup', error: (err as Error).message });
    } finally {
      await setFollowupFor(deps.sql, contact.id, inboundAt);
    }
  }
  return sent;
}
