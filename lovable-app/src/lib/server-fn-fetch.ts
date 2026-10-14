/**
 * Fetch used for every server-function call from the browser (wired in src/start.ts).
 *
 * Server functions answer in TanStack's serialized format. When something in between answers
 * instead (a hosting timeout, a gateway error page, a JSON error from the platform), TanStack
 * hands that body to the page as if it were the result, and the page crashes on it. This turns
 * any such answer into a normal error the page can show.
 */
export const serverFnFetch: typeof fetch = async (input, init) => {
  const res = await fetch(input, init);
  if (res.headers.get("x-tss-serialized") || res.headers.get("x-tss-raw") === "true") return res;
  // TanStack's own redirect / not-found answers are plain JSON with a 2xx/3xx status.
  if (res.status < 400 && (res.headers.get("content-type") ?? "").includes("application/json")) return res;
  const body = await res.text().catch(() => "");
  throw new Error(describeBadAnswer(res.status, body));
};

export function describeBadAnswer(status: number, body: string): string {
  const snippet = body
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 160);
  if ([408, 502, 503, 504, 522, 524].includes(status)) {
    return `The server took too long to answer (status ${status}). Try again in a moment.`;
  }
  return `The server answered with status ${status}${snippet ? `: ${snippet}` : ""}.`;
}
