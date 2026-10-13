import type { SalesAi } from '../ai/agent.js';
import type { Alerter } from '../alerts.js';
import type { Env } from '../config/env.js';
import { ConfigError, type Registry } from '../config/load.js';
import type { Business } from '../config/schema.js';
import { decryptToken, listConnections } from '../db/connections.js';
import type { Sql } from '../db/index.js';
import type { Logger } from '../log.js';
import { auditBusiness, blocksLive, type Issue } from '../logic/audit.js';
import { createMetaClient, type MetaApi } from '../meta/client.js';

/** Everything the engine needs, injected so tests can swap Meta and Claude for fakes. */
export interface Deps {
  sql: Sql;
  env: Env;
  registry: Registry;
  log: Logger;
  alert: Alerter;
  /** undefined when ANTHROPIC_API_KEY is not set: AI features stay off. */
  ai: SalesAi | undefined;
  /** Graph client for a business, or undefined when it has no Page token. */
  metaFor(business: Business): MetaApi | undefined;
  /** Graph client for any token (used by the connect flow). An empty token sends none. */
  graph(token: string): MetaApi;
  /** Whether real messages may be sent for this business (else: dry run, logged only). */
  isLive(business: Business): boolean;
  liveStatus(business: Business): LiveStatus;
  /** Reloads connected Pages from the database (after /admin/connect changes). */
  reloadConnections(): Promise<void>;
  now(): Date;
  sleep(ms: number): Promise<void>;
}

export interface LiveStatus {
  live: boolean;
  reason: string;
  issues: Issue[];
}

/** LIVE_SENDING env, business `live: true`, a connected Page with a token, and a clean audit are all required. */
export function liveStatus(b: Business, env: Env, hasToken: boolean): LiveStatus {
  const issues = auditBusiness(b, { hasToken });
  if (!env.LIVE_SENDING) return { live: false, reason: 'LIVE_SENDING is not true', issues };
  if (!b.enabled) return { live: false, reason: 'business disabled', issues };
  if (!b.live) return { live: false, reason: 'business live: false', issues };
  if (blocksLive(issues)) return { live: false, reason: 'audit has errors', issues };
  return { live: true, reason: 'live', issues };
}

export interface DepsOptions {
  sql: Sql;
  env: Env;
  registry: Registry;
  log: Logger;
  alert: Alerter;
  ai: SalesAi | undefined;
  graph?: (token: string) => MetaApi;
  processEnv?: NodeJS.ProcessEnv;
  now?: () => Date;
  sleep?: (ms: number) => Promise<void>;
}

export async function createDeps(o: DepsOptions): Promise<Deps> {
  const processEnv = o.processEnv ?? process.env;
  const graph = o.graph ?? ((token: string) => createMetaClient({ accessToken: token, version: o.env.META_GRAPH_VERSION }));
  let pageTokens = new Map<string, string>();
  let status = new Map<string, LiveStatus>();
  const clients = new Map<string, MetaApi>();

  const tokenFor = (b: Business): string | undefined =>
    (b.meta.page_token_env ? processEnv[b.meta.page_token_env] : undefined) ||
    (b.meta.page_id ? pageTokens.get(b.meta.page_id) : undefined);

  const recompute = () => {
    status = new Map(o.registry.businesses.map((b) => [b.slug, liveStatus(b, o.env, !!tokenFor(b))]));
  };

  const reloadConnections = async () => {
    const connections = await listConnections(o.sql);
    const next = new Map<string, string>();
    for (const c of connections) {
      const token = o.env.META_APP_SECRET ? decryptToken(c.token_enc, o.env.META_APP_SECRET) : undefined;
      if (token) next.set(c.page_id, token);
      else o.log.warn('cannot read the stored token for a connected Page (app secret changed?); connect it again', { page: c.page_id });
    }
    pageTokens = next;
    try {
      o.registry.refresh(connections);
    } catch (err) {
      if (!(err instanceof ConfigError)) throw err;
      o.log.error('connected Pages conflict with business files; keeping the previous mapping', { problems: err.problems });
    }
    clients.clear();
    recompute();
  };
  await reloadConnections();

  return {
    sql: o.sql,
    env: o.env,
    registry: o.registry,
    log: o.log,
    alert: o.alert,
    ai: o.ai,
    graph,
    metaFor(b) {
      const token = tokenFor(b);
      if (!token) return undefined;
      let client = clients.get(token);
      if (!client) {
        client = graph(token);
        clients.set(token, client);
      }
      return client;
    },
    isLive: (b) => status.get(b.slug)?.live ?? false,
    liveStatus: (b) => status.get(b.slug) ?? liveStatus(b, o.env, !!tokenFor(b)),
    reloadConnections,
    now: o.now ?? (() => new Date()),
    sleep: o.sleep ?? ((ms) => new Promise((r) => setTimeout(r, ms))),
  };
}
