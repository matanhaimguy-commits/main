import type { StudioGate } from "@/lib/api/studio";
import { dateTime } from "@/lib/format";
import { GateChip } from "./gate-chip";
import { gateLabel } from "./gates";

/** Every gate record of a step in order (loops included), with who checked, when, and their note. */
export function GateList({ gates }: { gates: StudioGate[] }) {
  return (
    <div className="space-y-2.5">
      <div className="text-xs font-medium uppercase tracking-wide text-muted-foreground">Gates</div>
      {gates.map((g, k) => (
        <div key={k} className="space-y-1">
          <GateChip status={g.status} label={gateLabel(g)} score={g.score} max={g.max} />
          <div className="text-xs text-muted-foreground">
            {[g.label ? g.gate : null, g.by ? `by ${g.by}` : null, g.at ? dateTime(g.at) : null].filter(Boolean).join(" · ")}
          </div>
          {g.note && (
            <p dir="auto" className="whitespace-pre-wrap text-sm text-muted-foreground">
              {g.note}
            </p>
          )}
        </div>
      ))}
    </div>
  );
}
