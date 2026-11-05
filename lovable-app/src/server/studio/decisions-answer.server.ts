import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import { StudioError } from "./errors";
import type { AnswerInput } from "./schema";
import type { DecisionAnswer, StudioDecisionRow } from "./types";
import { answerProblem } from "./validate";

/** The owner's answer. It can still change until the studio has taken it in (synced). */
export async function answerDecision(sql: Sql, id: number, a: AnswerInput, by: string): Promise<StudioDecisionRow> {
  const [d] = await sql<StudioDecisionRow[]>`SELECT * FROM studio_decisions WHERE id = ${id}`;
  if (!d) throw new StudioError("This question no longer exists.", 404);
  const problem = answerProblem(d, a);
  if (problem) throw new StudioError(problem, d.status === "synced" ? 409 : 400);
  const answer: DecisionAnswer = { choices: a.choices, note: a.note.trim(), by, at: new Date().toISOString() };
  const [row] = await sql<StudioDecisionRow[]>`
    UPDATE studio_decisions SET status = 'answered', answer = ${sql.json(answer)}, answered_at = now(), updated_at = now()
    WHERE id = ${id} AND status IN ('open', 'answered')
    RETURNING *`;
  if (!row) throw new StudioError("The studio has already taken this answer in.", 409);
  return row;
}
