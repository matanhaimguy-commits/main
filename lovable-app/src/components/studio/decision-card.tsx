import { useState } from "react";
import { Pill } from "@/components/app/shell";
import { Card, CardContent } from "@/components/ui/card";
import type { StudioDecisionView, StudioFileView, StudioStepView } from "@/lib/api/studio";
import { timeAgo } from "@/lib/format";
import { cn } from "@/lib/utils";
import { AnswerForm } from "./answer-form";
import { AnswerSummary } from "./answer-summary";
import { DecisionContext } from "./decision-context";
import { FileView } from "./file-view";

/**
 * One checkpoint question: what is asked, its background, the step's pictures and sound, then the answer form
 * (open, or when changing an answer) or the answer given.
 */
export function DecisionCard({
  decision: d,
  step,
  media,
  canAnswer,
  onAnswer,
}: {
  decision: StudioDecisionView;
  step?: Pick<StudioStepView, "n" | "name">;
  media: StudioFileView[];
  canAnswer: boolean;
  onAnswer: (decisionId: number, choices: string[], note: string) => Promise<boolean>;
}) {
  const [changing, setChanging] = useState(false);
  const showForm = d.status === "open" || (changing && d.status === "answered");
  const send = async (choices: string[], note: string) => {
    const ok = await onAnswer(d.id, choices, note);
    if (ok) setChanging(false);
    return ok;
  };
  return (
    <Card className={cn(d.status === "open" ? "border-amber-300 ring-1 ring-amber-200" : d.status === "answered" && "border-emerald-200")}>
      <CardContent className="space-y-3 p-4">
        <div className="flex flex-wrap items-center gap-2">
          <Pill tone={d.status === "open" ? "amber" : d.status === "answered" ? "green" : "gray"}>{d.checkpoint}</Pill>
          {step && (
            <span className="text-xs text-muted-foreground">
              Step {step.n} · {step.name}
            </span>
          )}
          <span className="ml-auto text-xs text-muted-foreground">asked {timeAgo(d.created_at)}</span>
        </div>
        <p dir="auto" className="whitespace-pre-wrap text-base font-medium leading-snug">
          {d.question}
        </p>
        {d.context && <DecisionContext context={d.context} />}
        {media.length > 0 && d.status !== "synced" && (
          <div className="space-y-3">
            {media.map((f) => (
              <FileView key={f.id} file={f} compact />
            ))}
          </div>
        )}
        {showForm ? (
          <AnswerForm decision={d} canAnswer={canAnswer} onSend={send} onCancel={d.status === "answered" ? () => setChanging(false) : undefined} />
        ) : (
          <AnswerSummary decision={d} onChange={canAnswer ? () => setChanging(true) : undefined} />
        )}
      </CardContent>
    </Card>
  );
}
