import { createHmac } from 'node:crypto';
import { z } from 'zod';

const bool = (fallback: boolean) =>
  z
    .string()
    .optional()
    .transform((v) => (v === undefined || v === '' ? fallback : ['1', 'true', 'yes', 'on'].includes(v.toLowerCase())));

const EnvSchema = z.object({
  PORT: z.coerce.number().int().default(3000),
  PUBLIC_URL: z.string().optional(), // e.g. https://agent.example.com, used for tracked links
  DATABASE_URL: z.string().optional(),
  META_APP_ID: z.string().optional(),
  META_APP_SECRET: z.string().optional(),
  META_VERIFY_TOKEN: z.string().optional(),
  META_GRAPH_VERSION: z.string().default('v26.0'),
  // Only for apps that use Facebook Login for Business configurations.
  META_LOGIN_CONFIG_ID: z.string().optional(),
  // Set automatically by the host; used when PUBLIC_URL is empty.
  RAILWAY_PUBLIC_DOMAIN: z.string().optional(),
  RENDER_EXTERNAL_URL: z.string().optional(),
  ANTHROPIC_API_KEY: z.string().optional(),
  CLAUDE_MODEL: z.string().default('claude-opus-5-5'),
  // Global kill switch. Nothing real is sent unless this is true.
  LIVE_SENDING: bool(false),
  RUN_WORKER: bool(true),
  ADMIN_PASSWORD: z.string().optional(),
  ALERT_WEBHOOK_URL: z.string().optional(),
  TELEGRAM_BOT_TOKEN: z.string().optional(),
  TELEGRAM_CHAT_ID: z.string().optional(),
  BUSINESSES_DIR: z.string().optional(),
  OPERATOR_NAME: z.string().optional(), // shown on /privacy
  OPERATOR_EMAIL: z.string().optional(),
});

export type Env = z.infer<typeof EnvSchema>;

export function loadEnv(source: NodeJS.ProcessEnv = process.env): Env {
  return EnvSchema.parse(source);
}

export function requireEnv<K extends keyof Env>(env: Env, key: K): NonNullable<Env[K]> {
  const value = env[key];
  if (value === undefined || value === null || value === '') {
    throw new Error(`Missing required environment variable ${String(key)}. See .env.example.`);
  }
  return value as NonNullable<Env[K]>;
}

/** META_VERIFY_TOKEN if set, otherwise a stable token derived from the app secret. */
export function verifyToken(env: Env): string | undefined {
  if (env.META_VERIFY_TOKEN) return env.META_VERIFY_TOKEN;
  if (!env.META_APP_SECRET) return undefined;
  return createHmac('sha256', env.META_APP_SECRET).update('social-agent:verify-token').digest('hex').slice(0, 32);
}

/** The public https base URL of this server, from config or the host's own variables. */
export function configuredPublicUrl(env: Env): string | undefined {
  const url =
    env.PUBLIC_URL ||
    (env.RAILWAY_PUBLIC_DOMAIN ? `https://${env.RAILWAY_PUBLIC_DOMAIN}` : undefined) ||
    env.RENDER_EXTERNAL_URL;
  return url?.replace(/\/$/, '');
}
