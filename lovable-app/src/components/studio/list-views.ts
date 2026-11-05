import type { StudioRunCard } from "@/lib/api/studio";

/** The Studio list's tabs and filters. */

export const LIST_VIEWS: { id: string; label: string; match: (r: StudioRunCard) => boolean }[] = [
  { id: "progress", label: "In progress", match: (r) => r.status !== "done" },
  { id: "done", label: "Done", match: (r) => r.status === "done" },
  { id: "all", label: "All", match: () => true },
];

/** [slug, name] of every business that has a run, in first-seen order. */
export function businessesOf(runs: StudioRunCard[]): [string, string][] {
  const seen = new Map<string, string>();
  for (const r of runs) seen.set(r.business, r.business_name);
  return [...seen.entries()];
}

/** The runs a tab and business filter show, keeping the server's order (waiting on the owner first). */
export function filterRuns(runs: StudioRunCard[], view: string, business: string): StudioRunCard[] {
  const v = LIST_VIEWS.find((x) => x.id === view) ?? LIST_VIEWS[0]!;
  return runs.filter((r) => v.match(r) && (!business || r.business === business));
}
