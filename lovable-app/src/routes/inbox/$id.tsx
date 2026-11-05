import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowLeft } from "lucide-react";
import { useEffect, useState } from "react";
import { toast } from "sonner";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { getConversationFn, setAiPausedFn, updateContactFn } from "@/lib/api/inbox.functions";
import { dateTime, errorText, timeAgo } from "@/lib/format";
import { requireLogin } from "@/lib/session";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/inbox/$id")({
  head: () => ({ meta: [{ title: "Conversation · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: ConversationPage,
});

const STAGES = ["new", "engaged", "qualified", "hot", "booked", "won", "lost"];
const SOURCE_LABEL: Record<string, string> = {
  user: "",
  comment: "comment",
  funnel: "funnel",
  ai: "AI",
  human: "you (from Instagram/Facebook)",
  system: "system",
};

function ConversationPage() {
  const { id } = Route.useParams();
  const contactId = Number(id);
  const qc = useQueryClient();
  const convo = useQuery({ queryKey: ["conversation", contactId], queryFn: () => getConversationFn({ data: { id: contactId } }), refetchInterval: 10_000 });
  const [notes, setNotes] = useState("");
  const [lead, setLead] = useState({ name: "", phone: "", email: "" });

  const c = convo.data?.contact;
  useEffect(() => {
    if (!c) return;
    setNotes(c.notes ?? "");
    setLead({ name: c.name ?? "", phone: c.phone ?? "", email: c.email ?? "" });
  }, [c?.id, c?.notes, c?.name, c?.phone, c?.email]);

  const act = async (fn: () => Promise<unknown>, done: string) => {
    try {
      await fn();
      toast.success(done);
      await qc.invalidateQueries({ queryKey: ["conversation", contactId] });
      await qc.invalidateQueries({ queryKey: ["contacts"] });
    } catch (err) {
      toast.error(errorText(err));
    }
  };

  const paused = c?.ai_paused_until && new Date(c.ai_paused_until).getTime() > Date.now();

  return (
    <Shell
      title={c ? (c.name ?? (c.username ? `@${c.username}` : "Conversation")) : "Conversation"}
      description={
        c && (
          <>
            {c.platform === "instagram" ? "Instagram" : String(c.platform) === "web" ? "Lead form" : "Facebook"} · {c.business} · came from {c.source ?? "a DM"} · first seen {timeAgo(c.created_at)}
          </>
        )
      }
      actions={
        <Button variant="outline" asChild>
          <Link to="/inbox">
            <ArrowLeft /> Inbox
          </Link>
        </Button>
      }
    >
      {convo.isLoading && <LoadingBlock />}
      {convo.error && <ErrorBlock error={convo.error} />}
      {convo.data === null && <ErrorBlock error="Conversation not found." />}
      {convo.data && c && (
        <div className="grid gap-6 lg:grid-cols-[1fr_320px]">
          <Card>
            <CardContent className="space-y-2 p-4">
              {convo.data.messages.length === 0 && <p className="text-sm text-muted-foreground">No messages yet.</p>}
              {convo.data.messages.map((m) => (
                <div key={m.id} className={cn("flex", m.direction === "out" ? "justify-end" : "justify-start")}>
                  <div
                    dir="auto"
                    className={cn(
                      "max-w-[80%] whitespace-pre-wrap rounded-2xl px-3.5 py-2 text-sm",
                      m.direction === "out" ? "bg-primary text-primary-foreground" : "bg-muted",
                      m.source === "comment" && "border border-dashed bg-background",
                    )}
                  >
                    {m.text}
                    <div className={cn("mt-1 text-[10px]", m.direction === "out" ? "text-primary-foreground/70" : "text-muted-foreground")}>
                      {SOURCE_LABEL[m.source] ? `${SOURCE_LABEL[m.source]} · ` : ""}
                      {dateTime(m.created_at)}
                    </div>
                  </div>
                </div>
              ))}
              <p className="pt-3 text-center text-xs text-muted-foreground">
                To answer yourself, reply from the Instagram app or Meta Business Suite. The AI notices and steps back in this thread.
              </p>
            </CardContent>
          </Card>

          <div className="space-y-4">
            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-base">Lead</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div className="flex flex-wrap gap-1.5">
                  {STAGES.map((s) => (
                    <button
                      key={s}
                      onClick={() => act(() => updateContactFn({ data: { id: c.id, stage: s } }), `Stage: ${s}`)}
                      className={cn("rounded-full border px-2.5 py-0.5 text-xs capitalize", c.stage === s ? "bg-primary text-primary-foreground" : "bg-background")}
                    >
                      {s}
                    </button>
                  ))}
                </div>
                {c.opted_out && <Pill tone="red">Opted out: the bot will not message them</Pill>}
                {(c.interest || c.budget || c.timeline) && (
                  <div className="space-y-1 text-sm">
                    {c.interest && <div>Interest: {c.interest}</div>}
                    {c.budget && <div>Budget: {c.budget}</div>}
                    {c.timeline && <div>Timeline: {c.timeline}</div>}
                  </div>
                )}
                {(["name", "phone", "email"] as const).map((k) => (
                  <div key={k} className="space-y-1">
                    <Label className="text-xs capitalize">{k}</Label>
                    <Input value={lead[k]} onChange={(e) => setLead({ ...lead, [k]: e.target.value })} />
                  </div>
                ))}
                <div className="space-y-1">
                  <Label className="text-xs">Notes</Label>
                  <Textarea rows={4} value={notes} onChange={(e) => setNotes(e.target.value)} />
                </div>
                <Button size="sm" onClick={() => act(() => updateContactFn({ data: { id: c.id, notes, ...lead } }), "Saved.")}>
                  Save lead
                </Button>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-base">AI in this conversation</CardTitle>
              </CardHeader>
              <CardContent className="space-y-2 text-sm">
                {paused ? (
                  <>
                    <p>
                      Paused until {dateTime(c.ai_paused_until)}
                      {c.ai_pause_reason ? ` (${c.ai_pause_reason})` : ""}.
                    </p>
                    <Button size="sm" variant="outline" onClick={() => act(() => setAiPausedFn({ data: { id: c.id, paused: false } }), "The AI is back on.")}>
                      Let the AI answer again
                    </Button>
                  </>
                ) : (
                  <>
                    <p className="text-muted-foreground">The AI answers here.</p>
                    <Button size="sm" variant="outline" onClick={() => act(() => setAiPausedFn({ data: { id: c.id, paused: true, days: 30 } }), "The AI is paused here.")}>
                      Pause the AI here
                    </Button>
                  </>
                )}
              </CardContent>
            </Card>

            {convo.data.sends.length > 0 && (
              <Card>
                <CardHeader className="pb-3">
                  <CardTitle className="text-base">Sends</CardTitle>
                </CardHeader>
                <CardContent className="space-y-1.5 text-xs">
                  {convo.data.sends.slice(0, 12).map((s) => (
                    <div key={s.id} className="flex justify-between gap-2">
                      <span>
                        {s.step ?? s.kind}
                        {s.funnel_id ? ` · ${s.funnel_id}` : ""}
                      </span>
                      <span className={cn(s.status === "sent" ? "text-emerald-700" : s.status === "failed" || s.status === "unknown" ? "text-rose-700" : "text-muted-foreground")}>
                        {s.status === "sent" ? (s.read_at ? "read" : s.delivered_at ? "delivered" : "sent") : s.status.replace("_", " ")}
                      </span>
                    </div>
                  ))}
                </CardContent>
              </Card>
            )}
          </div>
        </div>
      )}
    </Shell>
  );
}
