import type { Platform } from '../config/schema.js';
import type { Sql } from './index.js';

export type Stage = 'new' | 'engaged' | 'qualified' | 'hot' | 'booked' | 'won' | 'lost';
export const STAGES: Stage[] = ['new', 'engaged', 'qualified', 'hot', 'booked', 'won', 'lost'];

export interface Contact {
  id: number;
  business: string;
  platform: Platform;
  external_id: string;
  username: string | null;
  name: string | null;
  phone: string | null;
  email: string | null;
  stage: Stage;
  interest: string | null;
  budget: string | null;
  timeline: string | null;
  notes: string | null;
  source: string | null;
  follows_business: boolean | null;
  opted_out: boolean;
  ai_paused_until: Date | null;
  ai_pause_reason: string | null;
  needs_reply: boolean;
  reply_due_at: Date | null;
  last_inbound_at: Date | null;
  last_outbound_at: Date | null;
  followup_for: Date | null;
  created_at: Date;
}

export interface MessageRow {
  id: number;
  contact_id: number;
  direction: 'in' | 'out';
  source: 'user' | 'comment' | 'funnel' | 'ai' | 'human' | 'system';
  mid: string | null;
  text: string | null;
  payload: unknown;
  created_at: Date;
}

// ---- webhook events -------------------------------------------------------

export async function insertWebhookEvent(sql: Sql, object: string | undefined, payload: unknown): Promise<number> {
  const [row] = await sql<{ id: number }[]>`
    INSERT INTO webhook_events (object, payload) VALUES (${object ?? null}, ${sql.json(payload as any)})
    RETURNING id`;
  return row!.id;
}

export interface WebhookEventRow {
  id: number;
  payload: any;
  attempts: number;
  received_at: Date;
}

/** Claims pending events (or ones whose lease expired) with a 2-minute lease. */
export async function claimWebhookEvents(sql: Sql, limit = 20): Promise<WebhookEventRow[]> {
  return sql<WebhookEventRow[]>`
    UPDATE webhook_events SET status = 'processing', attempts = attempts + 1,
      locked_until = now() + interval '2 minutes'
    WHERE id IN (
      SELECT id FROM webhook_events
      WHERE status = 'pending' OR (status = 'processing' AND locked_until < now())
      ORDER BY id LIMIT ${limit}
      FOR UPDATE SKIP LOCKED)
    RETURNING id, payload, attempts, received_at`;
}

export async function finishWebhookEvent(sql: Sql, id: number, status: 'done' | 'error' | 'pending', error?: string) {
  await sql`
    UPDATE webhook_events SET status = ${status}, processed_at = now(), locked_until = NULL,
      error = ${error ?? null}
    WHERE id = ${id}`;
}

// ---- contacts --------------------------------------------------------------

export async function upsertContact(
  sql: Sql,
  c: { business: string; platform: Platform; externalId: string; username?: string; name?: string; source?: string },
): Promise<Contact> {
  const [row] = await sql<Contact[]>`
    INSERT INTO contacts (business, platform, external_id, username, name, source)
    VALUES (${c.business}, ${c.platform}, ${c.externalId}, ${c.username ?? null}, ${c.name ?? null}, ${c.source ?? null})
    ON CONFLICT (business, platform, external_id) DO UPDATE SET
      username = COALESCE(EXCLUDED.username, contacts.username),
      name = COALESCE(contacts.name, EXCLUDED.name),
      source = COALESCE(contacts.source, EXCLUDED.source),
      updated_at = now()
    RETURNING *`;
  return row!;
}

export async function getContact(sql: Sql, id: number): Promise<Contact | undefined> {
  const [row] = await sql<Contact[]>`SELECT * FROM contacts WHERE id = ${id}`;
  return row;
}

export async function findContact(sql: Sql, business: string, platform: Platform, externalId: string) {
  const [row] = await sql<Contact[]>`
    SELECT * FROM contacts WHERE business = ${business} AND platform = ${platform} AND external_id = ${externalId}`;
  return row;
}

/** Records an inbound message and (optionally) schedules an AI reply after the debounce delay. */
export async function markInbound(sql: Sql, contactId: number, at: Date, replyDueAt: Date | null) {
  await sql`
    UPDATE contacts SET
      last_inbound_at = GREATEST(COALESCE(last_inbound_at, ${at}::timestamptz), ${at}::timestamptz),
      needs_reply = needs_reply OR ${replyDueAt !== null}::boolean,
      reply_due_at = COALESCE(${replyDueAt}::timestamptz, reply_due_at),
      stage = CASE WHEN stage = 'new' THEN 'engaged' ELSE stage END,
      updated_at = now()
    WHERE id = ${contactId}`;
}

export async function markOutbound(sql: Sql, contactId: number, at: Date = new Date()) {
  await sql`UPDATE contacts SET last_outbound_at = ${at}, updated_at = now() WHERE id = ${contactId}`;
}

/** Claims contacts whose debounced reply is due, with a lease so two workers never answer twice. */
export async function claimDueReplies(sql: Sql, limit = 5): Promise<Contact[]> {
  return sql<Contact[]>`
    UPDATE contacts SET reply_lock_until = now() + interval '3 minutes'
    WHERE id IN (
      SELECT id FROM contacts
      WHERE needs_reply AND reply_due_at <= now()
        AND (reply_lock_until IS NULL OR reply_lock_until < now())
      ORDER BY reply_due_at LIMIT ${limit}
      FOR UPDATE SKIP LOCKED)
    RETURNING *`;
}

/** Clears needs_reply unless something new arrived after the run started. */
export async function finishReply(sql: Sql, contactId: number, startedAt: Date) {
  await sql`
    UPDATE contacts SET
      needs_reply = (last_inbound_at > ${startedAt}),
      reply_lock_until = NULL, updated_at = now()
    WHERE id = ${contactId}`;
}

export async function pauseAi(sql: Sql, contactId: number, until: Date, reason: string) {
  await sql`
    UPDATE contacts SET ai_paused_until = ${until}, ai_pause_reason = ${reason}, needs_reply = false, updated_at = now()
    WHERE id = ${contactId}`;
}

export async function resumeAi(sql: Sql, contactId: number) {
  await sql`UPDATE contacts SET ai_paused_until = NULL, ai_pause_reason = NULL, updated_at = now() WHERE id = ${contactId}`;
}

export interface LeadUpdate {
  name?: string | null;
  phone?: string | null;
  email?: string | null;
  interest?: string | null;
  budget?: string | null;
  timeline?: string | null;
  notes?: string | null;
  stage?: Stage | null;
}

export async function updateLead(sql: Sql, contactId: number, u: LeadUpdate) {
  await sql`
    UPDATE contacts SET
      name = COALESCE(${u.name ?? null}, name),
      phone = COALESCE(${u.phone ?? null}, phone),
      email = COALESCE(${u.email ?? null}, email),
      interest = COALESCE(${u.interest ?? null}, interest),
      budget = COALESCE(${u.budget ?? null}, budget),
      timeline = COALESCE(${u.timeline ?? null}, timeline),
      notes = CASE WHEN ${u.notes ?? null}::text IS NULL THEN notes
                   ELSE concat_ws(E'\n', notes, ${u.notes ?? null}::text) END,
      stage = COALESCE(${u.stage ?? null}, stage),
      updated_at = now()
    WHERE id = ${contactId}`;
}

export async function setOptedOut(sql: Sql, contactId: number) {
  await sql`UPDATE contacts SET opted_out = true, needs_reply = false, stage = 'lost', updated_at = now() WHERE id = ${contactId}`;
}

// ---- comments --------------------------------------------------------------

export interface CommentRow {
  business: string;
  platform: Platform;
  comment_id: string;
  post_id?: string;
  parent_id?: string;
  author_id?: string;
  author_name?: string;
  text: string;
  commented_at: Date;
  outcome: 'funnel' | 'ai' | 'skipped';
  skip_reason?: string;
  funnel_id?: string;
}

/** Inserts the comment's ledger row. Returns false when the comment was already recorded. */
export async function insertComment(sql: Sql, c: CommentRow): Promise<boolean> {
  const rows = await sql`
    INSERT INTO comments (business, platform, comment_id, post_id, parent_id, author_id, author_name, text,
      commented_at, outcome, skip_reason, funnel_id)
    VALUES (${c.business}, ${c.platform}, ${c.comment_id}, ${c.post_id ?? null}, ${c.parent_id ?? null},
      ${c.author_id ?? null}, ${c.author_name ?? null}, ${c.text}, ${c.commented_at}, ${c.outcome},
      ${c.skip_reason ?? null}, ${c.funnel_id ?? null})
    ON CONFLICT (platform, comment_id) DO NOTHING
    RETURNING id`;
  return rows.length > 0;
}

export async function updateComment(
  sql: Sql,
  platform: Platform,
  commentId: string,
  u: { outcome?: string; skip_reason?: string | null; ai_intent?: string; ai_decision?: unknown; contact_id?: number },
) {
  await sql`
    UPDATE comments SET
      outcome = COALESCE(${u.outcome ?? null}, outcome),
      skip_reason = CASE WHEN ${u.skip_reason !== undefined}::boolean THEN ${u.skip_reason ?? null} ELSE skip_reason END,
      ai_intent = COALESCE(${u.ai_intent ?? null}, ai_intent),
      ai_decision = COALESCE(${u.ai_decision === undefined ? null : sql.json(u.ai_decision as any)}, ai_decision),
      contact_id = COALESCE(${u.contact_id ?? null}, contact_id)
    WHERE platform = ${platform} AND comment_id = ${commentId}`;
}

// ---- messages --------------------------------------------------------------

export async function insertMessage(
  sql: Sql,
  m: {
    contactId: number;
    direction: 'in' | 'out';
    source: MessageRow['source'];
    mid?: string | null;
    text?: string | null;
    payload?: unknown;
    sendId?: number | null;
    at?: Date;
  },
): Promise<number | undefined> {
  const rows = await sql<{ id: number }[]>`
    INSERT INTO messages (contact_id, direction, source, mid, text, payload, send_id, created_at)
    VALUES (${m.contactId}, ${m.direction}, ${m.source}, ${m.mid ?? null}, ${m.text ?? null},
      ${m.payload === undefined ? null : sql.json(m.payload as any)}, ${m.sendId ?? null}, ${m.at ?? new Date()})
    ON CONFLICT (mid) DO NOTHING
    RETURNING id`;
  return rows[0]?.id;
}

export async function recentMessages(sql: Sql, contactId: number, limit = 40): Promise<MessageRow[]> {
  const rows = await sql<MessageRow[]>`
    SELECT * FROM messages WHERE contact_id = ${contactId} ORDER BY created_at DESC, id DESC LIMIT ${limit}`;
  return rows.reverse();
}

export async function lastInboundMessageId(sql: Sql, contactId: number): Promise<number | undefined> {
  const [row] = await sql<{ id: number }[]>`
    SELECT id FROM messages WHERE contact_id = ${contactId} AND direction = 'in' ORDER BY created_at DESC, id DESC LIMIT 1`;
  return row?.id;
}

// ---- sends (ledger) ---------------------------------------------------------

export interface SendClaim {
  business: string;
  platform: Platform;
  kind: 'private_reply' | 'message' | 'public_reply' | 'hide_comment';
  key: string;
  funnelId?: string;
  step?: string;
  commentId?: string;
  contactId?: number;
  recipientId?: string;
  request?: unknown;
}

/** Claims the idempotency key. Returns undefined if this send was already attempted, ever. */
export async function claimSend(sql: Sql, c: SendClaim): Promise<number | undefined> {
  const rows = await sql<{ id: number }[]>`
    INSERT INTO sends (business, platform, kind, idempotency_key, funnel_id, step, comment_id, contact_id,
      recipient_id, request)
    VALUES (${c.business}, ${c.platform}, ${c.kind}, ${c.key}, ${c.funnelId ?? null}, ${c.step ?? null},
      ${c.commentId ?? null}, ${c.contactId ?? null}, ${c.recipientId ?? null},
      ${c.request === undefined ? null : sql.json(c.request as any)})
    ON CONFLICT (idempotency_key) DO NOTHING
    RETURNING id`;
  return rows[0]?.id;
}

export async function completeSend(
  sql: Sql,
  id: number,
  r: {
    status: 'sent' | 'failed' | 'unknown' | 'dry_run' | 'skipped';
    messageId?: string;
    recipientId?: string;
    contactId?: number;
    errorCode?: number;
    errorSubcode?: number;
    errorMessage?: string;
  },
) {
  await sql`
    UPDATE sends SET status = ${r.status}, message_id = ${r.messageId ?? null},
      recipient_id = COALESCE(${r.recipientId ?? null}, recipient_id),
      contact_id = COALESCE(${r.contactId ?? null}, contact_id),
      error_code = ${r.errorCode ?? null}, error_subcode = ${r.errorSubcode ?? null},
      error_message = ${r.errorMessage ?? null},
      sent_at = CASE WHEN ${r.status} IN ('sent', 'dry_run') THEN now() ELSE NULL END
    WHERE id = ${id}`;
}

export async function isOurMessage(sql: Sql, mid: string): Promise<boolean> {
  const rows = await sql`SELECT 1 FROM sends WHERE message_id = ${mid} LIMIT 1`;
  return rows.length > 0;
}

// Meta's watermark is the timestamp of the last message received/read, on Meta's clock, in ms.
// Our sent_at is stamped after Meta answers, so allow a few seconds of slack.
const WATERMARK_SLACK = "interval '10 seconds'";

/** Facebook delivery receipts. Instagram never sends these. */
export async function markDelivered(sql: Sql, contactId: number, mids: string[], watermark?: Date) {
  if (mids.length) {
    await sql`UPDATE sends SET delivered_at = COALESCE(delivered_at, now())
      WHERE contact_id = ${contactId} AND message_id IN ${sql(mids)}`;
  }
  if (watermark) {
    await sql`UPDATE sends SET delivered_at = COALESCE(delivered_at, ${watermark})
      WHERE contact_id = ${contactId} AND status = 'sent' AND delivered_at IS NULL
        AND sent_at <= ${watermark}::timestamptz + ${sql.unsafe(WATERMARK_SLACK)}`;
  }
}

/** Facebook sends a watermark (everything before it is read); Instagram names the message read. */
export async function markRead(sql: Sql, contactId: number, mids: string[], watermark?: Date) {
  if (watermark) {
    await sql`UPDATE sends SET read_at = COALESCE(read_at, now())
      WHERE contact_id = ${contactId} AND status = 'sent' AND read_at IS NULL
        AND sent_at <= ${watermark}::timestamptz + ${sql.unsafe(WATERMARK_SLACK)}`;
  }
  if (mids.length) {
    await sql`UPDATE sends SET read_at = COALESCE(read_at, now())
      WHERE contact_id = ${contactId} AND status = 'sent' AND read_at IS NULL
        AND sent_at <= (SELECT max(sent_at) FROM sends WHERE contact_id = ${contactId} AND message_id IN ${sql(mids)})`;
  }
}

export async function countRecentSends(
  sql: Sql,
  where: { business: string; kind?: SendClaim['kind']; contactId?: number; step?: string; sinceHours: number },
): Promise<number> {
  const [row] = await sql<{ n: number }[]>`
    SELECT count(*)::int AS n FROM sends
    WHERE business = ${where.business}
      AND created_at > now() - make_interval(hours => ${where.sinceHours})
      AND status IN ('sent', 'dry_run', 'pending', 'unknown')
      ${where.kind ? sql`AND kind = ${where.kind}` : sql``}
      ${where.contactId ? sql`AND contact_id = ${where.contactId}` : sql``}
      ${where.step ? sql`AND step = ${where.step}` : sql``}`;
  return row!.n;
}

// ---- links, taps, ai runs --------------------------------------------------

export async function createLink(
  sql: Sql,
  l: { token: string; business: string; contactId?: number; funnelId?: string; url: string },
) {
  await sql`INSERT INTO links (token, business, contact_id, funnel_id, url)
    VALUES (${l.token}, ${l.business}, ${l.contactId ?? null}, ${l.funnelId ?? null}, ${l.url})`;
}

export async function attachLinkToSend(sql: Sql, token: string, sendId: number) {
  await sql`UPDATE links SET send_id = ${sendId} WHERE token = ${token}`;
}

export async function recordClick(sql: Sql, token: string): Promise<string | undefined> {
  const [row] = await sql<{ url: string }[]>`
    UPDATE links SET clicks = clicks + 1, first_clicked_at = COALESCE(first_clicked_at, now())
    WHERE token = ${token} RETURNING url`;
  return row?.url;
}

export async function recordTap(sql: Sql, t: { business: string; contactId: number; funnelId?: string; payload: string }) {
  await sql`INSERT INTO taps (business, contact_id, funnel_id, payload)
    VALUES (${t.business}, ${t.contactId}, ${t.funnelId ?? null}, ${t.payload})`;
}

export async function recordAiRun(
  sql: Sql,
  r: {
    business: string;
    contactId?: number;
    kind: 'reply' | 'followup' | 'comment';
    model?: string;
    inputTokens?: number;
    outputTokens?: number;
    cacheReadTokens?: number;
    stopReason?: string | null;
    error?: string;
  },
) {
  await sql`INSERT INTO ai_runs (business, contact_id, kind, model, input_tokens, output_tokens, cache_read_tokens,
      stop_reason, error)
    VALUES (${r.business}, ${r.contactId ?? null}, ${r.kind}, ${r.model ?? null}, ${r.inputTokens ?? null},
      ${r.outputTokens ?? null}, ${r.cacheReadTokens ?? null}, ${r.stopReason ?? null}, ${r.error ?? null})`;
}

// ---- alerts -----------------------------------------------------------------

/** True if an alert with this key may fire now (and records that it did). */
export async function claimAlert(sql: Sql, key: string, cooldownMinutes: number): Promise<boolean> {
  const rows = await sql`
    INSERT INTO alerts (key, last_sent_at) VALUES (${key}, now())
    ON CONFLICT (key) DO UPDATE SET last_sent_at = now(), count = alerts.count + 1
      WHERE alerts.last_sent_at < now() - make_interval(mins => ${cooldownMinutes})
    RETURNING key`;
  return rows.length > 0;
}

// ---- business state -----------------------------------------------------------

export async function sendingPausedUntil(sql: Sql, business: string): Promise<Date | undefined> {
  const [row] = await sql<{ sending_paused_until: Date | null }[]>`
    SELECT sending_paused_until FROM business_state WHERE business = ${business} AND sending_paused_until > now()`;
  return row?.sending_paused_until ?? undefined;
}

export async function pauseSending(sql: Sql, business: string, until: Date, reason: string) {
  await sql`
    INSERT INTO business_state (business, sending_paused_until, paused_reason) VALUES (${business}, ${until}, ${reason})
    ON CONFLICT (business) DO UPDATE SET sending_paused_until = EXCLUDED.sending_paused_until,
      paused_reason = EXCLUDED.paused_reason, updated_at = now()`;
}

export async function linkSendToContact(sql: Sql, sendId: number, contactId: number) {
  await sql`UPDATE sends SET contact_id = ${contactId} WHERE id = ${sendId}`;
}

export async function sendExists(sql: Sql, key: string): Promise<boolean> {
  const rows = await sql`SELECT 1 FROM sends WHERE idempotency_key = ${key}`;
  return rows.length > 0;
}

export async function setFollows(sql: Sql, contactId: number, follows: boolean) {
  await sql`UPDATE contacts SET follows_business = ${follows}, updated_at = now() WHERE id = ${contactId}`;
}

export async function setProfile(sql: Sql, contactId: number, p: { username?: string; name?: string }) {
  await sql`UPDATE contacts SET username = COALESCE(${p.username ?? null}, username),
    name = COALESCE(name, ${p.name ?? null}), updated_at = now() WHERE id = ${contactId}`;
}

export async function setFollowupFor(sql: Sql, contactId: number, at: Date) {
  await sql`UPDATE contacts SET followup_for = ${at}, reply_lock_until = NULL WHERE id = ${contactId}`;
}

export async function clearOptOut(sql: Sql, contactId: number) {
  await sql`UPDATE contacts SET opted_out = false, stage = 'engaged', updated_at = now() WHERE id = ${contactId}`;
}

export async function retryWebhookEvent(sql: Sql, id: number, delaySeconds: number, error: string) {
  await sql`
    UPDATE webhook_events SET status = 'processing', error = ${error},
      locked_until = now() + make_interval(secs => ${delaySeconds})
    WHERE id = ${id}`;
}
