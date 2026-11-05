import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import type { FileInput } from "./schema";
import type { StudioFileRow } from "./types";

/** A run's files: docs (inline markdown or a link), audio, images and video (links to the "content" bucket). */

/** Makes `files` the run's file list: same keys update, new ones are added, missing ones removed. */
export async function replaceFiles(sql: Sql, runId: number, files: FileInput[]): Promise<void> {
  for (const [i, f] of files.entries()) {
    await sql`
      INSERT INTO studio_files (run_id, key, step, label, kind, url, markdown, sha256, position)
      VALUES (${runId}, ${f.key}, ${f.step ?? null}, ${f.label}, ${f.kind}, ${f.url ?? null}, ${f.markdown ?? null},
              ${f.sha256 ?? null}, ${i})
      ON CONFLICT (run_id, key) DO UPDATE SET
        step = EXCLUDED.step, label = EXCLUDED.label, kind = EXCLUDED.kind, url = EXCLUDED.url, markdown = EXCLUDED.markdown,
        sha256 = EXCLUDED.sha256, position = EXCLUDED.position, updated_at = now()`;
  }
  // An empty IN list would match nothing, so "no files" is its own statement.
  if (files.length) await sql`DELETE FROM studio_files WHERE run_id = ${runId} AND key NOT IN ${sql(files.map((f) => f.key))}`;
  else await sql`DELETE FROM studio_files WHERE run_id = ${runId}`;
}

/** A run's files in page order, without their markdown. */
export async function listFiles(sql: Sql, runId: number): Promise<StudioFileRow[]> {
  const rows = await sql<StudioFileRow[]>`
    SELECT id, run_id, key, step, label, kind, url, sha256, position, markdown IS NOT NULL AS has_markdown,
           coalesce(length(markdown), 0) AS markdown_chars, updated_at
    FROM studio_files WHERE run_id = ${runId}
    ORDER BY step NULLS FIRST, position, id`;
  return [...rows];
}

/** One doc's markdown, loaded when someone opens it. */
export async function fileMarkdown(sql: Sql, id: number): Promise<{ id: number; label: string; markdown: string } | null> {
  const [row] = await sql<{ id: number; label: string; markdown: string | null }[]>`
    SELECT id, label, markdown FROM studio_files WHERE id = ${id}`;
  return row ? { id: row.id, label: row.label, markdown: row.markdown ?? "" } : null;
}
