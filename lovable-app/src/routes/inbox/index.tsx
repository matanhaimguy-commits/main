import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { businessSlugsFn } from "@/lib/api/businesses.functions";
import { listContactsFn } from "@/lib/api/inbox.functions";
import { STAGE_TONE, timeAgo } from "@/lib/format";
import { requireLogin } from "@/lib/session";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/inbox/")({
  head: () => ({ meta: [{ title: "Inbox · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: InboxPage,
});

const STAGES = ["new", "engaged", "qualified", "hot", "booked", "won", "lost"];

function InboxPage() {
  const [business, setBusiness] = useState("");
  const [stage, setStage] = useState("");
  const [search, setSearch] = useState("");
  const slugs = useQuery({ queryKey: ["business-slugs"], queryFn: () => businessSlugsFn() });
  const list = useQuery({
    queryKey: ["contacts", business, stage, search],
    queryFn: () =>
      listContactsFn({ data: { ...(business ? { business } : {}), ...(stage ? { stage } : {}), ...(search.trim() ? { search: search.trim() } : {}) } }),
    refetchInterval: 15_000,
  });

  return (
    <Shell title="Inbox" description="Everyone who commented or wrote, newest first. Open a conversation to read it, take over, or update the lead.">
      <div className="mb-4 flex flex-wrap gap-2">
        {(slugs.data?.length ?? 0) > 1 && (
          <select className="h-9 rounded-md border bg-background px-2 text-sm" value={business} onChange={(e) => setBusiness(e.target.value)}>
            <option value="">All businesses</option>
            {slugs.data!.map((b) => (
              <option key={b.slug} value={b.slug}>
                {b.name}
              </option>
            ))}
          </select>
        )}
        <Input className="h-9 max-w-xs" placeholder="Search name, username, email, phone" value={search} onChange={(e) => setSearch(e.target.value)} />
      </div>
      <div className="mb-4 flex flex-wrap gap-1.5">
        <button
          className={cn("rounded-full border px-3 py-1 text-xs", stage === "" ? "bg-primary text-primary-foreground" : "bg-background")}
          onClick={() => setStage("")}
        >
          All
        </button>
        {STAGES.map((s) => (
          <button
            key={s}
            className={cn("rounded-full border px-3 py-1 text-xs capitalize", stage === s ? "bg-primary text-primary-foreground" : "bg-background")}
            onClick={() => setStage(stage === s ? "" : s)}
          >
            {s} {list.data?.stages[s] ? `(${list.data.stages[s]})` : ""}
          </button>
        ))}
      </div>

      {list.isLoading && <LoadingBlock />}
      {list.error && <ErrorBlock error={list.error} />}
      {list.data && list.data.contacts.length === 0 && (
        <Card>
          <CardContent className="p-10 text-center text-sm text-muted-foreground">No conversations yet.</CardContent>
        </Card>
      )}
      {list.data && list.data.contacts.length > 0 && (
        <Card>
          <div className="divide-y">
            {list.data.contacts.map((c) => {
              const paused = c.ai_paused_until && new Date(c.ai_paused_until).getTime() > Date.now();
              const last = [c.last_inbound_at, c.last_outbound_at].filter(Boolean).map((d) => new Date(d!).getTime());
              return (
                <Link key={c.id} to="/inbox/$id" params={{ id: String(c.id) }} className="flex items-center gap-3 px-4 py-3 hover:bg-accent/40">
                  <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-muted text-xs font-semibold uppercase">
                    {(c.name ?? c.username ?? "?").slice(0, 2)}
                  </div>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2">
                      <span className="truncate font-medium">{c.name ?? (c.username ? `@${c.username}` : "Unknown")}</span>
                      <span className="text-xs text-muted-foreground">{c.platform === "instagram" ? "IG" : c.platform === "web" ? "FORM" : "FB"}</span>
                    </div>
                    <div className="truncate text-sm text-muted-foreground" dir="auto">
                      {c.last_direction === "out" ? "You: " : ""}
                      {c.last_text ?? c.source ?? ""}
                    </div>
                  </div>
                  <div className="flex shrink-0 flex-col items-end gap-1">
                    <span className="text-xs text-muted-foreground">{last.length ? timeAgo(new Date(Math.max(...last))) : ""}</span>
                    <div className="flex gap-1">
                      {c.opted_out && <Pill tone="red">opted out</Pill>}
                      {paused && <Pill tone="gray">AI paused</Pill>}
                      <Pill tone={STAGE_TONE[c.stage] ?? "gray"}>{c.stage}</Pill>
                    </div>
                  </div>
                </Link>
              );
            })}
          </div>
        </Card>
      )}
    </Shell>
  );
}
