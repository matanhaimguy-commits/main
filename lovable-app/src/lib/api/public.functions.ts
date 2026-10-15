import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
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

const LeadSlug = z.string().regex(/^[a-z0-9][a-z0-9-]{0,63}$/);

/** The public lead form at /l/<slug>: no login, nothing private. */
export const leadFormInfoFn = createServerFn({ method: "GET" })
  .validator(z.object({ slug: LeadSlug }))
  .handler(async ({ data }) => {
    const { leadFormInfo } = await import("@/server/leads.server");
    return leadFormInfo(data.slug);
  });

export const submitLeadFn = createServerFn({ method: "POST" })
  .validator(
    z.object({
      slug: LeadSlug,
      name: z.string().max(120),
      phone: z.string().max(40),
      instagram: z.string().max(60).optional(),
      need: z.string().max(1000).optional(),
      heard: z.string().max(300).optional(),
      source: z.string().max(60).optional(),
      website: z.string().max(200).optional(),
    }),
  )
  .handler(async ({ data }) => {
    const { submitLeadForm } = await import("@/server/leads.server");
    const { slug, ...input } = data;
    return submitLeadForm(slug, input);
  });
