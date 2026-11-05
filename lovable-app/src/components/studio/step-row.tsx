import { ChevronDown } from "lucide-react";
import type { StudioFileView, StudioStepView } from "@/lib/api/studio";
import { cn } from "@/lib/utils";
import { STEP_LABEL, STEP_TEXT_TONE } from "./labels";
import { StepDetails } from "./step-details";
import { StepMarker } from "./step-marker";
import { StepSummary } from "./step-summary";

/** One step on the timeline: marker and line on the left, a card that opens to its gates, notes and files. */
export function StepRow({
  step,
  last,
  files,
  asks,
  open,
  onToggle,
}: {
  step: StudioStepView;
  last: boolean;
  files: StudioFileView[];
  /** Open questions on this step. */
  asks: number;
  open: boolean;
  onToggle: () => void;
}) {
  const hasDetail = step.gates.length > 0 || files.length > 0 || !!step.note;
  return (
    <li className="relative flex gap-3 pb-2">
      {!last && <div className={cn("absolute bottom-0 left-4 top-8 w-px", step.status === "done" ? "bg-emerald-300" : "bg-border")} aria-hidden />}
      <div className="pt-2">
        <StepMarker n={step.n} status={step.status} />
      </div>
      <div
        className={cn(
          "min-w-0 flex-1 rounded-xl border bg-background",
          step.status === "active" && "border-sky-300 shadow-sm",
          step.status === "blocked" && "border-rose-300",
          step.status === "na" && "border-dashed bg-transparent opacity-70",
        )}
      >
        <button
          type="button"
          onClick={onToggle}
          aria-expanded={open}
          disabled={!hasDetail}
          className="flex min-h-12 w-full items-start gap-2 px-3 py-2.5 text-left disabled:cursor-default"
        >
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-baseline gap-x-2">
              <span className="font-medium">{step.name}</span>
              <span className={cn("text-xs font-medium", STEP_TEXT_TONE[step.status])}>{STEP_LABEL[step.status]}</span>
              {asks > 0 && <span className="text-xs font-semibold text-amber-700">· your call</span>}
            </div>
            {!open && <StepSummary step={step} files={files.length} />}
          </div>
          {hasDetail && <ChevronDown className={cn("mt-0.5 h-5 w-5 shrink-0 text-muted-foreground transition-transform", open && "rotate-180")} />}
        </button>
        {open && hasDetail && <StepDetails step={step} files={files} />}
      </div>
    </li>
  );
}
