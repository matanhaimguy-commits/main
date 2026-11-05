import "@tanstack/react-start/server-only";
import { getState, setState } from "@/agent/db/connections";
import { describeError } from "@/lib/error-capture";
import { getDb } from "./db.server";

/**
 * The last server errors, kept in app_state('server_errors') so they can be read from the
 * database: the hosted app's console output is not available to us.
 */
export interface ServerErrorEntry {
  at: string;
  where: string;
  message: string;
}

const KEEP = 20;

/** Long opaque strings (access tokens, keys) never go into the log. */
export function redactSecrets(text: string): string {
  return text.replace(/\bBearer\s+\S+/gi, "Bearer [redacted]").replace(/[A-Za-z0-9_\-.]{40,}/g, "[redacted]");
}

/** Best effort and bounded: logging must never break or slow down a request much. */
export async function recordServerError(where: string, error: unknown): Promise<void> {
  const write = async () => {
    const sql = getDb();
    const entry: ServerErrorEntry = { at: new Date().toISOString(), where, message: redactSecrets(describeError(error)).slice(0, 2000) };
    const prev = (await getState<ServerErrorEntry[]>(sql, "server_errors"))?.value ?? [];
    await setState(sql, "server_errors", [entry, ...prev].slice(0, KEEP));
  };
  try {
    await Promise.race([write(), new Promise((resolve) => setTimeout(resolve, 3000))]);
  } catch {
    // ignore
  }
}
