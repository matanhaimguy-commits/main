import type { Sql } from './sql';

/**
 * The queue behind a funnel's `after_delay_minutes`: last messages waiting for their time.
 * (Table: funnel_followups, migration 20261028090000_funnel_followups.sql.)
 */

export interface FollowupRow {
  id: number;
  key: string;
  business: string;
  funnel_id: string;
  contact_id: number;
  due_at: Date;
  dry_run: boolean;
  watermark: number;
  attempts: number;
}

/** A claimed row stays ours this long; a worker that dies mid-way lets it go. */
export const FOLLOWUP_LEASE_MS = 3 * 60_000;
/** A row that keeps failing is given up on after this many claims. */
export const FOLLOWUP_MAX_ATTEMPTS = 3;

/** Postgres "undefined_table": the migration has not been applied yet. */
export const isMissingTable = (err: unknown): boolean => (err as { code?: unknown } | null)?.code === '42P01';

/**
 * Queues the message. The watermark is the newest message of this person's thread right now,
 * so anything newer later on is a message that came in while the message waited.
 * Returns false when this key was already queued (nothing is queued twice).
 */
export async function queueFollowup(
  sql: Sql,
  q: { key: string; business: string; funnelId: string; contactId: number; dueAt: Date; dryRun: boolean },
): Promise<boolean> {
  const rows = await sql`
    INSERT INTO funnel_followups (key, business, funnel_id, contact_id, due_at, dry_run, watermark)
    VALUES (${q.key}, ${q.business}, ${q.funnelId}, ${q.contactId}, ${q.dueAt}, ${q.dryRun},
      (SELECT COALESCE(max(id), 0) FROM messages WHERE contact_id = ${q.contactId}))
    ON CONFLICT (key) DO NOTHING
    RETURNING id`;
  return rows.length > 0;
}

/**
 * Claims the messages whose time has come, with a lease so two workers never take the same one.
 * Returns nothing (not an error) until the migration is applied.
 */
export async function claimDueFollowups(sql: Sql, now: Date, limit: number): Promise<FollowupRow[]> {
  const lease = new Date(now.getTime() + FOLLOWUP_LEASE_MS);
  try {
    return await sql<FollowupRow[]>`
      UPDATE funnel_followups SET status = 'sending', attempts = attempts + 1, locked_until = ${lease}
      WHERE id IN (
        SELECT id FROM funnel_followups
        WHERE due_at <= ${now} AND attempts < ${FOLLOWUP_MAX_ATTEMPTS}
          AND (status = 'pending' OR (status = 'sending' AND locked_until < ${now}))
        ORDER BY due_at LIMIT ${limit}
        FOR UPDATE SKIP LOCKED)
      RETURNING id, key, business, funnel_id, contact_id, due_at, dry_run, watermark, attempts`;
  } catch (err) {
    if (isMissingTable(err)) return [];
    throw err;
  }
}

export async function finishFollowup(sql: Sql, id: number, status: 'done' | 'skipped', result: string, now: Date) {
  await sql`
    UPDATE funnel_followups SET status = ${status}, result = ${result}, locked_until = NULL, finished_at = ${now}
    WHERE id = ${id}`;
}

/** Whether the person, or a team member, wrote in this thread after the watermark. */
export async function threadActivitySince(
  sql: Sql,
  contactId: number,
  watermark: number,
): Promise<{ personReplied: boolean; teamReplied: boolean }> {
  const [row] = await sql<{ person_replied: boolean; team_replied: boolean }[]>`
    SELECT
      EXISTS (SELECT 1 FROM messages WHERE contact_id = ${contactId} AND id > ${watermark}
        AND direction = 'in' AND source = 'user') AS person_replied,
      EXISTS (SELECT 1 FROM messages WHERE contact_id = ${contactId} AND id > ${watermark}
        AND source = 'human') AS team_replied`;
  return { personReplied: !!row?.person_replied, teamReplied: !!row?.team_replied };
}
