import type { Business } from '../config/schema';
import type { CommentEvent } from '../meta/webhook';
import type { SkipReason } from './funnels';
import { normalize } from './text';

// Meta lets you send a private reply up to 7 days after the comment.
export const PRIVATE_REPLY_WINDOW_MS = 7 * 24 * 60 * 60 * 1000;

export function isOwnAccount(business: Business, userId: string | undefined): boolean {
  return !!userId && (userId === business.meta.page_id || userId === business.meta.instagram_id);
}

/**
 * On Facebook every comment has a parent_id, and for a top-level comment it equals the
 * post_id. Treating "has a parent" as "is a reply" silently drops every real comment.
 * On Instagram, parent_id is only present on replies.
 */
export function isReply(ev: Pick<CommentEvent, 'platform' | 'parentId' | 'postId'>): boolean {
  if (!ev.parentId) return false;
  if (ev.platform === 'facebook') return ev.parentId !== ev.postId;
  return true;
}

/** Returns why a comment should be skipped before funnel matching, or undefined if it is eligible. */
export function screenComment(ev: CommentEvent, business: Business, now: Date = new Date()): SkipReason | undefined {
  if (ev.verb !== 'add') return 'not_new';
  // Our own public replies fire the comment webhook too. Skipping them stops a DM loop.
  if (isOwnAccount(business, ev.authorId)) return 'own_comment';
  if (isReply(ev) && !business.comments.include_replies) return 'is_reply';
  if (!normalize(ev.text)) return 'no_text';
  if (now.getTime() - ev.createdAt.getTime() > PRIVATE_REPLY_WINDOW_MS) return 'outside_reply_window';
  return undefined;
}

/** While a business has testers, only they get automated messages. */
export function isAllowedRecipient(business: Business, ids: { id?: string; username?: string }): boolean {
  if (business.testers.length === 0) return true;
  const wanted = new Set(business.testers.map((t) => t.replace(/^@/, '').toLowerCase()));
  return (
    (!!ids.id && wanted.has(ids.id.toLowerCase())) ||
    (!!ids.username && wanted.has(ids.username.replace(/^@/, '').toLowerCase()))
  );
}
