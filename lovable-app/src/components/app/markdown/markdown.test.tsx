import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { Markdown } from "./index";

describe("Markdown", () => {
  it("renders tables and links as elements, never as raw HTML", () => {
    render(<Markdown source={"| A | B |\n|---|---|\n| <b>1</b> | [ok](https://example.com) |\n\n[bad](javascript:alert(1))"} />);
    expect(screen.getByRole("table")).toBeInTheDocument();
    expect(screen.getByText("<b>1</b>")).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "ok" })).toHaveAttribute("href", "https://example.com");
    expect(screen.queryByRole("link", { name: "bad" })).toBeNull();
  });

  it("starts a doc's headings at h2, under the page title", () => {
    render(<Markdown source={"# Lyrics\n\n## Verse 1"} />);
    expect(screen.getByRole("heading", { level: 2, name: "Lyrics" })).toBeInTheDocument();
    expect(screen.getByRole("heading", { level: 3, name: "Verse 1" })).toBeInTheDocument();
  });
});
