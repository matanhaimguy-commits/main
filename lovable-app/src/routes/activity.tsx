import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Card } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { listCommentsFn, listSendsFn } from "@/lib/api/inbox.functions";
import { dateTime } from "@/lib/format";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/activity")({
  head: () => ({ meta: [{ title: "Activity · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: ActivityPage,
});

const SEND_TONE: Record<string, "green" | "amber" | "red" | "gray" | "blue"> = {
  sent: "green",
  dry_run: "amber",
  failed: "red",
  unknown: "red",
  pending: "gray",
  skipped: "gray",
};

function ActivityPage() {
  const [tab, setTab] = useState("comments");
  const [outcome, setOutcome] = useState("");
  const [status, setStatus] = useState("");
  const comments = useQuery({
    queryKey: ["comments", outcome],
    queryFn: () => listCommentsFn({ data: outcome ? { outcome } : {} }),
    enabled: tab === "comments",
    refetchInterval: 15_000,
  });
  const sends = useQuery({
    queryKey: ["sends", status],
    queryFn: () => listSendsFn({ data: status ? { status } : {} }),
    enabled: tab === "sends",
    refetchInterval: 15_000,
  });

  return (
    <Shell title="Activity" description="Every comment and what the bot decided about it, and every message it sent (or would have sent in a dry run).">
      <Tabs value={tab} onValueChange={setTab}>
        <TabsList>
          <TabsTrigger value="comments">Comments</TabsTrigger>
          <TabsTrigger value="sends">Sends</TabsTrigger>
        </TabsList>

        <TabsContent value="comments" className="space-y-3">
          <select className="h-9 rounded-md border bg-background px-2 text-sm" value={outcome} onChange={(e) => setOutcome(e.target.value)}>
            <option value="">All comments</option>
            <option value="funnel">Matched a funnel</option>
            <option value="ai">Handled by the AI</option>
            <option value="skipped">Skipped</option>
          </select>
          {comments.isLoading && <LoadingBlock />}
          {comments.error && <ErrorBlock error={comments.error} />}
          {comments.data && (
            <Card>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>When</TableHead>
                    <TableHead>Who</TableHead>
                    <TableHead>Comment</TableHead>
                    <TableHead>Decision</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {comments.data.length === 0 && (
                    <TableRow>
                      <TableCell colSpan={4} className="py-8 text-center text-muted-foreground">
                        No comments yet.
                      </TableCell>
                    </TableRow>
                  )}
                  {comments.data.map((c) => (
                    <TableRow key={c.id}>
                      <TableCell className="whitespace-nowrap text-xs text-muted-foreground">
                        {dateTime(c.received_at)}
                        <div>
                          {c.platform === "instagram" ? "IG" : "FB"} · {c.business}
                        </div>
                      </TableCell>
                      <TableCell className="text-sm">
                        {c.contact_id ? (
                          <Link to="/inbox/$id" params={{ id: String(c.contact_id) }} className="underline">
                            {c.author_name ?? "open"}
                          </Link>
                        ) : (
                          (c.author_name ?? "—")
                        )}
                      </TableCell>
                      <TableCell className="max-w-xs text-sm">
                        <div className="line-clamp-3" dir="auto">{c.text}</div>
                        {c.post_id && <div className="truncate text-xs text-muted-foreground">post {c.post_id}</div>}
                      </TableCell>
                      <TableCell className="text-sm">
                        {c.outcome === "funnel" && <Pill tone="green">Funnel {c.funnel_id}</Pill>}
                        {c.outcome === "ai" && <Pill tone="blue">AI{c.ai_intent ? `: ${c.ai_intent}` : ""}</Pill>}
                        {c.outcome === "skipped" && (
                          <>
                            <Pill tone="gray">Skipped</Pill>
                            <div className="mt-1 text-xs text-muted-foreground">{c.explanation}</div>
                          </>
                        )}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Card>
          )}
        </TabsContent>

        <TabsContent value="sends" className="space-y-3">
          <select className="h-9 rounded-md border bg-background px-2 text-sm" value={status} onChange={(e) => setStatus(e.target.value)}>
            <option value="">All sends</option>
            <option value="sent">Sent</option>
            <option value="dry_run">Dry run (not sent)</option>
            <option value="failed">Failed</option>
            <option value="unknown">Unknown (timed out)</option>
            <option value="skipped">Skipped</option>
          </select>
          {sends.isLoading && <LoadingBlock />}
          {sends.error && <ErrorBlock error={sends.error} />}
          {sends.data && (
            <Card>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>When</TableHead>
                    <TableHead>To</TableHead>
                    <TableHead>Message</TableHead>
                    <TableHead>Status</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {sends.data.length === 0 && (
                    <TableRow>
                      <TableCell colSpan={4} className="py-8 text-center text-muted-foreground">
                        Nothing sent yet.
                      </TableCell>
                    </TableRow>
                  )}
                  {sends.data.map((s) => (
                    <TableRow key={s.id}>
                      <TableCell className="whitespace-nowrap text-xs text-muted-foreground">
                        {dateTime(s.created_at)}
                        <div>
                          {s.platform === "instagram" ? "IG" : "FB"} · {s.business}
                        </div>
                      </TableCell>
                      <TableCell className="text-sm">
                        {s.contact_id ? (
                          <Link to="/inbox/$id" params={{ id: String(s.contact_id) }} className="underline">
                            {s.username ? `@${s.username}` : "open"}
                          </Link>
                        ) : (
                          "—"
                        )}
                        <div className="text-xs text-muted-foreground">
                          {s.step ?? s.kind}
                          {s.funnel_id ? ` · ${s.funnel_id}` : ""}
                        </div>
                      </TableCell>
                      <TableCell className="max-w-sm text-sm">
                        <div className="line-clamp-3 whitespace-pre-wrap" dir="auto">{s.preview}</div>
                        {s.error_message && (
                          <div className="mt-1 text-xs text-rose-700">
                            {s.error_code ? `${s.error_code}: ` : ""}
                            {s.error_message}
                          </div>
                        )}
                      </TableCell>
                      <TableCell>
                        <Pill tone={SEND_TONE[s.status] ?? "gray"}>{s.status === "sent" ? (s.read_at ? "read" : s.delivered_at ? "delivered" : "sent") : s.status.replace("_", " ")}</Pill>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Card>
          )}
        </TabsContent>
      </Tabs>
    </Shell>
  );
}
