// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import type { Sql } from "@/agent/db/sql";
import { makeBusiness } from "@/agent/test/fixtures";
import { dbAvailable, freshDb, truncate } from "@/agent/test/harness";

// The endpoint reads its database from getDb(); point it at the test database.
const shared = vi.hoisted(() => ({ sql: undefined as unknown as Sql }));
vi.mock("./db.server", async (original) => ({ ...(await original<typeof import("./db.server")>()), getDb: () => shared.sql }));

import { contentApi } from "./content-api.server";
import { createStudioToken } from "./content.server";

const hasDb = await dbAvailable();

const funnel = (over: Record<string, unknown> = {}) => ({
  id: "words-dm",
  trigger: "dm_keyword",
  keywords: ["WORDS"],
  opener: { text: "Want the WORDS Sheet?", button: "Send it" },
  deliver: { text: "Here it is.", link: "https://acme.studio/words.pdf", button: "Open the sheet" },
  after: "One question: what does a normal month bring in for you right now?",
  ...over,
});

/** POST /api/content/funnels (what `hub.py funnel` calls): the delay is checked like every other funnel field. */
describe.skipIf(!hasDb)("POST /api/content/funnels and after_delay_minutes (Postgres)", () => {
  let sql: Sql;
  let token: string;

  beforeAll(async () => {
    sql = await freshDb();
    shared.sql = sql;
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await truncate(sql);
    const config = { ...makeBusiness(), funnels: [] };
    await sql`INSERT INTO businesses (slug, config) VALUES ('acme', ${sql.json(config)})`;
    token = await createStudioToken(sql);
  });

  const post = async (body: unknown, auth = true) => {
    const res = await contentApi(
      new Request("https://hub.example/api/content/funnels", {
        method: "POST",
        headers: { "content-type": "application/json", ...(auth ? { authorization: `Bearer ${token}` } : {}) },
        body: JSON.stringify(body),
      }),
      "funnels",
    );
    return { status: res.status, body: (await res.json()) as any };
  };
  const stored = async () => {
    const [row] = await sql<{ config: { funnels: Record<string, unknown>[] } }[]>`SELECT config FROM businesses WHERE slug = 'acme'`;
    return row!.config.funnels;
  };

  it("needs the studio token", async () => {
    expect((await post({ business: "acme", funnel: funnel() }, false)).status).toBe(401);
  });

  it("stores a funnel with a delay", async () => {
    const res = await post({ business: "acme", funnel: funnel({ after_delay_minutes: 15 }) });
    expect(res).toMatchObject({ status: 200, body: { ok: true, problems: [] } });
    expect((await stored())[0]).toMatchObject({ id: "words-dm", after_delay_minutes: 15 });
  });

  it("stores a funnel without the setting as it always did", async () => {
    const res = await post({ business: "acme", funnel: funnel() });
    expect(res.status).toBe(200);
    expect(await stored()).toHaveLength(1);
    expect((await stored())[0]).not.toHaveProperty("after_delay_minutes");
  });

  it.each([
    ["above 60", 61],
    ["negative", -1],
    ["not a whole number", 12.5],
    ["text", "10"],
  ])("refuses a delay that is %s, and stores nothing", async (_name, value) => {
    const res = await post({ business: "acme", funnel: funnel({ after_delay_minutes: value }) });
    expect(res.status).toBe(422);
    expect(res.body.ok).toBe(false);
    expect(res.body.problems.join(" ")).toContain("after_delay_minutes");
    expect(await stored()).toHaveLength(0);
  });

  it("replaces a funnel's delay when the same funnel is sent again", async () => {
    await post({ business: "acme", funnel: funnel({ after_delay_minutes: 15 }) });
    await post({ business: "acme", funnel: funnel({ after_delay_minutes: 30 }) });
    const funnels = await stored();
    expect(funnels).toHaveLength(1);
    expect(funnels[0]).toMatchObject({ after_delay_minutes: 30 });
  });

  it("warns, without refusing, when there is a delay but no last message", async () => {
    const res = await post({ business: "acme", funnel: funnel({ after: undefined, after_delay_minutes: 15 }) });
    expect(res.status).toBe(200);
    expect(res.body.issues.some((i: { message: string }) => i.message.includes("after_delay_minutes"))).toBe(true);
  });
});
