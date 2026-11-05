import "@tanstack/react-start/server-only";
import { z } from "zod/v4";
import type { Sql } from "@/agent/db/sql";
import { json, queryParam, readJson } from "./api-common.server";
import { createDecision } from "./decisions-create.server";
import { listDecisions } from "./decisions-list.server";
import { DECISION_STATUSES, DecisionInput } from "./schema";

/** GET /api/studio/decisions?status=answered[&business=B]: answered (by default) questions, for the studio to take in. */
export async function getDecisions(request: Request, sql: Sql): Promise<Response> {
  const status = z.enum(DECISION_STATUSES).safeParse(queryParam(request, "status") ?? "answered");
  if (!status.success) return json({ error: `status is one of ${DECISION_STATUSES.join(", ")}.` }, 400);
  return json({ decisions: await listDecisions(sql, { status: status.data, business: queryParam(request, "business"), limit: 500 }) });
}

const Many = z.object({ decisions: z.array(DecisionInput).min(1).max(20) });

/** POST /api/studio/decisions: one question, or {"decisions": [...]}. */
export async function postDecisions(request: Request, sql: Sql): Promise<Response> {
  const body = await readJson(request);
  const many = Many.safeParse(body);
  if (many.success) {
    const saved = [];
    for (const d of many.data.decisions) saved.push(await createDecision(sql, d));
    return json({ decisions: saved.map((s) => ({ ...s.decision, updated: s.updated })) });
  }
  const one = DecisionInput.safeParse(body);
  if (!one.success) return json({ error: "Invalid decision.", details: z.prettifyError(one.error) }, 400);
  const saved = await createDecision(sql, one.data);
  return json({ decision: saved.decision, updated: saved.updated });
}
