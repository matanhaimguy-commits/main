import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import type { DecisionStatus } from "./schema";
import type { DecisionListRow } from "./types";

/** Questions with their run's business and post_id: open first, then answered, then synced; newest first. */
export async function listDecisions(
  sql: Sql,
  filter: { status?: DecisionStatus; business?: string; runId?: number; limit?: number },
): Promise<DecisionListRow[]> {
  const rows = await sql<DecisionListRow[]>`
    SELECT d.*, r.business, r.post_id, r.title AS run_title
    FROM studio_decisions d JOIN studio_runs r ON r.id = d.run_id
    WHERE (${filter.status ?? null}::text IS NULL OR d.status = ${filter.status ?? null})
      AND (${filter.business ?? null}::text IS NULL OR r.business = ${filter.business ?? null})
      AND (${filter.runId ?? null}::bigint IS NULL OR d.run_id = ${filter.runId ?? null})
    ORDER BY CASE d.status WHEN 'open' THEN 0 WHEN 'answered' THEN 1 ELSE 2 END, d.created_at DESC, d.id DESC
    LIMIT ${filter.limit ?? 200}`;
  return [...rows];
}
