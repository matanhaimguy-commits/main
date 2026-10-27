import type { Sql } from "@/agent/db/sql";

/** A run's columns without its ledger (which can be large and is only needed by the studio). */
export const runColumns = (sql: Sql, alias = "") => {
  const p = alias ? `${alias}.` : "";
  return sql.unsafe(
    ["id", "business", "post_id", "title", "format", "family", "current_step", "status", "waiting_on_owner", "summary", "steps", "pushed_at", "created_at", "updated_at"]
      .map((c) => p + c)
      .join(", "),
  );
};
