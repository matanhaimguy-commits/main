import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import {
  changePassword,
  createFirstPassword,
  createReviewerPassword,
  login,
  logout,
  passwordState,
  removeReviewerPassword,
  sessionRole,
  type Role,
} from "@/server/auth.server";
import { asAdmin, isSecureRequest } from "@/server/admin.server";
import { checkDb, getDb } from "@/server/db.server";

export interface SessionInfo {
  loggedIn: boolean;
  /** "reviewer" is the limited login made for Meta's App Review. */
  role: Role | null;
  hasPassword: boolean;
  passwordFromSecret: boolean;
  db: { ok: boolean; problem?: string };
}

export const getSession = createServerFn({ method: "GET" }).handler(async (): Promise<SessionInfo> => {
  const db = await checkDb();
  if (!db.ok) return { loggedIn: false, role: null, hasPassword: false, passwordFromSecret: false, db };
  const sql = getDb();
  const state = await passwordState(sql);
  const role = await sessionRole(sql);
  return { loggedIn: role !== null, role, hasPassword: state.exists, passwordFromSecret: state.fromSecret, db };
});

const Password = z.object({ password: z.string().min(1).max(200) });

export const loginFn = createServerFn({ method: "POST" })
  .validator(Password)
  .handler(async ({ data }) => login(getDb(), data.password, isSecureRequest()));

export const createPasswordFn = createServerFn({ method: "POST" })
  .validator(Password)
  .handler(async ({ data }) => createFirstPassword(getDb(), data.password, isSecureRequest()));

export const logoutFn = createServerFn({ method: "POST" }).handler(async () => {
  await logout();
  return { ok: true };
});

export const changePasswordFn = createServerFn({ method: "POST" })
  .validator(z.object({ current: z.string().max(200), next: z.string().max(200) }))
  .handler(async ({ data }) => asAdmin((sql) => changePassword(sql, data.current, data.next, isSecureRequest())));

/** Creates (or replaces) the reviewer password and returns it once. */
export const createReviewerPasswordFn = createServerFn({ method: "POST" }).handler(async () =>
  asAdmin(async (sql) => ({ password: await createReviewerPassword(sql) })),
);

export const removeReviewerPasswordFn = createServerFn({ method: "POST" }).handler(async () =>
  asAdmin(async (sql) => {
    await removeReviewerPassword(sql);
    return { ok: true };
  }),
);
