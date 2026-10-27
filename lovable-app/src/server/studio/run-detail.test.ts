// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { createDecision } from "./decisions-create.server";
import { runDetail } from "./run-detail.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput, songQuestion } from "./test-fixtures";

describe.skipIf(!hasDb)("runDetail (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  it("shows a run with its files, questions and the queue items no question covers", async () => {
    const { run } = await upsertRun(
      db.sql,
      runInput({
        waiting_on_owner: true,
        ledger: {
          queue: [
            { id: "G-HUMAN-SONG:", checkpoint: "G-HUMAN-SONG", status: "PENDING", note: "listen" },
            { id: "G-HUMAN-VOICE:V1", checkpoint: "G-HUMAN-VOICE", asset: "V1", status: "PENDING", note: "voice" },
          ],
        },
        files: [{ key: "img", label: "Board", kind: "image", url: "https://cdn.example/board.png", step: 4 }],
      }),
    );
    await createDecision(db.sql, songQuestion());
    const d = await runDetail(db.sql, run.id);
    expect(d?.run).toMatchObject({ id: run.id, business_name: "Acme Studio", waiting_on_owner: true });
    expect(d?.run).not.toHaveProperty("queue");
    expect(d?.files.map((f) => f.label)).toEqual(["Board"]);
    expect(d?.decisions.map((x) => x.checkpoint)).toEqual(["G-HUMAN-SONG"]);
    expect(d?.queue.map((q) => q.id)).toEqual(["G-HUMAN-VOICE:V1"]);
  });

  it("is null for a run that doesn't exist", async () => {
    expect(await runDetail(db.sql, 12345)).toBeNull();
  });
});
