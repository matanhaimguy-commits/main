import "@tanstack/react-start/server-only";
import { createClaudeAi } from "@/agent/ai/agent";
import { createAlerter } from "@/agent/alerts";
import { buildRegistry, ConfigError, parseBusiness } from "@/agent/config/load";
import type { Business } from "@/agent/config/schema";
import type { Sql } from "@/agent/db/sql";
import { createDeps, type Deps } from "@/agent/engine/deps";
import { log } from "@/agent/log";
import { getDb, runtimeVars } from "./db.server";
import { currentWaitUntil } from "./request-context";
import { loadRuntimeEnv } from "./settings.server";

export interface BusinessRow {
  slug: string;
  config: Record<string, unknown>;
  updated_at: Date;
}

export interface LoadedBusinesses {
  businesses: Business[];
  /** Rows that fail validation are left out of the engine and listed here. */
  invalid: { slug: string; problems: string[] }[];
  rows: BusinessRow[];
}

export async function loadBusinesses(sql: Sql): Promise<LoadedBusinesses> {
  const rows = await sql<BusinessRow[]>`SELECT slug, config, updated_at FROM businesses ORDER BY slug`;
  const businesses: Business[] = [];
  const invalid: LoadedBusinesses["invalid"] = [];
  for (const row of rows) {
    try {
      businesses.push(parseBusiness(row.config, row.slug));
    } catch (err) {
      invalid.push({ slug: row.slug, problems: err instanceof ConfigError ? err.problems : [(err as Error).message] });
    }
  }
  return { businesses, invalid, rows };
}

/** Everything the engine needs, built fresh for this request from the database and settings. */
export async function createRuntimeDeps(sql: Sql = getDb()): Promise<{ deps: Deps; loaded: LoadedBusinesses }> {
  const [{ env }, loaded] = await Promise.all([loadRuntimeEnv(sql), loadBusinesses(sql)]);
  let registry;
  try {
    registry = buildRegistry(loaded.businesses);
  } catch (err) {
    // Two businesses claiming one Page: keep running with none rather than guessing.
    log.error("business config conflict", { problems: err instanceof ConfigError ? err.problems : String(err) });
    registry = buildRegistry([]);
  }
  const deps = await createDeps({
    sql,
    env,
    registry,
    log,
    alert: createAlerter(env, sql, log),
    ai: env.ANTHROPIC_API_KEY ? createClaudeAi({ model: env.CLAUDE_MODEL, apiKey: env.ANTHROPIC_API_KEY }) : undefined,
    secrets: runtimeVars(),
  });
  return { deps, loaded };
}

/**
 * Runs `task` after the response when the host allows it (Cloudflare `waitUntil`),
 * otherwise before answering. `task` learns which, so it can keep the inline case short.
 * Errors are logged, never thrown at the caller.
 */
export async function runAfterResponse(
  request: Request,
  name: string,
  task: (inBackground: boolean) => Promise<unknown>,
): Promise<void> {
  const waitUntil = currentWaitUntil(request);
  const safe = task(!!waitUntil).then(
    () => undefined,
    (err) => log.error(`${name} failed`, { err }),
  );
  if (waitUntil) waitUntil(safe);
  else await safe;
}
