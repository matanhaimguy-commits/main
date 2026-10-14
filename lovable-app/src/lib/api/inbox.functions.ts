import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { pauseAi, resumeAi, STAGES, type Contact } from "@/agent/db/repo";
import { explainReason } from "@/agent/logic/funnels";
import { asAdmin } from "@/server/admin.server";

const Stage = z.enum(STAGES as [string, ...string[]]);

export interface ContactListItem {
  id: number;
  business: string;
  platform: string;
  username: string | null;
  name: string | null;
  stage: string;
  source: string | null;
  interest: string | null;
  opted_out: boolean;
  ai_paused_until: Date | null;
  last_inbound_at: Date | null;
  last_outbound_at: Date | null;
  last_text: string | null;
  last_direction: string | null;
}

export const listContactsFn = createServerFn({ method: "GET" })
  .validator(
    z.object({
      business: z.string().optional(),
      stage: z.string().optional(),
      search: z.string().max(100).optional(),
      limit: z.number().int().min(1).max(500).optional(),
    }),
  )
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const like = data.search ? `%${data.search.replace(/[%_\\]/g, (m) => `\\${m}`)}%` : null;
      const rows = await sql<ContactListItem[]>`
        SELECT c.id, c.business, c.platform, c.username, c.name, c.stage, c.source, c.interest, c.opted_out,
               c.ai_paused_until, c.last_inbound_at, c.last_outbound_at, m.text AS last_text, m.direction AS last_direction
        FROM contacts c
        LEFT JOIN LATERAL (SELECT text, direction FROM messages WHERE contact_id = c.id ORDER BY id DESC LIMIT 1) m ON true
        WHERE (${data.business ?? null}::text IS NULL OR c.business = ${data.business ?? null})
          AND (${data.stage ?? null}::text IS NULL OR c.stage = ${data.stage ?? null})
          AND (${like}::text IS NULL OR c.username ILIKE ${like} OR c.name ILIKE ${like} OR c.email ILIKE ${like} OR c.phone ILIKE ${like})
        ORDER BY greatest(c.last_inbound_at, c.last_outbound_at, c.created_at) DESC NULLS LAST
        LIMIT ${data.limit ?? 200}`;
      const counts = await sql<{ stage: string; n: number }[]>`
        SELECT stage, count(*)::int AS n FROM contacts
        WHERE (${data.business ?? null}::text IS NULL OR business = ${data.business ?? null}) GROUP BY stage`;
      return { contacts: [...rows], stages: Object.fromEntries(counts.map((c) => [c.stage, c.n])) as Record<string, number> };
    }),
  );

export interface SendRow {
  id: number;
  kind: string;
  step: string | null;
  funnel_id: string | null;
  status: string;
  error_code: number | null;
  error_message: string | null;
  created_at: Date;
  sent_at: Date | null;
  delivered_at: Date | null;
  read_at: Date | null;
}

export interface ConversationMessage {
  id: number;
  direction: "in" | "out";
  source: string;
  text: string | null;
  created_at: Date;
}

export const getConversationFn = createServerFn({ method: "GET" })
  .validator(z.object({ id: z.number().int() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const [contact] = await sql<Contact[]>`SELECT * FROM contacts WHERE id = ${data.id}`;
      if (!contact) return null;
      const messages = await sql<ConversationMessage[]>`
        SELECT id, direction, source, text, created_at FROM messages
        WHERE contact_id = ${data.id} ORDER BY created_at, id LIMIT 500`;
      const sends = await sql<SendRow[]>`
        SELECT id, kind, step, funnel_id, status, error_code, error_message, created_at, sent_at, delivered_at, read_at
        FROM sends WHERE contact_id = ${data.id} ORDER BY created_at DESC LIMIT 100`;
      return { contact, messages: [...messages], sends: [...sends] };
    }),
  );

export const setAiPausedFn = createServerFn({ method: "POST" })
  .validator(z.object({ id: z.number().int(), paused: z.boolean(), days: z.number().min(0.1).max(365).optional() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      if (data.paused) await pauseAi(sql, data.id, new Date(Date.now() + (data.days ?? 30) * 86_400_000), "paused from the dashboard");
      else await resumeAi(sql, data.id);
      return { ok: true };
    }),
  );

export const updateContactFn = createServerFn({ method: "POST" })
  .validator(
    z.object({
      id: z.number().int(),
      stage: Stage.optional(),
      notes: z.string().max(5000).optional(),
      name: z.string().max(200).optional(),
      phone: z.string().max(100).optional(),
      email: z.string().max(200).optional(),
    }),
  )
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      // Replace (not append) notes edited by a person.
      if (data.notes !== undefined) await sql`UPDATE contacts SET notes = ${data.notes || null}, updated_at = now() WHERE id = ${data.id}`;
      await sql`
        UPDATE contacts SET
          stage = COALESCE(${data.stage ?? null}, stage),
          name = COALESCE(${data.name ?? null}, name),
          phone = COALESCE(${data.phone ?? null}, phone),
          email = COALESCE(${data.email ?? null}, email),
          updated_at = now()
        WHERE id = ${data.id}`;
      return { ok: true };
    }),
  );

// ---- activity ---------------------------------------------------------------------------------

export interface CommentItem {
  id: number;
  business: string;
  platform: string;
  comment_id: string;
  post_id: string | null;
  author_name: string | null;
  text: string | null;
  received_at: Date;
  outcome: string;
  skip_reason: string | null;
  explanation: string;
  funnel_id: string | null;
  ai_intent: string | null;
  contact_id: number | null;
}

export const listCommentsFn = createServerFn({ method: "GET" })
  .validator(z.object({ business: z.string().optional(), outcome: z.string().optional(), limit: z.number().int().min(1).max(500).optional() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const rows = await sql<Omit<CommentItem, "explanation">[]>`
        SELECT id, business, platform, comment_id, post_id, author_name, text, received_at, outcome, skip_reason, funnel_id, ai_intent, contact_id
        FROM comments
        WHERE (${data.business ?? null}::text IS NULL OR business = ${data.business ?? null})
          AND (${data.outcome ?? null}::text IS NULL OR outcome = ${data.outcome ?? null})
        ORDER BY received_at DESC LIMIT ${data.limit ?? 200}`;
      return rows.map((r): CommentItem => ({ ...r, explanation: explainReason(r.skip_reason) }));
    }),
  );

export interface SendItem extends SendRow {
  business: string;
  platform: string;
  contact_id: number | null;
  username: string | null;
  /** What was (or would have been) sent, as readable text. */
  preview: string | null;
}

export const listSendsFn = createServerFn({ method: "GET" })
  .validator(z.object({ business: z.string().optional(), status: z.string().optional(), limit: z.number().int().min(1).max(500).optional() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const rows = await sql<SendItem[]>`
        SELECT s.id, s.business, s.platform, s.kind, s.step, s.funnel_id, s.status, s.error_code, s.error_message,
               s.created_at, s.sent_at, s.delivered_at, s.read_at, s.contact_id, c.username,
               coalesce(s.request->>'text', s.request->'attachment'->'payload'->>'text', s.request->>'message',
                        CASE WHEN s.kind = 'hide_comment' THEN '(hid the comment)' END) AS preview
        FROM sends s LEFT JOIN contacts c ON c.id = s.contact_id
        WHERE (${data.business ?? null}::text IS NULL OR s.business = ${data.business ?? null})
          AND (${data.status ?? null}::text IS NULL OR s.status = ${data.status ?? null})
        ORDER BY s.created_at DESC LIMIT ${data.limit ?? 200}`;
      return [...rows];
    }),
  );

/** Headline numbers for the last 7 days. */
export const statsFn = createServerFn({ method: "GET" })
  .validator(z.object({ business: z.string().optional() }))
  .handler(async ({ data }) =>
    asAdmin(async (sql) => {
      const b = data.business ?? null;
      const [row] = await sql<
        { comments: number; funnel_comments: number; dms_sent: number; dry_runs: number; taps: number; clicks: number; ai_replies: number; new_contacts: number; hot: number; failed: number }[]
      >`
        SELECT
          (SELECT count(*)::int FROM comments WHERE received_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS comments,
          (SELECT count(*)::int FROM comments WHERE outcome = 'funnel' AND received_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS funnel_comments,
          (SELECT count(*)::int FROM sends WHERE status = 'sent' AND created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS dms_sent,
          (SELECT count(*)::int FROM sends WHERE status = 'dry_run' AND created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS dry_runs,
          (SELECT count(*)::int FROM taps WHERE created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS taps,
          (SELECT coalesce(sum(clicks), 0)::int FROM links WHERE created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS clicks,
          (SELECT count(*)::int FROM sends WHERE step IN ('ai', 'followup') AND status IN ('sent', 'dry_run') AND created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS ai_replies,
          (SELECT count(*)::int FROM contacts WHERE created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS new_contacts,
          (SELECT count(*)::int FROM contacts WHERE stage IN ('hot', 'booked') AND (${b}::text IS NULL OR business = ${b})) AS hot,
          (SELECT count(*)::int FROM sends WHERE status IN ('failed', 'unknown') AND created_at > now() - interval '7 days' AND (${b}::text IS NULL OR business = ${b})) AS failed`;
      return row!;
    }),
  );
