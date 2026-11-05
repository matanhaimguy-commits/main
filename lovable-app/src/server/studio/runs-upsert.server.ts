import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import { runColumns } from "./columns";
import { StudioError } from "./errors";
import { listFiles, replaceFiles } from "./files.server";
import type { RunInput } from "./schema";
import { currentStepOf, runStatusOf } from "./steps";
import type { StudioFileRow, StudioRunRow } from "./types";
import { runInputProblems } from "./validate";

/**
 * Creates the run, or updates the one with the same business and post_id. A re-push without a title, format or
 * family keeps the old one; `files`, when given, becomes the run's whole file list.
 */
export async function upsertRun(sql: Sql, input: RunInput): Promise<{ run: StudioRunRow; files: StudioFileRow[] }> {
  const problems = runInputProblems(input);
  if (problems.length) throw new StudioError(problems.join(" "));
  const [biz] = await sql<{ slug: string }[]>`SELECT slug FROM businesses WHERE slug = ${input.business}`;
  if (!biz) throw new StudioError(`No business "${input.business}" in the app. Use the business slug from Businesses.`, 404);
  const steps = [...input.steps].sort((a, b) => a.n - b.n);
  const status = input.status ?? runStatusOf(steps);
  const current = input.current_step !== undefined ? input.current_step : currentStepOf(steps);
  const [run] = await sql<StudioRunRow[]>`
    INSERT INTO studio_runs (business, post_id, title, format, family, current_step, status, waiting_on_owner, summary, steps, ledger)
    VALUES (${input.business}, ${input.post_id}, ${input.title ?? null}, ${input.format ?? null}, ${input.family ?? null},
            ${current}, ${status}, ${input.waiting_on_owner}, ${input.summary ?? null}, ${sql.json(steps)}, ${sql.json(input.ledger)})
    ON CONFLICT (business, post_id) DO UPDATE SET
      title = coalesce(EXCLUDED.title, studio_runs.title), format = coalesce(EXCLUDED.format, studio_runs.format),
      family = coalesce(EXCLUDED.family, studio_runs.family), current_step = EXCLUDED.current_step, status = EXCLUDED.status,
      waiting_on_owner = EXCLUDED.waiting_on_owner, summary = EXCLUDED.summary, steps = EXCLUDED.steps,
      ledger = EXCLUDED.ledger, pushed_at = now(), updated_at = now()
    RETURNING ${runColumns(sql)}`;
  if (input.files) await replaceFiles(sql, run!.id, input.files);
  return { run: run!, files: await listFiles(sql, run!.id) };
}
