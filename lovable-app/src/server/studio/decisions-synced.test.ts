// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { answerDecision } from "./decisions-answer.server";
import { createDecision } from "./decisions-create.server";
import { markSynced } from "./decisions-synced.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, songQuestion } from "./test-fixtures";

describe.skipIf(!hasDb)("markSynced (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  it("marks answered questions once, and says why it can't mark the others", async () => {
    await upsertRun(db.sql, runInput());
    const answered = (await createDecision(db.sql, songQuestion())).decision.id;
    const open = (await createDecision(db.sql, songQuestion({ key: "GATE-4", checkpoint: "GATE-4", step: null }))).decision.id;
    await answerDecision(db.sql, answered, { choices: ["Yes"], note: "" }, "owner");

    expect(await markSynced(db.sql, [answered, open, 999])).toEqual({
      synced: [answered],
      already: [],
      problems: [
        { id: open, error: "Still open: the owner hasn't answered it." },
        { id: 999, error: "No such decision." },
      ],
    });
    expect(await markSynced(db.sql, [answered, answered])).toEqual({ synced: [], already: [answered], problems: [] });
    expect(await markSynced(db.sql, [])).toEqual({ synced: [], already: [], problems: [] });
  });
});
