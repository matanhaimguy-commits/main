import "./lib/error-capture";

import { consumeLastCapturedError } from "./lib/error-capture";
import { renderErrorPage } from "./lib/error-page";
import { recordServerError } from "./server/error-log.server";
import { pickWaitUntil, runWithRequestContext } from "./server/request-context";

type ServerEntry = {
  fetch: (request: Request, env: unknown, ctx: unknown) => Promise<Response> | Response;
};

let serverEntryPromise: Promise<ServerEntry> | undefined;

async function getServerEntry(): Promise<ServerEntry> {
  if (!serverEntryPromise) {
    serverEntryPromise = import("@tanstack/react-start/server-entry").then(
      (m) => (m.default ?? m) as ServerEntry,
    );
  }
  return serverEntryPromise;
}

// h3 swallows in-handler throws into a normal 500 Response with body
// {"unhandled":true,"message":"HTTPError"} — try/catch alone never fires for those.
async function normalizeCatastrophicSsrResponse(response: Response, captured: unknown): Promise<Response> {
  const contentType = response.headers.get("content-type") ?? "";
  if (!contentType.includes("application/json")) return response;

  const body = await response.clone().text();
  if (!isH3SwallowedErrorBody(body)) return response;

  console.error(captured ?? new Error(`h3 swallowed SSR error: ${body}`));
  return new Response(renderErrorPage(), {
    status: 500,
    headers: { "content-type": "text/html; charset=utf-8" },
  });
}

function isH3SwallowedErrorBody(body: string): boolean {
  try {
    const payload = JSON.parse(body) as { unhandled?: unknown; message?: unknown };
    return payload.unhandled === true && payload.message === "HTTPError";
  } catch {
    return false;
  }
}

export default {
  async fetch(request: Request, env: unknown, ctx: unknown) {
    // Lets webhook handlers finish their work after answering (see server/request-context.ts).
    return runWithRequestContext({ waitUntil: pickWaitUntil(request, ctx) }, () => handle(request, env, ctx));
  },
};

async function handle(request: Request, env: unknown, ctx: unknown): Promise<Response> {
  try {
    const handler = await getServerEntry();
    const response = await handler.fetch(request, env, ctx);
    // Server-function errors arrive serialized and the page shows them; anything else is a crash.
    if (response.status < 500 || response.headers.get("x-tss-serialized")) return response;
    const captured = consumeLastCapturedError();
    await recordServerError(describeRequest(request, response.status), captured ?? `status ${response.status}`);
    return await normalizeCatastrophicSsrResponse(response, captured);
  } catch (error) {
    console.error(error);
    await recordServerError(describeRequest(request, 500), error);
    return new Response(renderErrorPage(), {
      status: 500,
      headers: { "content-type": "text/html; charset=utf-8" },
    });
  }
}

function describeRequest(request: Request, status: number): string {
  return `${request.method} ${new URL(request.url).pathname} → ${status}`;
}
