import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import { runColumns } from "./columns";
import { listDecisions } from "./decisions-list.server";
import { listFiles } from "./files.server";
import { openQueueItems } from "./queue";
import type { RunDetail, StudioRunRow } from "./types";

/** One run for its page: steps, files (no markdown), every question, and the open queue items no question covers. */
export async function runDetail(sql: Sql, id: number): Promise<RunDetail | null> {
  const [row] = await sql<(StudioRunRow & { business_name: string; queue: unknown })[]>`
    SELECT ${runColumns(sql, "r")}, coalesce(b.config->>'name', r.business) AS business_name, r.ledger->'queue' AS queue
    FROM studio_runs r LEFT JOIN businesses b ON b.slug = r.business
    WHERE r.id = ${id}`;
  if (!row) return null;
  const [files, decisions] = await Promise.all([listFiles(sql, id), listDecisions(sql, { runId: id })]);
  const { queue, ...run } = row;
  return { run, files, decisions, queue: openQueueItems(queue, decisions) };
}
