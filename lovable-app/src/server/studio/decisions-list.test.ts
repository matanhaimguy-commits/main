// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { answerDecision } from "./decisions-answer.server";
import { createDecision } from "./decisions-create.server";
import { listDecisions } from "./decisions-list.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, songQuestion } from "./test-fixtures";

describe.skipIf(!hasDb)("listDecisions (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  it("filters by status and business, with each question's run", async () => {
    const { run } = await upsertRun(db.sql, runInput());
    const song = (await createDecision(db.sql, songQuestion())).decision;
    const spine = (await createDecision(db.sql, songQuestion({ key: "GATE-4", checkpoint: "GATE-4", step: null }))).decision;
    await answerDecision(db.sql, song.id, { choices: ["Yes"], note: "" }, "owner");

    const answered = await listDecisions(db.sql, { status: "answered" });
    expect(answered.map((d) => [d.id, d.business, d.post_id, d.run_title, d.answer?.choices])).toEqual([[song.id, "acme", "AC-EN-03", "Maya's quilt", ["Yes"]]]);
    expect((await listDecisions(db.sql, { runId: run.id })).map((d) => d.id)).toEqual([spine.id, song.id]); // open first
    expect(await listDecisions(db.sql, { status: "answered", business: "other" })).toEqual([]);
  });
});
