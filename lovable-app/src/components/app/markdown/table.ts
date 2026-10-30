import { isBlank } from "./patterns";
import type { Align, Block, Read } from "./types";

/** Splits a table row on pipes that are neither escaped nor inside inline code. */
export function splitRow(line: string): string[] {
  let s = line.trim();
  if (s.startsWith("|")) s = s.slice(1);
  if (s.endsWith("|") && !s.endsWith("\\|")) s = s.slice(0, -1);
  const cells: string[] = [];
  let cur = "";
  let inCode = false;
  for (let i = 0; i < s.length; i++) {
    const ch = s[i]!;
    if (ch === "\\" && s[i + 1] === "|") {
      cur += "|";
      i++;
    } else if (ch === "`") {
      inCode = !inCode;
      cur += ch;
    } else if (ch === "|" && !inCode) {
      cells.push(cur.trim());
      cur = "";
    } else cur += ch;
  }
  cells.push(cur.trim());
  return cells;
}

const alignOf = (c: string): Align =>
  c.startsWith(":") && c.endsWith(":") ? "center" : c.endsWith(":") ? "right" : c.startsWith(":") ? "left" : null;

/** A pipe table starting at line i (the caller checked startsTable). */
export function readTable(lines: string[], i: number): Read<Extract<Block, { t: "table" }>> {
  const head = splitRow(lines[i]!);
  const align = splitRow(lines[i + 1]!).map(alignOf);
  const rows: string[][] = [];
  let j = i + 2;
  while (j < lines.length && !isBlank(lines[j]!) && lines[j]!.includes("|")) rows.push(splitRow(lines[j++]!));
  return { block: { t: "table", head, rows, align }, next: j };
}
