import "@tanstack/react-start/server-only";
import { decryptToken, getState, listConnections, setState } from "@/agent/db/connections";
import type { Sql } from "@/agent/db/sql";
import { createMetaClient, MetaApiError } from "@/agent/meta/client";
import { INSTAGRAM_FIELDS, LOGIN_SCOPES, PAGE_FIELDS } from "@/agent/meta/subscriptions";
import { loadRuntimeEnv } from "./settings.server";

const describeMetaError = (err: unknown) =>
  err instanceof MetaApiError ? `${err.message} (code ${err.code ?? "?"}${err.subcode ? `/${err.subcode}` : ""})` : (err as Error).message;

/**
 * Asks Meta how the app is wired up: app webhooks, each business Page's subscription and
 * permissions, and the latest Instagram comments (to compare with what reached us).
 * Tokens stay on the server; the report is plain facts and findings, kept in
 * app_state('meta_diagnostics').
 */
export interface MetaDiagnostics {
  at: string;
  findings: string[];
  app: { object: string; active: boolean; callbackUrl: string; fields: string[] }[] | { error: string };
  pages: PageReport[];
  webhook: { eventsStored: number; lastEventAt: string | null; rejected: WebhookRejections | null };
}

interface PageReport {
  page: string;
  pageId: string;
  business: string | null;
  instagram: string | null;
  subscribedFields?: string[] | { error: string };
  token?: { valid: boolean; missingScopes: string[]; expiresAt: string | null } | { error: string };
  recentComments?: { when: string; username: string | null; text: string; post: string }[] | { error: string };
  recentDms?: { when: string; from: string | null; text: string }[] | { error: string };
  /** Every app installed on the Page: another DM tool here can take the messages. */
  pageApps?: { id: string; name: string | null; fields: string[] }[] | { error: string };
  /** Which app Meta hands the latest Instagram contact's DMs to (handover protocol). */
  threadOwner?: { contact: string; ownerAppId: string | null; ours: boolean } | { error: string };
}

export interface WebhookRejections {
  count: number;
  last: { at: string; reason: string; signaturePresent: boolean }[];
}

const short = (s: string | undefined | null, n: number) => (s ?? "").replace(/\s+/g, " ").slice(0, n);

export async function runMetaDiagnostics(sql: Sql): Promise<MetaDiagnostics> {
  const { env } = await loadRuntimeEnv(sql);
  const findings: string[] = [];
  const report: MetaDiagnostics = {
    at: new Date().toISOString(),
    findings,
    app: [],
    pages: [],
    webhook: { eventsStored: 0, lastEventAt: null, rejected: null },
  };
  const [stats] = await sql<{ n: number; last: Date | null }[]>`SELECT count(*)::int AS n, max(received_at) AS last FROM webhook_events`;
  report.webhook = {
    eventsStored: stats?.n ?? 0,
    lastEventAt: stats?.last ? new Date(stats.last).toISOString() : null,
    rejected: (await getState<WebhookRejections>(sql, "webhook_rejections"))?.value ?? null,
  };
  if (report.webhook.rejected?.count) {
    findings.push(
      `Meta called our webhook ${report.webhook.rejected.count} time(s) but the signature did not match. The App Secret in Settings is not the secret of the app sending the events.`,
    );
  }

  if (!env.META_APP_ID || !env.META_APP_SECRET) {
    findings.push("The Meta App ID or App Secret is missing in Settings.");
    await setState(sql, "meta_diagnostics", report);
    return report;
  }
  const version = env.META_GRAPH_VERSION;
  const appApi = createMetaClient({ accessToken: `${env.META_APP_ID}|${env.META_APP_SECRET}`, version });

  try {
    const subs = await appApi.get<{ data: { object: string; active: boolean; callback_url: string; fields: { name: string }[] }[] }>(
      `${env.META_APP_ID}/subscriptions`,
    );
    report.app = subs.data.map((s) => ({ object: s.object, active: s.active, callbackUrl: s.callback_url, fields: s.fields.map((f) => f.name) }));
    for (const [object, needed] of [
      ["instagram", INSTAGRAM_FIELDS],
      ["page", PAGE_FIELDS],
    ] as const) {
      const sub = report.app.find((s) => s.object === object);
      if (!sub) findings.push(`The app has no "${object}" webhook. On Connect, press "Register webhooks".`);
      else {
        if (!sub.active) findings.push(`The app's "${object}" webhook is switched off in Meta.`);
        const missing = needed.filter((f) => !sub.fields.includes(f));
        if (missing.length) findings.push(`The app's "${object}" webhook is missing: ${missing.join(", ")}. On Connect, press "Register webhooks".`);
        if (!sub.callbackUrl.endsWith("/api/meta/webhook")) findings.push(`The "${object}" webhook points at ${sub.callbackUrl}, not at this app.`);
      }
    }
  } catch (err) {
    report.app = { error: describeMetaError(err) };
    findings.push(`Could not read the app's webhooks: ${describeMetaError(err)}`);
  }

  const connections = (await listConnections(sql)).filter((c) => c.business);
  if (connections.length === 0) findings.push("No Page is assigned to a business, so no events would be handled.");
  for (const c of connections) {
    const page: PageReport = { page: c.page_name, pageId: c.page_id, business: c.business, instagram: c.instagram_username };
    report.pages.push(page);
    const token = decryptToken(c.token_enc, env.META_APP_SECRET);
    if (!token) {
      page.token = { error: "cannot read the stored Page token (the App Secret changed)" };
      findings.push(`${c.page_name}: the stored Page token cannot be read. Press Connect again.`);
      continue;
    }
    const pageApi = createMetaClient({ accessToken: token, version });

    try {
      const res = await pageApi.get<{ data: { id: string; name?: string; subscribed_fields?: string[] }[] }>(`${c.page_id}/subscribed_apps`);
      const ours = res.data.find((a) => a.id === env.META_APP_ID);
      page.subscribedFields = ours?.subscribed_fields ?? [];
      page.pageApps = res.data.map((a) => ({ id: a.id, name: a.name ?? null, fields: a.subscribed_fields ?? [] }));
      if (!ours) findings.push(`${c.page_name}: the Page is not subscribed to the app. On Connect, press "Subscribe again".`);
      const others = res.data.filter((a) => a.id !== env.META_APP_ID);
      if (others.length) {
        findings.push(
          `${c.page_name}: other apps are installed on this Page too: ${others.map((a) => a.name ?? a.id).join(", ")}. If one of them is a DM tool (e.g. ManyChat), it can take the Instagram messages before us.`,
        );
      }
    } catch (err) {
      page.subscribedFields = { error: describeMetaError(err) };
    }

    const [contact] = await sql<{ external_id: string; username: string | null }[]>`
      SELECT external_id, username FROM contacts WHERE business = ${c.business} AND platform = 'instagram' ORDER BY updated_at DESC LIMIT 1`;
    if (contact) {
      try {
        const res = await pageApi.get<{ data: { thread_owner?: { app_id?: string } }[] }>(`${c.page_id}/thread_owner`, {
          recipient: contact.external_id,
          platform: "instagram",
        });
        const owner = res.data[0]?.thread_owner?.app_id ?? null;
        page.threadOwner = { contact: contact.username ?? contact.external_id, ownerAppId: owner, ours: owner === env.META_APP_ID };
        if (owner && owner !== env.META_APP_ID) {
          findings.push(
            `${c.page_name}: Meta hands @${contact.username}'s DMs to another app (${owner}), so we only get them on "standby". Make this app the main receiver, or disconnect the other tool.`,
          );
        }
      } catch (err) {
        page.threadOwner = { error: describeMetaError(err) };
        if (err instanceof MetaApiError && err.subcode === 2534048) {
          findings.push(
            `${c.page_name}: Meta withholds @${contact.username}'s DMs, button taps and replies: the app has only standard access to instagram_manage_messages and this person has no role on the app. ` +
              "Give the account a Tester role to test, and get advanced access through App Review for real customers.",
          );
        }
      }
    }

    try {
      const dbg = await appApi.get<{ data: { is_valid: boolean; scopes?: string[]; expires_at?: number } }>("debug_token", { input_token: token });
      const scopes = dbg.data.scopes ?? [];
      const missingScopes = LOGIN_SCOPES.filter((s) => !scopes.includes(s));
      page.token = {
        valid: dbg.data.is_valid,
        missingScopes,
        expiresAt: dbg.data.expires_at ? new Date(dbg.data.expires_at * 1000).toISOString() : null,
      };
      if (!dbg.data.is_valid) findings.push(`${c.page_name}: the Page token is no longer valid. Press Connect again.`);
      if (missingScopes.length) findings.push(`${c.page_name}: permissions not granted: ${missingScopes.join(", ")}.`);
    } catch (err) {
      page.token = { error: describeMetaError(err) };
    }

    if (c.instagram_id) {
      try {
        const media = await pageApi.get<{ data: { id: string; caption?: string; comments_count?: number }[] }>(`${c.instagram_id}/media`, {
          fields: "id,caption,comments_count",
          limit: "5",
        });
        const comments: { when: string; username: string | null; text: string; post: string }[] = [];
        for (const m of media.data.filter((x) => (x.comments_count ?? 0) > 0).slice(0, 3)) {
          const res = await pageApi.get<{ data: { text?: string; timestamp?: string; username?: string }[] }>(`${m.id}/comments`, {
            fields: "text,timestamp,username",
            limit: "5",
          });
          for (const k of res.data) {
            comments.push({ when: k.timestamp ?? "", username: k.username ?? null, text: short(k.text, 60), post: short(m.caption, 30) });
          }
        }
        comments.sort((a, b) => b.when.localeCompare(a.when));
        page.recentComments = comments.slice(0, 8);
        const lastEvent = report.webhook.lastEventAt ? Date.parse(report.webhook.lastEventAt) : 0;
        const unseen = comments.filter((k) => Date.parse(k.when) > lastEvent && k.username !== c.instagram_username);
        if (unseen.length) {
          findings.push(
            `${c.page_name}: Instagram has ${unseen.length} comment(s) from other accounts that never reached us (latest ${unseen[0]!.when} by @${unseen[0]!.username}). ` +
              "If the webhooks above are fine, Meta is holding them back: until App Review grants Advanced Access, Meta only sends events about people who have a role on the app.",
          );
        }
      } catch (err) {
        page.recentComments = { error: describeMetaError(err) };
        findings.push(`${c.page_name}: could not read Instagram comments: ${describeMetaError(err)}`);
      }

      try {
        const conv = await pageApi.get<{
          data: { messages?: { data: { message?: string; created_time?: string; from?: { id?: string; username?: string } }[] } }[];
        }>(`${c.page_id}/conversations`, { platform: "instagram", fields: "messages.limit(2){message,created_time,from}", limit: "5" });
        const dms = conv.data
          .flatMap((t) => t.messages?.data ?? [])
          .map((m) => ({ when: m.created_time ?? "", from: m.from?.username ?? null, text: short(m.message, 60) }))
          .sort((a, b) => b.when.localeCompare(a.when));
        page.recentDms = dms.slice(0, 8);
        const [dmEvents] = await sql<{ last: Date | null }[]>`
          SELECT max(received_at) AS last FROM webhook_events WHERE object = 'instagram' AND payload::text LIKE '%"messaging"%'`;
        const lastDmEvent = dmEvents?.last ? new Date(dmEvents.last).getTime() : 0;
        const unseen = dms.filter((m) => m.from !== c.instagram_username && Date.parse(m.when) > lastDmEvent);
        if (unseen.length) {
          findings.push(
            `${c.page_name}: Instagram has ${unseen.length} DM(s) to @${c.instagram_username} that never reached us (latest ${unseen[0]!.when} from @${unseen[0]!.from}). ` +
              "Meta can read them but is not sending message webhooks.",
          );
        }
      } catch (err) {
        page.recentDms = { error: describeMetaError(err) };
        findings.push(
          `${c.page_name}: Meta refuses to show the Instagram DMs (${describeMetaError(err)}). On @${c.instagram_username}, turn on Settings → Messages and story replies → Message controls → Connected tools → Allow access to messages, then press Connect again.`,
        );
      }
    }
  }
  if (findings.length === 0) findings.push("Everything Meta reports looks right.");
  return finish(sql, report);
}

async function finish(sql: Sql, report: MetaDiagnostics): Promise<MetaDiagnostics> {
  await setState(sql, "meta_diagnostics", report);
  return report;
}

/** Lets the check be requested from the database: the scheduled tick runs it once. */
export async function runRequestedDiagnostics(sql: Sql): Promise<void> {
  const req = await getState(sql, "meta_diagnostics_request");
  if (!req) return;
  await sql`DELETE FROM app_state WHERE key = 'meta_diagnostics_request'`;
  await runMetaDiagnostics(sql);
}

/** Records a webhook call we turned away, so a wrong App Secret is visible. */
export async function recordWebhookRejection(sql: Sql, reason: string, signaturePresent: boolean): Promise<void> {
  const prev = (await getState<WebhookRejections>(sql, "webhook_rejections"))?.value ?? { count: 0, last: [] };
  await setState(sql, "webhook_rejections", {
    count: prev.count + 1,
    last: [{ at: new Date().toISOString(), reason, signaturePresent }, ...prev.last].slice(0, 10),
  });
}
