import { AsyncLocalStorage } from "node:async_hooks";

/**
 * Per-request handle on the host's `waitUntil`, so work can continue after the response
 * is sent (Cloudflare Workers keeps the request alive for it). src/server.ts sets it.
 */
export interface RequestContext {
  waitUntil?: (promise: Promise<unknown>) => void;
}

const storage = new AsyncLocalStorage<RequestContext>();

export function runWithRequestContext<T>(ctx: RequestContext, fn: () => T): T {
  return storage.run(ctx, fn);
}

type HostRequest = Request & {
  waitUntil?: (promise: Promise<unknown>) => void;
  runtime?: { cloudflare?: { context?: { waitUntil?: (promise: Promise<unknown>) => void } } };
};

/** Finds `waitUntil` on the request (nitro's Cloudflare handler puts it there) or the worker context. */
export function pickWaitUntil(request: Request, ctx?: unknown): RequestContext["waitUntil"] {
  const r = request as HostRequest;
  if (typeof r.waitUntil === "function") return r.waitUntil.bind(r);
  const cf = r.runtime?.cloudflare?.context;
  if (cf && typeof cf.waitUntil === "function") return cf.waitUntil.bind(cf);
  const c = ctx as { waitUntil?: (promise: Promise<unknown>) => void } | undefined;
  if (c && typeof c.waitUntil === "function") return c.waitUntil.bind(c);
  return undefined;
}

export function currentWaitUntil(request?: Request): RequestContext["waitUntil"] {
  return (request ? pickWaitUntil(request) : undefined) ?? storage.getStore()?.waitUntil;
}
