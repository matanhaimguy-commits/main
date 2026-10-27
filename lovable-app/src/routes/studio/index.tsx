import { useQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import { ErrorBlock, LoadingBlock, Shell } from "@/components/app/shell";
import { EmptyState } from "@/components/studio/empty-state";
import { filterRuns } from "@/components/studio/list-views";
import { RunCard } from "@/components/studio/run-card";
import { RunListFilters } from "@/components/studio/run-list-filters";
import { WaitingNotice } from "@/components/studio/waiting-notice";
import { listStudioRunsFn } from "@/lib/api/studio";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/studio/")({
  head: () => ({ meta: [{ title: "Studio · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: StudioPage,
});

function StudioPage() {
  const [view, setView] = useState("progress");
  const [business, setBusiness] = useState("");
  const runs = useQuery({ queryKey: ["studio"], queryFn: () => listStudioRunsFn({ data: {} }), refetchInterval: 30_000 });
  const shown = filterRuns(runs.data ?? [], view, business);

  return (
    <Shell title="Studio" description="Every piece the studio is making, step by step. When a piece needs your call it waits at the top; open it to answer.">
      <WaitingNotice count={(runs.data ?? []).filter((r) => r.waiting).length} />
      <RunListFilters runs={runs.data} view={view} onView={setView} business={business} onBusiness={setBusiness} />
      {runs.isLoading && <LoadingBlock />}
      {runs.error && <ErrorBlock error={runs.error} />}
      {runs.data && shown.length === 0 && <EmptyState>Nothing here yet. The studio shows each piece here as it works on it (hub.py studio-push).</EmptyState>}
      <div className="grid gap-3 lg:grid-cols-2">
        {shown.map((r) => (
          <RunCard key={r.id} run={r} />
        ))}
      </div>
    </Shell>
  );
}
