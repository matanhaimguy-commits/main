import type { Business, Funnel } from '../config/schema';
import { isMissingTable, queueFollowup } from '../db/followups';
import type { Contact } from '../db/repo';
import { afterDueAt } from '../logic/after-delay';
import type { Deps } from './deps';
import { sendDm, type SendOutcome } from './send';

/** The ledger key of a funnel's last message for one trigger (one tap): it can be claimed once, ever. */
export const afterKey = (funnelId: string, triggerKey: string): string => `funnel:${funnelId}:after:${triggerKey}`;

/** The funnel's last message as a normal DM. Whoever calls it, the ledger key lets it leave once. */
export function sendAfter(deps: Deps, b: Business, f: Funnel, contact: Contact, text: string, key: string): Promise<SendOutcome> {
  return sendDm(deps, b, contact, { text }, { key, source: 'funnel', funnelId: f.id, step: 'after' });
}

/**
 * Called once the funnel's delivery went out. With no delay (the default) the last message is sent
 * now, exactly as it always was. With `after_delay_minutes` it is queued instead, and the scheduled
 * tick sends it when its time comes (see after-run.ts).
 */
export async function handleAfter(
  deps: Deps,
  b: Business,
  f: Funnel,
  contact: Contact,
  triggerKey: string,
  delivery: 'sent' | 'dry_run',
): Promise<void> {
  if (!f.after) return;
  const key = afterKey(f.id, triggerKey);
  if (f.after_delay_minutes <= 0) {
    await sendAfter(deps, b, f, contact, f.after, key);
    return;
  }
  try {
    const queued = await queueFollowup(deps.sql, {
      key,
      business: b.slug,
      funnelId: f.id,
      contactId: contact.id,
      dueAt: afterDueAt(deps.now(), f.after_delay_minutes),
      dryRun: delivery === 'dry_run',
    });
    deps.log.info(queued ? 'funnel last message queued' : 'funnel last message was already queued', {
      business: b.slug,
      funnel: f.id,
      contact: contact.id,
      minutes: f.after_delay_minutes,
    });
  } catch (err) {
    if (!isMissingTable(err)) throw err;
    // The migration is not applied. Do not send early (the owner asked for a wait); say so loudly instead.
    deps.log.error('funnel_followups table is missing; the last message was not sent', { business: b.slug, funnel: f.id });
    await deps.alert({
      key: `followups-table:${b.slug}`,
      text: `⚠️ ${b.name}: funnel "${f.id}" waits ${f.after_delay_minutes} minutes before its last message, but the database has no funnel_followups table yet. Apply supabase/migrations/20261028090000_funnel_followups.sql. Until then that last message is not sent.`,
      cooldownMinutes: 360,
    });
  }
}
