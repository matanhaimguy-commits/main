import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import type { DecisionStatus } from "./schema";

export interface SyncResult {
  synced: number[];
  already: number[];
  problems: { id: number; error: string }[];
}

/** The studio took these answers in. Open questions can't be marked; already synced ones are left as they are. */
export async function markSynced(sql: Sql, ids: number[]): Promise<SyncResult> {
  const unique = [...new Set(ids)];
  if (!unique.length) return { synced: [], already: [], problems: [] };
  const done = await sql<{ id: number }[]>`
    UPDATE studio_decisions SET status = 'synced', synced_at = now(), updated_at = now()
    WHERE id IN ${sql(unique)} AND status = 'answered'
    RETURNING id`;
  const synced = done.map((r) => Number(r.id));
  const rest = unique.filter((id) => !synced.includes(id));
  const found = rest.length ? await sql<{ id: number; status: DecisionStatus }[]>`SELECT id, status FROM studio_decisions WHERE id IN ${sql(rest)}` : [];
  const result: SyncResult = { synced, already: [], problems: [] };
  for (const id of rest) {
    const status = found.find((r) => Number(r.id) === id)?.status;
    if (!status) result.problems.push({ id, error: "No such decision." });
    else if (status === "synced") result.already.push(id);
    else result.problems.push({ id, error: "Still open: the owner hasn't answered it." });
  }
  return result;
}
