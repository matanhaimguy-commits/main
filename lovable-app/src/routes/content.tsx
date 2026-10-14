import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { Copy, ExternalLink } from "lucide-react";
import { useMemo, useState } from "react";
import { toast } from "sonner";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { contentActionFn, listContentFn, type ContentRow } from "@/lib/api/content.functions";
import { getSession } from "@/lib/api/session.functions";
import { dateTime, errorText } from "@/lib/format";
import { requireLogin } from "@/lib/session";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/content")({
  head: () => ({ meta: [{ title: "Content · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: ContentPage,
});

const STATUS_TONE: Record<string, "green" | "amber" | "red" | "gray" | "blue"> = {
  draft: "amber",
  approved: "blue",
  scheduled: "blue",
  publishing: "blue",
  published: "green",
  rejected: "gray",
  failed: "red",
};

const VIEWS: { id: string; label: string; match: (s: string) => boolean }[] = [
  { id: "review", label: "To review", match: (s) => s === "draft" || s === "failed" },
  { id: "ready", label: "Approved", match: (s) => s === "approved" || s === "scheduled" || s === "publishing" },
  { id: "published", label: "Published", match: (s) => s === "published" },
  { id: "all", label: "All", match: () => true },
];

function ContentPage() {
  const [view, setView] = useState("review");
  const [business, setBusiness] = useState("");
  const items = useQuery({ queryKey: ["content"], queryFn: () => listContentFn({ data: {} }), refetchInterval: 30_000 });
  const session = useQuery({ queryKey: ["session"], queryFn: () => getSession(), staleTime: 60_000 });
  const canEdit = session.data?.role === "admin";

  const businesses = useMemo(() => {
    const seen = new Map<string, string>();
    for (const it of items.data ?? []) seen.set(it.business, it.business_name);
    return [...seen.entries()];
  }, [items.data]);
  const v = VIEWS.find((x) => x.id === view)!;
  const shown = (items.data ?? []).filter((it) => v.match(it.status) && (!business || it.business === business));
  const count = (id: string) => (items.data ?? []).filter((it) => VIEWS.find((x) => x.id === id)!.match(it.status)).length;

  return (
    <Shell
      title="Content"
      description="Posts the studio made for each business. Check them, approve, set a time, and post. Every post's keyword is answered by the DM bot."
    >
      <div className="mb-4 flex flex-wrap items-center gap-2">
        {VIEWS.map((x) => (
          <button
            key={x.id}
            onClick={() => setView(x.id)}
            className={cn("rounded-full border px-3 py-1 text-sm", x.id === view ? "bg-primary text-primary-foreground" : "bg-background")}
          >
            {x.label} {items.data ? <span className="opacity-70">({count(x.id)})</span> : null}
          </button>
        ))}
        {businesses.length > 1 && (
          <select className="ml-auto h-8 rounded-md border bg-background px-2 text-sm" value={business} onChange={(e) => setBusiness(e.target.value)}>
            <option value="">All businesses</option>
            {businesses.map(([slug, name]) => (
              <option key={slug} value={slug}>
                {name}
              </option>
            ))}
          </select>
        )}
      </div>
      {items.isLoading && <LoadingBlock />}
      {items.error && <ErrorBlock error={items.error} />}
      {items.data && shown.length === 0 && (
        <div className="rounded-xl border bg-background p-10 text-center text-sm text-muted-foreground">
          Nothing here yet. The studio adds drafts here after each weekly run.
        </div>
      )}
      <div className="grid gap-5 lg:grid-cols-2">
        {shown.map((it) => (
          <ItemCard key={it.id} item={it} canEdit={canEdit} />
        ))}
      </div>
    </Shell>
  );
}

function Preview({ item }: { item: ContentRow }) {
  const media = item.media ?? [];
  if (media.length === 0) return <div className="flex h-48 items-center justify-center rounded-lg bg-muted text-sm text-muted-foreground">No media</div>;
  if (item.kind === "reel" || media[0]!.type === "video") {
    return (
      <video
        src={media[0]!.url}
        poster={item.cover_url ?? undefined}
        controls
        playsInline
        preload="metadata"
        className="mx-auto max-h-[440px] rounded-lg bg-black"
      />
    );
  }
  return (
    <div className="flex snap-x gap-2 overflow-x-auto pb-1">
      {media.map((m, i) =>
        m.type === "video" ? (
          <video key={i} src={m.url} controls playsInline preload="metadata" className="h-80 shrink-0 snap-start rounded-lg bg-black" />
        ) : (
          <img key={i} src={m.url} alt={item.alt_text ?? ""} loading="lazy" className="h-80 shrink-0 snap-start rounded-lg object-cover" />
        ),
      )}
    </div>
  );
}

const toLocalInput = (iso: string | null) => {
  if (!iso) return "";
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
};

function ItemCard({ item, canEdit }: { item: ContentRow; canEdit: boolean }) {
  const qc = useQueryClient();
  const [busy, setBusy] = useState(false);
  const [when, setWhen] = useState(toLocalInput(item.scheduled_at));
  const [permalink, setPermalink] = useState("");
  const [postedOpen, setPostedOpen] = useState(false);
  const [expanded, setExpanded] = useState(false);

  const act = async (a: Parameters<typeof contentActionFn>[0]["data"]["act"], done?: string) => {
    setBusy(true);
    try {
      const res = await contentActionFn({ data: { id: item.id, act: a } });
      if (!res.ok) toast.error(res.error ?? "That did not work.");
      else if (done) toast.success(done);
      await qc.invalidateQueries({ queryKey: ["content"] });
    } catch (err) {
      toast.error(errorText(err));
    } finally {
      setBusy(false);
    }
  };
  const copy = async (text: string) => {
    await navigator.clipboard.writeText(text);
    toast.success("Copied.");
  };
  const long = item.caption.length > 280;

  return (
    <Card>
      <CardContent className="space-y-3 p-4">
        <div className="flex flex-wrap items-center gap-2">
          <Pill tone={STATUS_TONE[item.status] ?? "gray"}>{item.status}</Pill>
          <Pill tone="gray">{item.kind}</Pill>
          {item.keyword && <Pill tone="blue">Comment “{item.keyword}”</Pill>}
          <span className="ml-auto text-xs text-muted-foreground">{item.business_name}</span>
        </div>
        {item.title && <div className="font-medium">{item.title}</div>}
        <Preview item={item} />
        <div className="space-y-1">
          <div className="flex items-center justify-between">
            <span className="text-xs font-medium text-muted-foreground">Caption</span>
            <button className="text-xs text-muted-foreground hover:text-foreground" onClick={() => copy(item.caption)}>
              <Copy className="mr-1 inline h-3 w-3" />
              Copy
            </button>
          </div>
          <p dir="auto" className="whitespace-pre-wrap text-sm">
            {long && !expanded ? `${item.caption.slice(0, 280)}…` : item.caption}
          </p>
          {long && (
            <button className="text-xs underline" onClick={() => setExpanded(!expanded)}>
              {expanded ? "Show less" : "Show all"}
            </button>
          )}
        </div>
        {item.first_comment && (
          <div className="text-sm">
            <span className="text-xs font-medium text-muted-foreground">First comment: </span>
            <span dir="auto">{item.first_comment}</span>
          </div>
        )}
        {item.notes && (
          <div className="rounded-lg border border-amber-200 bg-amber-50 p-2.5 text-sm text-amber-900">
            <b>Check before posting:</b> <span className="whitespace-pre-wrap">{item.notes}</span>
          </div>
        )}
        {item.error && <div className="rounded-lg border border-rose-200 bg-rose-50 p-2.5 text-sm text-rose-800">{item.error}</div>}
        <div className="flex flex-wrap gap-2 text-xs text-muted-foreground">
          {item.media.map((m, i) => (
            <a key={i} href={m.url} target="_blank" rel="noreferrer" className="underline">
              file {i + 1}
            </a>
          ))}
          {item.permalink && (
            <a href={item.permalink} target="_blank" rel="noreferrer" className="underline">
              <ExternalLink className="mr-0.5 inline h-3 w-3" />
              on Instagram
            </a>
          )}
          {item.published_at && <span>posted {dateTime(item.published_at)}</span>}
          {!item.published_at && item.scheduled_at && <span>planned for {dateTime(item.scheduled_at)}</span>}
        </div>

        {canEdit && item.status !== "published" && item.status !== "publishing" && (
          <div className="space-y-2 border-t pt-3">
            <div className="flex flex-wrap items-center gap-2">
              <Input type="datetime-local" className="h-8 w-auto" value={when} onChange={(e) => setWhen(e.target.value)} />
              <Button
                size="sm"
                variant="outline"
                disabled={busy}
                onClick={() => act({ action: "schedule", at: when ? new Date(when).toISOString() : null }, when ? "Time saved." : "Time cleared.")}
              >
                Set time
              </Button>
            </div>
            <div className="flex flex-wrap gap-2">
              {(item.status === "draft" || item.status === "failed") && (
                <>
                  <Button size="sm" disabled={busy} onClick={() => act({ action: "approve" }, "Approved.")}>
                    Approve
                  </Button>
                  <Button size="sm" variant="outline" disabled={busy} onClick={() => act({ action: "reject" }, "Rejected.")}>
                    Reject
                  </Button>
                </>
              )}
              {(item.status === "approved" || item.status === "scheduled" || item.status === "rejected") && (
                <Button size="sm" variant="outline" disabled={busy} onClick={() => act({ action: "draft" }, "Back to review.")}>
                  Back to review
                </Button>
              )}
              {item.status !== "rejected" && (
                <Button size="sm" variant="outline" disabled={busy} onClick={() => setPostedOpen(!postedOpen)}>
                  I posted it
                </Button>
              )}
              {item.status === "rejected" && (
                <Button
                  size="sm"
                  variant="ghost"
                  disabled={busy}
                  onClick={() => window.confirm("Delete this item?") && act({ action: "delete" }, "Deleted.")}
                >
                  Delete
                </Button>
              )}
            </div>
            {postedOpen && (
              <div className="flex flex-wrap items-center gap-2">
                <Input
                  className="h-8 flex-1"
                  placeholder="Link to the post on Instagram (optional)"
                  value={permalink}
                  onChange={(e) => setPermalink(e.target.value)}
                />
                <Button size="sm" disabled={busy} onClick={() => act({ action: "posted", permalink }, "Marked as posted.")}>
                  Save
                </Button>
              </div>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
