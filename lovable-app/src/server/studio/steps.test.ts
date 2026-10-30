// @vitest-environment node
import { describe, expect, it } from "vitest";
import { currentStepOf, progressOf, runStatusOf } from "./steps";
import { step } from "./test-fixtures";

describe("studio steps", () => {
  it("finds the current step: the first one neither done nor skipped", () => {
    expect(currentStepOf([step(0, "done"), step(1, "na"), step(2, "active"), step(3, "pending")])).toBe(2);
    expect(currentStepOf([step(0, "done"), step(1, "na")])).toBeNull();
  });

  it("works out the run's status", () => {
    expect(runStatusOf([step(0, "done"), step(1, "na")])).toBe("done");
    expect(runStatusOf([step(0, "done"), step(1, "blocked"), step(2, "pending")])).toBe("blocked");
    expect(runStatusOf([step(0, "done"), step(1, "active")])).toBe("active");
    expect(runStatusOf([])).toBe("active");
  });

  it("counts progress over the steps that apply", () => {
    expect(progressOf([step(0, "done"), step(1, "na"), step(2, "active"), step(3, "pending")])).toEqual({ done: 1, total: 3 });
  });
});
