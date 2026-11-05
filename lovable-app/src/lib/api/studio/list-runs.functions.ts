import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { asMember } from "@/server/admin.server";
import { listRuns } from "@/server/studio/index.server";
import { toRunCard } from "./to-view";
import type { StudioRunCard } from "./views";

/** Every piece for the Studio list, waiting on the owner first. Owner and reviewers. */
export const listStudioRunsFn = createServerFn({ method: "GET" })
  .validator(z.object({ business: z.string().max(64).optional() }))
  .handler(async ({ data }) => asMember(async (sql): Promise<StudioRunCard[]> => (await listRuns(sql, { business: data.business })).map(toRunCard)));
