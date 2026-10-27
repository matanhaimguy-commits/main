import { Fragment, type ReactNode } from "react";
import { parseInline } from "./parse-inline";
import type { Inline } from "./types";

function renderInline(nodes: Inline[]): ReactNode {
  return nodes.map((n, k) => {
    switch (n.t) {
      case "text":
        return <Fragment key={k}>{n.v}</Fragment>;
      case "code":
        return (
          <code key={k} className="rounded bg-muted px-1 py-0.5 font-mono text-[0.85em]">
            {n.v}
          </code>
        );
      case "b":
        return <strong key={k}>{renderInline(n.c)}</strong>;
      case "i":
        return <em key={k}>{renderInline(n.c)}</em>;
      case "a":
        return n.href ? (
          <a key={k} href={n.href} target={n.href.startsWith("#") ? undefined : "_blank"} rel="noreferrer" className="break-words underline">
            {renderInline(n.c)}
          </a>
        ) : (
          <Fragment key={k}>{renderInline(n.c)}</Fragment>
        );
    }
  });
}

/** A line or more of inline markdown, its line breaks kept. */
export function InlineText({ text }: { text: string }) {
  return (
    <>
      {text.split("\n").map((line, k) => (
        <Fragment key={k}>
          {k > 0 && <br />}
          {renderInline(parseInline(line))}
        </Fragment>
      ))}
    </>
  );
}
