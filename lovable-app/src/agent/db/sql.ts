/**
 * A small stand-in for the postgres.js tagged template, for hosts that cannot open a
 * Postgres connection (Lovable runs the app on Cloudflare Workers).
 *
 * Each query is compiled to plain SQL with every value written as a quoted literal, then
 * run by the `agent_sql` database function through Supabase's REST endpoint with the
 * service-role key. The engine keeps writing ordinary SQL:
 *
 *   await sql`SELECT * FROM contacts WHERE id = ${id}`
 *   sql`AND kind = ${kind}`        (a fragment, when nested inside another query)
 *   sql(['a', 'b'])                (an IN list)
 *   sql.json(value)                (a jsonb value)
 *   sql.unsafe("interval '1 day'") (trusted raw SQL, fragments only)
 *
 * Values are never spliced in unquoted: strings are single-quoted with quotes doubled
 * (the database runs with standard_conforming_strings on, so that is the whole escape),
 * numbers must be finite, and dates become typed timestamptz literals.
 */

export type Row = Record<string, any>;
export type Result<T extends readonly unknown[] = Row[]> = T & { count: number };

/** Runs one compiled statement. `wantRows` is false for statements that return no rows. */
export type Executor = (query: string, wantRows: boolean) => Promise<{ rows: Row[]; count: number }>;

class Json {
  constructor(readonly value: unknown) {}
}
class Raw {
  constructor(readonly text: string) {}
}
class List {
  constructor(readonly items: readonly unknown[]) {}
}

export class SqlError extends Error {
  constructor(
    message: string,
    readonly code?: string,
    readonly detail?: string,
  ) {
    super(message);
    this.name = 'SqlError';
  }
}

export class Query<T extends readonly unknown[] = Row[]> implements Promise<Result<T>> {
  readonly [Symbol.toStringTag] = 'Promise';
  private promise: Promise<Result<T>> | undefined;

  constructor(
    private readonly exec: Executor,
    private readonly strings: readonly string[],
    private readonly values: readonly unknown[],
  ) {}

  /** The statement text with every value inlined. */
  compile(): string {
    let text = this.strings[0] ?? '';
    for (let i = 0; i < this.values.length; i++) text += render(this.values[i]) + (this.strings[i + 1] ?? '');
    return text;
  }

  /** The template text only (values left out), used to decide whether rows come back. */
  shape(): string {
    let text = this.strings[0] ?? '';
    for (let i = 0; i < this.values.length; i++) {
      const v = this.values[i];
      text += (v instanceof Query ? v.shape() : v instanceof Raw ? v.text : ' ? ') + (this.strings[i + 1] ?? '');
    }
    return text;
  }

  private run(): Promise<Result<T>> {
    this.promise ??= (async () => {
      const text = this.compile().trim().replace(/;\s*$/, '');
      const { rows, count } = await this.exec(text, returnsRows(this.shape()));
      const result = rows.map(reviveRow) as unknown as Result<T>;
      result.count = count;
      return result;
    })();
    return this.promise;
  }

  then<A = Result<T>, B = never>(
    onfulfilled?: ((value: Result<T>) => A | PromiseLike<A>) | null,
    onrejected?: ((reason: unknown) => B | PromiseLike<B>) | null,
  ): Promise<A | B> {
    return this.run().then(onfulfilled, onrejected);
  }

  catch<B = never>(onrejected?: ((reason: unknown) => B | PromiseLike<B>) | null): Promise<Result<T> | B> {
    return this.run().catch(onrejected);
  }

  finally(onfinally?: (() => void) | null): Promise<Result<T>> {
    return this.run().finally(onfinally);
  }
}

export interface Sql {
  <T extends readonly unknown[] = Row[]>(strings: TemplateStringsArray, ...values: unknown[]): Query<T>;
  /** An IN list: `WHERE id IN ${sql(ids)}`. */
  (items: readonly unknown[]): List;
  json(value: unknown): Json;
  /** Trusted SQL text, inlined as is. Never pass user input. */
  unsafe(text: string): Raw;
  /** Runs `fn` with this client. Statements run one by one; there is no transaction. */
  begin<T>(fn: (tx: Sql) => Promise<T>): Promise<T>;
  end(opts?: { timeout?: number }): Promise<void>;
}

export function createSql(exec: Executor): Sql {
  const sql = ((first: TemplateStringsArray | readonly unknown[], ...values: unknown[]) => {
    if (isTemplate(first)) return new Query(exec, first, values);
    return new List(first);
  }) as Sql;
  sql.json = (value) => new Json(value);
  sql.unsafe = (text) => new Raw(text);
  sql.begin = (fn) => fn(sql);
  sql.end = async () => {};
  return sql;
}

function isTemplate(v: unknown): v is TemplateStringsArray {
  return Array.isArray(v) && Array.isArray((v as unknown as TemplateStringsArray).raw);
}

/** Statements that would make `WITH t AS (...) SELECT ... FROM t` invalid return no rows. */
export function returnsRows(shape: string): boolean {
  const s = shape.replace(/--[^\n]*/g, ' ').replace(/\bfor\s+(no\s+key\s+)?update\b/gi, ' ');
  if (/\breturning\b/i.test(s)) return true;
  if (/^\s*\(?\s*(select|values|table)\b/i.test(s)) return true;
  if (/^\s*with\b/i.test(s)) return !/\b(insert|update|delete)\b/i.test(s);
  return false;
}

function render(v: unknown): string {
  if (v instanceof Query) return v.compile();
  if (v instanceof Raw) return v.text;
  if (v instanceof Json) return `${quote(JSON.stringify(v.value ?? null))}::jsonb`;
  if (v instanceof List) {
    if (!v.items.length) return '(NULL)';
    return `(${v.items.map(literal).join(', ')})`;
  }
  return literal(v);
}

export function literal(v: unknown): string {
  if (v === null || v === undefined) return 'NULL';
  if (typeof v === 'boolean') return v ? 'TRUE' : 'FALSE';
  if (typeof v === 'number') {
    if (!Number.isFinite(v)) throw new SqlError(`cannot store the number ${v}`);
    return v < 0 ? `(${v})` : String(v);
  }
  if (typeof v === 'bigint') return v < 0n ? `(${v})` : String(v);
  if (v instanceof Date) {
    if (Number.isNaN(v.getTime())) throw new SqlError('cannot store an invalid date');
    return `${quote(v.toISOString())}::timestamptz`;
  }
  if (typeof v === 'string') return quote(v);
  if (Array.isArray(v)) return quote(`{${v.map(arrayElement).join(',')}}`);
  if (v instanceof Uint8Array) return `'\\x${[...v].map((b) => b.toString(16).padStart(2, '0')).join('')}'::bytea`;
  if (typeof v === 'object') return `${quote(JSON.stringify(v))}::jsonb`;
  throw new SqlError(`cannot store a value of type ${typeof v}`);
}

function quote(s: string): string {
  return `'${s.replace(/\0/g, '').replace(/'/g, "''")}'`;
}

function arrayElement(v: unknown): string {
  if (v === null || v === undefined) return 'NULL';
  if (typeof v === 'number' || typeof v === 'bigint') return String(v);
  if (typeof v === 'boolean') return v ? 't' : 'f';
  const s = v instanceof Date ? v.toISOString() : String(v);
  return `"${s.replace(/\0/g, '').replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
}

// to_jsonb() writes timestamptz as "2026-10-14T07:53:16.859123+00:00". postgres.js would
// hand back Date objects, and the engine relies on that.
const TIMESTAMPTZ = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?[+-]\d{2}(:\d{2})?$/;

function reviveRow(row: Row): Row {
  if (row === null || typeof row !== 'object') return row;
  for (const key of Object.keys(row)) {
    const v = row[key];
    if (typeof v === 'string' && TIMESTAMPTZ.test(v)) row[key] = new Date(v);
  }
  return row;
}

/** Runs statements through the `agent_sql` function with Supabase's REST API. */
export function restExecutor(opts: { url: string; key: string; fetch?: typeof fetch; timeoutMs?: number }): Executor {
  const endpoint = `${opts.url.replace(/\/$/, '')}/rest/v1/rpc/agent_sql`;
  const doFetch = opts.fetch ?? fetch;
  // New-style secret keys (sb_secret_...) go in the apikey header only; legacy keys are JWTs.
  const headers: Record<string, string> = { apikey: opts.key, 'Content-Type': 'application/json' };
  if (!opts.key.startsWith('sb_')) headers['Authorization'] = `Bearer ${opts.key}`;
  return async (query, wantRows) => {
    const res = await doFetch(endpoint, {
      method: 'POST',
      headers,
      body: JSON.stringify({ q: query, want_rows: wantRows }),
      signal: AbortSignal.timeout(opts.timeoutMs ?? 20_000),
    });
    const text = await res.text();
    let body: any;
    try {
      body = text ? JSON.parse(text) : null;
    } catch {
      body = text;
    }
    if (!res.ok) {
      const message = typeof body === 'object' && body ? body.message ?? text : text;
      throw new SqlError(`database error: ${message}`, body?.code, body?.details ?? body?.hint);
    }
    if (wantRows) {
      const rows = Array.isArray(body) ? body : [];
      return { rows, count: rows.length };
    }
    return { rows: [], count: Number(body?.count ?? 0) };
  };
}
