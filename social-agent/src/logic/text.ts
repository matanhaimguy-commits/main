export type MatchMode = 'exact' | 'word' | 'contains';

const HEBREW_MARKS = /[֑-ׇ]/g; // niqqud and cantillation
const INVISIBLES = /[​-‏‪-‮⁦-⁩﻿]/g; // zero-width and bidi controls
const IN_WORD_QUOTES = /['’`׳״"]/g; // apostrophes and geresh/gershayim inside words (צ׳יפס, ת״א)

/** Lowercases, strips marks, emoji and punctuation, and collapses whitespace. */
export function normalize(text: string): string {
  return text
    .normalize('NFKC')
    .toLowerCase()
    .replace(HEBREW_MARKS, '')
    .replace(INVISIBLES, '')
    .replace(IN_WORD_QUOTES, '')
    .replace(/[^\p{L}\p{N}]+/gu, ' ')
    .trim();
}

const HEBREW = /\p{Script=Hebrew}/u;
// One-letter Hebrew prefixes (and, the, in, to, from, that, as) can stack: "ולמדריך".
const HEBREW_PREFIXES = /^[והבלמשכ]{1,3}$/;

function tokenMatches(token: string, keywordToken: string, allowPrefix: boolean): boolean {
  if (token === keywordToken) return true;
  if (!allowPrefix || !token.endsWith(keywordToken)) return false;
  return HEBREW_PREFIXES.test(token.slice(0, token.length - keywordToken.length));
}

/**
 * exact:    the whole comment is the keyword (emoji and punctuation ignored).
 * word:     the keyword appears as whole word(s). Hebrew keywords also match with
 *           attached prefixes (מדריך matches למדריך / והמדריך).
 * contains: the keyword appears anywhere, even inside another word. Risky for short keywords.
 */
export function matchesKeyword(text: string, keyword: string, mode: MatchMode): boolean {
  const t = normalize(text);
  const k = normalize(keyword);
  if (!k) return false;
  if (mode === 'exact') return t === k;
  if (mode === 'contains') return t.includes(k);

  const tokens = t.split(' ');
  const kTokens = k.split(' ');
  const allowPrefix = HEBREW.test(kTokens[0]!);
  for (let i = 0; i + kTokens.length <= tokens.length; i++) {
    if (!tokenMatches(tokens[i]!, kTokens[0]!, allowPrefix)) continue;
    let all = true;
    for (let j = 1; j < kTokens.length; j++) {
      if (tokens[i + j] !== kTokens[j]) {
        all = false;
        break;
      }
    }
    if (all) return true;
  }
  return false;
}

export function matchesAny(text: string, keywords: readonly string[], mode: MatchMode): string | undefined {
  return keywords.find((k) => matchesKeyword(text, k, mode));
}

/** Deterministic pick from a list (same comment always gets the same variant). */
export function pickVariant<T>(items: readonly T[], seed: string): T | undefined {
  if (items.length === 0) return undefined;
  let h = 0;
  for (const ch of seed) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return items[h % items.length];
}
