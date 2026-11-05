import { Link } from "@tanstack/react-router";
import { ChevronRight } from "lucide-react";
import type { StudioRunCard } from "@/lib/api/studio";
import { timeAgo } from "@/lib/format";
import { cn } from "@/lib/utils";
import { ProgressLine } from "./progress-line";
import { RunStatusPill } from "./run-status-pill";
import { StepBar } from "./step-bar";
import { WaitingBadge } from "./waiting-badge";

/** One piece in the Studio list: the whole card opens it. */
export function RunCard({ run }: { run: StudioRunCard }) {
  const current = run.steps.find((s) => s.n === run.current_step);
  return (
    <Link
      to="/studio/$id"
      params={{ id: String(run.id) }}
      className={cn(
        "block rounded-xl border bg-background p-4 shadow-sm transition-colors hover:bg-accent/40 active:bg-accent/60",
        run.waiting && "border-amber-300 ring-1 ring-amber-200",
      )}
    >
      <div className="flex flex-wrap items-center gap-2">
        {run.waiting ? (
          <WaitingBadge>{run.open_decisions > 1 ? `${run.open_decisions} questions for you` : "Waiting on you"}</WaitingBadge>
        ) : (
          <RunStatusPill status={run.status} />
        )}
        <span className="ml-auto text-xs text-muted-foreground">{timeAgo(run.updated_at)}</span>
      </div>
      <div className="mt-2 flex items-start gap-2">
        <div className="min-w-0 flex-1">
          <div dir="auto" className="text-base font-semibold leading-snug">
            {run.title || run.post_id}
          </div>
          <div className="mt-0.5 truncate text-xs text-muted-foreground">
            {[run.business_name, run.format, run.title ? run.post_id : null].filter(Boolean).join(" · ")}
          </div>
        </div>
        <ChevronRight className="mt-1 h-5 w-5 shrink-0 text-muted-foreground" />
      </div>
      {run.steps.length > 0 ? (
        <div className="mt-3 space-y-2">
          <StepBar steps={run.steps} />
          <ProgressLine status={run.status} current={current} progress={run.progress} />
        </div>
      ) : (
        <div className="mt-3 text-xs text-muted-foreground">No production steps ({run.family ?? "library"} run).</div>
      )}
      {run.summary && (
        <p dir="auto" className="mt-1.5 line-clamp-2 text-sm text-muted-foreground">
          {run.summary}
        </p>
      )}
    </Link>
  );
}
