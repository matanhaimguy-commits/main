import { cn } from "@/lib/utils";
import { InlineText } from "./inline-text";
import { ListView } from "./list-view";
import { TableView } from "./table-view";
import type { Block } from "./types";

const HEADING_CLASS: Record<number, string> = {
  1: "text-lg font-semibold",
  2: "text-base font-semibold",
  3: "text-sm font-semibold",
};

export function BlockView({ block: b }: { block: Block }) {
  switch (b.t) {
    case "h": {
      // The page title is the only h1: a doc's headings start at h2.
      const Tag = `h${Math.min(b.level + 1, 6)}` as "h2";
      return (
        <Tag dir="auto" className={cn("pt-2", HEADING_CLASS[b.level] ?? "text-sm font-semibold")}>
          <InlineText text={b.text} />
        </Tag>
      );
    }
    case "p":
      return (
        <p dir="auto">
          <InlineText text={b.text} />
        </p>
      );
    case "list":
      return <ListView list={b.list} />;
    case "code":
      return <pre className="whitespace-pre-wrap break-words rounded-lg bg-muted p-3 font-mono text-xs leading-relaxed">{b.text}</pre>;
    case "quote":
      return (
        <blockquote className="space-y-2 border-l-2 pl-3 text-muted-foreground">
          {b.blocks.map((x, k) => (
            <BlockView key={k} block={x} />
          ))}
        </blockquote>
      );
    case "hr":
      return <hr className="border-border" />;
    case "table":
      return <TableView table={b} />;
  }
}
