import "@tanstack/react-start/server-only";
import { getRequest } from "@tanstack/react-start/server";
import type { Sql } from "@/agent/db/sql";
import { requireAdmin } from "./auth.server";
import { getDb } from "./db.server";
import { requestOrigin } from "./handlers.server";

/** Runs a dashboard action for the logged-in admin, or throws UNAUTHENTICATED. */
export async function asAdmin<T>(fn: (sql: Sql) => Promise<T>): Promise<T> {
  const sql = getDb();
  await requireAdmin(sql);
  return fn(sql);
}

export function currentOrigin(): string {
  return requestOrigin(getRequest());
}

export function isSecureRequest(): boolean {
  return currentOrigin().startsWith("https://");
}
