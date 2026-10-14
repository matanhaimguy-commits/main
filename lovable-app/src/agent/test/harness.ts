import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import postgres from 'postgres';
import type { CommentDecision, ReplyInput, ReplyResult, SalesAi } from '../ai/agent';
import { loadEnv } from '../config/env';
import { buildRegistry } from '../config/load';
import type { Business } from '../config/schema';
import { createSql, type Sql } from '../db/sql';
import { createDeps, type Deps } from '../engine/deps';
import { silentLog } from '../log';
import { MetaApiError, MetaNetworkError, type MetaApi } from '../meta/client';
import { APP_SECRET, IG_ID, PAGE_ID, VERIFY_TOKEN } from './fixtures';

export const TEST_DB = process.env.TEST_DATABASE_URL ?? 'postgres://agent:agent@localhost:5432/social_agent_test';
export const APP_ID = '999000999';
const MIGRATION = fileURLToPath(new URL('../../../supabase/migrations/20261014090000_social_agent.sql', import.meta.url));

let pg: postgres.Sql | undefined;
const admin = () => (pg ??= postgres(TEST_DB, { max: 4, onnotice: () => {} }));

export async function dbAvailable(): Promise<boolean> {
  try {
    await admin()`SELECT 1`;
    return true;
  } catch {
    return false;
  }
}

/**
 * A fresh schema from the Lovable migration (minus the pg_cron part, which a plain
 * Postgres lacks). Queries go through the same `agent_sql` function and literal
 * encoding the hosted app uses, so these tests cover the shim end to end.
 */
export async function freshDb(): Promise<Sql> {
  const db = admin();
  await db.unsafe('DROP SCHEMA public CASCADE; CREATE SCHEMA public;');
  const text = readFileSync(MIGRATION, 'utf8');
  await db.unsafe(text.slice(0, text.indexOf('-- ---- background work')));
  return createSql(async (q, wantRows) => {
    const [row] = await db`SELECT public.agent_sql(${q}, ${wantRows}) AS r`;
    const r = row!['r'];
    return wantRows ? { rows: r, count: r.length } : { rows: [], count: Number(r.count) };
  });
}

export async function truncate(_sql: Sql) {
  await admin().unsafe(`TRUNCATE webhook_events, contacts, comments, sends, messages, links, taps, ai_runs, alerts, business_state, meta_connections, app_state, businesses
    RESTART IDENTITY CASCADE`);
}

export interface Call {
  method: string;
  args: any[];
}

export class FakeMeta implements MetaApi {
  calls: Call[] = [];
  tokens: string[] = [];
  /** Queue of errors to throw on the next sendMessage calls. */
  failNext: Error[] = [];
  follows = new Map<string, boolean>();
  profiles = new Map<string, Record<string, unknown>>();
  private n = 0;

  async sendMessage(input: Parameters<MetaApi['sendMessage']>[0]) {
    this.calls.push({ method: 'sendMessage', args: [input] });
    const err = this.failNext.shift();
    if (err) throw err;
    this.n++;
    const recipient = 'comment_id' in input.recipient ? `PSID_FOR_${input.recipient.comment_id}` : input.recipient.id;
    return { recipient_id: recipient, message_id: `mid.${this.n}` };
  }
  async replyToComment(platform: string, commentId: string, text: string) {
    this.calls.push({ method: 'replyToComment', args: [platform, commentId, text] });
    return { id: `reply_${commentId}` };
  }
  async hideComment(platform: string, commentId: string, hide: boolean) {
    this.calls.push({ method: 'hideComment', args: [platform, commentId, hide] });
    return { success: true };
  }
  async getUserProfile(userId: string, fields: string[]) {
    this.calls.push({ method: 'getUserProfile', args: [userId, fields] });
    return { ...(this.profiles.get(userId) ?? {}), is_user_follow_business: this.follows.get(userId) ?? false };
  }
  /** Pages returned by me/accounts during the connect flow. */
  pages: { id: string; name: string; access_token?: string; instagram_business_account?: { id: string; username?: string } }[] = [];
  async get(path: string, params?: Record<string, string>) {
    this.calls.push({ method: 'get', args: [path, params] });
    if (path === 'oauth/access_token') return { access_token: params?.code ? 'SHORT_USER_TOKEN' : 'LONG_USER_TOKEN' } as any;
    if (path === 'me/accounts') return { data: this.pages } as any;
    return { data: [{ id: APP_ID }] } as any;
  }
  async post(path: string, body?: Record<string, unknown>) {
    this.calls.push({ method: 'post', args: [path, body] });
    return { success: true } as any;
  }
  sends() {
    return this.calls.filter((c) => c.method === 'sendMessage').map((c) => c.args[0]);
  }
}

export const apiError = (code: number, subcode?: number, message = 'error') => new MetaApiError(message, 400, code, subcode);
export const networkError = () => new MetaNetworkError('socket hang up');

export class FakeAi implements SalesAi {
  replies: ReplyInput[] = [];
  nextReply: Partial<ReplyResult> = { text: 'Happy to help! What are you looking for?' };
  nextDecision: CommentDecision = {
    intent: 'pricing',
    public_reply: 'Sent you a DM 🙌',
    send_dm: true,
    dm_text: 'Our ads management starts at 4,000 ILS a month. What do you sell?',
    hide: false,
    alert_owner: false,
    reason: 'asked about price',
  };
  async reply(input: ReplyInput): Promise<ReplyResult> {
    this.replies.push(input);
    return {
      text: null,
      lead: {},
      optOut: false,
      usage: { model: 'fake', inputTokens: 10, outputTokens: 5, cacheReadTokens: 0, stopReason: 'end_turn' },
      ...this.nextReply,
    };
  }
  async triageComment() {
    return { decision: this.nextDecision, usage: { model: 'fake', inputTokens: 1, outputTokens: 1, cacheReadTokens: 0, stopReason: 'end_turn' } };
  }
}

export interface Harness {
  deps: Deps;
  meta: FakeMeta;
  ai: FakeAi;
  alerts: string[];
  live: Set<string>;
}

export async function makeHarness(sql: Sql, businesses: Business[], extraEnv: Record<string, string> = {}): Promise<Harness> {
  const meta = new FakeMeta();
  const ai = new FakeAi();
  const alerts: string[] = [];
  const live = new Set(businesses.map((b) => b.slug));
  const env = loadEnv({
    META_APP_ID: APP_ID,
    META_APP_SECRET: APP_SECRET,
    META_VERIFY_TOKEN: VERIFY_TOKEN,
    LIVE_SENDING: 'true',
    ...extraEnv,
  });
  const base = await createDeps({
    sql,
    env,
    registry: buildRegistry(businesses),
    log: silentLog,
    alert: async (a) => {
      alerts.push(a.text);
    },
    ai,
    graph: (token) => {
      meta.tokens.push(token);
      return meta;
    },
    secrets: { PAGE_TOKEN_ACME: 'env-page-token' },
    sleep: async () => {},
  });
  // Tests flip a business to dry run by removing it from `live`.
  const deps: Deps = { ...base, isLive: (b) => live.has(b.slug) && base.isLive(b) };
  return { deps, meta, ai, alerts, live };
}

// ---- webhook payload builders --------------------------------------------------

const nowSec = () => Math.floor(Date.now() / 1000);

export function fbComment(o: { id: string; post?: string; parent?: string; from?: string; text: string; verb?: string }) {
  const post = o.post ?? `${PAGE_ID}_POST_A`;
  return {
    object: 'page',
    entry: [
      {
        id: PAGE_ID,
        time: nowSec(),
        changes: [
          {
            field: 'feed',
            value: {
              item: 'comment',
              verb: o.verb ?? 'add',
              comment_id: o.id,
              post_id: post,
              parent_id: o.parent ?? post,
              from: { id: o.from ?? 'FB_USER_1', name: 'Dana Levi' },
              message: o.text,
              created_time: nowSec(),
            },
          },
        ],
      },
    ],
  };
}

export function igComment(o: { id: string; media?: string; from?: string; username?: string; text: string; parent?: string }) {
  return {
    object: 'instagram',
    entry: [
      {
        id: IG_ID,
        time: nowSec(),
        changes: [
          {
            field: 'comments',
            value: {
              id: o.id,
              text: o.text,
              from: { id: o.from ?? 'IG_USER_1', username: o.username ?? 'dana' },
              media: { id: o.media ?? 'MEDIA_A', media_product_type: 'REELS' },
              ...(o.parent ? { parent_id: o.parent } : {}),
            },
          },
        ],
      },
    ],
  };
}

export function igMessaging(items: Record<string, unknown>[]) {
  return { object: 'instagram', entry: [{ id: IG_ID, time: Date.now(), messaging: items }] };
}

export const igText = (from: string, mid: string, text: string, extra: Record<string, unknown> = {}) => ({
  sender: { id: from },
  recipient: { id: IG_ID },
  timestamp: Date.now(),
  message: { mid, text, ...extra },
});

export const igPostback = (from: string, mid: string, payload: string, title = 'Send it to me') => ({
  sender: { id: from },
  recipient: { id: IG_ID },
  timestamp: Date.now(),
  postback: { mid, payload, title },
});

export const igEcho = (to: string, mid: string, text: string, appId?: string) => ({
  sender: { id: IG_ID },
  recipient: { id: to },
  timestamp: Date.now(),
  message: { mid, text, is_echo: true, ...(appId ? { app_id: appId } : {}) },
});
