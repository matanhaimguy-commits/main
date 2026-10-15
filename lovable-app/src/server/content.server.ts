import "@tanstack/react-start/server-only";
import { createHash, randomBytes, timingSafeEqual } from "node:crypto";
import { z } from "zod/v4";
import { ConfigError, parseBusiness } from "@/agent/config/load";
import { getState, listConnections, setState } from "@/agent/db/connections";
import type { Sql } from "@/agent/db/sql";
import { auditBusiness, type Issue } from "@/agent/logic/audit";
import { dbConfig } from "./db.server";
import { createRuntimeDeps } from "./runtime.server";

/**
 * The Growth Engine's side of the hub: the content calendar the studio fills (drafts with
 * media in the public "content" bucket), the funnels each post's keyword needs, and the
 * numbers each post produced. The studio talks to it through /api/content/* with one
 * secret token; people use the Content page.
 */

// ---- studio token ------------------------------------------------------------------------------

const TOKEN_STATE = "studio_token";
const sha256 = (s: string) => createHash("sha256").update(s).digest("hex");

/** A new studio token, returned once. Replaces the previous one. Only its hash is stored. */
export async function createStudioToken(sql: Sql): Promise<string> {
  const token = `ssk_${randomBytes(24).toString("base64url")}`;
  await setState(sql, TOKEN_STATE, { hash: sha256(token), created_at: new Date().toISOString() });
  return token;
}

export async function studioTokenState(sql: Sql): Promise<{ exists: boolean; createdAt: string | null }> {
  const s = (await getState<{ hash: string; created_at: string }>(sql, TOKEN_STATE))?.value;
  return { exists: !!s, createdAt: s?.created_at ?? null };
}

export async function checkStudioToken(sql: Sql, request: Request): Promise<boolean> {
  const given = request.headers.get("authorization")?.match(/^Bearer\s+(\S+)$/i)?.[1];
  const stored = (await getState<{ hash: string }>(sql, TOKEN_STATE))?.value?.hash;
  if (!given || !stored) return false;
  const a = Buffer.from(sha256(given));
  const b = Buffer.from(stored);
  return a.length === b.length && timingSafeEqual(a, b);
}

// ---- items -------------------------------------------------------------------------------------

export const KINDS = ["reel", "carousel", "image", "story"] as const;
export const STATUSES = ["draft", "approved", "scheduled", "publishing", "published", "rejected", "failed"] as const;

const MediaInput = z.object({
  url: z.url(),
  path: z.string().max(500).optional(),
  type: z.enum(["image", "video"]),
  width: z.number().int().positive().optional(),
  height: z.number().int().positive().optional(),
});

export const ItemInput = z.object({
  business: z.string().min(1).max(64),
  external_key: z.string().min(1).max(200).optional(),
  kind: z.enum(KINDS),
  title: z.string().max(200).optional(),
  caption: z.string().max(2200).default(""),
  first_comment: z.string().max(2200).optional(),
  alt_text: z.string().max(2000).optional(),
  keyword: z.string().max(60).optional(),
  funnel_id: z.string().max(64).optional(),
  media: z.array(MediaInput).max(20).default([]),
  cover_url: z.url().optional(),
  scheduled_at: z.iso.datetime({ offset: true }).optional(),
  notes: z.string().max(4000).optional(),
  source: z.record(z.string(), z.unknown()).default({}),
});
export type ItemInput = z.infer<typeof ItemInput>;

export interface ContentItem {
  id: number;
  business: string;
  external_key: string | null;
  kind: (typeof KINDS)[number];
  status: (typeof STATUSES)[number];
  title: string | null;
  caption: string;
  first_comment: string | null;
  alt_text: string | null;
  keyword: string | null;
  funnel_id: string | null;
  media: { url: string; path?: string; type: "image" | "video"; width?: number; height?: number }[];
  cover_url: string | null;
  scheduled_at: Date | null;
  published_at: Date | null;
  ig_media_id: string | null;
  permalink: string | null;
  error: string | null;
  notes: string | null;
  source: Record<string, unknown>;
  metrics: Record<string, unknown>;
  /** The publisher's progress between runs (container ids, retries). */
  publish?: Record<string, unknown>;
  created_at: Date;
  updated_at: Date;
}

export class ContentError extends Error {
  constructor(
    message: string,
    readonly status = 400,
  ) {
    super(message);
  }
}

const LOCKED: ContentItem["status"][] = ["publishing", "published"];

/** Creates an item, or updates the one with the same external_key while it is not yet published. */
export async function upsertItem(sql: Sql, input: ItemInput): Promise<ContentItem> {
  const [biz] = await sql<{ slug: string }[]>`SELECT slug FROM businesses WHERE slug = ${input.business}`;
  if (!biz) throw new ContentError(`No business "${input.business}".`, 404);
  if (input.kind === "carousel" && (input.media.length < 2 || input.media.length > 10)) {
    throw new ContentError("A carousel needs 2 to 10 media files.");
  }
  if ((input.kind === "image" || input.kind === "reel") && input.media.length > 1) {
    throw new ContentError(`A ${input.kind} has exactly one media file.`);
  }
  if (input.external_key) {
    const [existing] = await sql<{ id: number; status: ContentItem["status"] }[]>`
      SELECT id, status FROM content_items WHERE business = ${input.business} AND external_key = ${input.external_key}`;
    if (existing && LOCKED.includes(existing.status)) {
      throw new ContentError(`Item ${input.external_key} is already ${existing.status}; it can no longer change.`, 409);
    }
  }
  const scheduled = input.scheduled_at ? new Date(input.scheduled_at) : null;
  const [row] = await sql<ContentItem[]>`
    INSERT INTO content_items (business, external_key, kind, title, caption, first_comment, alt_text, keyword, funnel_id,
                               media, cover_url, scheduled_at, notes, source)
    VALUES (${input.business}, ${input.external_key ?? null}, ${input.kind}, ${input.title ?? null}, ${input.caption},
            ${input.first_comment ?? null}, ${input.alt_text ?? null}, ${input.keyword ?? null}, ${input.funnel_id ?? null},
            ${sql.json(input.media)}, ${input.cover_url ?? null}, ${scheduled}, ${input.notes ?? null}, ${sql.json(input.source)})
    ON CONFLICT (business, external_key) DO UPDATE SET
      kind = EXCLUDED.kind, title = EXCLUDED.title, caption = EXCLUDED.caption, first_comment = EXCLUDED.first_comment,
      alt_text = EXCLUDED.alt_text, keyword = EXCLUDED.keyword, funnel_id = EXCLUDED.funnel_id, media = EXCLUDED.media,
      cover_url = EXCLUDED.cover_url, scheduled_at = EXCLUDED.scheduled_at, notes = EXCLUDED.notes, source = EXCLUDED.source,
      status = CASE WHEN content_items.status IN ('rejected', 'failed') THEN 'draft' ELSE content_items.status END,
      error = NULL, updated_at = now()
    RETURNING *`;
  return row!;
}

export async function listItems(
  sql: Sql,
  filter: { business?: string; status?: string; limit?: number },
): Promise<ContentItem[]> {
  const rows = await sql<ContentItem[]>`
    SELECT * FROM content_items
    WHERE (${filter.business ?? null}::text IS NULL OR business = ${filter.business ?? null})
      AND (${filter.status ?? null}::text IS NULL OR status = ${filter.status ?? null})
    ORDER BY coalesce(scheduled_at, created_at) DESC, id DESC
    LIMIT ${filter.limit ?? 200}`;
  return [...rows];
}

export type ItemAction =
  | { action: "approve" }
  | { action: "reject" }
  | { action: "draft" }
  | { action: "schedule"; at: string | null }
  | { action: "posted"; permalink?: string }
  | { action: "delete" };

/** What people do on the Content page. Publishing itself is the publisher's job (src/agent/engine/publish.ts). */
export async function applyItemAction(sql: Sql, id: number, a: ItemAction): Promise<ContentItem | null> {
  const [item] = await sql<ContentItem[]>`SELECT * FROM content_items WHERE id = ${id}`;
  if (!item) throw new ContentError("This item no longer exists.", 404);
  if (a.action === "delete") {
    if (item.status === "publishing") throw new ContentError("It is being published right now.");
    await sql`DELETE FROM content_items WHERE id = ${id}`;
    return null;
  }
  if (LOCKED.includes(item.status) && a.action !== "posted") {
    throw new ContentError(`It is already ${item.status}.`);
  }
  let rows: ContentItem[];
  switch (a.action) {
    case "approve":
      rows = await sql<ContentItem[]>`
        UPDATE content_items SET status = CASE WHEN scheduled_at IS NULL THEN 'approved' ELSE 'scheduled' END, error = NULL,
          publish = '{}'::jsonb, updated_at = now()
        WHERE id = ${id} RETURNING *`;
      break;
    case "reject":
      rows = await sql<ContentItem[]>`UPDATE content_items SET status = 'rejected', updated_at = now() WHERE id = ${id} RETURNING *`;
      break;
    case "draft":
      rows = await sql<ContentItem[]>`UPDATE content_items SET status = 'draft', error = NULL, updated_at = now() WHERE id = ${id} RETURNING *`;
      break;
    case "schedule": {
      const at = a.at ? new Date(a.at) : null;
      if (at && Number.isNaN(at.getTime())) throw new ContentError("That date is not valid.");
      rows = await sql<ContentItem[]>`
        UPDATE content_items SET scheduled_at = ${at},
          status = CASE WHEN status IN ('approved', 'scheduled') THEN (CASE WHEN ${at}::timestamptz IS NULL THEN 'approved' ELSE 'scheduled' END) ELSE status END,
          updated_at = now()
        WHERE id = ${id} RETURNING *`;
      break;
    }
    case "posted": {
      const permalink = a.permalink?.trim() || null;
      const mediaId = permalink ? await findMediaId(sql, item.business, permalink).catch(() => null) : null;
      rows = await sql<ContentItem[]>`
        UPDATE content_items SET status = 'published', published_at = coalesce(published_at, now()),
          permalink = coalesce(${permalink}, permalink), ig_media_id = coalesce(${mediaId}, ig_media_id), error = NULL, updated_at = now()
        WHERE id = ${id} RETURNING *`;
      break;
    }
  }
  return rows[0] ?? null;
}

const normalizeLink = (u: string) => u.replace(/[?#].*$/, "").replace(/\/+$/, "").toLowerCase();

/** The Instagram media id behind a permalink, from the business's recent posts. */
async function findMediaId(sql: Sql, business: string, permalink: string): Promise<string | null> {
  const { deps } = await createRuntimeDeps(sql);
  const b = deps.registry.bySlug(business);
  const api = b ? deps.metaFor(b) : undefined;
  if (!b?.meta.instagram_id || !api) return null;
  const res = await api.get<{ data: { id: string; permalink?: string }[] }>(`${b.meta.instagram_id}/media`, {
    fields: "id,permalink",
    limit: "50",
  });
  const want = normalizeLink(permalink);
  return res.data.find((m) => m.permalink && normalizeLink(m.permalink) === want)?.id ?? null;
}

// ---- media uploads -----------------------------------------------------------------------------

export const UploadInput = z.object({
  business: z.string().min(1).max(64),
  filename: z.string().min(1).max(200),
});

const safeName = (s: string) =>
  s
    .normalize("NFKD")
    .replace(/[^\w.\-]+/g, "-")
    .replace(/-+/g, "-")
    .slice(-120);

/**
 * A one-time upload URL in the public "content" bucket (PUT the file body to it) and the
 * public URL the file will have. Files never pass through this server.
 */
export async function signedUpload(input: z.infer<typeof UploadInput>): Promise<{ uploadUrl: string; publicUrl: string; path: string }> {
  const { url, key } = dbConfig();
  if (!url || !key) throw new ContentError("Storage is not available.", 503);
  const day = new Date().toISOString().slice(0, 10);
  const path = `${safeName(input.business)}/${day}/${randomBytes(4).toString("hex")}-${safeName(input.filename)}`;
  const res = await fetch(`${url}/storage/v1/object/upload/sign/content/${path}`, {
    method: "POST",
    headers: { apikey: key, Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: "{}",
  });
  const body = (await res.json().catch(() => ({}))) as { url?: string; message?: string };
  if (!res.ok || !body.url) throw new ContentError(`Storage refused the upload: ${body.message ?? res.status}`, 502);
  return {
    uploadUrl: `${url}/storage/v1${body.url}`,
    publicUrl: `${url}/storage/v1/object/public/content/${path}`,
    path,
  };
}

// ---- funnels -----------------------------------------------------------------------------------

export const FunnelUpsertInput = z.object({
  business: z.string().min(1).max(64),
  funnel: z.record(z.string(), z.unknown()),
});

/** Adds the funnel, or replaces the one with the same id, after validating the whole business. */
export async function upsertFunnel(
  sql: Sql,
  input: z.infer<typeof FunnelUpsertInput>,
): Promise<{ ok: boolean; problems: string[]; issues: Issue[] }> {
  const [row] = await sql<{ config: Record<string, unknown> }[]>`SELECT config FROM businesses WHERE slug = ${input.business}`;
  if (!row) throw new ContentError(`No business "${input.business}".`, 404);
  const id = input.funnel["id"];
  if (typeof id !== "string" || !id) return { ok: false, problems: ["The funnel needs an id."], issues: [] };
  const funnels = Array.isArray(row.config["funnels"]) ? [...(row.config["funnels"] as Record<string, unknown>[])] : [];
  const at = funnels.findIndex((f) => f["id"] === id);
  if (at >= 0) funnels[at] = input.funnel;
  else funnels.push(input.funnel);
  const config = { ...row.config, funnels };
  let business;
  try {
    business = parseBusiness(config, input.business);
  } catch (err) {
    return { ok: false, problems: err instanceof ConfigError ? err.problems : [(err as Error).message], issues: [] };
  }
  await sql`UPDATE businesses SET config = ${sql.json(config)}, updated_at = now() WHERE slug = ${input.business}`;
  const connections = await listConnections(sql);
  const hasPage = !!business.meta.page_id || connections.some((c) => c.business === business.slug);
  return { ok: true, problems: [], issues: auditBusiness(business, { hasToken: hasPage }) };
}

// ---- what the studio reads -------------------------------------------------------------------

/** Every business with what the studio needs to write for it. */
export async function clientsForStudio(sql: Sql) {
  const [rows, connections] = await Promise.all([
    sql<{ slug: string; config: Record<string, unknown> }[]>`SELECT slug, config FROM businesses ORDER BY slug`,
    listConnections(sql),
  ]);
  return rows.map((r) => {
    const c = r.config as {
      name?: string;
      enabled?: boolean;
      live?: boolean;
      timezone?: string;
      profile?: unknown;
      links?: unknown[];
      funnels?: { id: string; trigger?: string; status?: string; keywords?: string[]; all_posts?: boolean }[];
    };
    const conn = connections.find((x) => x.business === r.slug);
    return {
      slug: r.slug,
      name: c.name ?? r.slug,
      enabled: c.enabled !== false,
      live: !!c.live,
      timezone: c.timezone ?? "UTC",
      profile: c.profile ?? null,
      links: c.links ?? [],
      funnels: (c.funnels ?? []).map((f) => ({ id: f.id, trigger: f.trigger, status: f.status, keywords: f.keywords ?? [], all_posts: !!f.all_posts })),
      instagram: conn?.instagram_username ? { id: conn.instagram_id, username: conn.instagram_username } : null,
      page: conn ? { id: conn.page_id, name: conn.page_name } : null,
    };
  });
}

export interface ItemResults {
  id: number;
  external_key: string | null;
  kind: string;
  status: string;
  keyword: string | null;
  funnel_id: string | null;
  published_at: Date | null;
  permalink: string | null;
  instagram: { likes?: number; comments?: number } | null;
  funnel: { comments: number; dms_sent: number; taps: number; new_leads: number; hot_or_booked: number } | null;
}

/**
 * What each post produced: Instagram's public counts (likes, comments) and, through its
 * keyword funnel, the comments, DMs, taps and leads the bot recorded. Reach, saves and
 * shares need instagram_manage_insights (phase 2).
 */
export async function itemResults(sql: Sql, business: string, sinceDays: number): Promise<ItemResults[]> {
  const items = await sql<ContentItem[]>`
    SELECT * FROM content_items WHERE business = ${business}
      AND coalesce(published_at, created_at) > now() - make_interval(days => ${sinceDays})
    ORDER BY coalesce(published_at, created_at) DESC LIMIT 60`;
  const { deps } = await createRuntimeDeps(sql);
  const b = deps.registry.bySlug(business);
  const api = b ? deps.metaFor(b) : undefined;
  const out: ItemResults[] = [];
  for (const it of items) {
    let instagram: ItemResults["instagram"] = null;
    if (it.ig_media_id && api) {
      try {
        const m = await api.get<{ like_count?: number; comments_count?: number }>(it.ig_media_id, { fields: "like_count,comments_count" });
        instagram = { likes: m.like_count, comments: m.comments_count };
        await sql`UPDATE content_items SET metrics = metrics || ${sql.json({ ...instagram, at: new Date().toISOString() })} WHERE id = ${it.id}`;
      } catch {
        instagram = null;
      }
    }
    let funnel: ItemResults["funnel"] = null;
    if (it.funnel_id) {
      const since = it.published_at ?? it.created_at;
      const [f] = await sql<{ comments: number; dms_sent: number; taps: number; new_leads: number; hot_or_booked: number }[]>`
        SELECT
          (SELECT count(*)::int FROM comments WHERE business = ${business} AND funnel_id = ${it.funnel_id} AND received_at >= ${since}) AS comments,
          (SELECT count(*)::int FROM sends WHERE business = ${business} AND funnel_id = ${it.funnel_id} AND status = 'sent' AND created_at >= ${since}) AS dms_sent,
          (SELECT count(*)::int FROM taps WHERE business = ${business} AND funnel_id = ${it.funnel_id} AND created_at >= ${since}) AS taps,
          (SELECT count(*)::int FROM contacts WHERE business = ${business} AND source = ${`funnel:${it.funnel_id}`} AND created_at >= ${since}) AS new_leads,
          (SELECT count(*)::int FROM contacts WHERE business = ${business} AND source = ${`funnel:${it.funnel_id}`} AND created_at >= ${since}
             AND stage IN ('hot', 'booked', 'won')) AS hot_or_booked`;
      funnel = f ?? null;
    }
    out.push({
      id: it.id,
      external_key: it.external_key,
      kind: it.kind,
      status: it.status,
      keyword: it.keyword,
      funnel_id: it.funnel_id,
      published_at: it.published_at,
      permalink: it.permalink,
      instagram,
      funnel,
    });
  }
  return out;
}
