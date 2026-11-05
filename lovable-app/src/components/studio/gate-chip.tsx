import { cn } from "@/lib/utils";
import { GATE_WORD, type GateStatus } from "./labels";
import { scoreText } from "./score";

const TONE: Record<GateStatus, string> = {
  PASS: "bg-emerald-100 text-emerald-800 border-emerald-200",
  OVERRIDE: "bg-sky-100 text-sky-800 border-sky-200",
  FAIL: "bg-rose-100 text-rose-800 border-rose-200",
  PENDING: "bg-muted text-muted-foreground border-border",
};

/** "Pass · Script Lab 86/100", coloured by the gate's state. */
export function GateChip({ status, label, score, max, small }: { status: GateStatus; label: string; score?: number; max?: number; small?: boolean }) {
  const s = scoreText(score, max);
  return (
    <span className={cn("inline-flex max-w-full items-center gap-1 rounded-full border font-medium", small ? "px-2 py-0.5 text-[11px]" : "px-2.5 py-1 text-xs", TONE[status])}>
      <span className="shrink-0 opacity-80">{GATE_WORD[status]}</span>
      <span className="truncate">· {label}</span>
      {s && <span className="shrink-0 tabular-nums">{s}</span>}
    </span>
  );
}
