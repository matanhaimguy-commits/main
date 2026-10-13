import type { Funnel, Platform } from '../config/schema.js';
import { matchesAny } from './text.js';

export type SkipReason =
  | 'own_comment'
  | 'is_reply'
  | 'no_text'
  | 'not_new'
  | 'outside_reply_window'
  | 'no_funnel_for_post'
  | 'keyword_not_matched'
  | 'funnel_paused'
  | 'not_a_tester'
  | 'business_disabled'
  | 'already_handled';

export type FunnelDecision =
  | { kind: 'matched'; funnel: Funnel; keyword: string }
  | { kind: 'skipped'; reason: SkipReason; funnel?: Funnel; detail?: string };

/**
 * Decides which ONE funnel owns a comment, before any API call: Meta allows one private
 * reply per comment, ever, across every app.
 *
 * - Funnels pinned to this post win. If any exist, account-wide funnels stay silent on it.
 * - Among candidates, the first funnel in config order whose keyword matches owns it.
 * - If that owner is paused, the comment is skipped. It never falls through to another funnel.
 */
export function selectCommentFunnel(
  funnels: readonly Funnel[],
  ctx: { platform: Platform; postId: string | undefined; text: string },
): FunnelDecision {
  const candidates = funnels.filter((f) => f.trigger === 'comment' && f.platforms.includes(ctx.platform));
  const pinned = ctx.postId ? candidates.filter((f) => f.posts.includes(ctx.postId!)) : [];
  const scope = pinned.length > 0 ? pinned : candidates.filter((f) => f.all_posts);
  if (scope.length === 0) return { kind: 'skipped', reason: 'no_funnel_for_post' };
  return pickOwner(scope, ctx.text);
}

/** Story replies and DM keywords have no post to pin to, so their funnels are account-wide. */
export function selectMessageFunnel(
  funnels: readonly Funnel[],
  ctx: { platform: Platform; trigger: 'story_reply' | 'dm_keyword'; text: string },
): FunnelDecision {
  const scope = funnels.filter((f) => f.trigger === ctx.trigger && f.platforms.includes(ctx.platform));
  if (scope.length === 0) return { kind: 'skipped', reason: 'no_funnel_for_post' };
  return pickOwner(scope, ctx.text);
}

function pickOwner(scope: readonly Funnel[], text: string): FunnelDecision {
  for (const funnel of scope) {
    const keyword = matchesAny(text, funnel.keywords, funnel.match);
    if (keyword === undefined) continue;
    if (funnel.status === 'paused') return { kind: 'skipped', reason: 'funnel_paused', funnel };
    return { kind: 'matched', funnel, keyword };
  }
  return { kind: 'skipped', reason: 'keyword_not_matched' };
}

export function findFunnel(funnels: readonly Funnel[], id: string): Funnel | undefined {
  return funnels.find((f) => f.id === id);
}

// Postback payloads carry the funnel and the step to run when the button is tapped.
export type FunnelPayload = { funnelId: string; step: 'deliver' | 'gate' };

export function encodePayload(p: FunnelPayload): string {
  return `F|${p.funnelId}|${p.step}`;
}

export function decodePayload(payload: string | undefined): FunnelPayload | undefined {
  const parts = payload?.split('|');
  if (!parts || parts.length !== 3 || parts[0] !== 'F') return undefined;
  const step = parts[2];
  if (step !== 'deliver' && step !== 'gate') return undefined;
  return { funnelId: parts[1]!, step };
}
