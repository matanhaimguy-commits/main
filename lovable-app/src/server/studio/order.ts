import type { RunStatus } from "./schema";

export interface RunOrderKey {
  id: number;
  status: RunStatus;
  waiting: boolean;
  open_decisions?: number;
  updated_at: Date | string;
}

const rank = (r: RunOrderKey) =>
  (r.open_decisions ?? 0) > 0 ? 0 : r.waiting ? 1 : r.status === "active" || r.status === "blocked" ? 2 : r.status === "paused" ? 3 : 4;

/**
 * The Studio list's order: pieces with a question to answer here first, then the others waiting on the owner,
 * then the ones in progress, then paused and finished ones; newest first within each.
 */
export function sortRuns<T extends RunOrderKey>(runs: T[]): T[] {
  const time = (r: T) => new Date(r.updated_at).getTime();
  return [...runs].sort((a, b) => rank(a) - rank(b) || time(b) - time(a) || b.id - a.id);
}
