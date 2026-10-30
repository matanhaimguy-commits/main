import { cn } from "@/lib/utils";
import { InlineText } from "./inline-text";
import type { Block } from "./types";

/** A pipe table that scrolls sideways on a phone; long cells get a readable minimum width. */
export function TableView({ table }: { table: Extract<Block, { t: "table" }> }) {
  const { head, rows, align } = table;
  return (
    <div className="-mx-1 overflow-x-auto px-1">
      <table className="w-full border-collapse text-xs">
        <thead>
          <tr>
            {head.map((h, k) => (
              <th key={k} dir="auto" className="border bg-muted px-2 py-1.5 text-left align-bottom font-medium" style={{ textAlign: align[k] ?? undefined }}>
                <InlineText text={h} />
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((r, k) => (
            <tr key={k}>
              {head.map((_, c) => (
                <td
                  key={c}
                  dir="auto"
                  className={cn("border px-2 py-1.5 align-top", (r[c]?.length ?? 0) > 40 && "min-w-[11rem]")}
                  style={{ textAlign: align[c] ?? undefined }}
                >
                  <InlineText text={r[c] ?? ""} />
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
