import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { asMember } from "@/server/admin.server";
import { runDetail } from "@/server/studio/index.server";
import { toRunView } from "./to-view";
import type { StudioRunView } from "./views";

/** One piece with its steps, files and questions, or null. Owner and reviewers. */
export const getStudioRunFn = createServerFn({ method: "GET" })
  .validator(z.object({ id: z.number().int().positive() }))
  .handler(async ({ data }) =>
    asMember(async (sql): Promise<StudioRunView | null> => {
      const d = await runDetail(sql, data.id);
      return d ? toRunView(d) : null;
    }),
  );
