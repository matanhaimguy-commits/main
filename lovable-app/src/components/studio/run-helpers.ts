import type { StudioDecisionView, StudioFileView, StudioRunView } from "@/lib/api/studio";

/** Small questions the run page asks of its data. */

export function decisionsByStatus(decisions: StudioDecisionView[]) {
  return {
    open: decisions.filter((d) => d.status === "open"),
    answered: decisions.filter((d) => d.status === "answered"),
    synced: decisions.filter((d) => d.status === "synced"),
  };
}

/** The steps that start open: the current one and every step with an open question. */
export function initiallyOpenSteps(run: StudioRunView): Set<number> {
  const s = new Set<number>();
  if (run.run.current_step != null) s.add(run.run.current_step);
  for (const d of run.decisions) if (d.status === "open" && d.step != null) s.add(d.step);
  return s;
}

export const filesOfStep = (files: StudioFileView[], step: number | null) => files.filter((f) => f.step === step);

/** The pictures, audio and video of a question's step, shown right under the question. */
export const mediaOfStep = (files: StudioFileView[], step: number | null) =>
  step == null ? [] : files.filter((f) => f.step === step && f.kind !== "doc" && f.url);
