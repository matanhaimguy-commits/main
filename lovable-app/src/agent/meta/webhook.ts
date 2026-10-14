import { createHmac, timingSafeEqual } from 'node:crypto';
import type { Platform } from '../config/schema';

/** Checks X-Hub-Signature-256 ("sha256=<hex>") against the raw request bytes. */
export function verifySignature(rawBody: Uint8Array | string, header: string | undefined | null, appSecret: string): boolean {
  if (!header || !header.startsWith('sha256=')) return false;
  const given = header.slice('sha256='.length);
  const expected = createHmac('sha256', appSecret).update(rawBody).digest('hex');
  if (given.length !== expected.length || !/^[0-9a-f]+$/i.test(given)) return false;
  return timingSafeEqual(Buffer.from(given, 'hex'), Buffer.from(expected, 'hex'));
}

export function sign(rawBody: string, appSecret: string): string {
  return `sha256=${createHmac('sha256', appSecret).update(rawBody).digest('hex')}`;
}

/** GET verification handshake. Returns the challenge to echo, or undefined to reject. */
export function verifyHandshake(query: Record<string, string | undefined>, verifyToken: string): string | undefined {
  if (query['hub.mode'] !== 'subscribe') return undefined;
  if (!query['hub.verify_token'] || query['hub.verify_token'] !== verifyToken) return undefined;
  return query['hub.challenge'];
}

export interface CommentEvent {
  type: 'comment';
  platform: Platform;
  accountId: string; // Page ID or Instagram account ID the webhook was delivered for
  commentId: string;
  postId?: string;
  parentId?: string;
  authorId?: string;
  authorName?: string;
  text: string;
  createdAt: Date;
  verb: string; // add | edited | remove | hide ...
  mediaProductType?: string; // FEED | REELS | AD | STORY ...
}

export interface MessageEvent {
  type: 'message';
  platform: Platform;
  accountId: string;
  senderId: string;
  recipientId: string;
  mid: string;
  text?: string;
  quickReplyPayload?: string;
  attachments: { type: string; url?: string }[];
  storyReply?: { id?: string; url?: string };
  isEcho: boolean;
  appId?: string;
  isDeleted: boolean;
  // Delivered under entry.standby: another app (e.g. ManyChat) owns this thread right now.
  standby: boolean;
  timestamp: Date;
}

export interface PostbackEvent {
  type: 'postback';
  platform: Platform;
  accountId: string;
  senderId: string;
  payload: string;
  title?: string;
  mid?: string;
  timestamp: Date;
}

export interface ReceiptEvent {
  type: 'delivery' | 'read';
  platform: Platform;
  accountId: string;
  senderId: string; // the person who read / received
  watermark?: Date;
  mids: string[];
}

export type MetaEvent = CommentEvent | MessageEvent | PostbackEvent | ReceiptEvent;

type Json = Record<string, any>;

const str = (v: unknown): string | undefined => (v === undefined || v === null || v === '' ? undefined : String(v));

function toDate(v: unknown, fallback: Date): Date {
  if (typeof v === 'number') return new Date(v < 1e12 ? v * 1000 : v); // seconds or ms
  if (typeof v === 'string' && v) {
    const n = Number(v);
    if (!Number.isNaN(n)) return toDate(n, fallback);
    const d = new Date(v.replace(/\+0000$/, 'Z'));
    if (!Number.isNaN(d.getTime())) return d;
  }
  return fallback;
}

/**
 * Turns one webhook POST body into flat events. Unknown shapes are dropped here
 * (the raw payload is already stored, so nothing is lost).
 */
export function parseWebhook(body: Json, now: Date = new Date()): MetaEvent[] {
  const platform: Platform | undefined =
    body?.object === 'page' ? 'facebook' : body?.object === 'instagram' ? 'instagram' : undefined;
  if (!platform || !Array.isArray(body.entry)) return [];

  const events: MetaEvent[] = [];
  for (const entry of body.entry as Json[]) {
    const accountId = str(entry.id);
    if (!accountId) continue;
    const entryTime = toDate(entry.time, now);

    for (const change of (entry.changes ?? []) as Json[]) {
      const v = (change.value ?? {}) as Json;
      if (platform === 'facebook' && change.field === 'feed' && v.item === 'comment') {
        const commentId = str(v.comment_id);
        if (!commentId) continue;
        events.push({
          type: 'comment',
          platform,
          accountId,
          commentId,
          postId: str(v.post_id),
          parentId: str(v.parent_id),
          authorId: str(v.from?.id),
          authorName: str(v.from?.name),
          text: String(v.message ?? ''),
          createdAt: toDate(v.created_time, entryTime),
          verb: String(v.verb ?? 'add'),
        });
      } else if (platform === 'instagram' && (change.field === 'comments' || change.field === 'live_comments')) {
        // Facebook-Login deliveries have been seen with comment_id instead of id.
        const commentId = str(v.id ?? v.comment_id);
        if (!commentId) continue;
        events.push({
          type: 'comment',
          platform,
          accountId,
          commentId,
          postId: str(v.media?.id),
          parentId: str(v.parent_id),
          authorId: str(v.from?.id),
          authorName: str(v.from?.username),
          text: String(v.text ?? ''),
          createdAt: toDate(v.timestamp ?? v.created_time, entryTime),
          verb: 'add',
          mediaProductType: str(v.media?.media_product_type),
        });
      }
    }

    const messaging = [
      ...((entry.messaging ?? []) as Json[]).map((m) => ({ m, standby: false })),
      ...((entry.standby ?? []) as Json[]).map((m) => ({ m, standby: true })),
    ];
    for (const { m, standby } of messaging) {
      const senderId = str(m.sender?.id);
      const recipientId = str(m.recipient?.id);
      const timestamp = toDate(m.timestamp, entryTime);
      if (!senderId) continue;

      if (m.message) {
        const msg = m.message as Json;
        const mid = str(msg.mid);
        if (!mid) continue;
        const story = msg.reply_to?.story as Json | undefined;
        events.push({
          type: 'message',
          platform,
          accountId,
          senderId,
          recipientId: recipientId ?? accountId,
          mid,
          text: str(msg.text),
          quickReplyPayload: str(msg.quick_reply?.payload),
          attachments: ((msg.attachments ?? []) as Json[]).map((a) => ({
            type: String(a.type ?? 'unknown'),
            url: str(a.payload?.url),
          })),
          storyReply: story ? { id: str(story.id), url: str(story.url) } : undefined,
          isEcho: msg.is_echo === true,
          appId: str(msg.app_id),
          isDeleted: msg.is_deleted === true,
          standby,
          timestamp,
        });
      } else if (m.postback && !standby) {
        const pb = m.postback as Json;
        events.push({
          type: 'postback',
          platform,
          accountId,
          senderId,
          payload: String(pb.payload ?? ''),
          title: str(pb.title),
          mid: str(pb.mid),
          timestamp,
        });
      } else if (m.delivery) {
        events.push({
          type: 'delivery',
          platform,
          accountId,
          senderId,
          watermark: m.delivery.watermark ? toDate(m.delivery.watermark, timestamp) : undefined,
          mids: ((m.delivery.mids ?? []) as unknown[]).map(String),
        });
      } else if (m.read) {
        events.push({
          type: 'read',
          platform,
          accountId,
          senderId,
          watermark: m.read.watermark ? toDate(m.read.watermark, timestamp) : undefined,
          mids: m.read.mid ? [String(m.read.mid)] : [],
        });
      }
    }
  }
  return events;
}
