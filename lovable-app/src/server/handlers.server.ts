import "@tanstack/react-start/server-only";
import { randomBytes, timingSafeEqual } from "node:crypto";
import { getCookie, setCookie, deleteCookie } from "@tanstack/react-start/server";
import { verifyToken, type Env } from "@/agent/config/env";
import { encryptToken, setState, upsertConnection } from "@/agent/db/connections";
import { insertWebhookEvent, recordClick } from "@/agent/db/repo";
import { createMetaClient, MetaApiError } from "@/agent/meta/client";
import { LOGIN_SCOPES } from "@/agent/meta/subscriptions";
import { drain, scheduledRun, tick } from "@/agent/engine/tick";
import { verifyHandshake, verifySignature } from "@/agent/meta/webhook";
import { log } from "@/agent/log";
import { isLoggedIn, readSigned, signValue } from "./auth.server";
import { getDb, NoDatabaseError } from "./db.server";
import { recordWebhookRejection, runRequestedDiagnostics } from "./diagnostics.server";
import { createRuntimeDeps, runAfterResponse } from "./runtime.server";
import { loadRuntimeEnv, rememberPublicOrigin, tickSecret } from "./settings.server";

/**
 * The HTTP endpoints Meta, the database scheduler and the browser call directly. Route
 * files in src/routes/api only forward to these, so they stay testable without a server.
 */

const text = (body: string, status = 200) => new Response(body, { status, headers: { "content-type": "text/plain; charset=utf-8" } });
const json = (body: unknown, status = 200) => new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json" } });
const goTo = (location: string) => new Response(null, { status: 302, headers: { location } });

/** https://host the browser or Meta used to reach us. */
export function requestOrigin(request: Request): string {
  const u = new URL(request.url);
  const proto = request.headers.get("x-forwarded-proto")?.split(",")[0]?.trim() || u.protocol.replace(":", "");
  const host = request.headers.get("x-forwarded-host")?.split(",")[0]?.trim() || request.headers.get("host") || u.host;
  return `${proto}://${host}`;
}

export function publicBase(env: Env, request: Request): string {
  return env.PUBLIC_URL?.replace(/\/$/, "") || requestOrigin(request);
}

export const WEBHOOK_PATH = "/api/meta/webhook";
export const CALLBACK_PATH = "/api/connect/callback";

// ---- Meta webhook ---------------------------------------------------------------------------

/** Meta calls this once when the callback URL is registered. */
export async function webhookGet(request: Request): Promise<Response> {
  const sql = getDb();
  const { env } = await loadRuntimeEnv(sql);
  const token = verifyToken(env);
  if (!token) return text("The Meta App Secret is not set yet (dashboard → Settings).", 503);
  const query = Object.fromEntries(new URL(request.url).searchParams);
  const challenge = verifyHandshake(query, token);
  if (challenge === undefined) {
    log.warn("webhook verification rejected");
    return text("Forbidden", 403);
  }
  await setState(sql, "webhook_verified_at", new Date()).catch(() => {});
  await rememberPublicOrigin(sql, requestOrigin(request)).catch(() => {});
  return text(challenge);
}

/**
 * Verify, store, answer. Processing runs after the response (Workers `waitUntil`), so Meta
 * gets its 200 in milliseconds and never re-sends a batch because our code was slow.
 */
export async function webhookPost(request: Request): Promise<Response> {
  const sql = getDb();
  const { env } = await loadRuntimeEnv(sql);
  if (!env.META_APP_SECRET) return text("The Meta App Secret is not set yet.", 503);
  const raw = new Uint8Array(await request.arrayBuffer());
  const signature = request.headers.get("x-hub-signature-256") ?? undefined;
  if (!verifySignature(raw, signature, env.META_APP_SECRET)) {
    log.warn("webhook signature rejected");
    await recordWebhookRejection(sql, "signature did not match the App Secret", !!signature).catch(() => {});
    return text("Invalid signature", 401);
  }
  let body: { object?: string };
  try {
    body = JSON.parse(new TextDecoder().decode(raw));
  } catch {
    return text("Invalid JSON", 400);
  }
  try {
    await insertWebhookEvent(sql, body.object, body);
  } catch (err) {
    // Not stored = would be lost. A 500 makes Meta redeliver; the send ledger makes that safe.
    log.error("could not store webhook event", { err });
    return text("Storage error", 500);
  }
  await runAfterResponse(request, "webhook processing", async (inBackground) => {
    await setState(sql, "last_event_at", { object: body.object }).catch(() => {});
    const { deps } = await createRuntimeDeps(sql);
    if (inBackground) {
      // Workers keep a request alive ~30 s after the response; stay well inside that.
      await drain(deps, { waitUpToSeconds: 15, deadline: Date.now() + 25_000 });
    } else {
      // Meta is still waiting for the answer: handle the new event only. Debounced AI
      // replies go out on the next scheduled tick (within a minute).
      await tick(deps, { replies: 0 });
    }
  });
  return text("EVENT_RECEIVED");
}

// ---- scheduled tick (pg_cron → pg_net → here, every minute) ---------------------------------

function sameSecret(given: string | null, expected: string | undefined): boolean {
  if (!given || !expected) return false;
  const a = Buffer.from(given);
  const b = Buffer.from(expected);
  return a.length === b.length && timingSafeEqual(a, b);
}

export async function tickPost(request: Request): Promise<Response> {
  const sql = getDb();
  if (!sameSecret(request.headers.get("x-agent-tick"), await tickSecret(sql))) return text("Forbidden", 403);
  await runAfterResponse(request, "scheduled tick", async (inBackground) => {
    const { deps } = await createRuntimeDeps(sql);
    // The database scheduler gives up on the call after 30 s.
    await scheduledRun(deps, Date.now() + (inBackground ? 25_000 : 20_000));
    await runRequestedDiagnostics(sql).catch((err) => log.error("meta diagnostics failed", { err }));
  });
  return json({ ok: true }, 202);
}

// ---- tracked links ------------------------------------------------------------------------------

export async function linkRedirect(token: string): Promise<Response> {
  const url = await recordClick(getDb(), token);
  return url ? goTo(url) : text("Link not found", 404);
}

// ---- Connect Facebook & Instagram (OAuth) -------------------------------------------------------

const STATE_COOKIE = "sa_connect_state";
const back = (key: "msg" | "err", message: string) => goTo(`/connect?${key}=${encodeURIComponent(message)}`);

export const describeMetaError = (err: unknown) =>
  err instanceof MetaApiError ? `${err.message} (code ${err.code ?? "?"}${err.subcode ? `/${err.subcode}` : ""})` : (err as Error).message;

export async function connectStart(request: Request): Promise<Response> {
  const sql = getDb();
  if (!(await isLoggedIn(sql))) return goTo("/login");
  const { env } = await loadRuntimeEnv(sql);
  if (!env.META_APP_ID || !env.META_APP_SECRET) return back("err", "Add the Meta App ID and App Secret in Settings first.");
  const base = publicBase(env, request);
  const state = randomBytes(16).toString("hex");
  setCookie(STATE_COOKIE, signValue(state, "connect"), {
    httpOnly: true,
    secure: base.startsWith("https://"),
    sameSite: "lax",
    path: "/api/connect",
    maxAge: 900,
  });
  const url = new URL(`https://www.facebook.com/${env.META_GRAPH_VERSION}/dialog/oauth`);
  url.searchParams.set("client_id", env.META_APP_ID);
  url.searchParams.set("redirect_uri", `${base}${CALLBACK_PATH}`);
  url.searchParams.set("state", state);
  url.searchParams.set("response_type", "code");
  if (env.META_LOGIN_CONFIG_ID) url.searchParams.set("config_id", env.META_LOGIN_CONFIG_ID);
  else url.searchParams.set("scope", LOGIN_SCOPES.join(","));
  return goTo(url.toString());
}

export async function connectCallback(request: Request): Promise<Response> {
  const sql = getDb();
  if (!(await isLoggedIn(sql))) return goTo("/login");
  const q = Object.fromEntries(new URL(request.url).searchParams);
  if (q["error"]) return back("err", `Facebook login was cancelled or failed: ${q["error_description"] ?? q["error"]}`);
  const expected = readSigned(getCookie(STATE_COOKIE), "connect");
  deleteCookie(STATE_COOKIE, { path: "/api/connect" });
  if (!q["state"] || !expected || q["state"] !== expected) return back("err", "The login expired or came from somewhere else. Press Connect again.");
  const { env } = await loadRuntimeEnv(sql);
  if (!q["code"] || !env.META_APP_ID || !env.META_APP_SECRET) return back("err", "Missing login code.");

  const graph = (token: string) => createMetaClient({ accessToken: token, version: env.META_GRAPH_VERSION });
  try {
    const anon = graph("");
    const short = await anon.get<{ access_token: string }>("oauth/access_token", {
      client_id: env.META_APP_ID,
      client_secret: env.META_APP_SECRET,
      redirect_uri: `${publicBase(env, request)}${CALLBACK_PATH}`,
      code: q["code"],
    });
    // Page tokens made from a long-lived user token do not expire.
    const long = await anon.get<{ access_token: string }>("oauth/access_token", {
      grant_type: "fb_exchange_token",
      client_id: env.META_APP_ID,
      client_secret: env.META_APP_SECRET,
      fb_exchange_token: short.access_token,
    });
    const pages = await graph(long.access_token).get<{
      data: { id: string; name: string; access_token?: string; instagram_business_account?: { id: string; username?: string } }[];
    }>("me/accounts", { fields: "id,name,access_token,instagram_business_account{id,username}", limit: "100" });

    const usable = pages.data.filter((p) => p.access_token);
    for (const p of usable) {
      await upsertConnection(sql, {
        pageId: p.id,
        pageName: p.name,
        ...(p.instagram_business_account?.id ? { instagramId: p.instagram_business_account.id } : {}),
        ...(p.instagram_business_account?.username ? { instagramUsername: p.instagram_business_account.username } : {}),
        tokenEnc: encryptToken(p.access_token!, env.META_APP_SECRET),
      });
    }
    await setState(sql, "last_connect", { pages: usable.map((p) => p.name), at: new Date() });
    if (usable.length === 0) {
      return back("err", "Logged in, but Meta shared no Pages. Press Connect again and tick your Page (and its Instagram account) in the Meta dialog.");
    }
    return back("msg", `Connected ${usable.length} Page(s): ${usable.map((p) => p.name).join(", ")}. Now choose the business for each one below.`);
  } catch (err) {
    log.error("connect failed", { err });
    return back("err", `Meta refused the connection: ${describeMetaError(err)}`);
  }
}

/** Route-level guard: a missing database or an unexpected error becomes a plain-text answer. */
export async function guarded(name: string, fn: () => Promise<Response>): Promise<Response> {
  try {
    return await fn();
  } catch (err) {
    log.error(`${name} failed`, { err });
    if (err instanceof NoDatabaseError) return text(err.message, 503);
    return text("Server error", 500);
  }
}
