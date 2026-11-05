import { readList } from "./list";
import { FENCE, HEADING, HR, isBlank, LIST_ITEM, QUOTE, startsBlock, startsTable } from "./patterns";
import { readTable } from "./table";
import type { Block, Read } from "./types";

function readFence(lines: string[], i: number, m: RegExpMatchArray): Read {
  const body: string[] = [];
  let j = i + 1;
  while (j < lines.length && !lines[j]!.trim().startsWith(m[1]!)) body.push(lines[j++]!);
  return { block: { t: "code", text: body.join("\n"), lang: m[2] ?? "" }, next: j + 1 };
}

function readQuote(lines: string[], i: number): Read {
  const body: string[] = [];
  let j = i;
  while (j < lines.length && QUOTE.test(lines[j]!)) body.push(lines[j++]!.replace(QUOTE, ""));
  return { block: { t: "quote", blocks: parseBlocks(body.join("\n")) }, next: j };
}

function readParagraph(lines: string[], i: number): Read {
  const para: string[] = [];
  let j = i;
  while (j < lines.length && !isBlank(lines[j]!) && (para.length === 0 || !startsBlock(lines, j))) para.push(lines[j++]!.trim());
  return { block: { t: "p", text: para.join("\n") }, next: j };
}

/** The block that starts at line i (which is not blank). */
function readBlock(lines: string[], i: number): Read {
  const line = lines[i]!;
  const fence = line.match(FENCE);
  if (fence) return readFence(lines, i, fence);
  const heading = line.match(HEADING);
  if (heading) return { block: { t: "h", level: heading[1]!.length, text: heading[2]! }, next: i + 1 };
  if (HR.test(line)) return { block: { t: "hr" }, next: i + 1 };
  if (startsTable(lines, i)) return readTable(lines, i);
  if (QUOTE.test(line)) return readQuote(lines, i);
  if (LIST_ITEM.test(line)) return readList(lines, i);
  return readParagraph(lines, i);
}

/** Markdown text to blocks: headings, paragraphs, lists, pipe tables, fenced code, quotes and rules. */
export function parseBlocks(source: string): Block[] {
  const lines = source.replace(/\r\n?/g, "\n").split("\n");
  const blocks: Block[] = [];
  let i = 0;
  while (i < lines.length) {
    if (isBlank(lines[i]!)) {
      i++;
      continue;
    }
    const { block, next } = readBlock(lines, i);
    blocks.push(block);
    i = next;
  }
  return blocks;
}
