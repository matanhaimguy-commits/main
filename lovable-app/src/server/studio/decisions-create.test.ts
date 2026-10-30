// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { answerDecision } from "./decisions-answer.server";
import { createDecision } from "./decisions-create.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, songQuestion } from "./test-fixtures";

describe.skipIf(!hasDb)("createDecision (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  it("needs the run to be pushed first, and a step the run has", async () => {
    await expect(createDecision(db.sql, songQuestion())).rejects.toMatchObject({ status: 404 });
    await upsertRun(db.sql, runInput());
    await expect(createDecision(db.sql, songQuestion({ step: 9 }))).rejects.toThrow("Step 9 is not one of this run's steps.");
  });

  it("asks once per key: asking again while open updates the question", async () => {
    await upsertRun(db.sql, runInput());
    const { decision, updated } = await createDecision(db.sql, songQuestion());
    expect(updated).toBe(false);
    expect(decision).toMatchObject({ key: "G-HUMAN-SONG", status: "open", step: 4, multi: false });
    const again = await createDecision(db.sql, songQuestion({ question: "Is the song master ready?" }));
    expect(again).toMatchObject({ updated: true, decision: { id: decision.id, question: "Is the song master ready?" } });
  });

  it("refuses to re-ask an answered key, and takes a new key for a new question", async () => {
    await upsertRun(db.sql, runInput());
    const { decision } = await createDecision(db.sql, songQuestion());
    await answerDecision(db.sql, decision.id, { choices: ["Yes"], note: "" }, "owner");
    await expect(createDecision(db.sql, songQuestion())).rejects.toMatchObject({ status: 409 });
    expect((await createDecision(db.sql, songQuestion({ key: "G-HUMAN-SONG:2" }))).decision.id).not.toBe(decision.id);
  });
});
