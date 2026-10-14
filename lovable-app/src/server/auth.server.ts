import "@tanstack/react-start/server-only";
import { createHmac, randomBytes, timingSafeEqual } from "node:crypto";
import { deleteCookie, getCookie, setCookie } from "@tanstack/react-start/server";
import { getState, setState } from "@/agent/db/connections";
import type { Sql } from "@/agent/db/sql";
import { runtimeVars, serverKey } from "./db.server";

/**
 * One admin password protects the dashboard. It is created on first visit (stored as a
 * PBKDF2 hash) unless an ADMIN_PASSWORD secret is set in Lovable Cloud, which then wins.
 * The session is an HMAC-signed cookie; changing the password signs everyone out.
 */
const COOKIE = "sa_session";
const SESSION_DAYS = 30;
const ITERATIONS = 100_000;
const MIN_LENGTH = 8;

interface StoredPassword {
  salt: string;
  hash: string;
  iterations: number;
}

export class UnauthenticatedError extends Error {
  constructor() {
    super("UNAUTHENTICATED");
    this.name = "UnauthenticatedError";
  }
}

async function pbkdf2(password: string, salt: string, iterations: number): Promise<string> {
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(password), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits(
    { name: "PBKDF2", hash: "SHA-256", salt: new TextEncoder().encode(salt), iterations },
    key,
    256,
  );
  return Buffer.from(bits).toString("base64url");
}

const envPassword = () => runtimeVars()["ADMIN_PASSWORD"];

async function storedPassword(sql: Sql): Promise<StoredPassword | undefined> {
  return (await getState<StoredPassword>(sql, "admin_password"))?.value;
}

export async function passwordState(sql: Sql): Promise<{ exists: boolean; fromSecret: boolean }> {
  if (envPassword()) return { exists: true, fromSecret: true };
  return { exists: !!(await storedPassword(sql)), fromSecret: false };
}

function equal(a: string, b: string): boolean {
  const x = Buffer.from(a);
  const y = Buffer.from(b);
  return x.length === y.length && timingSafeEqual(x, y);
}

async function passwordMatches(sql: Sql, password: string): Promise<boolean> {
  const fromEnv = envPassword();
  if (fromEnv) return equal(createHmac("sha256", "pw").update(password).digest("hex"), createHmac("sha256", "pw").update(fromEnv).digest("hex"));
  const stored = await storedPassword(sql);
  if (!stored) return false;
  return equal(await pbkdf2(password, stored.salt, stored.iterations), stored.hash);
}

/** Part of the signing key, so a new password invalidates old sessions. */
async function passwordEpoch(sql: Sql): Promise<string> {
  const fromEnv = envPassword();
  if (fromEnv) return createHmac("sha256", "epoch").update(fromEnv).digest("hex").slice(0, 16);
  return (await storedPassword(sql))?.hash.slice(0, 16) ?? "none";
}

async function sign(sql: Sql, payload: string): Promise<string> {
  return createHmac("sha256", `session:${serverKey()}:${await passwordEpoch(sql)}`).update(payload).digest("base64url");
}

async function issueSession(sql: Sql, secure: boolean) {
  const payload = Buffer.from(JSON.stringify({ exp: Date.now() + SESSION_DAYS * 86_400_000 })).toString("base64url");
  setCookie(COOKIE, `${payload}.${await sign(sql, payload)}`, {
    httpOnly: true,
    secure,
    sameSite: "lax",
    path: "/",
    maxAge: SESSION_DAYS * 86_400,
  });
}

export async function isLoggedIn(sql: Sql): Promise<boolean> {
  const raw = getCookie(COOKIE);
  if (!raw) return false;
  const [payload, sig] = raw.split(".");
  if (!payload || !sig) return false;
  if (!equal(sig, await sign(sql, payload))) return false;
  try {
    const { exp } = JSON.parse(Buffer.from(payload, "base64url").toString("utf8")) as { exp: number };
    return typeof exp === "number" && exp > Date.now();
  } catch {
    return false;
  }
}

export async function requireAdmin(sql: Sql): Promise<void> {
  if (!(await isLoggedIn(sql))) throw new UnauthenticatedError();
}

// A simple brake on guessing: 10 failed logins in 15 minutes locks logins for 15 minutes.
async function tooManyFailures(sql: Sql): Promise<boolean> {
  const s = (await getState<{ count: number; since: number }>(sql, "login_failures"))?.value;
  return !!s && s.count >= 10 && Date.now() - s.since < 15 * 60_000;
}

async function recordFailure(sql: Sql) {
  const s = (await getState<{ count: number; since: number }>(sql, "login_failures"))?.value;
  const fresh = !s || Date.now() - s.since > 15 * 60_000;
  await setState(sql, "login_failures", fresh ? { count: 1, since: Date.now() } : { count: s.count + 1, since: s.since });
}

export async function login(sql: Sql, password: string, secure: boolean): Promise<{ ok: boolean; error?: string }> {
  if (await tooManyFailures(sql)) return { ok: false, error: "Too many wrong passwords. Try again in 15 minutes." };
  if (!(await passwordMatches(sql, password))) {
    await recordFailure(sql);
    return { ok: false, error: "Wrong password." };
  }
  await setState(sql, "login_failures", { count: 0, since: Date.now() });
  await issueSession(sql, secure);
  return { ok: true };
}

export async function logout() {
  deleteCookie(COOKIE, { path: "/" });
}

async function storePassword(sql: Sql, password: string) {
  const salt = randomBytes(16).toString("base64url");
  await setState(sql, "admin_password", { salt, hash: await pbkdf2(password, salt, ITERATIONS), iterations: ITERATIONS });
}

/** First visit only: there is no password yet. */
export async function createFirstPassword(sql: Sql, password: string, secure: boolean): Promise<{ ok: boolean; error?: string }> {
  const state = await passwordState(sql);
  if (state.exists) return { ok: false, error: "A password already exists. Log in instead." };
  if (password.length < MIN_LENGTH) return { ok: false, error: `Use at least ${MIN_LENGTH} characters.` };
  await storePassword(sql, password);
  await issueSession(sql, secure);
  return { ok: true };
}

export async function changePassword(
  sql: Sql,
  current: string,
  next: string,
  secure: boolean,
): Promise<{ ok: boolean; error?: string }> {
  if (envPassword()) return { ok: false, error: "The password is set by the ADMIN_PASSWORD secret in Lovable Cloud. Change it there." };
  if (!(await passwordMatches(sql, current))) return { ok: false, error: "The current password is wrong." };
  if (next.length < MIN_LENGTH) return { ok: false, error: `Use at least ${MIN_LENGTH} characters.` };
  await storePassword(sql, next);
  await issueSession(sql, secure);
  return { ok: true };
}

// ---- short-lived signed values (OAuth state) ------------------------------------------------

export function signValue(value: string, purpose: string): string {
  return `${value}.${createHmac("sha256", `${purpose}:${serverKey()}`).update(value).digest("base64url")}`;
}

export function readSigned(signed: string | undefined, purpose: string): string | undefined {
  if (!signed) return undefined;
  const i = signed.lastIndexOf(".");
  if (i <= 0) return undefined;
  const value = signed.slice(0, i);
  return equal(signed, signValue(value, purpose)) ? value : undefined;
}
