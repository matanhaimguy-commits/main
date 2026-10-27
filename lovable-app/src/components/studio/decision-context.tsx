import { useState } from "react";
import { Markdown } from "@/components/app/markdown";
import { cn } from "@/lib/utils";

const LONG = 500;

/** The background of a question, as markdown; long ones start folded with "Read all". */
export function DecisionContext({ context }: { context: string }) {
  const [all, setAll] = useState(false);
  const long = context.length > LONG;
  return (
    <div className="rounded-lg bg-muted/50 p-3">
      <div className={cn(long && !all && "max-h-40 overflow-hidden [mask-image:linear-gradient(to_bottom,black_60%,transparent)]")}>
        <Markdown source={context} />
      </div>
      {long && (
        <button type="button" className="mt-2 min-h-9 text-sm font-medium underline" onClick={() => setAll(!all)}>
          {all ? "Show less" : "Read all"}
        </button>
      )}
    </div>
  );
}
