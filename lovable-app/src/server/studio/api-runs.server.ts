import "@tanstack/react-start/server-only";
import { z } from "zod/v4";
import type { Sql } from "@/agent/db/sql";
import { json, queryParam, readJson } from "./api-common.server";
import { listDecisions } from "./decisions-list.server";
import { listFiles } from "./files.server";
import { findRun, listRuns } from "./runs-read.server";
import { upsertRun } from "./runs-upsert.server";
import { RunInput } from "./schema";

/**
 * GET  /api/studio/runs                         every run (no steps, no ledgers)
 * GET  /api/studio/runs?business=B&post_id=P    one run with its files (no markdown) and questions
 */
export async function getRuns(request: Request, sql: Sql): Promise<Response> {
  const business = queryParam(request, "business");
  const postId = queryParam(request, "post_id");
  if (!postId) {
    const runs = await listRuns(sql, { business });
    return json({ runs: runs.map(({ steps: _steps, ...r }) => r) });
  }
  if (!business) return json({ error: "Add ?business=<slug> with post_id." }, 400);
  const run = await findRun(sql, business, postId);
  if (!run) return json({ error: `No run ${business}/${postId}.` }, 404);
  const [files, decisions] = await Promise.all([listFiles(sql, run.id), listDecisions(sql, { runId: run.id })]);
  return json({ run, files, decisions });
}

/** POST /api/studio/runs: create or update a run with its steps (and, when given, its whole file list). */
export async function postRun(request: Request, sql: Sql): Promise<Response> {
  const input = RunInput.safeParse(await readJson(request));
  if (!input.success) return json({ error: "Invalid run.", details: z.prettifyError(input.error) }, 400);
  return json(await upsertRun(sql, input.data));
}
