import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import type { StudioDecisionView } from "@/lib/api/studio";
import { OptionButton } from "./option-button";
import { canSend, pick } from "./pick";

/**
 * The options, a note and "Send answer". Reviewers see the options but can't pick or send.
 * `onSend` resolves true when the answer was saved.
 */
export function AnswerForm({
  decision: d,
  canAnswer,
  onSend,
  onCancel,
}: {
  decision: StudioDecisionView;
  canAnswer: boolean;
  onSend: (choices: string[], note: string) => Promise<boolean>;
  /** Shown when changing an earlier answer. */
  onCancel?: () => void;
}) {
  const [choices, setChoices] = useState<string[]>(d.answer?.choices ?? []);
  const [note, setNote] = useState(d.answer?.note ?? "");
  const [busy, setBusy] = useState(false);
  const send = async () => {
    setBusy(true);
    try {
      await onSend(choices, note);
    } finally {
      setBusy(false);
    }
  };
  return (
    <div className="space-y-3">
      {d.options.length > 0 && (
        <div role={d.multi ? "group" : "radiogroup"} aria-label={d.question} className="space-y-2">
          {d.multi && <div className="text-xs text-muted-foreground">Pick all that apply.</div>}
          {d.options.map((o) => (
            <OptionButton
              key={o.label}
              label={o.label}
              description={o.description}
              multi={d.multi}
              checked={choices.includes(o.label)}
              disabled={!canAnswer || busy}
              onClick={() => setChoices((c) => pick(c, o.label, d.multi))}
            />
          ))}
        </div>
      )}
      {canAnswer ? (
        <>
          <Textarea
            dir="auto"
            rows={3}
            value={note}
            onChange={(e) => setNote(e.target.value)}
            placeholder={d.options.length ? "Anything to add? (optional)" : "Your answer"}
            className="text-base md:text-sm"
          />
          <div className="flex flex-wrap gap-2">
            <Button size="lg" className="h-11 flex-1 px-6 sm:flex-none" disabled={busy || !canSend(choices, note)} onClick={send}>
              {d.status === "answered" ? "Save new answer" : "Send answer"}
            </Button>
            {onCancel && (
              <Button size="lg" variant="ghost" className="h-11" disabled={busy} onClick={onCancel}>
                Cancel
              </Button>
            )}
          </div>
        </>
      ) : (
        <p className="text-sm text-muted-foreground">Only the owner can answer this.</p>
      )}
    </div>
  );
}
