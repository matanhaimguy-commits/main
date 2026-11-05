/** How each kind of block starts. */

export const FENCE = /^\s{0,3}(`{3,}|~{3,})\s*([\w+-]*)/;
export const HEADING = /^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$/;
export const HR = /^\s{0,3}([-*_])(\s*\1){2,}\s*$/;
export const QUOTE = /^\s{0,3}>\s?/;
export const LIST_ITEM = /^(\s*)([-*+]|(\d{1,9})[.)])\s+(.*)$/;
export const TABLE_SEP = /^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$/;

export const isBlank = (s: string) => s.trim() === "";

/** A pipe table: a row with a pipe, then a separator row of dashes. */
export function startsTable(lines: string[], i: number): boolean {
  const sep = lines[i + 1] ?? "";
  return (lines[i] ?? "").includes("|") && sep.includes("-") && TABLE_SEP.test(sep);
}

/** Whether line i opens a block other than a paragraph. */
export function startsBlock(lines: string[], i: number): boolean {
  const line = lines[i]!;
  return FENCE.test(line) || HEADING.test(line) || HR.test(line) || QUOTE.test(line) || LIST_ITEM.test(line) || startsTable(lines, i);
}
