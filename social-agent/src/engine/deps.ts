import type { SalesAi } from '../ai/agent.js';
import type { Alerter } from '../alerts.js';
import type { Env } from '../config/env.js';
import type { Registry } from '../config/load.js';
import type { Business } from '../config/schema.js';
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
  /** Graph client for a business, or undefined when its Page token is missing. */
  metaFor(business: Business): MetaApi | undefined;
  /** Whether real messages may be sent for this business (else: dry run, logged only). */
  isLive(business: Business): boolean;
  now(): Date;
  sleep(ms: number): Promise<void>;
}

export interface LiveStatus {
  live: boolean;
  reason: string;
  issues: Issue[];
}

/** LIVE_SENDING env, business `live: true`, a token, and a clean audit are all required. */
export function liveStatus(b: Business, env: Env, processEnv: NodeJS.ProcessEnv = process.env): LiveStatus {
  const issues = auditBusiness(b, processEnv);
  if (!env.LIVE_SENDING) return { live: false, reason: 'LIVE_SENDING is not true', issues };
  if (!b.enabled) return { live: false, reason: 'business disabled', issues };
  if (!b.live) return { live: false, reason: 'business live: false', issues };
  if (blocksLive(issues)) return { live: false, reason: 'audit has errors', issues };
  return { live: true, reason: 'live', issues };
}

export function metaClientFactory(env: Env, processEnv: NodeJS.ProcessEnv = process.env) {
  const cache = new Map<string, MetaApi>();
  return (b: Business): MetaApi | undefined => {
    const token = processEnv[b.meta.page_token_env];
    if (!token) return undefined;
    const key = `${b.slug}:${token.slice(-8)}`;
    let client = cache.get(key);
    if (!client) {
      client = createMetaClient({ accessToken: token, version: env.META_GRAPH_VERSION });
      cache.set(key, client);
    }
    return client;
  };
}
