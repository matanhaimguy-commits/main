import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { businessToYaml, ConfigError, parseBusiness, yamlToRaw } from "@/agent/config/load";
import { starterBusiness } from "@/agent/config/starter";
import { listConnections } from "@/agent/db/connections";
import { auditBusiness, type Issue } from "@/agent/logic/audit";
import { asAdmin, asMember } from "@/server/admin.server";
import { describeMetaError } from "@/server/handlers.server";
import { createRuntimeDeps, loadBusinesses } from "@/server/runtime.server";

const Slug = z.string().regex(/^[a-z0-9][a-z0-9_-]*$/, "Use lowercase letters, digits, - and _");

export const listBusinessesFn = createServerFn({ method: "GET" }).handler(async () =>
  asMember(async (sql) => {
    const { deps, loaded } = await createRuntimeDeps(sql);
    return {
      businesses: deps.registry.businesses.map((b) => {
        const st = deps.liveStatus(b);
        return {
          slug: b.slug,
          name: b.name,
          enabled: b.enabled,
          live: st.live,
          reason: st.reason,
          errors: st.issues.filter((i) => i.level === "error").length,
          warnings: st.issues.filter((i) => i.level === "warn").length,
          funnels: b.funnels.length,
          activeFunnels: b.funnels.filter((f) => f.status === "active").length,
          connected: !!b.meta.page_id,
        };
      }),
      invalid: loaded.invalid,
    };
  }),
);

export interface BusinessDetail {
  slug: string;
  /** The business with every default filled in, for the form editor. */
  config: Record<string, any> | null;
  /** As stored, for the YAML editor. */
  yaml: string;
  problems: string[];
  issues: Issue[];
  live: { live: boolean; reason: string } | null;
  connected: { pageName: string | null; instagramUsername: string | null } | null;
}

export const getBusinessFn = createServerFn({ method: "GET" })
  .validator(z.object({ slug: Slug }))
  .handler(async ({ data }) =>
    asMember(async (sql): Promise<BusinessDetail | null> => {
      const { deps, loaded } = await createRuntimeDeps(sql);
      const row = loaded.rows.find((r) => r.slug === data.slug);
      if (!row) return null;
      const b = deps.registry.bySlug(data.slug);
      const invalid = loaded.invalid.find((i) => i.slug === data.slug);
      const conn = b?.meta.page_id ? (await listConnections(sql)).find((c) => c.page_id === b.meta.page_id) : undefined;
      const st = b ? deps.liveStatus(b) : null;
      return {
        slug: row.slug,
        config: b ? (JSON.parse(JSON.stringify(b)) as Record<string, any>) : null,
        yaml: businessToYaml(row.config),
        problems: invalid?.problems ?? [],
        issues: st?.issues ?? [],
        live: st ? { live: st.live, reason: st.reason } : null,
        connected: conn ? { pageName: conn.page_name, instagramUsername: conn.instagram_username } : null,
      };
    }),
  );

export const createBusinessFn = createServerFn({ method: "POST" })
  .validator(z.object({ slug: Slug, name: z.string().min(1).max(100) }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const [exists] = await sql<{ slug: string }[]>`SELECT slug FROM businesses WHERE slug = ${data.slug}`;
      if (exists) return { ok: false, problems: [`A business with the id "${data.slug}" already exists.`] };
      const config = starterBusiness(data.slug, data.name);
      parseBusiness(config, data.slug);
      await sql`INSERT INTO businesses (slug, config) VALUES (${data.slug}, ${sql.json(config)})`;
      return { ok: true, problems: [] as string[] };
    }),
  );

/**
 * Saves a business from the form (an object) or the YAML editor (text). It is validated
 * first; the slug cannot change, because conversations and stats are filed under it.
 */
export const saveBusinessFn = createServerFn({ method: "POST" })
  .validator(z.object({ slug: Slug, config: z.record(z.string(), z.unknown()).optional(), yaml: z.string().max(200_000).optional() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      let raw: unknown;
      try {
        raw = data.yaml !== undefined ? yamlToRaw(data.yaml, data.slug) : data.config;
        parseBusiness(raw, data.slug);
      } catch (err) {
        return { ok: false, problems: err instanceof ConfigError ? err.problems : [(err as Error).message], issues: [] as Issue[] };
      }
      if ((raw as { slug?: unknown }).slug !== data.slug) {
        return { ok: false, problems: [`The id must stay "${data.slug}". Create a new business for a new id.`], issues: [] as Issue[] };
      }
      const [row] = await sql<{ slug: string }[]>`
        UPDATE businesses SET config = ${sql.json(raw)}, updated_at = now() WHERE slug = ${data.slug} RETURNING slug`;
      if (!row) return { ok: false, problems: ["This business no longer exists."], issues: [] as Issue[] };
      const b = parseBusiness(raw, data.slug);
      const connections = await listConnections(sql);
      const hasPage = !!b.meta.page_id || connections.some((c) => c.business === b.slug);
      return { ok: true, problems: [] as string[], issues: auditBusiness(b, { hasToken: hasPage }) };
    }),
  );

export const deleteBusinessFn = createServerFn({ method: "POST" })
  .validator(z.object({ slug: Slug }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      await sql`UPDATE meta_connections SET business = NULL WHERE business = ${data.slug}`;
      await sql`DELETE FROM businesses WHERE slug = ${data.slug}`;
      return { ok: true };
    }),
  );

export interface RecentPost {
  platform: "instagram" | "facebook";
  id: string;
  date: string;
  kind: string;
  text: string;
  url: string | null;
}

/** Recent posts and reels, so a funnel can be pinned to one without hunting for IDs. */
export const recentPostsFn = createServerFn({ method: "GET" })
  .validator(z.object({ slug: Slug }))
  .handler(async ({ data }) =>
    asMember(async (sql): Promise<{ posts: RecentPost[]; error: string | null }> => {
      const { deps } = await createRuntimeDeps(sql);
      const b = deps.registry.bySlug(data.slug);
      const api = b ? deps.metaFor(b) : undefined;
      if (!b || !api) return { posts: [], error: "Connect a Facebook Page to this business first (Connect page)." };
      const posts: RecentPost[] = [];
      const errors: string[] = [];
      if (b.meta.instagram_id) {
        try {
          const res = await api.get<{ data: { id: string; caption?: string; media_product_type?: string; timestamp: string; permalink?: string }[] }>(
            `${b.meta.instagram_id}/media`,
            { fields: "id,caption,media_product_type,timestamp,permalink", limit: "25" },
          );
          for (const m of res.data)
            posts.push({ platform: "instagram", id: m.id, date: m.timestamp, kind: m.media_product_type ?? "", text: m.caption ?? "", url: m.permalink ?? null });
        } catch (err) {
          errors.push(`Instagram: ${describeMetaError(err)}`);
        }
      }
      if (b.meta.page_id) {
        try {
          const res = await api.get<{ data: { id: string; message?: string; created_time: string; permalink_url?: string }[] }>(`${b.meta.page_id}/posts`, {
            fields: "id,message,created_time,permalink_url",
            limit: "25",
          });
          for (const p of res.data)
            posts.push({ platform: "facebook", id: p.id, date: p.created_time, kind: "post", text: p.message ?? "", url: p.permalink_url ?? null });
        } catch (err) {
          errors.push(`Facebook: ${describeMetaError(err)}`);
        }
      }
      posts.sort((x, y) => y.date.localeCompare(x.date));
      return { posts, error: errors.length ? errors.join(" · ") : null };
    }),
  );

export const businessSlugsFn = createServerFn({ method: "GET" }).handler(async () =>
  asMember(async (sql) => (await loadBusinesses(sql)).rows.map((r) => ({ slug: r.slug, name: String(r.config["name"] ?? r.slug) }))),
);
