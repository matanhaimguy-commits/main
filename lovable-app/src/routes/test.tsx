import { useQuery } from "@tanstack/react-query";
import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { useEffect, useRef, useState, type FormEvent } from "react";
import { ErrorBlock, LoadingBlock, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { businessSlugsFn } from "@/lib/api/businesses.functions";
import { simulateCommentFn, testChatFn, type CommentSimulation, type TestChatState } from "@/lib/api/test.functions";
import { errorText } from "@/lib/format";
import { requireLogin } from "@/lib/session";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/test")({
  head: () => ({ meta: [{ title: "Test the bot · Social Agent" }, { name: "robots", content: "noindex" }] }),
  validateSearch: (s: Record<string, unknown>): { b?: string } => (typeof s["b"] === "string" ? { b: s["b"] } : {}),
  beforeLoad: requireLogin,
  component: TestPage,
});

const emptyChat = (): TestChatState => ({ platform: "instagram", msgs: [], lead: {}, notes: [] });

function TestPage() {
  const { b } = Route.useSearch();
  const navigate = useNavigate({ from: "/test" });
  const slugs = useQuery({ queryKey: ["business-slugs"], queryFn: () => businessSlugsFn() });
  const slug = b ?? slugs.data?.[0]?.slug;

  return (
    <Shell title="Test the bot" description="Talk to it like a customer, or check what a comment would trigger. Nothing is sent to Instagram or Facebook.">
      {slugs.isLoading && <LoadingBlock />}
      {slugs.error && <ErrorBlock error={slugs.error} />}
      {slugs.data && slugs.data.length === 0 && <p className="text-sm text-muted-foreground">Create a business first.</p>}
      {slugs.data && slugs.data.length > 1 && (
        <div className="mb-4 flex flex-wrap gap-1.5">
          {slugs.data.map((x) => (
            <button
              key={x.slug}
              onClick={() => navigate({ search: { b: x.slug } })}
              className={cn("rounded-full border px-3 py-1 text-sm", x.slug === slug ? "bg-primary text-primary-foreground" : "bg-background")}
            >
              {x.name}
            </button>
          ))}
        </div>
      )}
      {slug && (
        <div className="grid gap-6 lg:grid-cols-2">
          <ChatCard key={`chat-${slug}`} slug={slug} />
          <CommentCard key={`comment-${slug}`} slug={slug} />
        </div>
      )}
    </Shell>
  );
}

function ChatCard({ slug }: { slug: string }) {
  const [chat, setChat] = useState<TestChatState>(emptyChat);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const bottom = useRef<HTMLDivElement>(null);
  useEffect(() => bottom.current?.scrollIntoView({ behavior: "smooth", block: "nearest" }), [chat.msgs.length, busy]);

  const send = async (e: FormEvent) => {
    e.preventDefault();
    const t = text.trim();
    if (!t || busy) return;
    setBusy(true);
    setError(null);
    setText("");
    setChat((c) => ({ ...c, msgs: [...c.msgs, { d: "in", t }] }));
    try {
      const res = await testChatFn({ data: { slug, state: chat, text: t } });
      if (!Array.isArray(res?.state?.msgs)) throw new Error("The server sent an unexpected answer. Try again.");
      setChat(res.state);
      if (res.error) setError(res.error);
    } catch (err) {
      setChat((c) => ({ ...c, msgs: c.msgs.slice(0, -1) }));
      setError(errorText(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <Card className="flex flex-col">
      <CardHeader>
        <CardTitle>Chat as a customer</CardTitle>
        <CardDescription>The real AI with this business's details. Nothing is saved.</CardDescription>
      </CardHeader>
      <CardContent className="flex flex-1 flex-col gap-3">
        <div className="flex h-[420px] flex-col gap-2 overflow-y-auto rounded-lg border bg-muted/30 p-3">
          {chat.msgs.length === 0 && <p className="m-auto text-sm text-muted-foreground">Say hi, ask for a price, or ask something tricky.</p>}
          {chat.msgs.map((m, i) => (
            <div key={i} className={cn("flex", m.d === "out" ? "justify-start" : "justify-end")}>
              <div dir="auto" className={cn("max-w-[85%] whitespace-pre-wrap rounded-2xl px-3.5 py-2 text-sm", m.d === "out" ? "bg-background shadow-sm" : "bg-primary text-primary-foreground")}>
                {m.t}
              </div>
            </div>
          ))}
          {busy && <div className="text-xs text-muted-foreground">typing…</div>}
          <div ref={bottom} />
        </div>
        {chat.notes.length > 0 && (
          <div className="space-y-0.5 text-xs text-muted-foreground">
            {chat.notes.slice(-4).map((n, i) => (
              <div key={i}>• {n}</div>
            ))}
          </div>
        )}
        {error && <p className="text-sm text-destructive">{error}</p>}
        <form onSubmit={send} className="flex gap-2">
          <Input value={text} onChange={(e) => setText(e.target.value)} placeholder="Write like a customer would…" disabled={busy} />
          <Button type="submit" disabled={busy || !text.trim()}>
            Send
          </Button>
        </form>
        <div className="flex items-center justify-between">
          <select
            className="h-8 rounded-md border bg-background px-2 text-xs"
            value={chat.platform}
            onChange={(e) => setChat({ ...emptyChat(), platform: e.target.value as TestChatState["platform"] })}
          >
            <option value="instagram">As Instagram</option>
            <option value="facebook">As Facebook</option>
          </select>
          <Button variant="ghost" size="sm" onClick={() => setChat(emptyChat())}>
            Start over
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}

function CommentCard({ slug }: { slug: string }) {
  const [platform, setPlatform] = useState<"instagram" | "facebook">("instagram");
  const [postId, setPostId] = useState("");
  const [text, setText] = useState("");
  const [result, setResult] = useState<CommentSimulation | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const check = async (e: FormEvent) => {
    e.preventDefault();
    setBusy(true);
    setError(null);
    try {
      const res = await simulateCommentFn({ data: { slug, platform, text, ...(postId.trim() ? { postId: postId.trim() } : {}) } });
      if (typeof res?.summary !== "string") throw new Error("The server sent an unexpected answer. Try again.");
      setResult(res);
    } catch (err) {
      setError(errorText(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle>Simulate a comment</CardTitle>
        <CardDescription>Which funnel would fire, and exactly what the person would receive.</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <form onSubmit={check} className="space-y-3">
          <div className="grid gap-2 sm:grid-cols-[auto_1fr]">
            <select className="h-9 rounded-md border bg-background px-2 text-sm" value={platform} onChange={(e) => setPlatform(e.target.value as "instagram" | "facebook")}>
              <option value="instagram">Instagram</option>
              <option value="facebook">Facebook</option>
            </select>
            <Input value={postId} onChange={(e) => setPostId(e.target.value)} placeholder="Post / reel ID (from the funnel)" />
          </div>
          <Input value={text} onChange={(e) => setText(e.target.value)} placeholder="Comment text, e.g. מדריך please" />
          <Button type="submit" disabled={busy}>
            Check
          </Button>
        </form>
        {error && <p className="text-sm text-destructive">{error}</p>}
        {result && (
          <div className="space-y-3 rounded-lg border p-3 text-sm">
            <p className={result.fires ? "font-medium text-emerald-700" : "font-medium text-rose-700"}>{result.summary}</p>
            {result.publicReplies.length > 0 && <p className="text-muted-foreground">Public reply: {result.publicReplies.join(" / ")}</p>}
            {result.steps.map((s, i) => (
              <div key={i}>
                <div className="text-xs text-muted-foreground">{s.title}</div>
                <div dir="auto" className="mt-1 whitespace-pre-wrap rounded-2xl bg-muted px-3.5 py-2">{s.message}</div>
              </div>
            ))}
            {result.notes.map((n, i) => (
              <p key={i} className="text-muted-foreground">
                {n}
              </p>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
