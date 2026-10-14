import { afterEach, describe, expect, it, vi } from "vitest";
import { redactSecrets } from "@/server/error-log.server";
import { serverFnFetch } from "./server-fn-fetch";

vi.mock("@tanstack/react-start/server-only", () => ({}));

const answer = (body: string, status: number, headers: Record<string, string>) =>
  vi.spyOn(globalThis, "fetch").mockResolvedValue(new Response(body, { status, headers }));

describe("serverFnFetch", () => {
  afterEach(() => vi.restoreAllMocks());

  it("passes serialized answers through, errors included", async () => {
    answer("{}", 500, { "content-type": "application/json", "x-tss-serialized": "true" });
    const res = await serverFnFetch("/_serverFn/x");
    expect(res.status).toBe(500);
  });

  it("passes plain JSON redirects through", async () => {
    answer('{"isRedirect":true}', 200, { "content-type": "application/json" });
    expect((await serverFnFetch("/_serverFn/x")).status).toBe(200);
  });

  it("turns a gateway timeout into a readable error", async () => {
    answer('{"error":"upstream timed out"}', 504, { "content-type": "application/json" });
    await expect(serverFnFetch("/_serverFn/x")).rejects.toThrow("took too long to answer (status 504)");
  });

  it("turns an HTML error page into a short message", async () => {
    answer("<html><style>p{}</style><h1>Worker exceeded resource limits</h1></html>", 503, { "content-type": "text/html" });
    await expect(serverFnFetch("/_serverFn/x")).rejects.toThrow("status 503");
    answer("<html><h1>Bad thing</h1></html>", 500, { "content-type": "text/html" });
    await expect(serverFnFetch("/_serverFn/x")).rejects.toThrow("status 500: Bad thing.");
  });

  it("rejects a 200 answer that is not from a server function", async () => {
    answer("<html>hello</html>", 200, { "content-type": "text/html" });
    await expect(serverFnFetch("/_serverFn/x")).rejects.toThrow("status 200");
  });
});

describe("redactSecrets", () => {
  it("removes tokens and bearer headers from logged errors", () => {
    const token = "EAAB" + "x".repeat(60);
    expect(redactSecrets(`failed for ${token} with Bearer abc.def`)).toBe("failed for [redacted] with Bearer [redacted]");
  });
});
