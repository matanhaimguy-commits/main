// @vitest-environment node
import { describe, expect, it } from "vitest";
import { sortRuns } from "./order";

describe("studio list order", () => {
  it("puts pieces with a question first, then the others waiting on the owner, then those in progress, newest first", () => {
    const at = (h: number) => new Date(Date.UTC(2026, 9, 27, h));
    const order = sortRuns([
      { id: 1, status: "done" as const, waiting: false, updated_at: at(9) },
      { id: 2, status: "active" as const, waiting: false, updated_at: at(10) },
      { id: 3, status: "active" as const, waiting: true, open_decisions: 1, updated_at: at(8) },
      { id: 4, status: "paused" as const, waiting: false, updated_at: at(11) },
      { id: 5, status: "blocked" as const, waiting: false, updated_at: at(12) },
      { id: 6, status: "active" as const, waiting: true, open_decisions: 0, updated_at: at(13) },
    ]).map((r) => r.id);
    expect(order).toEqual([3, 6, 5, 2, 4, 1]);
  });
});
