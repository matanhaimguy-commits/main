import type { AnswerInput, DecisionInput, RunInput } from "./schema";
import type { StudioDecisionRow } from "./types";

/** Checks a schema can't make: they return plain sentences, empty when all is well. */

const MAX_LEDGER_CHARS = 2_000_000;

const firstDuplicate = <T>(xs: T[]): T | undefined => xs.find((x, i) => xs.indexOf(x) !== i);

/** Duplicate steps or file keys, files on steps the run doesn't have, a ledger that is too big. */
export function runInputProblems(input: RunInput): string[] {
  const out: string[] = [];
  const ns = input.steps.map((s) => s.n);
  const dupStep = firstDuplicate(ns);
  if (dupStep !== undefined) out.push(`Step ${dupStep} appears twice.`);
  if (input.current_step != null && !ns.includes(input.current_step)) out.push(`current_step ${input.current_step} is not one of the steps.`);
  const dupKey = firstDuplicate((input.files ?? []).map((f) => f.key));
  if (dupKey !== undefined) out.push(`File key "${dupKey}" appears twice.`);
  for (const f of input.files ?? []) {
    if (f.step == null || ns.includes(f.step)) continue;
    out.push(
      ns.length
        ? `File "${f.label}" names step ${f.step}, which this run doesn't have.`
        : `File "${f.label}" names step ${f.step}, but this run has no steps: leave the step out.`,
    );
  }
  if (JSON.stringify(input.ledger).length > MAX_LEDGER_CHARS) out.push("The ledger is too big (over 2 MB).");
  return out;
}

/** Options that repeat, or a multi-select question without a choice to make. */
export function decisionInputProblems(input: DecisionInput): string[] {
  const out: string[] = [];
  const lower = input.options.map((o) => o.label.toLowerCase());
  const again = lower.findIndex((l, i) => lower.indexOf(l) !== i);
  if (again >= 0) out.push(`Option "${input.options[again]!.label}" appears twice.`);
  if (input.multi && input.options.length < 2) out.push("A multi-select question needs at least 2 options.");
  return out;
}

/** Why this answer doesn't fit the question, or null when it does. */
export function answerProblem(d: Pick<StudioDecisionRow, "options" | "multi" | "status">, a: AnswerInput): string | null {
  if (d.status === "synced") return "The studio has already taken this answer in. If it should change, say so in chat.";
  const labels = d.options.map((o) => o.label);
  const unknown = a.choices.find((c) => !labels.includes(c));
  if (unknown !== undefined) return `"${unknown}" is not one of the options.`;
  if (new Set(a.choices).size !== a.choices.length) return "The same option is chosen twice.";
  if (!d.multi && a.choices.length > 1) return "Pick one option.";
  if (a.choices.length === 0 && !a.note.trim()) return d.options.length ? "Pick an option or write a note." : "Write your answer in the note.";
  return null;
}
