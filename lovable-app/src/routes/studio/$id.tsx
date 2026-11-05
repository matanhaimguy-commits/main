import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowLeft } from "lucide-react";
import { ErrorBlock, LoadingBlock, Shell } from "@/components/app/shell";
import { DecisionList } from "@/components/studio/decision-list";
import { QueueCard } from "@/components/studio/queue-card";
import { RunFiles } from "@/components/studio/run-files";
import { RunHeaderCard } from "@/components/studio/run-header-card";
import { decisionsByStatus, filesOfStep } from "@/components/studio/run-helpers";
import { StepTimeline } from "@/components/studio/step-timeline";
import { Button } from "@/components/ui/button";
import { getSession } from "@/lib/api/session.functions";
import { getStudioRunFn } from "@/lib/api/studio";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/studio/$id")({
  head: () => ({ meta: [{ title: "Studio · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: RunPage,
});

function RunPage() {
  const runId = Number(Route.useParams().id);
  const q = useQuery({
    queryKey: ["studio-run", runId],
    queryFn: () => getStudioRunFn({ data: { id: runId } }),
    enabled: Number.isInteger(runId) && runId > 0,
    refetchInterval: 30_000,
  });
  const session = useQuery({ queryKey: ["session"], queryFn: () => getSession(), staleTime: 60_000 });
  const canAnswer = session.data?.role === "admin";
  const d = q.data;
  const asks = d ? decisionsByStatus(d.decisions) : null;

  return (
    <Shell
      title={d ? d.run.title || d.run.post_id : "Studio"}
      description={d && [d.run.business_name, d.run.format, d.run.title ? d.run.post_id : null].filter(Boolean).join(" · ")}
      actions={
        <Button variant="outline" asChild>
          <Link to="/studio">
            <ArrowLeft /> Studio
          </Link>
        </Button>
      }
    >
      {q.isLoading && <LoadingBlock />}
      {q.error && <ErrorBlock error={q.error} />}
      {q.data === null && <ErrorBlock error="This piece is not in the Studio (any more)." />}
      {d && asks && (
        <div className="mx-auto max-w-3xl space-y-6">
          <RunHeaderCard run={d.run} openQuestions={asks.open.length} />
          <DecisionList title={asks.open.length ? "Your call" : "Your answers"} decisions={[...asks.open, ...asks.answered]} run={d} canAnswer={canAnswer} />
          <QueueCard items={d.queue} />
          <StepTimeline key={d.run.id} run={d} />
          <RunFiles files={filesOfStep(d.files, null)} />
          <DecisionList title="Earlier decisions" decisions={asks.synced} run={d} canAnswer={false} />
        </div>
      )}
    </Shell>
  );
}
