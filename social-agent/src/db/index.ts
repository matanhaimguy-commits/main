import { readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';
import postgres from 'postgres';
import { PROJECT_ROOT } from '../config/load.js';

export type Sql = postgres.Sql;

export function connect(url: string, opts: { max?: number } = {}): Sql {
  return postgres(url, {
    max: opts.max ?? 10,
    onnotice: () => {},
    // bigserial ids as JS numbers (they stay far below 2^53).
    types: {
      bigint: {
        to: 20,
        from: [20],
        serialize: (x: number) => String(x),
        parse: (x: string) => Number(x),
      },
    },
  });
}

const MIGRATIONS_DIR = path.join(PROJECT_ROOT, 'migrations');

/** Applies migrations/*.sql in name order, each once, each in its own transaction. */
export async function migrate(sql: Sql, log: (msg: string) => void = () => {}): Promise<string[]> {
  await sql`CREATE TABLE IF NOT EXISTS schema_migrations (
    version text PRIMARY KEY,
    applied_at timestamptz NOT NULL DEFAULT now()
  )`;
  const done = new Set((await sql<{ version: string }[]>`SELECT version FROM schema_migrations`).map((r) => r.version));
  const applied: string[] = [];
  for (const file of readdirSync(MIGRATIONS_DIR).filter((f) => f.endsWith('.sql')).sort()) {
    if (done.has(file)) continue;
    const body = readFileSync(path.join(MIGRATIONS_DIR, file), 'utf8');
    await sql.begin(async (tx) => {
      await tx.unsafe(body);
      await tx`INSERT INTO schema_migrations (version) VALUES (${file})`;
    });
    log(`applied ${file}`);
    applied.push(file);
  }
  return applied;
}
