import { cn } from "@/lib/utils";
import { BlockView } from "./block-view";
import { parseBlocks } from "./parse-blocks";

/**
 * A small markdown renderer for the studio's docs (scripts, hook stacks, lyrics): headings, paragraphs, nested
 * lists, pipe tables, fenced code, quotes, rules, bold, italic, inline code and links. It builds React elements
 * (never HTML strings), and links only open http(s), mailto and in-page addresses.
 */
export function Markdown({ source, className }: { source: string; className?: string }) {
  return (
    <div className={cn("space-y-3 break-words text-sm leading-relaxed", className)}>
      {parseBlocks(source).map((b, k) => (
        <BlockView key={k} block={b} />
      ))}
    </div>
  );
}

export { parseBlocks } from "./parse-blocks";
export { parseInline } from "./parse-inline";
export { safeHref } from "./safe-href";
export { splitRow } from "./table";
export type { Block, Inline, ListNode } from "./types";
