/** The parsed shape of a markdown doc: blocks, and the inline pieces inside their text. */

export type Inline =
  | { t: "text"; v: string }
  | { t: "code"; v: string }
  | { t: "b"; c: Inline[] }
  | { t: "i"; c: Inline[] }
  | { t: "a"; href: string | null; c: Inline[] };

export interface ListNode {
  ordered: boolean;
  start: number;
  items: { text: string; children: ListNode | null }[];
}

export type Align = "left" | "center" | "right" | null;

export type Block =
  | { t: "h"; level: number; text: string }
  | { t: "p"; text: string }
  | { t: "list"; list: ListNode }
  | { t: "code"; text: string; lang: string }
  | { t: "quote"; blocks: Block[] }
  | { t: "table"; head: string[]; rows: string[][]; align: Align[] }
  | { t: "hr" };

/** A block reader's result: the block and the index of the first line after it. */
export interface Read<T = Block> {
  block: T;
  next: number;
}
