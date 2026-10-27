import "@tanstack/react-start/server-only";
import { z } from "zod/v4";
import type { Sql } from "@/agent/db/sql";
import { json, readJson } from "./api-common.server";
import { markSynced } from "./decisions-synced.server";
import { SyncedInput } from "./schema";

/** POST /api/studio/synced {"ids": [..]}: the studio took these answers in. 409 when one can't be marked. */
export async function postSynced(request: Request, sql: Sql): Promise<Response> {
  const input = SyncedInput.safeParse(await readJson(request));
  if (!input.success) return json({ error: 'Send {"ids": [decision ids]}.', details: z.prettifyError(input.error) }, 400);
  const res = await markSynced(sql, input.data.ids);
  return json(res, res.problems.length ? 409 : 200);
}
