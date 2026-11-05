import { describe, expect, it } from "vitest";
import { gateLabel, latestGates } from "./gates";
import { businessesOf, filterRuns } from "./list-views";
import { canSend, pick } from "./pick";
import { decisionsByStatus, filesOfStep, initiallyOpenSteps, mediaOfStep } from "./run-helpers";
import { scoreText } from "./score";
import { decisionView, fileView, runCard, runView } from "./test-fixtures";

describe("studio page helpers", () => {
  it("keeps the latest record per gate and asset, in first-seen order", () => {
    const gates = latestGates([
      { gate: "G-SCRIPT", status: "FAIL", score: 81 },
      { gate: "G-VIS", status: "PASS", asset: "SB@v1" },
      { gate: "G-SCRIPT", status: "PASS", score: 86 },
    ]);
    expect(gates.map((g) => [g.gate, g.status])).toEqual([
      ["G-SCRIPT", "PASS"],
      ["G-VIS", "PASS"],
    ]);
    expect(gateLabel({ gate: "G-VIS", status: "PASS", asset: "SB@v1", label: "Visual review" })).toBe("SB@v1 Visual review");
    expect(gateLabel({ gate: "G-X", status: "PENDING" })).toBe("G-X");
  });

  it("writes scores out of 100 unless told otherwise", () => {
    expect(scoreText(86, undefined)).toBe("86/100");
    expect(scoreText(8.5, 10)).toBe("8.5/10");
    expect(scoreText(undefined, 100)).toBeNull();
  });

  it("picks one option, or several in a multi-select question", () => {
    expect(pick([], "A", false)).toEqual(["A"]);
    expect(pick(["A"], "B", false)).toEqual(["B"]);
    expect(pick(["A"], "A", false)).toEqual([]);
    expect(pick(["A"], "B", true)).toEqual(["A", "B"]);
    expect(pick(["A", "B"], "A", true)).toEqual(["B"]);
    expect(canSend([], " ")).toBe(false);
    expect(canSend([], "a note")).toBe(true);
  });

  it("filters the list by tab and business, and names each business once", () => {
    const runs = [runCard(1), runCard(2, { status: "done" }), runCard(3, { business: "zeta", business_name: "Zeta" })];
    expect(filterRuns(runs, "progress", "").map((r) => r.id)).toEqual([1, 3]);
    expect(filterRuns(runs, "done", "").map((r) => r.id)).toEqual([2]);
    expect(filterRuns(runs, "all", "zeta").map((r) => r.id)).toEqual([3]);
    expect(businessesOf(runs)).toEqual([
      ["acme", "Acme"],
      ["zeta", "Zeta"],
    ]);
  });

  it("opens the current step and the steps with an open question", () => {
    const run = runView({ decisions: [decisionView(1, { step: 7 }), decisionView(2, { step: 9, status: "answered" })] });
    expect([...initiallyOpenSteps(run)].sort()).toEqual([3, 7]);
    expect(decisionsByStatus(run.decisions).answered.map((d) => d.id)).toEqual([2]);
  });

  it("finds a step's files, and the media shown under its question", () => {
    const files = [fileView(1, "doc", { step: 4 }), fileView(2, "audio", { step: 4 }), fileView(3, "image", { step: 5 }), fileView(4, "image")];
    expect(filesOfStep(files, 4).map((f) => f.id)).toEqual([1, 2]);
    expect(filesOfStep(files, null).map((f) => f.id)).toEqual([4]);
    expect(mediaOfStep(files, 4).map((f) => f.id)).toEqual([2]);
    expect(mediaOfStep(files, null)).toEqual([]);
  });
});
