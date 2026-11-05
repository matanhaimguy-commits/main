import { DecisionInput, RunInput, type StudioStep } from "./schema";

/** Sample input for the Studio tests (no database). */

export const step = (n: number, status: StudioStep["status"], extra: Partial<StudioStep> = {}): StudioStep => ({
  n,
  name: `Step ${n}`,
  status,
  gates: [],
  ...extra,
});

/** A song piece at step 3 (Script), with loop history on its gates. */
export const runInput = (over: Record<string, unknown> = {}) =>
  RunInput.parse({
    business: "acme",
    post_id: "AC-EN-03",
    title: "Maya's quilt",
    format: "reel_song",
    family: "song",
    steps: [
      step(0, "done", { name: "Foundation and brief", gates: [{ gate: "G-BRIEF", status: "PASS", by: "claude" }] }),
      step(1, "done"),
      step(2, "done", { gates: [{ gate: "G-HOOK", label: "Hook Lab", status: "FAIL", note: "round 1" }] }),
      step(3, "active", {
        name: "Script",
        gates: [
          { gate: "G-SCRIPT", label: "Script Lab", status: "FAIL", score: 81 },
          { gate: "G-SCRIPT", label: "Script Lab", status: "PASS", score: 86 },
        ],
      }),
      step(4, "pending"),
      step(5, "na"),
    ],
    ledger: { post_id: "AC-EN-03", queue: [] },
    ...over,
  });

/** The owner's song listen on run AC-EN-03, step 4. */
export const songQuestion = (over: Record<string, unknown> = {}) =>
  DecisionInput.parse({
    business: "acme",
    post_id: "AC-EN-03",
    checkpoint: "G-HUMAN-SONG",
    step: 4,
    question: "Is the song ready for pictures?",
    options: [
      { label: "Yes", description: "Go on to the timeline." },
      { label: "Fix the hook", description: "One more take of the chorus." },
    ],
    ...over,
  });
