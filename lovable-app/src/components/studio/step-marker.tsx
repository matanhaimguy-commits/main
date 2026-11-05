import { Check, Minus, TriangleAlert } from "lucide-react";
import { cn } from "@/lib/utils";
import type { StepStatus } from "./labels";

const TONE: Record<StepStatus, string> = {
  done: "bg-emerald-500 text-white",
  active: "bg-sky-50 text-sky-700 ring-2 ring-sky-500",
  blocked: "bg-rose-500 text-white",
  na: "border border-dashed border-muted-foreground/40 bg-background text-muted-foreground",
  pending: "border-2 border-muted-foreground/25 bg-background text-muted-foreground",
};

/** The circle on the timeline: a tick when done, a warning when blocked, a dash when skipped, else the number. */
export function StepMarker({ n, status }: { n: number; status: StepStatus }) {
  return (
    <span className={cn("relative z-[1] flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-xs font-semibold", TONE[status])} aria-hidden>
      {status === "done" ? <Check className="h-4 w-4" /> : status === "blocked" ? <TriangleAlert className="h-4 w-4" /> : status === "na" ? <Minus className="h-4 w-4" /> : n}
    </span>
  );
}
