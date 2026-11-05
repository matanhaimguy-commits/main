// @vitest-environment node
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { createSql, literal, returnsRows, type Executor, type Sql } from '../db/sql';
import { dbAvailable, freshDb } from './harness';

/** Captures what would be sent instead of running it. */
function recorder() {
  const seen: { query: string; wantRows: boolean }[] = [];
  const exec: Executor = async (query, wantRows) => {
    seen.push({ query, wantRows });
    return { rows: [{ ok: 1, at: '2026-10-14T07:53:16.859123+00:00', label: '2026-10-14' }], count: 1 };
  };
  return { sql: createSql(exec), seen };
}

describe('sql shim: compiling', () => {
  it('quotes strings by doubling single quotes and keeps backslashes literal', () => {
    expect(literal("it's")).toBe("'it''s'");
    expect(literal('a\\b')).toBe("'a\\b'");
    expect(literal("x'); DROP TABLE contacts; --")).toBe("'x''); DROP TABLE contacts; --'");
    expect(literal('nul\0byte')).toBe("'nulbyte'");
  });

  it('writes numbers, booleans, nulls, dates and json as typed literals', () => {
    expect(literal(42)).toBe('42');
    expect(literal(-5)).toBe('(-5)');
    expect(literal(true)).toBe('TRUE');
    expect(literal(null)).toBe('NULL');
    expect(literal(undefined)).toBe('NULL');
    expect(literal(new Date('2026-01-02T03:04:05.000Z'))).toBe("'2026-01-02T03:04:05.000Z'::timestamptz");
    expect(literal({ a: "o'k" })).toBe(`'{"a":"o''k"}'::jsonb`);
    expect(() => literal(Number.NaN)).toThrow();
  });

  it('inlines fragments, IN lists, json and raw text', async () => {
    const { sql, seen } = recorder();
    const kind = 'message';
    await sql`SELECT * FROM sends WHERE id IN ${sql([1, 2])} ${kind ? sql`AND kind = ${kind}` : sql``}
      AND created_at > now() - ${sql.unsafe("interval '1 day'")} AND request = ${sql.json({ x: 1 })}`;
    expect(seen[0]!.query).toBe(
      `SELECT * FROM sends WHERE id IN (1, 2) AND kind = 'message'\n      AND created_at > now() - interval '1 day' AND request = '{"x":1}'::jsonb`,
    );
  });

  it('does not run fragments on their own, and runs a query once however often it is awaited', async () => {
    const { sql, seen } = recorder();
    sql`AND kind = ${'x'}`;
    const q = sql`SELECT 1`;
    await q;
    await q;
    expect(seen).toHaveLength(1);
  });

  it('turns timestamptz strings back into Dates, and leaves other text alone', async () => {
    const { sql } = recorder();
    const [row] = await sql`SELECT 1`;
    expect(row!['at']).toBeInstanceOf(Date);
    expect(row!['label']).toBe('2026-10-14');
  });

  it('decides from the template, never from values, whether rows come back', async () => {
    expect(returnsRows('SELECT 1')).toBe(true);
    expect(returnsRows('INSERT INTO t VALUES ( ? )')).toBe(false);
    expect(returnsRows('INSERT INTO t VALUES ( ? ) RETURNING id')).toBe(true);
    expect(returnsRows('UPDATE t SET a = 1 WHERE id IN (SELECT id FROM t FOR UPDATE SKIP LOCKED)')).toBe(false);
    expect(returnsRows('WITH x AS (SELECT 1) SELECT * FROM x')).toBe(true);

    const { sql, seen } = recorder();
    await sql`INSERT INTO messages (text) VALUES (${'please keep returning my calls'})`;
    expect(seen[0]!.wantRows).toBe(false);
  });
});

const hasDb = await dbAvailable();

describe.skipIf(!hasDb)('sql shim: against Postgres', () => {
  let sql: Sql;
  beforeAll(async () => {
    sql = await freshDb();
  });
  afterAll(async () => {
    await sql?.end();
  });

  it('stores and reads back hostile and multilingual text unchanged', async () => {
    const samples = [
      "Robert'); DROP TABLE contacts;--",
      'back\\slash \\x00 and $1 and $$dollar$$',
      'שלום! כמה עולה? 🙌',
      'line one\nline two\ttab',
      'keep returning my calls',
      "E'escape' U&'\\0041'",
    ];
    const [c] = await sql<{ id: number }[]>`
      INSERT INTO contacts (business, platform, external_id) VALUES ('acme', 'instagram', 'U1') RETURNING id`;
    for (const text of samples) {
      await sql`INSERT INTO messages (contact_id, direction, source, text) VALUES (${c!.id}, 'in', 'user', ${text})`;
    }
    const rows = await sql<{ text: string }[]>`SELECT text FROM messages WHERE contact_id = ${c!.id} ORDER BY id`;
    expect(rows.map((r) => r.text)).toEqual(samples);
    const [{ n }] = (await sql<{ n: number }[]>`SELECT count(*)::int AS n FROM contacts`) as unknown as [{ n: number }];
    expect(n).toBe(1);
  });

  it('reports affected row counts for statements without RETURNING', async () => {
    const r = await sql`UPDATE contacts SET stage = 'engaged' WHERE business = ${'acme'}`;
    expect(r.count).toBe(1);
    expect(r).toHaveLength(0);
  });

  it('round-trips jsonb, timestamps and booleans', async () => {
    const at = new Date('2026-03-04T05:06:07.123Z');
    await sql`INSERT INTO app_state (key, value, updated_at) VALUES ('k', ${sql.json({ a: [1, 'two'], b: null })}, ${at})`;
    const [row] = await sql<{ value: unknown; updated_at: Date; yes: boolean }[]>`
      SELECT value, updated_at, true AS yes FROM app_state WHERE key = 'k'`;
    expect(row!.value).toEqual({ a: [1, 'two'], b: null });
    expect(row!.updated_at).toBeInstanceOf(Date);
    expect(row!.updated_at.getTime()).toBe(at.getTime());
    expect(row!.yes).toBe(true);
  });

  it('surfaces database errors', async () => {
    await expect(sql`SELECT * FROM no_such_table`).rejects.toThrow(/no_such_table/);
  });
});
