import type { StudioStepView } from "@/lib/api/studio";
import { GateChip } from "./gate-chip";
import { gateLabel, latestGates } from "./gates";

const SHOWN = 4;

/** Under a collapsed step: the latest state of its first gates, and how many files it has. */
export function StepSummary({ step, files }: { step: StudioStepView; files: number }) {
  const latest = latestGates(step.gates);
  if (latest.length === 0 && files === 0) return null;
  return (
    <div className="mt-1.5 flex flex-wrap items-center gap-1">
      {latest.slice(0, SHOWN).map((g, k) => (
        <GateChip key={k} small status={g.status} label={gateLabel(g)} score={g.score} max={g.max} />
      ))}
      {latest.length > SHOWN && <span className="text-[11px] text-muted-foreground">+{latest.length - SHOWN} more</span>}
      {files > 0 && <span className="text-[11px] text-muted-foreground">{files === 1 ? "1 file" : `${files} files`}</span>}
    </div>
  );
}
