// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { createStudioToken } from "../content.server";
import { withStudioToken, type StudioHandler } from "./api-common.server";
import { getDecisions, postDecisions } from "./api-decisions.server";
import { getRuns, postRun } from "./api-runs.server";
import { postSynced } from "./api-synced.server";
import { answerDecision } from "./decisions-answer.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput } from "./test-fixtures";

/** The /api/studio/* handlers end to end: token, validation, answers and status codes. */
describe.skipIf(!hasDb)("the /api/studio endpoints (Postgres)", () => {
  let db: StudioDb;
  let token: string;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(async () => {
    await resetStudio(db);
    token = await createStudioToken(db.sql);
  });

  const call = async (handler: StudioHandler, method: string, path: string, body?: unknown, auth = true) => {
    const req = new Request(`https://hub.example/api/studio/${path}`, {
      method,
      headers: { "content-type": "application/json", ...(auth ? { authorization: `Bearer ${token}` } : {}) },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    const res = await withStudioToken(req, handler, db.sql);
    return { status: res.status, body: (await res.json()) as any };
  };

  it("needs the studio token", async () => {
    expect((await call(getRuns, "GET", "runs", undefined, false)).status).toBe(401);
  });

  it("upserts a run and reads it back, one or all", async () => {
    const bad = await call(postRun, "POST", "runs", { business: "acme" });
    expect(bad).toMatchObject({ status: 400, body: { error: "Invalid run." } });
    const saved = await call(postRun, "POST", "runs", runInput());
    expect(saved.status).toBe(200);
    const one = await call(getRuns, "GET", "runs?business=acme&post_id=AC-EN-03");
    expect(one.body).toMatchObject({ run: { id: saved.body.run.id, post_id: "AC-EN-03" }, files: [], decisions: [] });
    expect((await call(getRuns, "GET", "runs?business=acme&post_id=NOPE")).status).toBe(404);
    expect((await call(getRuns, "GET", "runs?post_id=AC-EN-03")).status).toBe(400);
    const all = await call(getRuns, "GET", "runs");
    expect(all.body.runs).toHaveLength(1);
    expect(all.body.runs[0]).not.toHaveProperty("steps");
  });

  it("asks, lists answers, and marks them taken in", async () => {
    await call(postRun, "POST", "runs", runInput());
    const asked = await call(postDecisions, "POST", "decisions", {
      business: "acme",
      post_id: "AC-EN-03",
      checkpoint: "GATE-4",
      question: "Which spine?",
      options: [{ label: "A" }, { label: "B" }],
    });
    expect(asked.body).toMatchObject({ updated: false, decision: { key: "GATE-4", status: "open" } });
    const id = asked.body.decision.id as number;
    expect((await call(postSynced, "POST", "synced", { ids: [id] })).status).toBe(409);

    await answerDecision(db.sql, id, { choices: ["B"], note: "" }, "owner");
    expect((await call(getDecisions, "GET", "decisions")).body.decisions.map((d: { id: number }) => d.id)).toEqual([id]);
    expect((await call(getDecisions, "GET", "decisions?status=maybe")).status).toBe(400);
    expect(await call(postSynced, "POST", "synced", { ids: [id] })).toEqual({ status: 200, body: { synced: [id], already: [], problems: [] } });
    expect((await call(postSynced, "POST", "synced", {})).status).toBe(400);
  });

  it("takes several questions at once and turns studio errors into their status", async () => {
    const many = await call(postDecisions, "POST", "decisions", { decisions: [{ business: "acme", post_id: "AC-EN-03", checkpoint: "X", question: "?" }] });
    expect(many).toMatchObject({ status: 404, body: { error: expect.stringContaining("Push it first") } });
  });
});
