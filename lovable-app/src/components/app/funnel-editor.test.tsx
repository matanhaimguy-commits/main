import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { AnyObj } from "@/components/app/funnel/types";
import { FunnelEditor } from "./funnel-editor";

const funnel = (over: AnyObj = {}): AnyObj => ({
  id: "words",
  trigger: "comment",
  keywords: ["WORDS"],
  posts: ["MEDIA_A"],
  opener: { text: "Want the sheet?", button: "Send it", mode: "tap" },
  deliver: { text: "Here it is.", link: "guide_pdf", button: "Open the sheet" },
  after: "One question: what does a normal month bring in?",
  ...over,
});
const links = [{ id: "guide_pdf", title: "Guide", url: "https://acme.studio/guide.pdf" }];

function show(f: AnyObj, onChange = vi.fn()) {
  render(
    <QueryClientProvider client={new QueryClient()}>
      <FunnelEditor slug="acme" funnel={f} links={links} onChange={onChange} onRemove={vi.fn()} defaultOpen />
    </QueryClientProvider>,
  );
  return onChange;
}

describe("FunnelEditor", () => {
  it("shows every section of a comment funnel, with the wait before the last message", () => {
    show(funnel());
    for (const text of ["1 · First message", "2 · Delivery", "3 · Last message (optional)", "Wait before sending it (minutes)", "Pick from recent posts"]) {
      expect(screen.getByText(text)).toBeInTheDocument();
    }
    expect(screen.getByText("Ask to follow first (Instagram)")).toBeInTheDocument();
  });

  it("leaves out the post pinning for a DM funnel", () => {
    show(funnel({ trigger: "dm_keyword", posts: [] }));
    expect(screen.queryByText("Pick from recent posts")).toBeNull();
    expect(screen.getByText("Wait before sending it (minutes)")).toBeInTheDocument();
  });

  it("saves a wait into the funnel and leaves the rest as it was", () => {
    const onChange = show(funnel());
    fireEvent.change(screen.getByRole("spinbutton"), { target: { value: "20" } });
    expect(onChange).toHaveBeenCalledWith(funnel({ after_delay_minutes: 20 }));
  });

  it("removes the setting again when it is set back to 0", () => {
    const onChange = show(funnel({ after_delay_minutes: 20 }));
    fireEvent.change(screen.getByRole("spinbutton"), { target: { value: "0" } });
    expect(onChange).toHaveBeenCalledWith(funnel());
  });
});
