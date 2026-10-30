import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { asAdmin, asMember } from "@/server/admin.server";
import { applyItemAction, ContentError, createStudioToken, listItems, STATUSES, studioTokenState, type ContentItem } from "@/server/content.server";

/** The Content page: what the studio made, waiting for a person. */
export interface ContentRow {
  id: number;
  business: string;
  business_name: string;
  kind: ContentItem["kind"];
  status: ContentItem["status"];
  title: string | null;
  caption: string;
  first_comment: string | null;
  alt_text: string | null;
  keyword: string | null;
  funnel_id: string | null;
  media: { url: string; type: "image" | "video" }[];
  cover_url: string | null;
  scheduled_at: string | null;
  published_at: string | null;
  permalink: string | null;
  error: string | null;
  notes: string | null;
  created_at: string;
}

export const listContentFn = createServerFn({ method: "GET" })
  .validator(z.object({ business: z.string().optional(), status: z.enum(STATUSES).optional() }))
  .handler(async ({ data }) =>
    asMember(async (sql): Promise<ContentRow[]> => {
      const [items, names] = await Promise.all([
        listItems(sql, { business: data.business, status: data.status, limit: 300 }),
        sql<{ slug: string; name: string }[]>`SELECT slug, coalesce(config->>'name', slug) AS name FROM businesses`,
      ]);
      const nameOf = new Map(names.map((n) => [n.slug, n.name]));
      const iso = (d: Date | null) => (d ? new Date(d).toISOString() : null);
      return items.map((it) => ({
        id: it.id,
        business: it.business,
        business_name: nameOf.get(it.business) ?? it.business,
        kind: it.kind,
        status: it.status,
        title: it.title,
        caption: it.caption,
        first_comment: it.first_comment,
        alt_text: it.alt_text,
        keyword: it.keyword,
        funnel_id: it.funnel_id,
        media: (it.media ?? []).map((m) => ({ url: m.url, type: m.type })),
        cover_url: it.cover_url,
        scheduled_at: iso(it.scheduled_at),
        published_at: iso(it.published_at),
        permalink: it.permalink,
        error: it.error,
        notes: it.notes,
        created_at: iso(it.created_at)!,
      }));
    }),
  );

const Action = z.discriminatedUnion("action", [
  z.object({ action: z.literal("approve") }),
  z.object({ action: z.literal("reject") }),
  z.object({ action: z.literal("draft") }),
  z.object({ action: z.literal("schedule"), at: z.string().max(40).nullable() }),
  z.object({ action: z.literal("posted"), permalink: z.string().max(500).optional() }),
  z.object({ action: z.literal("post_now") }),
  z.object({ action: z.literal("delete") }),
]);

export const contentActionFn = createServerFn({ method: "POST" })
  .validator(z.object({ id: z.number().int().positive(), act: Action }))
  .handler(async ({ data }) =>
    asAdmin(async (sql): Promise<{ ok: boolean; error?: string }> => {
      try {
        await applyItemAction(sql, data.id, data.act);
        return { ok: true };
      } catch (err) {
        if (err instanceof ContentError) return { ok: false, error: err.message };
        throw err;
      }
    }),
  );

export const studioTokenStateFn = createServerFn({ method: "GET" }).handler(async () => asAdmin((sql) => studioTokenState(sql)));

/** A new studio token, shown once. The old one stops working. */
export const createStudioTokenFn = createServerFn({ method: "POST" }).handler(async () =>
  asAdmin(async (sql) => ({ token: await createStudioToken(sql) })),
);
