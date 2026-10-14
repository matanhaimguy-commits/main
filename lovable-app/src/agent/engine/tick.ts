import { getState, setState } from '../db/connections';
import { claimDueReplies, claimWebhookEvents, finishWebhookEvent, retryWebhookEvent, type WebhookEventRow } from '../db/repo';
import type { Deps } from './deps';
import { checkDmAccess, checkSubscriptions, runHealthChecks } from './health';
import { processPayload } from './process';
import { runFollowups, runReply } from './reply';

const MAX_ATTEMPTS = 3;

export async function processRow(deps: Deps, row: WebhookEventRow): Promise<void> {
  try {
    await processPayload(deps, row.payload);
    await finishWebhookEvent(deps.sql, row.id, 'done');
  } catch (err) {
    deps.log.error('webhook event failed', { event: row.id, attempt: row.attempts, err });
    if (row.attempts >= MAX_ATTEMPTS) {
      await finishWebhookEvent(deps.sql, row.id, 'error', (err as Error).message);
      await deps.alert({ key: `event-error:${row.id}`, text: `⚠️ Webhook event #${row.id} failed ${MAX_ATTEMPTS} times: ${(err as Error).message}` });
    } else {
      // Safe to re-run: every send is keyed in the ledger, so nothing goes out twice.
      await retryWebhookEvent(deps.sql, row.id, row.attempts * 30, (err as Error).message);
    }
  }
}

/** One pass over queued events and due AI replies. Returns how many items it handled. */
export async function tick(deps: Deps, limits: { events?: number; replies?: number } = {}): Promise<number> {
  const events = await claimWebhookEvents(deps.sql, limits.events ?? 10);
  // In order, one at a time: a comment, its button tap and the reply must not race.
  for (const row of events) await processRow(deps, row);
  const due = await claimDueReplies(deps.sql, limits.replies ?? 3);
  await Promise.all(due.map((c) => runReply(deps, c)));
  return events.length + due.length;
}

/** Seconds until the next AI reply is due, or undefined when none is waiting. */
export async function nextReplyIn(deps: Deps): Promise<number | undefined> {
  const [row] = await deps.sql<{ secs: number | null }[]>`
    SELECT EXTRACT(EPOCH FROM (min(reply_due_at) - now()))::float AS secs
    FROM contacts WHERE needs_reply AND reply_due_at IS NOT NULL
      AND (reply_lock_until IS NULL OR reply_lock_until < now())`;
  return row?.secs ?? undefined;
}

/**
 * Work that follows a webhook: process what was stored, then wait for a reply that is
 * due within `waitUpToSeconds` (the AI waits a few seconds so a burst of messages gets
 * one answer) and send it. Anything left is picked up by the scheduled tick.
 */
export async function drain(deps: Deps, opts: { waitUpToSeconds: number; deadline: number }): Promise<void> {
  while (Date.now() < opts.deadline) {
    const handled = await tick(deps);
    if (handled > 0) continue;
    const secs = await nextReplyIn(deps);
    if (secs === undefined || secs > opts.waitUpToSeconds) return;
    const waitMs = Math.max(0, secs * 1000) + 250;
    if (Date.now() + waitMs > opts.deadline) return;
    await deps.sleep(waitMs);
  }
}

const PERIODIC = {
  followups: 60_000,
  health: 10 * 60_000,
  subscriptions: 60 * 60_000,
  dm_access: 60 * 60_000,
} as const;

/** The scheduled run (every minute): queued work, then follow-ups and checks when due. */
export async function scheduledRun(deps: Deps, deadline: number): Promise<{ handled: number; ran: string[] }> {
  let handled = 0;
  while (Date.now() < deadline) {
    const n = await tick(deps);
    handled += n;
    if (n === 0) break;
  }
  const last: Record<string, number> = (await getState<Record<string, number>>(deps.sql, 'periodic_runs'))?.value ?? {};
  const ran: string[] = [];
  const now = Date.now();
  const jobs: Record<keyof typeof PERIODIC, () => Promise<unknown>> = {
    followups: () => runFollowups(deps),
    health: () => runHealthChecks(deps),
    subscriptions: () => checkSubscriptions(deps),
    dm_access: () => checkDmAccess(deps),
  };
  for (const name of Object.keys(PERIODIC) as (keyof typeof PERIODIC)[]) {
    // A little slack so a job due "every minute" runs on every one-minute tick.
    if (now - (last[name] ?? 0) < PERIODIC[name] - 5_000) continue;
    last[name] = now;
    ran.push(name);
    try {
      await jobs[name]();
    } catch (err) {
      deps.log.error(`${name} failed`, { err });
    }
  }
  if (ran.length) await setState(deps.sql, 'periodic_runs', last);
  await setState(deps.sql, 'last_tick_at', { at: new Date().toISOString(), handled });
  return { handled, ran };
}
