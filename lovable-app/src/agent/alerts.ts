import type { Env } from './config/env';
import type { Sql } from './db/sql';
import { claimAlert } from './db/repo';
import type { Logger } from './log';

export interface Alert {
  /** Same key = same problem; it fires at most once per cooldown. */
  key: string;
  text: string;
  cooldownMinutes?: number;
}

export type Alerter = (alert: Alert) => Promise<void>;

/** Sends alerts to Telegram and/or a generic webhook (Slack, Discord, Make, Zapier). Always logs. */
export function createAlerter(env: Env, sql: Sql, log: Logger, fetchImpl: typeof fetch = fetch): Alerter {
  return async ({ key, text, cooldownMinutes = 60 }) => {
    log.warn('alert', { key, text });
    try {
      if (!(await claimAlert(sql, key, cooldownMinutes))) return;
    } catch (err) {
      log.error('alert dedupe failed', { err });
    }
    const jobs: Promise<unknown>[] = [];
    if (env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID) {
      jobs.push(
        fetchImpl(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: env.TELEGRAM_CHAT_ID, text, disable_web_page_preview: true }),
          signal: AbortSignal.timeout(10_000),
        }),
      );
    }
    if (env.ALERT_WEBHOOK_URL) {
      jobs.push(
        fetchImpl(env.ALERT_WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          // "text" works for Slack incoming webhooks; "content" for Discord.
          body: JSON.stringify({ text, content: text }),
          signal: AbortSignal.timeout(10_000),
        }),
      );
    }
    const results = await Promise.allSettled(jobs);
    for (const r of results) if (r.status === 'rejected') log.error('alert delivery failed', { err: r.reason });
  };
}
