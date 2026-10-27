import { Card, CardContent } from "@/components/ui/card";
import type { StudioRunHeader } from "@/lib/api/studio";
import { timeAgo } from "@/lib/format";
import { ProgressLine } from "./progress-line";
import { RunStatusPill } from "./run-status-pill";
import { StepBar } from "./step-bar";
import { WaitingBadge } from "./waiting-badge";

/** The top of a run's page: waiting badge and status, the progress bar, the current step and the studio's summary. */
export function RunHeaderCard({ run, openQuestions }: { run: StudioRunHeader; openQuestions: number }) {
  return (
    <Card>
      <CardContent className="space-y-3 p-4">
        <div className="flex flex-wrap items-center gap-2">
          {openQuestions > 0 && <WaitingBadge />}
          <RunStatusPill status={run.status} />
          <span className="ml-auto text-xs text-muted-foreground">updated {timeAgo(run.pushed_at)}</span>
        </div>
        {run.steps.length > 0 ? (
          <>
            <StepBar steps={run.steps} />
            <ProgressLine status={run.status} current={run.steps.find((s) => s.n === run.current_step)} progress={run.progress} />
          </>
        ) : (
          <p className="text-sm text-muted-foreground">This is a {run.family ?? "library"} run: it has no production steps, only its files and questions.</p>
        )}
        {run.summary && (
          <p dir="auto" className="text-sm text-muted-foreground">
            {run.summary}
          </p>
        )}
      </CardContent>
    </Card>
  );
}
