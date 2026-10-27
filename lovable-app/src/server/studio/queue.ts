import type { QueueItem } from "./types";

/** Matches a decision key to a ledger queue id ("G-HUMAN-SONG:" and "G-HUMAN-SONG" are the same). */
const queueKey = (s: string) => s.trim().replace(/:$/, "");

const text = (v: unknown) => (typeof v === "string" ? v : "");

/** The ledger's open human-queue items that no question on the page covers yet (answered in chat today). */
export function openQueueItems(queue: unknown, decisions: { key: string }[]): QueueItem[] {
  if (!Array.isArray(queue)) return [];
  const covered = new Set(decisions.map((d) => queueKey(d.key)));
  return queue
    .filter((q): q is Record<string, unknown> => !!q && typeof q === "object" && (q as Record<string, unknown>)["status"] === "PENDING")
    .map((q) => ({
      id: String(q["id"] ?? q["checkpoint"] ?? ""),
      checkpoint: text(q["checkpoint"]),
      asset: text(q["asset"]) || null,
      note: text(q["note"]),
      asked_at: text(q["asked_at"]) || null,
    }))
    .filter((q) => !covered.has(queueKey(q.id)));
}
