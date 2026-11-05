// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { StudioError } from "./errors";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, step } from "./test-fixtures";

describe.skipIf(!hasDb)("upsertRun (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  it("creates a run with its current step and status worked out from the steps", async () => {
    const { run } = await upsertRun(db.sql, runInput());
    expect(run).toMatchObject({ business: "acme", post_id: "AC-EN-03", current_step: 3, status: "active", title: "Maya's quilt" });
    expect(run.steps.map((s) => s.status)).toEqual(["done", "done", "done", "active", "pending", "na"]);
    expect(run.steps[3]!.gates.map((g) => g.score)).toEqual([81, 86]);
  });

  it("updates the same run in place and keeps the title when a re-push has none", async () => {
    const first = await upsertRun(db.sql, runInput());
    const second = await upsertRun(db.sql, runInput({ title: undefined, steps: [step(0, "done"), step(1, "done")] }));
    expect(second.run.id).toBe(first.run.id);
    expect(second.run).toMatchObject({ title: "Maya's quilt", status: "done", current_step: null });
    expect((await db.pg`SELECT count(*)::int AS n FROM studio_runs`)[0]!.n).toBe(1);
  });

  it("refuses a business the app doesn't have, and input that contradicts itself", async () => {
    await expect(upsertRun(db.sql, runInput({ business: "nobody" }))).rejects.toMatchObject({ status: 404 });
    await expect(upsertRun(db.sql, runInput({ steps: [step(1, "done"), step(1, "done")] }))).rejects.toBeInstanceOf(StudioError);
  });
});
