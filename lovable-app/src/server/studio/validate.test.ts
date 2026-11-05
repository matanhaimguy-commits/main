// @vitest-environment node
import { describe, expect, it } from "vitest";
import { DecisionInput } from "./schema";
import { runInput, step } from "./test-fixtures";
import { answerProblem, decisionInputProblems, runInputProblems } from "./validate";

describe("studio input checks", () => {
  it("refuses duplicate steps and file keys, and files on steps the run doesn't have", () => {
    const input = runInput({
      steps: [step(0, "done"), step(0, "active")],
      files: [
        { key: "a", label: "A", kind: "doc", markdown: "# A", step: 7 },
        { key: "a", label: "B", kind: "doc", markdown: "# B" },
      ],
    });
    const problems = runInputProblems(input).join(" ");
    expect(problems).toContain("Step 0 appears twice");
    expect(problems).toContain('File key "a" appears twice');
    expect(problems).toContain("names step 7");
    expect(runInputProblems(runInput({ steps: [], files: [{ key: "x", label: "X", kind: "doc", markdown: "x", step: 1 }] })).join(" ")).toContain(
      "this run has no steps",
    );
    expect(runInputProblems(runInput({ current_step: 9 }))).toEqual(["current_step 9 is not one of the steps."]);
    expect(runInputProblems(runInput())).toEqual([]);
  });

  it("checks a question's options", () => {
    const q = DecisionInput.parse({
      business: "acme",
      post_id: "AC-EN-03",
      checkpoint: "G-HUMAN-SONG",
      question: "Which take?",
      options: [{ label: "Take 1" }, { label: "take 1" }],
      multi: true,
    });
    expect(decisionInputProblems(q)).toEqual(['Option "take 1" appears twice.']);
    expect(decisionInputProblems({ ...q, options: [{ label: "Only" }] })).toEqual(["A multi-select question needs at least 2 options."]);
  });

  it("checks an answer against its question", () => {
    const one = { options: [{ label: "A" }, { label: "B" }], multi: false, status: "open" as const };
    expect(answerProblem(one, { choices: ["A"], note: "" })).toBeNull();
    expect(answerProblem(one, { choices: [], note: "neither, because..." })).toBeNull();
    expect(answerProblem(one, { choices: ["A", "B"], note: "" })).toBe("Pick one option.");
    expect(answerProblem(one, { choices: ["C"], note: "" })).toBe('"C" is not one of the options.');
    expect(answerProblem(one, { choices: [], note: "  " })).toBe("Pick an option or write a note.");
    expect(answerProblem({ ...one, multi: true }, { choices: ["A", "B"], note: "" })).toBeNull();
    expect(answerProblem({ ...one, multi: true }, { choices: ["A", "A"], note: "" })).toBe("The same option is chosen twice.");
    expect(answerProblem({ ...one, options: [] }, { choices: [], note: "" })).toBe("Write your answer in the note.");
    expect(answerProblem({ ...one, status: "synced" }, { choices: ["A"], note: "" })).toMatch(/already taken this answer in/);
  });
});
