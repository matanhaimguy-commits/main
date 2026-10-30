import { describe, expect, it } from "vitest";
import { parseBlocks } from "./parse-blocks";
import { splitRow } from "./table";

describe("markdown: tables", () => {
  it("reads pipe tables, with alignment, escaped pipes and pipes inside code", () => {
    const [table] = parseBlocks("| # | Line | V |\n|---|:---|---:|\n| 1 | a \\| b | A |\n| 2 | `x|y` | B+ |\n\nafter");
    expect(table).toEqual({
      t: "table",
      head: ["#", "Line", "V"],
      align: [null, "left", "right"],
      rows: [
        ["1", "a | b", "A"],
        ["2", "`x|y`", "B+"],
      ],
    });
  });

  it("splits a row with or without its outer pipes", () => {
    expect(splitRow("| a | b |")).toEqual(["a", "b"]);
    expect(splitRow("a | b")).toEqual(["a", "b"]);
  });
});
