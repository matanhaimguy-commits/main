import type { Business } from '../config/schema';
import { fitsLimit } from '../meta/messages';
import type { AddIssue } from './audit-types';
import { riskyMatches } from './risky-keywords';
import { normalize } from './text';

/**
 * The funnel part of the safety audit: pinning, keywords, the delivery link, message sizes,
 * the follow gate, the wait before the last message, and keywords shared between funnels.
 */
export function auditFunnels(b: Business, linkIds: ReadonlySet<string>, add: AddIssue): void {
  const funnelIds = new Set<string>();
  for (const f of b.funnels) {
    const where = `funnels.${f.id}`;
    if (funnelIds.has(f.id)) add('error', `duplicate funnel id "${f.id}"`, where);
    funnelIds.add(f.id);

    if (f.trigger === 'comment') {
      if (f.posts.length === 0 && !f.all_posts) {
        add('error', 'comment funnel is not pinned to any post. Add post IDs to `posts` (see `npm run cli -- meta:posts`).', where);
      }
      if (f.all_posts && !f.all_posts_acknowledged) {
        add(
          'error',
          'all_posts funnel catches comments on every post, including ones from years ago. Pin it to posts, or set all_posts_acknowledged: true.',
          where,
        );
      }
      if (f.posts.length > 0 && f.all_posts) add('warn', 'has both posts and all_posts; it is account-wide', where);
    } else if (f.posts.length > 0) {
      add('warn', `${f.trigger} funnels are account-wide; the posts list is ignored`, where);
    }

    for (const kw of f.keywords) {
      const k = normalize(kw);
      if (!k) {
        add('error', `keyword "${kw}" is empty after removing emoji and punctuation`, where);
        continue;
      }
      const len = [...k.replace(/ /g, '')].length;
      if (f.match === 'contains' && len < 5) {
        add('error', `keyword "${kw}" is too short for match: contains (it matches inside other words). Use match: word.`, where);
      } else if (f.match !== 'exact' && len < 3) {
        add('error', `keyword "${kw}" is too short; it will catch ordinary comments. Use match: exact or a longer word.`, where);
      }
      const caught = riskyMatches(kw, f.match);
      if (caught.length > 0) {
        add(
          f.match === 'contains' ? 'error' : 'warn',
          `keyword "${kw}" (${f.match}) would also fire on ordinary words: ${caught.join(', ')}`,
          where,
        );
      }
    }

    if (!/^https?:\/\//.test(f.deliver.link) && !linkIds.has(f.deliver.link)) {
      add('error', `deliver.link "${f.deliver.link}" is not a URL and not a link id from links`, where);
    }
    if (f.after && f.platforms.includes('instagram') && !fitsLimit(f.after, 'instagram', false)) {
      add('error', 'after is longer than Instagram allows (1000 bytes; Hebrew letters count double)', where);
    }
    if (f.after_delay_minutes > 0 && !f.after) {
      add('warn', 'after_delay_minutes is set but the funnel has no last message (after) to delay', where);
    }
    if (f.follow_gate?.enabled && !f.platforms.includes('instagram')) {
      add('warn', 'follow_gate only works on Instagram; ignored here', where);
    }
    if (f.follow_gate?.enabled && f.opener.mode === 'link') {
      add('error', 'follow_gate needs opener.mode: tap (the gate runs when the button is tapped)', where);
    }
  }

  // Two funnels in the same scope sharing a keyword: only the first one ever fires.
  for (let i = 0; i < b.funnels.length; i++) {
    for (let j = i + 1; j < b.funnels.length; j++) {
      const a = b.funnels[i]!;
      const c = b.funnels[j]!;
      if (a.trigger !== c.trigger || !a.platforms.some((p) => c.platforms.includes(p))) continue;
      const sameScope =
        a.trigger !== 'comment' || (a.all_posts && c.all_posts) || a.posts.some((p) => c.posts.includes(p));
      if (!sameScope) continue;
      const shared = a.keywords.filter((k) => c.keywords.some((k2) => normalize(k) === normalize(k2)));
      if (shared.length > 0) {
        add('warn', `shares keyword(s) ${shared.join(', ')} with "${a.id}" in the same scope; "${a.id}" always wins`, `funnels.${c.id}`);
      }
    }
  }
}
