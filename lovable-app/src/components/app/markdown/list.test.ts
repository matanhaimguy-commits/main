import { describe, expect, it } from "vitest";
import { parseBlocks } from "./parse-blocks";

describe("markdown: lists", () => {
  it("nests lists by indentation and keeps continuation lines with their item", () => {
    const [list] = parseBlocks("- Named person: **1 master**\n  and its seam\n  - sub item\n- Characters explain\n\n1. first\n2. second");
    expect(list).toEqual({
      t: "list",
      list: {
        ordered: false,
        start: 1,
        items: [
          { text: "Named person: **1 master** and its seam", children: { ordered: false, start: 1, items: [{ text: "sub item", children: null }] } },
          { text: "Characters explain", children: null },
        ],
      },
    });
  });

  it("starts a new list when the marker kind changes, and keeps a list across a blank line", () => {
    const blocks = parseBlocks("- a\n\n- b\n\n1. one\n2. two");
    expect(blocks).toHaveLength(2);
    expect(blocks[0]).toMatchObject({ t: "list", list: { ordered: false, items: [{ text: "a" }, { text: "b" }] } });
    expect(blocks[1]).toMatchObject({ t: "list", list: { ordered: true, start: 1 } });
  });
});
