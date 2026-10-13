import { serve } from '@hono/node-server';
import { Hono } from 'hono';
import type { Env } from './config/env.js';
import { html, page } from './html.js';
import { log } from './log.js';

export interface SetupProblem {
  title: string;
  how: string;
}

/**
 * Started instead of the real server when something essential is missing (usually the
 * database). The deploy stays up and its address explains exactly what to add, instead of
 * crashing in a restart loop.
 */
export function startSetupMode(env: Env, problems: SetupProblem[]) {
  for (const p of problems) log.error('not configured', { problem: p.title });
  const app = new Hono();
  app.get('/health', (c) => c.json({ ok: false, setup: problems.map((p) => p.title) }, 503));
  app.all('*', (c) =>
    c.html(
      page(
        'Social Agent: almost there',
        html`<main><h1>Social Agent is running, but not set up yet</h1>
        <p>Fix the items below on your host (Railway → this service → <b>Variables</b>). Railway redeploys by itself after you save, then this address shows the real app.</p>
        ${problems.map((p) => html`<section class="card"><h2>✗ ${p.title}</h2><p>${p.how}</p></section>`)}
        <p class="muted">Then open <code>/admin/setup</code> on this address and log in with user <b>admin</b> and your ADMIN_PASSWORD.</p></main>`,
      ),
      503,
    ),
  );
  serve({ fetch: app.fetch, port: env.PORT }, (info) => log.info('setup mode: listening', { port: info.port }));
}

export const PROBLEMS = {
  noDatabase: {
    title: 'No database connected',
    how: 'In the Railway project click "+ New" → Database → PostgreSQL. Then open this service → Variables → New Variable: name DATABASE_URL, value ${{Postgres.DATABASE_URL}} (type it exactly like that; Railway fills in the real address).',
  },
  noPassword: {
    title: 'No admin password',
    how: 'Variables → New Variable: name ADMIN_PASSWORD, value: a password you choose. You will use it to log in to the admin pages (username: admin).',
  },
  badConfig: (message: string) => ({
    title: 'A business file has a problem',
    how: `The files in social-agent/businesses/ could not be read: ${message}`,
  }),
  dbUnreachable: (message: string) => ({
    title: 'The database cannot be reached',
    how: `Check that the DATABASE_URL variable is \${{Postgres.DATABASE_URL}} and that the Postgres service is running. Error: ${message}`,
  }),
} satisfies Record<string, SetupProblem | ((m: string) => SetupProblem)>;
