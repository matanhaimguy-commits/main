import { createServerFn } from "@tanstack/react-start";
import { getDb } from "@/server/db.server";
import { loadRuntimeEnv } from "@/server/settings.server";

/** Operator details for the public privacy and data-deletion pages Meta requires. */
export const operatorInfoFn = createServerFn({ method: "GET" }).handler(async () => {
  try {
    const { env } = await loadRuntimeEnv(getDb());
    return { name: env.OPERATOR_NAME ?? null, email: env.OPERATOR_EMAIL ?? null };
  } catch {
    return { name: null, email: null };
  }
});
