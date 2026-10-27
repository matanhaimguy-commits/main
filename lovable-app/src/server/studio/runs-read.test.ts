// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { createDecision } from "./decisions-create.server";
import { findRun, listRuns } from "./runs-read.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, songQuestion } from "./test-fixtures";

describe.skipIf(!hasDb)("reading runs (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  it("finds a run by business and post id, without its ledger", async () => {
    await upsertRun(db.sql, runInput());
    const run = await findRun(db.sql, "acme", "AC-EN-03");
    expect(run).toMatchObject({ post_id: "AC-EN-03", title: "Maya's quilt" });
    expect(run).not.toHaveProperty("ledger");
    expect(await findRun(db.sql, "acme", "NOPE")).toBeNull();
  });

  it("lists pieces with an open question first, with the business's name", async () => {
    await upsertRun(db.sql, runInput());
    await createDecision(db.sql, songQuestion());
    await upsertRun(db.sql, runInput({ post_id: "AC-EN-04", title: "Newer piece" }));
    const list = await listRuns(db.sql);
    expect(list.map((x) => [x.post_id, x.business_name, x.waiting, x.open_decisions])).toEqual([
      ["AC-EN-03", "Acme Studio", true, 1],
      ["AC-EN-04", "Acme Studio", false, 0],
    ]);
    expect(await listRuns(db.sql, { business: "other" })).toEqual([]);
  });
});
