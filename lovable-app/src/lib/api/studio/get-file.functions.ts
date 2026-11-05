import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { asMember } from "@/server/admin.server";
import { fileMarkdown } from "@/server/studio/index.server";

/** A doc's markdown, loaded when it is opened. Owner and reviewers. */
export const getStudioFileFn = createServerFn({ method: "GET" })
  .validator(z.object({ id: z.number().int().positive() }))
  .handler(async ({ data }) => asMember((sql) => fileMarkdown(sql, data.id)));
