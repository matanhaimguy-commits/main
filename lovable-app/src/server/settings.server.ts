import "@tanstack/react-start/server-only";
import { randomBytes } from "node:crypto";
import { ENV_KEYS, loadEnv, type Env } from "@/agent/config/env";
import { decryptToken, encryptToken, getState, setState } from "@/agent/db/connections";
import type { Sql } from "@/agent/db/sql";
import { runtimeVars, serverKey } from "./db.server";

/**
 * Settings entered in the dashboard. Stored in app_state('settings'); the three secrets are
 * encrypted with a key derived from the server's service-role key. A Lovable Cloud secret
 * with the same name (META_APP_SECRET, ...) overrides the stored value.
 */
export const SETTING_FIELDS = {
  META_APP_ID: { secret: false, label: "Meta App ID" },
  META_APP_SECRET: { secret: true, label: "Meta App Secret" },
  META_LOGIN_CONFIG_ID: { secret: false, label: "Facebook Login configuration ID (optional)" },
  ANTHROPIC_API_KEY: { secret: true, label: "Claude API key" },
  CLAUDE_MODEL: { secret: false, label: "Claude model" },
  TELEGRAM_BOT_TOKEN: { secret: true, label: "Telegram bot token (optional)" },
  TELEGRAM_CHAT_ID: { secret: false, label: "Telegram chat ID (optional)" },
  ALERT_WEBHOOK_URL: { secret: false, label: "Alert webhook URL (optional)" },
  OPERATOR_NAME: { secret: false, label: "Your business name (privacy page)" },
  OPERATOR_EMAIL: { secret: false, label: "Contact email (privacy page)" },
  PUBLIC_URL: { secret: false, label: "Public address" },
} as const;

export type SettingKey = keyof typeof SETTING_FIELDS;
export const SETTING_KEYS = Object.keys(SETTING_FIELDS) as SettingKey[];

interface Stored {
  values: Partial<Record<SettingKey, string>>;
  live_sending?: boolean;
}

const encKey = () => `settings:${serverKey()}`;

async function readStored(sql: Sql): Promise<Stored> {
  const row = await getState<Stored>(sql, "settings");
  return { values: {}, ...(row?.value ?? {}) };
}

let cache: { at: number; env: Env; sources: Record<string, "secret" | "dashboard"> } | undefined;
const CACHE_MS = 10_000;

export function clearSettingsCache() {
  cache = undefined;
}

/** The runtime Env: dashboard settings, overridden by Lovable Cloud secrets. */
export async function loadRuntimeEnv(sql: Sql): Promise<{ env: Env; sources: Record<string, "secret" | "dashboard"> }> {
  if (cache && Date.now() - cache.at < CACHE_MS) return cache;
  const stored = await readStored(sql);
  const merged: Record<string, unknown> = {};
  const sources: Record<string, "secret" | "dashboard"> = {};
  for (const key of SETTING_KEYS) {
    const raw = stored.values[key];
    if (!raw) continue;
    const value = SETTING_FIELDS[key].secret ? decryptToken(raw, encKey()) : raw;
    if (value) {
      merged[key] = value;
      sources[key] = "dashboard";
    }
  }
  if (stored.live_sending !== undefined) merged["LIVE_SENDING"] = stored.live_sending;
  const vars = runtimeVars();
  for (const key of ENV_KEYS) {
    const v = vars[key];
    if (v) {
      merged[key] = v;
      sources[key] = "secret";
    }
  }
  const env = loadEnv(merged);
  cache = { at: Date.now(), env, sources };
  return cache;
}

export interface SettingsView {
  fields: { key: SettingKey; label: string; secret: boolean; set: boolean; value?: string; source?: "secret" | "dashboard" }[];
  liveSending: boolean;
  liveSendingSource: "secret" | "dashboard";
}

/** What the Settings page shows. Secret values never leave the server, only whether they are set. */
export async function settingsView(sql: Sql): Promise<SettingsView> {
  const { env, sources } = await loadRuntimeEnv(sql);
  return {
    fields: SETTING_KEYS.map((key) => {
      const def = SETTING_FIELDS[key];
      const value = env[key as keyof Env] as string | undefined;
      return {
        key,
        label: def.label,
        secret: def.secret,
        set: !!value,
        ...(def.secret ? {} : value !== undefined ? { value: String(value) } : {}),
        ...(sources[key] ? { source: sources[key] } : {}),
      };
    }),
    liveSending: env.LIVE_SENDING,
    liveSendingSource: sources["LIVE_SENDING"] === "secret" ? "secret" : "dashboard",
  };
}

/** Saves the given fields. An empty string clears a field; undefined leaves it as is. */
export async function saveSettings(
  sql: Sql,
  patch: { values?: Partial<Record<SettingKey, string>>; liveSending?: boolean },
): Promise<void> {
  const stored = await readStored(sql);
  for (const [key, value] of Object.entries(patch.values ?? {}) as [SettingKey, string | undefined][]) {
    if (!(key in SETTING_FIELDS) || value === undefined) continue;
    const trimmed = value.trim();
    if (!trimmed) delete stored.values[key];
    else stored.values[key] = SETTING_FIELDS[key].secret ? encryptToken(trimmed, encKey()) : trimmed;
  }
  if (patch.liveSending !== undefined) stored.live_sending = patch.liveSending;
  await setState(sql, "settings", stored);
  clearSettingsCache();
}

// ---- the published address and the scheduled tick ----------------------------------------

const isPreviewHost = (host: string) =>
  /^(id-preview--|preview--)/.test(host) || host === "localhost" || host.startsWith("127.") || host.endsWith(".lovableproject.com");

/**
 * Remembers this app's public address the first time it is used from the published site,
 * and points the database's once-a-minute job at /api/tick with a fresh secret.
 */
export async function rememberPublicOrigin(sql: Sql, origin: string): Promise<void> {
  let host: string;
  try {
    const u = new URL(origin);
    if (u.protocol !== "https:") return;
    host = u.hostname;
  } catch {
    return;
  }
  if (isPreviewHost(host)) return;
  const { env } = await loadRuntimeEnv(sql);
  const base = env.PUBLIC_URL?.replace(/\/$/, "") || origin;
  if (!env.PUBLIC_URL) await saveSettings(sql, { values: { PUBLIC_URL: origin } });
  const tick = (await getState<{ url: string; secret: string }>(sql, "tick_target"))?.value;
  const url = `${base}/api/tick`;
  if (tick?.url === url && tick.secret) return;
  await setState(sql, "tick_target", { url, secret: tick?.secret || randomBytes(24).toString("hex") });
}

export async function tickSecret(sql: Sql): Promise<string | undefined> {
  return (await getState<{ secret: string }>(sql, "tick_target"))?.value?.secret;
}
