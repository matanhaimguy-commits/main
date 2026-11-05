import { describe, expect, it } from "vitest";
import { parseInline } from "./parse-inline";
import { safeHref } from "./safe-href";

describe("markdown: inline", () => {
  it("reads bold, italic, code and links, and leaves snake_case alone", () => {
    expect(parseInline("**Stack** *one* `two` file_name_here")).toEqual([
      { t: "b", c: [{ t: "text", v: "Stack" }] },
      { t: "text", v: " " },
      { t: "i", c: [{ t: "text", v: "one" }] },
      { t: "text", v: " " },
      { t: "code", v: "two" },
      { t: "text", v: " file_name_here" },
    ]);
    expect(parseInline("see [the offer](https://example.com/o) now")[1]).toEqual({ t: "a", href: "https://example.com/o", c: [{ t: "text", v: "the offer" }] });
  });

  it("links bare web addresses without their trailing punctuation", () => {
    expect(parseInline("at https://example.com/a.")).toEqual([
      { t: "text", v: "at " },
      { t: "a", href: "https://example.com/a", c: [{ t: "text", v: "https://example.com/a" }] },
      { t: "text", v: "." },
    ]);
  });

  it("keeps escaped characters and lone stars as text", () => {
    expect(parseInline("\\*not em\\* 3 * 4")).toEqual([{ t: "text", v: "*not em* 3 * 4" }]);
  });

  it("never links to a script", () => {
    expect(safeHref("javascript:alert(1)")).toBeNull();
    expect(safeHref("//evil.example")).toBeNull();
    expect(safeHref("/studio/1")).toBe("/studio/1");
    expect(parseInline("[x](javascript:alert(1))")[0]).toMatchObject({ t: "a", href: null });
  });
});
