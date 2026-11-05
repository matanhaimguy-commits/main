// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { answerDecision } from "./decisions-answer.server";
import { createDecision } from "./decisions-create.server";
import { markSynced } from "./decisions-synced.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, songQuestion } from "./test-fixtures";

describe.skipIf(!hasDb)("answerDecision (Postgres)", () => {
  let db: StudioDb;
  let id: number;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(async () => {
    await resetStudio(db);
    await upsertRun(db.sql, runInput());
    id = (await createDecision(db.sql, songQuestion())).decision.id;
  });

  it("stores the choice and the trimmed note, with who answered and when", async () => {
    const a = await answerDecision(db.sql, id, { choices: ["Fix the hook"], note: " slower chorus " }, "owner");
    expect(a).toMatchObject({ status: "answered", answer: { choices: ["Fix the hook"], note: "slower chorus", by: "owner" } });
    expect(a.answered_at).toBeInstanceOf(Date);
  });

  it("refuses an answer that isn't one of the options", async () => {
    await expect(answerDecision(db.sql, id, { choices: ["Maybe"], note: "" }, "owner")).rejects.toThrow('"Maybe" is not one of the options.');
  });

  it("lets the owner change the answer until the studio takes it in", async () => {
    await answerDecision(db.sql, id, { choices: ["Fix the hook"], note: "" }, "owner");
    expect((await answerDecision(db.sql, id, { choices: ["Yes"], note: "" }, "owner")).answer?.choices).toEqual(["Yes"]);
    await markSynced(db.sql, [id]);
    await expect(answerDecision(db.sql, id, { choices: ["Fix the hook"], note: "" }, "owner")).rejects.toMatchObject({ status: 409 });
    await expect(answerDecision(db.sql, 999, { choices: ["Yes"], note: "" }, "owner")).rejects.toMatchObject({ status: 404 });
  });
});
