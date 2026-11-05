import type { StudioDecisionView, StudioRunView } from "@/lib/api/studio";
import { DecisionCard } from "./decision-card";
import { mediaOfStep } from "./run-helpers";
import { useAnswer } from "./use-answer";

/** A titled list of question cards for one run; nothing when the list is empty. */
export function DecisionList({
  title,
  decisions,
  run,
  canAnswer,
}: {
  title: string;
  decisions: StudioDecisionView[];
  run: StudioRunView;
  canAnswer: boolean;
}) {
  const answer = useAnswer(run.run.id);
  if (decisions.length === 0) return null;
  return (
    <section className="space-y-3">
      <h2 className="text-base font-semibold">{title}</h2>
      {decisions.map((d) => (
        <DecisionCard
          key={d.id}
          decision={d}
          step={run.run.steps.find((s) => s.n === d.step)}
          media={mediaOfStep(run.files, d.step)}
          canAnswer={canAnswer}
          onAnswer={answer}
        />
      ))}
    </section>
  );
}
