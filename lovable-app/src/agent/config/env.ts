import { createHmac } from 'node:crypto';
import { z } from 'zod/v4';

const bool = (fallback: boolean) =>
  z
    .union([z.boolean(), z.string()])
    .optional()
    .transform((v) =>
      typeof v === 'boolean' ? v : v === undefined || v === '' ? fallback : ['1', 'true', 'yes', 'on'].includes(v.toLowerCase()),
    );

const text = z
  .string()
  .optional()
  .transform((v) => (v === undefined || v.trim() === '' ? undefined : v.trim()));

/**
 * Runtime settings. On Lovable they come from two places, merged by `src/server/runtime.server.ts`:
 * the dashboard's Settings (stored in the database, secrets encrypted) and, overriding those,
 * secrets added under Lovable Cloud → Secrets.
 */
const EnvSchema = z.object({
  PUBLIC_URL: text, // e.g. https://social-agent.lovable.app, used for webhooks, OAuth and tracked links
  META_APP_ID: text,
  META_APP_SECRET: text,
  META_VERIFY_TOKEN: text,
  META_GRAPH_VERSION: z.string().default('v26.0'),
  // Only for apps that use Facebook Login for Business configurations.
  META_LOGIN_CONFIG_ID: text,
  ANTHROPIC_API_KEY: text,
  CLAUDE_MODEL: z.string().default('claude-opus-5-5'),
  // Global kill switch. Nothing real is sent unless this is true.
  LIVE_SENDING: bool(false),
  ALERT_WEBHOOK_URL: text,
  TELEGRAM_BOT_TOKEN: text,
  TELEGRAM_CHAT_ID: text,
  OPERATOR_NAME: text, // shown on /privacy
  OPERATOR_EMAIL: text,
});

export type Env = z.infer<typeof EnvSchema>;

export function loadEnv(source: Record<string, unknown>): Env {
  const picked: Record<string, unknown> = {};
  for (const key of Object.keys(EnvSchema.shape)) if (source[key] !== undefined && source[key] !== null) picked[key] = source[key];
  return EnvSchema.parse(picked);
}

export const ENV_KEYS = Object.keys(EnvSchema.shape) as (keyof Env)[];

export function requireEnv<K extends keyof Env>(env: Env, key: K): NonNullable<Env[K]> {
  const value = env[key];
  if (value === undefined || value === null || value === '') {
    throw new Error(`Missing setting ${String(key)}. Add it in the dashboard under Settings.`);
  }
  return value as NonNullable<Env[K]>;
}

/** META_VERIFY_TOKEN if set, otherwise a stable token derived from the app secret. */
export function verifyToken(env: Env): string | undefined {
  if (env.META_VERIFY_TOKEN) return env.META_VERIFY_TOKEN;
  if (!env.META_APP_SECRET) return undefined;
  return createHmac('sha256', env.META_APP_SECRET).update('social-agent:verify-token').digest('hex').slice(0, 32);
}

/** The public https base URL of this app. */
export function configuredPublicUrl(env: Env): string | undefined {
  return env.PUBLIC_URL?.replace(/\/$/, '');
}
