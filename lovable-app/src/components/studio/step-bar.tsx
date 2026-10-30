import { cn } from "@/lib/utils";
import { STEP_LABEL, type StepStatus } from "./labels";

const SEGMENT: Record<StepStatus, string> = {
  done: "bg-emerald-500",
  active: "bg-sky-500",
  blocked: "bg-rose-500",
  na: "border border-dashed border-muted-foreground/30 bg-transparent",
  pending: "bg-muted-foreground/20",
};

/** The progress bar: one segment per step, in order. Nothing when the run has no steps. */
export function StepBar({ steps, className }: { steps: { n: number; name: string; status: StepStatus }[]; className?: string }) {
  if (steps.length === 0) return null;
  const counted = steps.filter((s) => s.status !== "na");
  const done = counted.filter((s) => s.status === "done").length;
  return (
    <div className={cn("flex h-2.5 gap-[3px]", className)} role="img" aria-label={`${done} of ${counted.length} steps done`}>
      {steps.map((s) => (
        <div key={s.n} title={`${s.n} ${s.name}: ${STEP_LABEL[s.status]}`} className={cn("h-full min-w-0 flex-1 rounded-full", SEGMENT[s.status])} />
      ))}
    </div>
  );
}
