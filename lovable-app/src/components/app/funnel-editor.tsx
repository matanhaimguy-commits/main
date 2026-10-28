import { ChevronDown, ChevronRight, Trash2 } from "lucide-react";
import { useState } from "react";
import { Pill } from "@/components/app/shell";
import { CommaField, Field, SelectField, setIn, TextField } from "@/components/app/fields";
import { AfterFields } from "@/components/app/funnel/after-fields";
import { CommentFields } from "@/components/app/funnel/comment-fields";
import { DeliveryFields } from "@/components/app/funnel/delivery-fields";
import { FollowGateFields } from "@/components/app/funnel/follow-gate-fields";
import { OpenerFields } from "@/components/app/funnel/opener-fields";
import type { AnyObj } from "@/components/app/funnel/types";
import { Button } from "@/components/ui/button";

/** One funnel in the business editor: a header that opens into its sections (each in components/app/funnel/). */
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
  const set = (path: (string | number)[], value: unknown) => onChange(setIn(funnel, path, value));
  const trigger = funnel["trigger"] ?? "comment";
  const platforms: string[] = funnel["platforms"] ?? ["instagram", "facebook"];
  const sections = { funnel, set };

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

          {trigger === "comment" && <CommentFields slug={slug} {...sections} />}
          <OpenerFields {...sections} />
          <FollowGateFields {...sections} />
          <DeliveryFields {...sections} links={links} />
          <AfterFields {...sections} />

          <div className="flex justify-end">
            <Button type="button" variant="ghost" className="text-destructive" onClick={() => confirm("Delete this funnel?") && onRemove()}>
              <Trash2 /> Delete funnel
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
