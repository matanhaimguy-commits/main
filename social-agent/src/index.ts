import { existsSync } from 'node:fs';
import path from 'node:path';
import { serve } from '@hono/node-server';
import { createClaudeAi } from './ai/agent.js';
import { createAlerter } from './alerts.js';
import { loadEnv, requireEnv } from './config/env.js';
import { loadRegistry, PROJECT_ROOT } from './config/load.js';
import { connect, migrate } from './db/index.js';
import { liveStatus, metaClientFactory, type Deps } from './engine/deps.js';
import { log } from './log.js';
import { createApp } from './server.js';
import { startWorker } from './worker.js';

// Local development reads .env; hosted deployments set real environment variables.
const envFile = path.join(PROJECT_ROOT, '.env');
if (existsSync(envFile)) process.loadEnvFile(envFile);

async function main() {
  const env = loadEnv();
  const registry = loadRegistry(env.BUSINESSES_DIR);
  const sql = connect(requireEnv(env, 'DATABASE_URL'));
  await migrate(sql, (m) => log.info(m));

  const status = new Map(registry.businesses.map((b) => [b.slug, liveStatus(b, env)]));
  for (const b of registry.businesses) {
    const s = status.get(b.slug)!;
    log.info('business', { slug: b.slug, live: s.live, reason: s.reason, testers: b.testers.length, funnels: b.funnels.length });
    for (const issue of s.issues) log[issue.level === 'error' ? 'error' : 'warn']('audit', { ...issue });
  }
  for (const key of ['META_APP_SECRET', 'META_VERIFY_TOKEN', 'META_APP_ID'] as const) {
    if (!env[key]) log.warn(`${key} is not set`);
  }
  if (!env.ANTHROPIC_API_KEY) log.warn('ANTHROPIC_API_KEY is not set: AI replies are off, funnels still run');

  const deps: Deps = {
    sql,
    env,
    registry,
    log,
    alert: createAlerter(env, sql, log),
    ai: env.ANTHROPIC_API_KEY ? createClaudeAi({ model: env.CLAUDE_MODEL, apiKey: env.ANTHROPIC_API_KEY }) : undefined,
    metaFor: metaClientFactory(env),
    isLive: (b) => status.get(b.slug)?.live ?? false,
    now: () => new Date(),
    sleep: (ms) => new Promise((r) => setTimeout(r, ms)),
  };

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
