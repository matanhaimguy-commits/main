import { existsSync } from 'node:fs';
import path from 'node:path';
import { serve } from '@hono/node-server';
import { createClaudeAi } from './ai/agent.js';
import { createAlerter } from './alerts.js';
import { configuredPublicUrl, loadEnv, requireEnv } from './config/env.js';
import { ConfigError, loadRegistry, PROJECT_ROOT, type Registry } from './config/load.js';
import { connect, migrate, type Sql } from './db/index.js';
import { createDeps } from './engine/deps.js';
import { log } from './log.js';
import { createApp } from './server.js';
import { PROBLEMS, startSetupMode, type SetupProblem } from './setup-mode.js';
import { startWorker } from './worker.js';

// Local development reads .env; hosted deployments set real environment variables.
const envFile = path.join(PROJECT_ROOT, '.env');
if (existsSync(envFile)) process.loadEnvFile(envFile);

/** Connects and migrates, retrying while a freshly created database is still starting. */
async function openDatabase(url: string): Promise<{ sql: Sql } | { error: string }> {
  let error = '';
  for (let attempt = 1; attempt <= 6; attempt++) {
    const sql = connect(url);
    try {
      await migrate(sql, (m) => log.info(m));
      return { sql };
    } catch (err) {
      error = (err as Error).message;
      log.warn('database not reachable yet', { attempt, error });
      await sql.end({ timeout: 1 }).catch(() => {});
      await new Promise((r) => setTimeout(r, 5_000));
    }
  }
  return { error };
}

async function main() {
  const env = loadEnv();
  const problems: SetupProblem[] = [];
  let registry: Registry | undefined;
  try {
    registry = loadRegistry(env.BUSINESSES_DIR);
  } catch (err) {
    problems.push(PROBLEMS.badConfig(err instanceof ConfigError ? err.problems.join('; ') : (err as Error).message));
  }
  if (!env.DATABASE_URL) problems.push(PROBLEMS.noDatabase);
  if (!env.ADMIN_PASSWORD) problems.push(PROBLEMS.noPassword);
  if (problems.length || !registry || !env.DATABASE_URL) return startSetupMode(env, problems);

  const db = await openDatabase(requireEnv(env, 'DATABASE_URL'));
  if ('error' in db) return startSetupMode(env, [PROBLEMS.dbUnreachable(db.error)]);
  const sql = db.sql;

  const deps = await createDeps({
    sql,
    env,
    registry,
    log,
    alert: createAlerter(env, sql, log),
    ai: env.ANTHROPIC_API_KEY ? createClaudeAi({ model: env.CLAUDE_MODEL, apiKey: env.ANTHROPIC_API_KEY }) : undefined,
  });

  for (const b of registry.businesses) {
    const s = deps.liveStatus(b);
    log.info('business', { slug: b.slug, live: s.live, reason: s.reason, page: b.meta.page_id ?? null, testers: b.testers.length, funnels: b.funnels.length });
    for (const issue of s.issues) log[issue.level === 'error' ? 'error' : 'warn']('audit', { ...issue });
  }
  for (const key of ['META_APP_ID', 'META_APP_SECRET', 'ADMIN_PASSWORD'] as const) {
    if (!env[key]) log.warn(`${key} is not set`);
  }
  if (!env.ANTHROPIC_API_KEY) log.warn('ANTHROPIC_API_KEY is not set: AI replies are off, funnels still run');
  log.info('setup page', { url: `${configuredPublicUrl(env) ?? `http://localhost:${env.PORT}`}/admin/setup` });

  const worker = env.RUN_WORKER ? startWorker(deps) : undefined;
  const app = createApp(deps, { onEvent: () => worker?.nudge() });
  const server = serve({ fetch: app.fetch, port: env.PORT }, (info) => log.info('listening', { port: info.port }));

  const shutdown = async (signal: string) => {
    log.info('shutting down', { signal });
    server.close();
    await worker?.stop();
    await sql.end({ timeout: 5 });
    process.exit(0);
  };
  process.on('SIGTERM', () => void shutdown('SIGTERM'));
  process.on('SIGINT', () => void shutdown('SIGINT'));
}

main().catch((err) => {
  log.error('fatal', { err });
  process.exit(1);
});
