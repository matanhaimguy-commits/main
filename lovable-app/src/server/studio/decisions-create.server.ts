import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import { StudioError } from "./errors";
import type { DecisionInput, DecisionStatus, StudioStep } from "./schema";
import type { StudioDecisionRow } from "./types";
import { decisionInputProblems } from "./validate";

/** Puts a checkpoint question to the owner, or updates it while it is still open. */
export async function createDecision(sql: Sql, input: DecisionInput): Promise<{ decision: StudioDecisionRow; updated: boolean }> {
  const problems = decisionInputProblems(input);
  if (problems.length) throw new StudioError(problems.join(" "));
  const [run] = await sql<{ id: number; steps: StudioStep[] }[]>`
    SELECT id, steps FROM studio_runs WHERE business = ${input.business} AND post_id = ${input.post_id}`;
  if (!run) throw new StudioError(`No run ${input.business}/${input.post_id} in the hub yet. Push it first (hub.py studio-push).`, 404);
  if (input.step != null && !(run.steps ?? []).some((s) => s.n === input.step)) {
    throw new StudioError(`Step ${input.step} is not one of this run's steps.`);
  }
  const key = input.key ?? input.checkpoint;
  const answered = () =>
    new StudioError(`"${key}" was already answered for ${input.post_id}. To ask again, give the new question its own "key" (for example "${key}:2").`, 409);
  const [existing] = await sql<{ id: number; status: DecisionStatus }[]>`
    SELECT id, status FROM studio_decisions WHERE run_id = ${run.id} AND key = ${key}`;
  if (existing && existing.status !== "open") throw answered();
  const [row] = await sql<StudioDecisionRow[]>`
    INSERT INTO studio_decisions (run_id, key, checkpoint, step, question, context, options, multi)
    VALUES (${run.id}, ${key}, ${input.checkpoint}, ${input.step ?? null}, ${input.question}, ${input.context ?? null},
            ${sql.json(input.options)}, ${input.multi})
    ON CONFLICT (run_id, key) DO UPDATE SET
      checkpoint = EXCLUDED.checkpoint, step = EXCLUDED.step, question = EXCLUDED.question, context = EXCLUDED.context,
      options = EXCLUDED.options, multi = EXCLUDED.multi, updated_at = now()
      WHERE studio_decisions.status = 'open'
    RETURNING *`;
  // Answered between the check and the write: the guard on the update kept it.
  if (!row) throw answered();
  return { decision: row, updated: !!existing };
}
