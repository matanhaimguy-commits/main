import { describe, expect, it } from "vitest";
import { parseBlocks } from "./parse-blocks";

describe("markdown: blocks", () => {
  it("reads headings, paragraphs, rules, quotes and fenced code", () => {
    const blocks = parseBlocks("# Speech scripts\n\nLoop 1 is first;\nloop 2 below.\n\n---\n\n> a quote\n\n```\nLumpy months?\n  kept as is\n```\n");
    expect(blocks).toEqual([
      { t: "h", level: 1, text: "Speech scripts" },
      { t: "p", text: "Loop 1 is first;\nloop 2 below." },
      { t: "hr" },
      { t: "quote", blocks: [{ t: "p", text: "a quote" }] },
      { t: "code", text: "Lumpy months?\n  kept as is", lang: "" },
    ]);
  });

  it("ends a paragraph where another block starts", () => {
    expect(parseBlocks("Intro line\n- item\n## Next").map((b) => b.t)).toEqual(["p", "list", "h"]);
  });

  it("keeps an unclosed fence as code to the end", () => {
    expect(parseBlocks("```yaml\na: 1")).toEqual([{ t: "code", text: "a: 1", lang: "yaml" }]);
  });
});
