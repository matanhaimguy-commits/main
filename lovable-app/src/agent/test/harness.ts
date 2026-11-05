import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import postgres from 'postgres';
import { loadEnv } from '../config/env';
import { buildRegistry } from '../config/load';
import type { Business } from '../config/schema';
import { createSql, type Sql } from '../db/sql';
import { createDeps, type Deps } from '../engine/deps';
import { silentLog } from '../log';
import { FakeAi, FakeMeta } from './fakes';
import { APP_ID, APP_SECRET, VERIFY_TOKEN } from './fixtures';

// The fakes and payload builders live in their own files; tests still import everything from here.
export * from './fakes';
export * from './payloads';
export { APP_ID };

export const TEST_DB = process.env.TEST_DATABASE_URL ?? 'postgres://agent:agent@localhost:5432/social_agent_test';
const MIGRATION = fileURLToPath(new URL('../../../supabase/migrations/20261014090000_social_agent.sql', import.meta.url));
const FOLLOWUPS_MIGRATION = fileURLToPath(new URL('../../../supabase/migrations/20261028090000_funnel_followups.sql', import.meta.url));

let pg: postgres.Sql | undefined;
const admin = () => (pg ??= postgres(TEST_DB, { max: 4, onnotice: () => {} }));

export async function dbAvailable(): Promise<boolean> {
  try {
    await admin()`SELECT 1`;
    return true;
  } catch {
    return false;
  }
}

/**
 * A fresh schema from the Lovable migration (minus the pg_cron part, which a plain
 * Postgres lacks). Queries go through the same `agent_sql` function and literal
 * encoding the hosted app uses, so these tests cover the shim end to end.
 */
export async function freshDb(): Promise<Sql> {
  const db = admin();
  await db.unsafe('DROP SCHEMA public CASCADE; CREATE SCHEMA public;');
  const text = readFileSync(MIGRATION, 'utf8');
  await db.unsafe(text.slice(0, text.indexOf('-- ---- background work')));
  // Applied twice: the migration must be safe to run again.
  const followups = readFileSync(FOLLOWUPS_MIGRATION, 'utf8');
  await db.unsafe(followups);
  await db.unsafe(followups);
  return createSql(async (q, wantRows) => {
    const [row] = await db`SELECT public.agent_sql(${q}, ${wantRows}) AS r`;
    const r = row!['r'];
    return wantRows ? { rows: r, count: r.length } : { rows: [], count: Number(r.count) };
  });
}

export async function truncate(_sql: Sql) {
  await admin().unsafe(`TRUNCATE webhook_events, funnel_followups, contacts, comments, sends, messages, links, taps, ai_runs, alerts, business_state, meta_connections, app_state, businesses
    RESTART IDENTITY CASCADE`);
}


export interface Harness {
  deps: Deps;
  meta: FakeMeta;
  ai: FakeAi;
  alerts: string[];
  live: Set<string>;
}

export async function makeHarness(sql: Sql, businesses: Business[], extraEnv: Record<string, string> = {}): Promise<Harness> {
  const meta = new FakeMeta();
  const ai = new FakeAi();
  const alerts: string[] = [];
  const live = new Set(businesses.map((b) => b.slug));
  const env = loadEnv({
    META_APP_ID: APP_ID,
    META_APP_SECRET: APP_SECRET,
    META_VERIFY_TOKEN: VERIFY_TOKEN,
    LIVE_SENDING: 'true',
    ...extraEnv,
  });
  const base = await createDeps({
    sql,
    env,
    registry: buildRegistry(businesses),
    log: silentLog,
    alert: async (a) => {
      alerts.push(a.text);
    },
    ai,
    graph: (token) => {
      meta.tokens.push(token);
      return meta;
    },
    secrets: { PAGE_TOKEN_ACME: 'env-page-token' },
    sleep: async () => {},
  });
  // Tests flip a business to dry run by removing it from `live`.
  const deps: Deps = { ...base, isLive: (b) => live.has(b.slug) && base.isLive(b) };
  return { deps, meta, ai, alerts, live };
}
