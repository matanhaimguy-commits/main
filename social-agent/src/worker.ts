import { claimDueReplies, claimWebhookEvents, finishWebhookEvent, retryWebhookEvent, type WebhookEventRow } from './db/repo.js';
import type { Deps } from './engine/deps.js';
import { checkSubscriptions, runHealthChecks } from './engine/health.js';
import { processPayload } from './engine/process.js';
import { runFollowups, runReply } from './engine/reply.js';

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

/** One pass over all queued work. Returns how many items it handled. */
export async function tick(deps: Deps): Promise<number> {
  const events = await claimWebhookEvents(deps.sql, 20);
  // In order, one at a time: a comment, its button tap and the reply must not race.
  for (const row of events) await processRow(deps, row);
  const due = await claimDueReplies(deps.sql, 5);
  await Promise.all(due.map((c) => runReply(deps, c)));
  return events.length + due.length;
}

export interface Worker {
  nudge(): void;
  stop(): Promise<void>;
}

export function startWorker(deps: Deps, opts: { idleMs?: number } = {}): Worker {
  const idleMs = opts.idleMs ?? 1000;
  let stopped = false;
  let wake: (() => void) | undefined;
  const timers = { followups: 0, health: 0, subscriptions: 0 };

  const every = async (name: keyof typeof timers, ms: number, fn: () => Promise<unknown>) => {
    const now = Date.now();
    if (now - timers[name] < ms) return;
    timers[name] = now;
    try {
      await fn();
    } catch (err) {
      deps.log.error(`${name} failed`, { err });
    }
  };

  const done = (async () => {
    deps.log.info('worker started');
    while (!stopped) {
      let handled = 0;
      try {
        handled = await tick(deps);
        await every('followups', 60_000, () => runFollowups(deps));
        await every('health', 10 * 60_000, () => runHealthChecks(deps));
        await every('subscriptions', 60 * 60_000, () => checkSubscriptions(deps));
      } catch (err) {
        deps.log.error('worker tick failed', { err });
      }
      if (handled > 0 || stopped) continue;
      await new Promise<void>((resolve) => {
        const t = setTimeout(resolve, idleMs);
        wake = () => {
          clearTimeout(t);
          resolve();
        };
      });
      wake = undefined;
    }
    deps.log.info('worker stopped');
  })();

  return {
    nudge: () => wake?.(),
    stop: async () => {
      stopped = true;
      wake?.();
      await done;
    },
  };
}
