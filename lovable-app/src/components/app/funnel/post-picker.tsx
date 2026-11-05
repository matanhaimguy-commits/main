import { useQuery } from "@tanstack/react-query";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { recentPostsFn } from "@/lib/api/businesses.functions";
import { dateTime } from "@/lib/format";

/** A list of the business's recent posts and reels (from Meta) to pin a comment funnel to. */
export function PostPicker({
  slug,
  open,
  onOpenChange,
  selected,
  onPick,
}: {
  slug: string;
  open: boolean;
  onOpenChange: (v: boolean) => void;
  selected: string[];
  onPick: (id: string) => void;
}) {
  const posts = useQuery({ queryKey: ["recent-posts", slug], queryFn: () => recentPostsFn({ data: { slug } }), enabled: open });
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-h-[85vh] max-w-2xl overflow-y-auto">
        <DialogHeader>
          <DialogTitle>Recent posts</DialogTitle>
          <DialogDescription>Pick the posts or reels this funnel should answer on.</DialogDescription>
        </DialogHeader>
        {posts.isLoading && <p className="text-sm text-muted-foreground">Loading from Meta…</p>}
        {posts.data?.error && <p className="text-sm text-rose-700">{posts.data.error}</p>}
        <div className="divide-y">
          {(posts.data?.posts ?? []).map((p) => (
            <div key={p.id} className="flex items-center gap-3 py-2.5">
              <div className="min-w-0 flex-1">
                <div className="truncate text-sm">{p.text || "(no caption)"}</div>
                <div className="text-xs text-muted-foreground">
                  {p.platform === "instagram" ? "Instagram" : "Facebook"} {p.kind && `· ${p.kind.toLowerCase()}`} · {dateTime(p.date)} ·{" "}
                  {p.url && (
                    <a href={p.url} target="_blank" rel="noreferrer" className="underline">
                      open
                    </a>
                  )}
                </div>
              </div>
              <Button size="sm" variant={selected.includes(p.id) ? "secondary" : "outline"} disabled={selected.includes(p.id)} onClick={() => onPick(p.id)}>
                {selected.includes(p.id) ? "Added" : "Add"}
              </Button>
            </div>
          ))}
        </div>
      </DialogContent>
    </Dialog>
  );
}
