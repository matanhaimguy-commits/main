import { Check } from "lucide-react";
import { Button } from "@/components/ui/button";
import type { StudioDecisionView } from "@/lib/api/studio";
import { dateTime } from "@/lib/format";

/** The answer given: the choices, the note, and whether the studio has taken it in yet. */
export function AnswerSummary({ decision: d, onChange }: { decision: StudioDecisionView; onChange?: () => void }) {
  if (!d.answer) return null;
  const synced = d.status === "synced";
  return (
    <div className="space-y-2 rounded-lg bg-emerald-50 p-3 text-sm text-emerald-950">
      <div className="flex flex-wrap items-center gap-1.5">
        <Check className="h-4 w-4 text-emerald-700" />
        <span className="font-medium">{synced ? "Decided" : "You answered"}</span>
        {d.answered_at && <span className="text-xs text-emerald-800/80">{dateTime(d.answered_at)}</span>}
      </div>
      {d.answer.choices.length > 0 && (
        <div className="flex flex-wrap gap-1.5">
          {d.answer.choices.map((c) => (
            <span key={c} dir="auto" className="rounded-full bg-emerald-100 px-2.5 py-1 text-xs font-medium text-emerald-900">
              {c}
            </span>
          ))}
        </div>
      )}
      {d.answer.note && (
        <p dir="auto" className="whitespace-pre-wrap">
          {d.answer.note}
        </p>
      )}
      <div className="text-xs text-emerald-800/80">
        {synced ? `Taken into the studio ${d.synced_at ? dateTime(d.synced_at) : ""}.` : "Saved. The studio picks it up at its next session."}
      </div>
      {!synced && onChange && (
        <Button variant="outline" size="sm" className="h-9 bg-background" onClick={onChange}>
          Change answer
        </Button>
      )}
    </div>
  );
}
