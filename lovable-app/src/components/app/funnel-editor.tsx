import { useQuery } from "@tanstack/react-query";
import { ChevronDown, ChevronRight, Trash2 } from "lucide-react";
import { useState } from "react";
import { Pill } from "@/components/app/shell";
import { AreaField, CommaField, Field, LinesField, SelectField, setIn, SwitchField, TextField } from "@/components/app/fields";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { recentPostsFn } from "@/lib/api/businesses.functions";
import { dateTime } from "@/lib/format";

type AnyObj = Record<string, any>;

export function FunnelEditor({
  slug,
  funnel,
  links,
  onChange,
  onRemove,
  defaultOpen,
}: {
  slug: string;
  funnel: AnyObj;
  links: AnyObj[];
  onChange: (f: AnyObj) => void;
  onRemove: () => void;
  defaultOpen?: boolean;
}) {
  const [open, setOpen] = useState(!!defaultOpen);
  const [picking, setPicking] = useState(false);
  const set = (path: (string | number)[], value: unknown) => onChange(setIn(funnel, path, value));
  const trigger = funnel["trigger"] ?? "comment";
  const platforms: string[] = funnel["platforms"] ?? ["instagram", "facebook"];
  const linkIds = links.map((l) => String(l["id"]));
  const deliverLink = String(funnel["deliver"]?.["link"] ?? "");
  const customLink = deliverLink !== "" && !linkIds.includes(deliverLink);

  return (
    <div className="rounded-xl border bg-background">
      <button type="button" className="flex w-full items-center gap-3 p-4 text-left" onClick={() => setOpen(!open)}>
        {open ? <ChevronDown className="h-4 w-4" /> : <ChevronRight className="h-4 w-4" />}
        <div className="min-w-0 flex-1">
          <div className="font-medium">{funnel["id"] || "(new funnel)"}</div>
          <div className="truncate text-xs text-muted-foreground">
            {trigger === "comment" ? "Comment" : trigger === "story_reply" ? "Story reply" : "DM"} with {(funnel["keywords"] ?? []).map((k: string) => `"${k}"`).join(", ") || "no keyword"}
            {trigger === "comment" && ` · ${funnel["all_posts"] ? "all posts" : `${(funnel["posts"] ?? []).length} post(s)`}`}
          </div>
        </div>
        {funnel["status"] === "paused" ? <Pill tone="gray">Paused</Pill> : <Pill tone="green">Active</Pill>}
      </button>

      {open && (
        <div className="space-y-5 border-t p-4">
          <div className="grid gap-4 sm:grid-cols-3">
            <TextField label="Funnel id" hint="Lowercase, digits, - and _" value={funnel["id"]} onChange={(v) => set(["id"], v ?? "")} />
            <SelectField
              label="Status"
              value={funnel["status"] ?? "active"}
              options={[
                { value: "active", label: "Active" },
                { value: "paused", label: "Paused (matching comments are skipped)" },
              ]}
              onChange={(v) => set(["status"], v)}
            />
            <SelectField
              label="Trigger"
              value={trigger}
              options={[
                { value: "comment", label: "Comment on a post" },
                { value: "story_reply", label: "Reply to a story (Instagram)" },
                { value: "dm_keyword", label: "Keyword sent as a DM" },
              ]}
              onChange={(v) => set(["trigger"], v)}
            />
          </div>

          <Field label="Platforms">
            <div className="flex gap-4">
              {["instagram", "facebook"].map((p) => (
                <label key={p} className="flex items-center gap-2 text-sm">
                  <input
                    type="checkbox"
                    checked={platforms.includes(p)}
                    onChange={(e) => set(["platforms"], e.target.checked ? [...platforms, p] : platforms.filter((x) => x !== p))}
                  />
                  {p === "instagram" ? "Instagram" : "Facebook"}
                </label>
              ))}
            </div>
          </Field>

          <div className="grid gap-4 sm:grid-cols-2">
            <CommaField
              label="Keywords"
              hint="Separate with commas. Hebrew prefixes (ו ה ב ל מ ש כ) are understood."
              value={funnel["keywords"]}
              onChange={(v) => set(["keywords"], v)}
              placeholder="guide, מדריך"
            />
            <SelectField
              label="Match"
              value={funnel["match"] ?? "word"}
              options={[
                { value: "word", label: "As a word (recommended)" },
                { value: "exact", label: "The whole comment is the keyword" },
                { value: "contains", label: "Anywhere, even inside words (risky)" },
              ]}
              onChange={(v) => set(["match"], v)}
            />
          </div>

          {trigger === "comment" && (
            <div className="space-y-3 rounded-lg bg-muted/40 p-3">
              <div className="flex flex-wrap items-end gap-2">
                <div className="min-w-64 flex-1">
                  <CommaField
                    label="Posts / reels this funnel is pinned to"
                    hint="Post or media IDs. Pinning keeps old posts from triggering it."
                    value={funnel["posts"]}
                    onChange={(v) => set(["posts"], v)}
                  />
                </div>
                <Button type="button" variant="outline" onClick={() => setPicking(true)} className="mb-5">
                  Pick from recent posts
                </Button>
              </div>
              <SwitchField
                label="Every post (account-wide)"
                hint="Catches the keyword on any post, including years-old ones. Pinned funnels win over this."
                checked={!!funnel["all_posts"]}
                onChange={(v) => set(["all_posts"], v)}
              />
              {funnel["all_posts"] && (
                <SwitchField
                  label="I understand old posts will trigger it too"
                  checked={!!funnel["all_posts_acknowledged"]}
                  onChange={(v) => set(["all_posts_acknowledged"], v)}
                />
              )}
              <LinesField
                label="Public replies under the comment (optional)"
                hint="One per line; one is picked at random each time."
                value={funnel["public_replies"]}
                onChange={(v) => set(["public_replies"], v)}
                rows={2}
              />
            </div>
          )}

          <div className="space-y-3">
            <div className="text-sm font-semibold">1 · First message</div>
            <AreaField label="Text" max={640} value={funnel["opener"]?.["text"]} onChange={(v) => set(["opener", "text"], v ?? "")} />
            <div className="grid gap-4 sm:grid-cols-2">
              <TextField label="Button" max={20} value={funnel["opener"]?.["button"]} onChange={(v) => set(["opener", "button"], v ?? "")} />
              <SelectField
                label="Button does"
                value={funnel["opener"]?.["mode"] ?? "tap"}
                options={[
                  { value: "tap", label: "Tap to receive (recommended: opens the chat for the AI)" },
                  { value: "link", label: "Opens the link directly" },
                ]}
                onChange={(v) => set(["opener", "mode"], v)}
              />
            </div>
          </div>

          <div className="space-y-3">
            <SwitchField
              label="Ask to follow first (Instagram)"
              hint="Costs one extra tap. People who already follow skip it."
              checked={!!funnel["follow_gate"]?.["enabled"] && !!funnel["follow_gate"]}
              onChange={(v) =>
                set(
                  ["follow_gate"],
                  v ? { enabled: true, text: funnel["follow_gate"]?.["text"] || "Follow us first, then tap again 👇", button: funnel["follow_gate"]?.["button"] || "I followed" } : undefined,
                )
              }
            />
            {funnel["follow_gate"]?.["enabled"] && (
              <div className="grid gap-4 sm:grid-cols-[2fr_1fr]">
                <AreaField label="Follow request text" max={640} rows={2} value={funnel["follow_gate"]?.["text"]} onChange={(v) => set(["follow_gate", "text"], v ?? "")} />
                <TextField label="Button" max={20} value={funnel["follow_gate"]?.["button"]} onChange={(v) => set(["follow_gate", "button"], v ?? "")} />
              </div>
            )}
          </div>

          <div className="space-y-3">
            <div className="text-sm font-semibold">2 · Delivery</div>
            <AreaField label="Text" max={640} value={funnel["deliver"]?.["text"]} onChange={(v) => set(["deliver", "text"], v ?? "")} />
            <div className="grid gap-4 sm:grid-cols-2">
              <Field label="Link" hint={linkIds.length ? "One of the business's links, or a full address." : "Add links on the Links tab, or paste a full address."}>
                <select
                  className="h-9 w-full rounded-md border bg-background px-2 text-sm"
                  value={customLink ? "__custom" : deliverLink}
                  onChange={(e) => set(["deliver", "link"], e.target.value === "__custom" ? "https://" : e.target.value)}
                >
                  <option value="">— choose —</option>
                  {links.map((l) => (
                    <option key={l["id"]} value={l["id"]}>
                      {l["title"]} ({l["id"]})
                    </option>
                  ))}
                  <option value="__custom">A full address…</option>
                </select>
                {customLink && <Input className="mt-2" value={deliverLink} onChange={(e) => set(["deliver", "link"], e.target.value)} />}
              </Field>
              <TextField label="Button" max={20} value={funnel["deliver"]?.["button"]} onChange={(v) => set(["deliver", "button"], v ?? "")} />
            </div>
          </div>

          <AreaField
            label="3 · Last message (optional)"
            hint="Open a conversation, e.g. a question about what they need. Only with the tap button."
            max={1000}
            rows={2}
            optional
            value={funnel["after"]}
            onChange={(v) => set(["after"], v)}
          />

          <div className="flex justify-end">
            <Button type="button" variant="ghost" className="text-destructive" onClick={() => confirm("Delete this funnel?") && onRemove()}>
              <Trash2 /> Delete funnel
            </Button>
          </div>
        </div>
      )}

      <PostPicker
        slug={slug}
        open={picking}
        onOpenChange={setPicking}
        selected={funnel["posts"] ?? []}
        onPick={(id) => set(["posts"], Array.from(new Set([...(funnel["posts"] ?? []), id])))}
      />
    </div>
  );
}

function PostPicker({
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
