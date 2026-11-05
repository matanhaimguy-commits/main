import type { StudioRunCard, StudioStepView } from "@/lib/api/studio";

/** Words and colours for step, gate and run states, shared by the Studio components. */

export type StepStatus = StudioStepView["status"];
export type GateStatus = StudioStepView["gates"][number]["status"];
export type RunStatus = StudioRunCard["status"];

export const STEP_LABEL: Record<StepStatus, string> = {
  done: "Done",
  active: "Now",
  blocked: "Blocked",
  na: "Not needed",
  pending: "Next",
};

export const STEP_TEXT_TONE: Record<StepStatus, string> = {
  done: "text-emerald-700",
  active: "text-sky-700",
  blocked: "text-rose-700",
  na: "text-muted-foreground",
  pending: "text-muted-foreground",
};

export const GATE_WORD: Record<GateStatus, string> = { PASS: "Pass", OVERRIDE: "Override", FAIL: "Fail", PENDING: "Open" };

export const RUN_LABEL: Record<RunStatus, string> = { active: "In progress", blocked: "Blocked", done: "Done", paused: "Paused" };
