import "@tanstack/react-start/server-only";
import { getRequest } from "@tanstack/react-start/server";
import type { Sql } from "@/agent/db/sql";
import { requireAdmin, requireMember, type Role } from "./auth.server";
import { getDb } from "./db.server";
import { requestOrigin } from "./handlers.server";

/** Runs a dashboard action for the logged-in admin, or throws UNAUTHENTICATED. */
export async function asAdmin<T>(fn: (sql: Sql) => Promise<T>): Promise<T> {
  const sql = getDb();
  await requireAdmin(sql);
  return fn(sql);
}

/** Runs a dashboard action for the owner or a reviewer (looking and testing, no changes). */
export async function asMember<T>(fn: (sql: Sql, role: Role) => Promise<T>): Promise<T> {
  const sql = getDb();
  const role = await requireMember(sql);
  return fn(sql, role);
}

export function currentOrigin(): string {
  return requestOrigin(getRequest());
}

export function isSecureRequest(): boolean {
  return currentOrigin().startsWith("https://");
}
