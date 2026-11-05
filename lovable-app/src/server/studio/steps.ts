import type { RunStatus, StudioStep } from "./schema";

/** Where a run stands, worked out from its steps only. */

type StepLike = Pick<StudioStep, "n" | "status">;

const settled = (s: Pick<StudioStep, "status">) => s.status === "done" || s.status === "na";

/** The step being worked on: the first one that is neither done nor skipped. */
export function currentStepOf(steps: StepLike[]): number | null {
  return steps.find((s) => !settled(s))?.n ?? null;
}

export function runStatusOf(steps: StepLike[]): RunStatus {
  if (steps.length > 0 && steps.every(settled)) return "done";
  return steps.find((s) => !settled(s))?.status === "blocked" ? "blocked" : "active";
}

/** Steps done out of the steps that apply (skipped ones don't count). */
export function progressOf(steps: Pick<StudioStep, "status">[]): { done: number; total: number } {
  const counted = steps.filter((s) => s.status !== "na");
  return { done: counted.filter((s) => s.status === "done").length, total: counted.length };
}
