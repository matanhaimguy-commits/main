import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import { runColumns } from "./columns";
import { sortRuns } from "./order";
import type { RunListRow, StudioRunRow } from "./types";

/** The run with this business and post_id (no ledger), or null. */
export async function findRun(sql: Sql, business: string, postId: string): Promise<StudioRunRow | null> {
  const [run] = await sql<StudioRunRow[]>`
    SELECT ${runColumns(sql)} FROM studio_runs WHERE business = ${business} AND post_id = ${postId}`;
  return run ?? null;
}

/** Every run for the Studio list, with how many questions are open, in the order the page shows them. */
export async function listRuns(sql: Sql, filter: { business?: string } = {}): Promise<RunListRow[]> {
  const rows = await sql<Omit<RunListRow, "waiting">[]>`
    SELECT ${runColumns(sql, "r")}, coalesce(b.config->>'name', r.business) AS business_name,
           (SELECT count(*)::int FROM studio_decisions d WHERE d.run_id = r.id AND d.status = 'open') AS open_decisions
    FROM studio_runs r LEFT JOIN businesses b ON b.slug = r.business
    WHERE (${filter.business ?? null}::text IS NULL OR r.business = ${filter.business ?? null})
    ORDER BY r.updated_at DESC
    LIMIT 300`;
  return sortRuns(rows.map((r) => ({ ...r, waiting: r.open_decisions > 0 || r.waiting_on_owner })));
}
