import type { Business, Funnel } from '../config/schema';
import { claimDueFollowups, FOLLOWUP_MAX_ATTEMPTS, finishFollowup, threadActivitySince, type FollowupRow } from '../db/followups';
import { getContact, type Contact } from '../db/repo';
import { AFTER_SKIP_TEXT, decideAfter, type AfterSkip } from '../logic/after-decision';
import { isAllowedRecipient } from '../logic/comments';
import type { Deps } from './deps';
import { sendAfter } from './funnel-after';
import { delivered } from './send';
import { recordSkippedSend } from './skipped-send';

interface Target {
  b: Business;
  f: Funnel;
  text: string;
}

/** What the queued row points at today. The funnel's current text is what goes out. */
function targetOf(deps: Deps, row: FollowupRow): Target | undefined {
  const b = deps.registry.bySlug(row.business);
  const f = b?.funnels.find((x) => x.id === row.funnel_id);
  return b && f?.after ? { b, f, text: f.after } : undefined;
}

/**
 * The scheduled tick's part of the funnel wait: sends every queued last message whose time has
 * come, unless it should not go (see decideAfter). Returns how many were sent (or dry-run).
 */
export async function runDueAfters(deps: Deps, limit = 20): Promise<number> {
  const due = await claimDueFollowups(deps.sql, deps.now(), limit);
  let sent = 0;
  for (const row of due) {
    try {
      if (await processDue(deps, row)) sent++;
    } catch (err) {
      deps.log.error('funnel last message failed', { business: row.business, funnel: row.funnel_id, row: row.id, attempt: row.attempts, err });
      // The lease lets it be tried again; after the last attempt it is given up on.
      if (row.attempts >= FOLLOWUP_MAX_ATTEMPTS) {
        await finishFollowup(deps.sql, row.id, 'skipped', `error: ${(err as Error).message}`, deps.now()).catch(() => {});
      }
    }
  }
  return sent;
}

async function processDue(deps: Deps, row: FollowupRow): Promise<boolean> {
  const contact = await getContact(deps.sql, row.contact_id);
  if (!contact) {
    await finishFollowup(deps.sql, row.id, 'skipped', 'contact_missing', deps.now());
    return false;
  }
  const target = targetOf(deps, row);
  const activity = await threadActivitySince(deps.sql, contact.id, row.watermark);
  const decision = decideAfter({
    now: deps.now(),
    funnelHasAfter: !!target,
    businessEnabled: !!target?.b.enabled,
    allowedRecipient: !target || isAllowedRecipient(target.b, { id: contact.external_id, username: contact.username ?? undefined }),
    optedOut: contact.opted_out,
    queuedInDryRunButLiveNow: row.dry_run && !!target && deps.isLive(target.b),
    personReplied: activity.personReplied,
    teamReplied: activity.teamReplied,
    lastInboundAt: contact.last_inbound_at,
  });
  if (!decision.send) {
    await skip(deps, row, contact, target, decision.reason);
    return false;
  }
  if (!target) return false; // not reachable: decideAfter skips when there is no target
  const outcome = await sendAfter(deps, target.b, target.f, contact, target.text, row.key);
  await finishFollowup(deps.sql, row.id, 'done', outcome.status, deps.now());
  return delivered(outcome);
}

/** Logs why, writes it to the send ledger (Activity page) and closes the queue row. */
async function skip(deps: Deps, row: FollowupRow, contact: Contact, target: Target | undefined, reason: AfterSkip) {
  const why = AFTER_SKIP_TEXT[reason];
  deps.log.info('funnel last message skipped', { business: row.business, funnel: row.funnel_id, contact: contact.id, reason, why });
  await recordSkippedSend(
    deps,
    {
      business: row.business,
      platform: contact.platform,
      kind: 'message',
      key: row.key,
      funnelId: row.funnel_id,
      step: 'after',
      contactId: contact.id,
      recipientId: contact.external_id,
      request: target ? { text: target.text } : undefined,
    },
    why,
  );
  await finishFollowup(deps.sql, row.id, 'skipped', reason, deps.now());
}
