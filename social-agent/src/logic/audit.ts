import type { Business, Funnel } from '../config/schema.js';
import { matchesKeyword, normalize } from './text.js';
import { fitsLimit } from '../meta/messages.js';

export interface Issue {
  level: 'error' | 'warn';
  business: string;
  where?: string;
  message: string;
}

// Link shorteners get DMs flagged as spam. Send the real URL.
const SHORTENERS = [
  'bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly', 'is.gd', 'buff.ly', 'cutt.ly', 'rebrand.ly',
  'shorturl.at', 'lnkd.in', 'tiny.cc', 'rb.gy', 'shorte.st', 'bl.ink', 'short.io', 'tny.im', 'v.gd',
];

const PLACEHOLDER = /\bTODO|REPLACE[_ ]?ME|CHANGE[_ ]?ME|YOUR[_ ]LINK|<[^<>\n]{1,40}>|\bexample\.(com|org|net)\b/i;

// Ordinary words that show up in comments. Used to show what a risky keyword would catch.
const COMMON_WORDS = (
  'about above across after again against agent ago agree ahead almost alone along already also although always ' +
  'amazing among another answer anyone anything appreciate area around article artist awesome back beautiful ' +
  'because before begin behind believe best better between beyond birthday book bought brand bring broken brother ' +
  'business busy came cancel cannot care catch change cheap check child choose class clean close code color come ' +
  'comment company content cool could course cover crazy create custom daily dark dear deal details different ' +
  'dinner discount done download dream drive early easy enough even event every everyone exactly expensive family ' +
  'feeling find fine first follow follower food free friend from front full funny game gift girl give glad going ' +
  'good great group guide guidelines guided misguided guy hair happy hard have hello help here hope house idea ' +
  'important inspire inspiring interest job join just keep kind know last later learn less life like link live ' +
  'love lovely made make many message mind money month more morning much music need never news next nice night ' +
  'nothing offer only open order other page people perfect phone photo place plan please post price product ' +
  'question quick ready real really reason recipe reply right same save send share shop show sign since site ' +
  'some something soon sorry start still story style sure take team thank thanks that there thing think this ' +
  'time today together tomorrow tried true trying update video wait want watch week what when where which while ' +
  'with without women wonderful work world would wow yes yesterday young ' +
  'מדריך מדריכה הדרכה שלום תודה רבה מה קורה איך כמה עולה מחיר מחירים אפשר פרטים בבקשה מעולה מדהים יפה אהבתי ' +
  'רוצה צריך צריכה שולחת שולח הודעה הודעות פרטי בפרטי לינק קישור קבוצה קורס סדנה וובינר מתנה חינם הנחה מבצע ' +
  'משלוח הזמנה הזמנתי לקוח לקוחה עסק עסקים שיווק פרסום ממומן קמפיין תוכן סרטון ריל רילס סטורי פוסט עוקבים ' +
  'אינסטגרם פייסבוק טיקטוק וואטסאפ טלפון מייל אתר חנות מוצר שירות פגישה שיחה ייעוץ זמן היום מחר אתמול בוקר ערב ' +
  'לילה שבוע חודש שנה תמיד אף פעם כן לא אולי ממש מאוד יותר פחות הכי גם רק עוד כבר עכשיו אחר כך אחרי לפני ' +
  'משפחה חבר חברה ילדים בית אוכל מתכון עוגה ספר ספרים שיר מוזיקה בגדים שמלה נעליים תיק צבע גודל מידה'
).split(/\s+/);

export function riskyMatches(keyword: string, mode: Funnel['match']): string[] {
  if (mode === 'exact') return [];
  const k = normalize(keyword);
  return COMMON_WORDS.filter((w) => w !== k && matchesKeyword(w, keyword, mode)).slice(0, 6);
}

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
export function auditBusiness(b: Business, env: Record<string, string | undefined> = {}): Issue[] {
  const issues: Issue[] = [];
  const add = (level: Issue['level'], message: string, where?: string) =>
    issues.push({ level, business: b.slug, where, message });

  for (const [field, value] of [['page_id', b.meta.page_id], ['instagram_id', b.meta.instagram_id]] as const) {
    if (value !== undefined && !/^\d+$/.test(value)) add('error', `meta.${field} must be the numeric ID, got "${value}"`);
  }
  if (!env[b.meta.page_token_env]) {
    add(b.live ? 'error' : 'warn', `env var ${b.meta.page_token_env} (this Page's access token) is not set`);
  }
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
  return issues;
}

export function blocksLive(issues: Issue[]): boolean {
  return issues.some((i) => i.level === 'error');
}
