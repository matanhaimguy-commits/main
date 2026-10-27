import { useState } from "react";
import type { StudioRunView } from "@/lib/api/studio";
import { filesOfStep, initiallyOpenSteps } from "./run-helpers";
import { StepRow } from "./step-row";

/** The vertical timeline of steps 0-15. The current step and steps with an open question start open. */
export function StepTimeline({ run }: { run: StudioRunView }) {
  const [open, setOpen] = useState<Set<number>>(() => initiallyOpenSteps(run));
  const toggle = (n: number) =>
    setOpen((prev) => {
      const next = new Set(prev);
      if (next.has(n)) next.delete(n);
      else next.add(n);
      return next;
    });
  const steps = run.run.steps;
  if (steps.length === 0) return null;
  return (
    <section>
      <h2 className="mb-3 text-base font-semibold">Steps</h2>
      <ol>
        {steps.map((s, i) => (
          <StepRow
            key={s.n}
            step={s}
            last={i === steps.length - 1}
            files={filesOfStep(run.files, s.n)}
            asks={run.decisions.filter((d) => d.status === "open" && d.step === s.n).length}
            open={open.has(s.n)}
            onToggle={() => toggle(s.n)}
          />
        ))}
      </ol>
    </section>
  );
}
