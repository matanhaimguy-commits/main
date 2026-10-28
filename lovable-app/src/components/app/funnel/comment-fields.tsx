import { useState } from "react";
import { CommaField, LinesField, SwitchField } from "@/components/app/fields";
import { Button } from "@/components/ui/button";
import { PostPicker } from "./post-picker";
import type { FunnelFieldsProps } from "./types";

/** For comment funnels: which posts it is pinned to, and the public replies under the comment. */
export function CommentFields({ slug, funnel, set }: FunnelFieldsProps & { slug: string }) {
  const [picking, setPicking] = useState(false);
  return (
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
