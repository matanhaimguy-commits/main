import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import postgres from "postgres";
import type { Sql } from "@/agent/db/sql";
import { dbAvailable, freshDb, TEST_DB, truncate } from "@/agent/test/harness";

/** The Studio's database tests: the local test Postgres (TEST_DATABASE_URL) loaded with the studio migration. */

export const hasDb = await dbAvailable();

const MIGRATION = fileURLToPath(new URL("../../../supabase/migrations/20261027090000_studio.sql", import.meta.url));

export interface StudioDb {
  sql: Sql;
  pg: postgres.Sql;
}

/** A fresh schema with the studio migration applied twice (it must be safe to re-run). */
export async function studioDb(): Promise<StudioDb> {
  const sql = await freshDb();
  const pg = postgres(TEST_DB, { max: 2, onnotice: () => {} });
  const text = readFileSync(MIGRATION, "utf8");
  await pg.unsafe(text);
  await pg.unsafe(text);
  return { sql, pg };
}

/** Empty tables and one business, "acme" (named "Acme Studio"). */
export async function resetStudio({ sql, pg }: StudioDb): Promise<void> {
  await pg`TRUNCATE studio_decisions, studio_files, studio_runs RESTART IDENTITY CASCADE`;
  await truncate(sql);
  await pg`INSERT INTO businesses (slug, config) VALUES ('acme', ${pg.json({ name: "Acme Studio" })})`;
}

export async function closeStudioDb(db: StudioDb | undefined): Promise<void> {
  await db?.sql.end({ timeout: 2 });
  await db?.pg.end({ timeout: 2 });
}
