import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { fireEvent, render, screen } from "@testing-library/react";
import type { ReactNode } from "react";
import { describe, expect, it, vi } from "vitest";
import { FileView } from "./file-view";
import { fileView } from "./test-fixtures";

vi.mock("@/lib/api/studio", () => ({
  getStudioFileFn: vi.fn(async () => ({ id: 1, label: "Script", markdown: "# Speech\n\n| Line | Words |\n|---|---|\n| Lumpy months? | 2 |" })),
}));

const wrap = (ui: ReactNode) => render(<QueryClientProvider client={new QueryClient()}>{ui}</QueryClientProvider>);

describe("FileView", () => {
  it("plays audio, shows images and video inline", () => {
    const { container } = wrap(
      <>
        <FileView file={fileView(1, "audio", { label: "Song master" })} />
        <FileView file={fileView(2, "image", { label: "Hook board" })} />
        <FileView file={fileView(3, "video", { label: "Cut v1" })} />
      </>,
    );
    expect(container.querySelector("audio")).toHaveAttribute("src", "https://cdn.example/f1");
    expect(screen.getByRole("img", { name: "Hook board" })).toHaveAttribute("src", "https://cdn.example/f2");
    expect(container.querySelector("video")).toHaveAttribute("playsinline");
  });

  it("loads a doc's markdown when it is opened and renders it", async () => {
    wrap(<FileView file={fileView(1, "doc", { label: "Script" })} />);
    expect(screen.queryByRole("table")).toBeNull();
    fireEvent.click(screen.getByRole("button", { name: /Script/ }));
    expect(await screen.findByRole("table")).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Speech" })).toBeInTheDocument();
  });

  it("links a doc that has no markdown", () => {
    wrap(<FileView file={fileView(1, "doc", { label: "Offer PDF", has_markdown: false, url: "https://cdn.example/offer.pdf" })} />);
    expect(screen.getByRole("link", { name: /Offer PDF/ })).toHaveAttribute("href", "https://cdn.example/offer.pdf");
  });
});
