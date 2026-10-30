import "@tanstack/react-start/server-only";
import type { Sql } from "@/agent/db/sql";
import { checkStudioToken } from "../content.server";
import { getDb } from "../db.server";
import { StudioError } from "./errors";

/**
 * What every /api/studio/* endpoint shares: the studio token (the same one /api/content/* takes, sent as
 * `Authorization: Bearer <token>`), JSON answers, and StudioErrors turned into their status.
 */

export const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8" } });

export type StudioHandler = (request: Request, sql: Sql) => Promise<Response>;

/** Runs `handler` for a request that carries the studio token. `db` is for tests. */
export async function withStudioToken(request: Request, handler: StudioHandler, db?: Sql): Promise<Response> {
  const sql = db ?? getDb();
  if (!(await checkStudioToken(sql, request))) return json({ error: "Missing or wrong studio token." }, 401);
  try {
    return await handler(request, sql);
  } catch (err) {
    if (err instanceof StudioError) return json({ error: err.message }, err.status);
    throw err;
  }
}

/** The request's JSON body, or null when there is none or it isn't JSON. */
export const readJson = (request: Request): Promise<unknown> => request.json().catch(() => null);

export const queryParam = (request: Request, name: string) => new URL(request.url).searchParams.get(name) || undefined;
