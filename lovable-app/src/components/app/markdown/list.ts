import { isBlank, LIST_ITEM, startsBlock } from "./patterns";
import type { Block, ListNode, Read } from "./types";

interface Entry {
  indent: number;
  ordered: boolean;
  num: number;
  text: string;
}

function entryOf(line: string): Entry | null {
  const m = line.match(LIST_ITEM);
  return m ? { indent: m[1]!.replace(/\t/g, "    ").length, ordered: !!m[3], num: m[3] ? Number(m[3]) : 1, text: m[4]! } : null;
}

/** Nests flat items by their indentation. */
export function buildList(entries: Entry[]): ListNode {
  const first = entries[0]!;
  const root: ListNode = { ordered: first.ordered, start: first.num, items: [] };
  const stack: { indent: number; node: ListNode }[] = [{ indent: first.indent, node: root }];
  for (const e of entries) {
    while (stack.length > 1 && e.indent < stack[stack.length - 1]!.indent) stack.pop();
    let top = stack[stack.length - 1]!;
    if (e.indent > top.indent && top.node.items.length > 0) {
      const parent = top.node.items[top.node.items.length - 1]!;
      parent.children ??= { ordered: e.ordered, start: e.num, items: [] };
      stack.push({ indent: e.indent, node: parent.children });
      top = stack[stack.length - 1]!;
    }
    top.node.items.push({ text: e.text, children: null });
  }
  return root;
}

/**
 * A list starting at line i: items, nested items, continuation lines. A blank line ends it unless another
 * item of it follows; a top-level item with the other kind of marker starts a new list.
 */
export function readList(lines: string[], i: number): Read<Extract<Block, { t: "list" }>> {
  const entries: Entry[] = [];
  const sameList = (e: Entry) => !entries.length || e.indent > entries[0]!.indent || e.ordered === entries[0]!.ordered;
  let j = i;
  while (j < lines.length) {
    const cur = lines[j]!;
    const e = entryOf(cur);
    if (e) {
      if (!sameList(e)) break;
      entries.push(e);
      j++;
    } else if (isBlank(cur)) {
      let k = j + 1;
      while (k < lines.length && isBlank(lines[k]!)) k++;
      const next = k < lines.length ? entryOf(lines[k]!) : null;
      if (!next || !sameList(next)) break;
      j = k;
    } else if (/^\s+\S/.test(cur) && !startsBlock(lines, j)) {
      entries[entries.length - 1]!.text += ` ${cur.trim()}`;
      j++;
    } else break;
  }
  return { block: { t: "list", list: buildList(entries) }, next: j };
}
