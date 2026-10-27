import { safeHref } from "./safe-href";
import type { Inline } from "./types";

const BARE_URL = /^https?:\/\/[^\s<>()]*[^\s<>().,;:!?'"*_]/;
const PUNCT = /[\\`*_{}[\]()#+\-.!|>~]/;

const isWordChar = (ch: string | undefined) => !!ch && /[\p{L}\p{N}]/u.test(ch);
const isSpace = (ch: string | undefined) => ch === undefined || /\s/.test(ch);

function pushText(out: Inline[], v: string) {
  const last = out[out.length - 1];
  if (last?.t === "text") last.v += v;
  else out.push({ t: "text", v });
}

/** The index of the delimiter that closes emphasis opened just before `from`, or -1. */
function closing(s: string, delim: string, from: number): number {
  for (let j = from; j <= s.length - delim.length; j++) {
    if (s[j] === "\\") {
      j++;
      continue;
    }
    if (s[j] === "`") {
      const end = s.indexOf("`", j + 1);
      if (end < 0) return -1;
      j = end;
      continue;
    }
    if (!s.startsWith(delim, j) || j === from || isSpace(s[j - 1])) continue;
    if (delim[0] === "_" && isWordChar(s[j + delim.length])) continue;
    if (delim === "*" && s[j + 1] === "*") {
      j++;
      continue;
    }
    return j;
  }
  return -1;
}

/** Emphasis can open here: not before a space, and `_` not inside a word (snake_case stays as it is). */
const opens = (s: string, i: number, width: number) =>
  !isSpace(s[i + width]) && !(s[i] === "_" && isWordChar(s[i - 1]));

/** Inline markdown: `code`, **bold**, *italic*, [links](https://...) and bare https:// links. */
export function parseInline(s: string): Inline[] {
  const out: Inline[] = [];
  let i = 0;
  while (i < s.length) {
    const ch = s[i]!;
    if (ch === "\\" && PUNCT.test(s[i + 1] ?? "")) {
      pushText(out, s[i + 1]!);
      i += 2;
      continue;
    }
    if (ch === "`") {
      let n = 1;
      while (s[i + n] === "`") n++;
      const end = s.indexOf("`".repeat(n), i + n);
      if (end > i) {
        out.push({ t: "code", v: s.slice(i + n, end).trim() });
        i = end + n;
        continue;
      }
    }
    if ((ch === "*" || ch === "_") && s[i + 1] === ch && opens(s, i, 2)) {
      const end = closing(s, ch + ch, i + 2);
      if (end > 0) {
        out.push({ t: "b", c: parseInline(s.slice(i + 2, end)) });
        i = end + 2;
        continue;
      }
    }
    if ((ch === "*" || ch === "_") && s[i + 1] !== ch && opens(s, i, 1)) {
      const end = closing(s, ch, i + 1);
      if (end > 0) {
        out.push({ t: "i", c: parseInline(s.slice(i + 1, end)) });
        i = end + 1;
        continue;
      }
    }
    if (ch === "[") {
      const close = s.indexOf("](", i + 1);
      const end = close > 0 ? s.indexOf(")", close + 2) : -1;
      if (close > 0 && end > 0 && !s.slice(i + 1, close).includes("]")) {
        out.push({ t: "a", href: safeHref(s.slice(close + 2, end)), c: parseInline(s.slice(i + 1, close)) });
        i = end + 1;
        continue;
      }
    }
    if ((ch === "h" || ch === "H") && !isWordChar(s[i - 1])) {
      const m = s.slice(i).match(BARE_URL);
      if (m) {
        out.push({ t: "a", href: m[0], c: [{ t: "text", v: m[0] }] });
        i += m[0].length;
        continue;
      }
    }
    pushText(out, ch);
    i++;
  }
  return out;
}
