// @vitest-environment node
import { describe, expect, it } from "vitest";
import { openQueueItems } from "./queue";

describe("studio queue", () => {
  it("lists the ledger's open queue items that no question on the page covers", () => {
    const queue = [
      { id: "G-HUMAN-SONG:", checkpoint: "G-HUMAN-SONG", asset: null, status: "PENDING", note: "listen", asked_at: "2026-10-27T10:00:00+00:00" },
      { id: "G-HUMAN-TEST:R1", checkpoint: "G-HUMAN-TEST", asset: "R1", status: "PENDING", note: "re-test" },
      { id: "G-HUMAN-LOOK:", checkpoint: "G-HUMAN-LOOK", status: "APPROVED", note: "done" },
    ];
    expect(openQueueItems(queue, [{ key: "G-HUMAN-SONG" }])).toEqual([
      { id: "G-HUMAN-TEST:R1", checkpoint: "G-HUMAN-TEST", asset: "R1", note: "re-test", asked_at: null },
    ]);
  });

  it("takes anything that isn't a list as an empty queue", () => {
    expect(openQueueItems(undefined, [])).toEqual([]);
    expect(openQueueItems({ id: "x" }, [])).toEqual([]);
  });
});
