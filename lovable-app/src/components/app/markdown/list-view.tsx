import { InlineText } from "./inline-text";
import type { ListNode } from "./types";

export function ListView({ list }: { list: ListNode }) {
  const items = list.items.map((it, k) => (
    <li key={k} dir="auto">
      <InlineText text={it.text} />
      {it.children && <ListView list={it.children} />}
    </li>
  ));
  return list.ordered ? (
    <ol start={list.start} className="list-decimal space-y-1 pl-5">
      {items}
    </ol>
  ) : (
    <ul className="list-disc space-y-1 pl-5">{items}</ul>
  );
}
