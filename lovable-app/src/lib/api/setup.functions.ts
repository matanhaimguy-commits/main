import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { verifyToken } from "@/agent/config/env";
import { assignConnection, decryptToken, deleteConnection, getState, listConnections, markSubscribed, setState } from "@/agent/db/connections";
import type { Sql } from "@/agent/db/sql";
import { subscribeApp, subscribePage } from "@/agent/meta/subscriptions";
import { createMetaClient } from "@/agent/meta/client";
import { asAdmin, asMember, currentOrigin } from "@/server/admin.server";
import { CALLBACK_PATH, describeMetaError, WEBHOOK_PATH } from "@/server/handlers.server";
import { createRuntimeDeps } from "@/server/runtime.server";
import {
  loadRuntimeEnv,
  rememberPublicOrigin,
  saveSettings,
  SETTING_KEYS,
  settingsView,
  type SettingKey,
} from "@/server/settings.server";
import { passwordState, reviewerState } from "@/server/auth.server";

const isPreview = (origin: string) => /\/\/(id-preview--|preview--)|localhost|127\.0\.0\.1|lovableproject\.com/.test(origin);

async function addresses(sql: Sql) {
  const origin = currentOrigin();
  await rememberPublicOrigin(sql, origin).catch(() => {});
  const { env } = await loadRuntimeEnv(sql);
  const base = env.PUBLIC_URL?.replace(/\/$/, "") || origin;
  return {
    env,
    base,
    preview: isPreview(origin),
    urls: {
      webhook: `${base}${WEBHOOK_PATH}`,
      callback: `${base}${CALLBACK_PATH}`,
      privacy: `${base}/privacy`,
      dataDeletion: `${base}/data-deletion`,
    },
    verifyToken: verifyToken(env) ?? null,
  };
}

export const getOverview = createServerFn({ method: "GET" }).handler(async () =>
  asMember(async (sql, role) => {
    const a = await addresses(sql);
    const { deps, loaded } = await createRuntimeDeps(sql);
    const [connections, verified, lastEvent, lastTick, tickTarget, appWebhooks] = await Promise.all([
      listConnections(sql),
      getState(sql, "webhook_verified_at"),
      getState(sql, "last_event_at"),
      getState<{ at: string; handled: number }>(sql, "last_tick_at"),
      getState<{ url: string }>(sql, "tick_target"),
      getState<{ results: { object: string; ok: boolean; error?: string }[] }>(sql, "app_webhooks"),
    ]);
    const businesses = deps.registry.businesses.map((b) => {
      const st = deps.liveStatus(b);
      const conn = connections.find((c) => c.page_id === b.meta.page_id);
      return {
        slug: b.slug,
        name: b.name,
        live: st.live,
        reason: st.reason,
        issues: st.issues,
        pageId: b.meta.page_id ?? null,
        pageName: conn?.page_name ?? null,
        instagramId: b.meta.instagram_id ?? null,
        instagramUsername: conn?.instagram_username ?? null,
        subscribedAt: conn?.subscribed_at ?? null,
        testers: b.testers,
        funnels: b.funnels.length,
        enabled: b.enabled,
        businessLive: b.live,
      };
    });
    return {
      base: a.base,
      preview: a.preview,
      urls: a.urls,
      verifyToken: role === "admin" ? a.verifyToken : null,
      metaApp: { id: a.env.META_APP_ID ?? null, hasSecret: !!a.env.META_APP_SECRET },
      webhookVerifiedAt: verified?.updated_at ?? null,
      appWebhooks: appWebhooks?.value?.results ?? null,
      connections: connections.map((c) => ({
        pageId: c.page_id,
        pageName: c.page_name,
        instagramId: c.instagram_id,
        instagramUsername: c.instagram_username,
        business: c.business,
        subscribedAt: c.subscribed_at,
      })),
      lastEventAt: lastEvent?.updated_at ?? null,
      ai: !!a.env.ANTHROPIC_API_KEY,
      liveSending: a.env.LIVE_SENDING,
      alerts: !!(a.env.TELEGRAM_BOT_TOKEN || a.env.ALERT_WEBHOOK_URL),
      tick: { target: tickTarget?.value?.url ?? null, lastAt: lastTick?.updated_at ?? null },
      businesses,
      invalidBusinesses: loaded.invalid,
    };
  }),
);

// ---- settings -------------------------------------------------------------------------------------

export const getSettings = createServerFn({ method: "GET" }).handler(async () =>
  asAdmin(async (sql) => ({ ...(await settingsView(sql)), password: await passwordState(sql), reviewer: await reviewerState(sql) })),
);

export const saveSettingsFn = createServerFn({ method: "POST" })
  .validator(
    z.object({
      values: z.record(z.string(), z.string().max(2000)).optional(),
      liveSending: z.boolean().optional(),
    }),
  )
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const values: Partial<Record<SettingKey, string>> = {};
      for (const [k, v] of Object.entries(data.values ?? {})) if ((SETTING_KEYS as string[]).includes(k)) values[k as SettingKey] = v;
      await saveSettings(sql, { values, ...(data.liveSending !== undefined ? { liveSending: data.liveSending } : {}) });
      return { ok: true };
    }),
  );

// ---- connected Pages --------------------------------------------------------------------------------

async function subscribeConnected(sql: Sql, pageId: string): Promise<string | undefined> {
  const { env } = await loadRuntimeEnv(sql);
  const page = (await listConnections(sql)).find((p) => p.page_id === pageId);
  const token = page && env.META_APP_SECRET ? decryptToken(page.token_enc, env.META_APP_SECRET) : undefined;
  if (!token) return "No usable token for this Page. Connect it again.";
  try {
    await subscribePage(createMetaClient({ accessToken: token, version: env.META_GRAPH_VERSION }), pageId);
    await markSubscribed(sql, pageId);
    return undefined;
  } catch (err) {
    return describeMetaError(err);
  }
}

export const assignPageFn = createServerFn({ method: "POST" })
  .validator(z.object({ pageId: z.string().min(1), business: z.string().nullable() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      if (data.business) {
        const [row] = await sql<{ slug: string }[]>`SELECT slug FROM businesses WHERE slug = ${data.business}`;
        if (!row) return { ok: false, message: "Unknown business." };
      }
      await assignConnection(sql, data.pageId, data.business);
      const problem = data.business ? await subscribeConnected(sql, data.pageId) : undefined;
      if (problem) return { ok: false, message: `Saved, but subscribing the Page to webhooks failed: ${problem}` };
      return { ok: true, message: data.business ? `Saved. ${data.business} now answers for this Page, and the Page is subscribed.` : "Saved." };
    }),
  );

export const subscribePageFn = createServerFn({ method: "POST" })
  .validator(z.object({ pageId: z.string().min(1) }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const problem = await subscribeConnected(sql, data.pageId);
      return problem ? { ok: false, message: `Subscribing failed: ${problem}` } : { ok: true, message: "Subscribed." };
    }),
  );

export const removePageFn = createServerFn({ method: "POST" })
  .validator(z.object({ pageId: z.string().min(1) }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      await deleteConnection(sql, data.pageId);
      return { ok: true, message: "Removed." };
    }),
  );

/** Registers the app-level webhooks for Page and Instagram objects (App Dashboard → Webhooks). */
export const registerWebhooksFn = createServerFn({ method: "POST" }).handler(async () =>
  asAdmin(async (sql) => {
    const a = await addresses(sql);
    const { env } = a;
    if (!env.META_APP_ID || !env.META_APP_SECRET || !a.verifyToken) return { ok: false, message: "Add the Meta App ID and App Secret in Settings first." };
    if (a.preview) return { ok: false, message: "Open the dashboard from the published address (not the Lovable preview) and try again." };
    const app = createMetaClient({ accessToken: `${env.META_APP_ID}|${env.META_APP_SECRET}`, version: env.META_GRAPH_VERSION });
    const results = await subscribeApp(app, env.META_APP_ID, a.urls.webhook, a.verifyToken);
    await setState(sql, "app_webhooks", { results, at: new Date() });
    const failed = results.filter((r) => !r.ok);
    if (failed.length === 0) return { ok: true, message: "Webhooks registered for Facebook Pages and Instagram." };
    return {
      ok: false,
      message: `${failed.map((f) => `${f.object}: ${f.error}`).join(" · ")}. You can also enter the callback URL and verify token by hand in App Dashboard → Webhooks.`,
    };
  }),
);
