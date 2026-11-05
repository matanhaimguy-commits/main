import "@tanstack/react-start/server-only";
import { createSql, restExecutor, type Sql } from "@/agent/db/sql";

/**
 * Variables the host gives the server at runtime: Lovable Cloud secrets (Cloudflare
 * bindings, mirrored on process.env) plus anything Vite inlined at build time. Read per
 * request, never at module scope: on Workers the values only exist inside a request.
 */
export function runtimeVars(): Record<string, string | undefined> {
  const out: Record<string, string | undefined> = {};
  const bindings = (globalThis as { __env__?: Record<string, unknown> }).__env__;
  if (bindings) for (const [k, v] of Object.entries(bindings)) if (typeof v === "string" && v !== "") out[k] = v;
  const proc = typeof process !== "undefined" && process.env ? process.env : {};
  for (const [k, v] of Object.entries(proc)) if (typeof v === "string" && v !== "" && out[k] === undefined) out[k] = v;
  return out;
}

export interface DbConfig {
  url?: string;
  key?: string;
}

export function dbConfig(vars = runtimeVars()): DbConfig {
  return {
    url: vars["SUPABASE_URL"] ?? (import.meta.env["VITE_SUPABASE_URL"] as string | undefined),
    key: vars["SUPABASE_SERVICE_ROLE_KEY"] ?? vars["SUPABASE_SECRET_KEY"],
  };
}

export class NoDatabaseError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "NoDatabaseError";
  }
}

let cached: { id: string; sql: Sql } | undefined;

/** The database client (service role). Throws NoDatabaseError when Lovable Cloud is not wired up. */
export function getDb(): Sql {
  const { url, key } = dbConfig();
  if (!url) throw new NoDatabaseError("SUPABASE_URL is not available. Enable Lovable Cloud for this project.");
  if (!key) throw new NoDatabaseError("The service-role key is not available to the server (SUPABASE_SERVICE_ROLE_KEY).");
  const id = `${url}|${key.slice(-12)}`;
  if (cached?.id !== id) cached = { id, sql: createSql(restExecutor({ url, key })) };
  return cached.sql;
}

/** A key only this server knows, for encrypting stored settings and signing cookies. */
export function serverKey(): string {
  const { key } = dbConfig();
  if (!key) throw new NoDatabaseError("The service-role key is not available to the server.");
  return key;
}

export interface DbHealth {
  ok: boolean;
  problem?: string;
}

export async function checkDb(): Promise<DbHealth> {
  try {
    const sql = getDb();
    await sql`SELECT 1 FROM app_state LIMIT 1`;
    return { ok: true };
  } catch (err) {
    const message = (err as Error).message;
    if (err instanceof NoDatabaseError) return { ok: false, problem: message };
    if (/agent_sql|PGRST202|schema cache/i.test(message)) {
      return { ok: false, problem: "The database tables are not created yet (run the migration in supabase/migrations)." };
    }
    if (/app_state/i.test(message)) return { ok: false, problem: "The database tables are not created yet." };
    return { ok: false, problem: message };
  }
}
