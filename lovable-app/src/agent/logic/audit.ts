import type { Business } from '../config/schema';
import { auditFunnels } from './audit-funnels';
import type { Issue } from './audit-types';

// The pieces live in their own files; both are still importable from here.
export { riskyMatches } from './risky-keywords';
export type { Issue };

// Link shorteners get DMs flagged as spam. Send the real URL.
const SHORTENERS = [
  'bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly', 'is.gd', 'buff.ly', 'cutt.ly', 'rebrand.ly',
  'shorturl.at', 'lnkd.in', 'tiny.cc', 'rb.gy', 'shorte.st', 'bl.ink', 'short.io', 'tny.im', 'v.gd',
];

const PLACEHOLDER = /\bTODO|REPLACE[_ ]?ME|CHANGE[_ ]?ME|YOUR[_ ]LINK|<[^<>\n]{1,40}>|\bexample\.(com|org|net)\b/i;

function allStrings(value: unknown, path = ''): { path: string; text: string }[] {
  if (typeof value === 'string') return [{ path, text: value }];
  if (Array.isArray(value)) return value.flatMap((v, i) => allStrings(v, `${path}[${i}]`));
  if (value && typeof value === 'object') {
    return Object.entries(value).flatMap(([k, v]) => allStrings(v, path ? `${path}.${k}` : k));
  }
  return [];
}

export function hasPlaceholders(business: Business): string[] {
  return allStrings(business)
    .filter((s) => PLACEHOLDER.test(s.text))
    .map((s) => s.path);
}

function shortenerIn(text: string): string | undefined {
  const lower = text.toLowerCase();
  return SHORTENERS.find((d) => new RegExp(`(^|[^a-z0-9.])${d.replace('.', '\\.')}(/|$|\\s)`).test(lower));
}

/**
 * Safety audit. Errors block live sending for that business; warnings are printed.
 * Run it after every config change, not only at setup.
 */
export function auditBusiness(b: Business, ctx: { hasToken: boolean }): Issue[] {
  const issues: Issue[] = [];
  const add = (level: Issue['level'], message: string, where?: string) =>
    issues.push({ level, business: b.slug, where, message });

  for (const [field, value] of [['page_id', b.meta.page_id], ['instagram_id', b.meta.instagram_id]] as const) {
    if (value !== undefined && !/^\d+$/.test(value)) add('error', `meta.${field} must be the numeric ID, got "${value}"`);
  }
  if (!b.meta.page_id) {
    add(b.live ? 'error' : 'warn', 'not connected to a Facebook Page yet: choose this business on the Connect page');
  } else if (!ctx.hasToken) {
    add(
      b.live ? 'error' : 'warn',
      b.meta.page_token_env
        ? `env var ${b.meta.page_token_env} (this Page's access token) is not set`
        : 'no access token for this Page: connect it again on the Connect page',
    );
  }
  if (b.meta.page_id && !b.meta.instagram_id) add('warn', 'no Instagram account linked to this Page; Instagram is off');
  for (const path of hasPlaceholders(b)) add('error', `placeholder text still in config`, path);
  if (b.live && b.testers.length === 0) add('warn', 'live for everyone (no testers list). Make sure a stranger test passed first.');
  if (b.ai.enabled && b.profile.about.trim().length < 40) {
    add('warn', 'profile.about is very short; the AI can only sell what you describe');
  }

  const linkIds = new Set<string>();
  for (const link of b.links) {
    if (linkIds.has(link.id)) add('error', `duplicate link id "${link.id}"`, `links.${link.id}`);
    linkIds.add(link.id);
    if (!link.url.startsWith('https://')) add('warn', 'link is not https', `links.${link.id}`);
  }
  for (const s of allStrings({ links: b.links, funnels: b.funnels })) {
    const shortener = shortenerIn(s.text);
    if (shortener) add('error', `link shortener ${shortener} in a message gets DMs flagged as spam; use the full URL`, s.path);
  }

  auditFunnels(b, linkIds, add);
  return issues;
}

export function blocksLive(issues: Issue[]): boolean {
  return issues.some((i) => i.level === 'error');
}
