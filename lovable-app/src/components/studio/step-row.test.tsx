import { fireEvent, render, screen } from "@testing-library/react";
import { useState } from "react";
import { describe, expect, it, vi } from "vitest";
import { StepRow } from "./step-row";
import { fileView, stepView } from "./test-fixtures";

vi.mock("@/lib/api/studio", () => ({ getStudioFileFn: vi.fn() }));

function Row({ files = [] as ReturnType<typeof fileView>[] }) {
  const [open, setOpen] = useState(false);
  const step = stepView(3, "done", {
    name: "Script",
    note: "Speech released at 86.",
    gates: [
      { gate: "G-SCRIPT", label: "Script Lab", status: "FAIL", score: 81, by: "fresh cold reader", note: "Lines 6-8 lose the thread." },
      { gate: "G-SCRIPT", label: "Script Lab", status: "PASS", score: 86 },
    ],
  });
  return (
    <ol>
      <StepRow step={step} last files={files} asks={0} open={open} onToggle={() => setOpen(!open)} />
    </ol>
  );
}

describe("StepRow", () => {
  it("shows the latest gate when closed and every record when opened", () => {
    render(<Row files={[fileView(1, "audio", { step: 3, label: "Song" })]} />);
    expect(screen.getByText("Done")).toBeInTheDocument();
    expect(screen.getByText("1 file")).toBeInTheDocument();
    expect(screen.queryByText("Lines 6-8 lose the thread.")).toBeNull();
    fireEvent.click(screen.getByRole("button", { name: /Script/ }));
    expect(screen.getByText("Speech released at 86.")).toBeInTheDocument();
    expect(screen.getByText("Lines 6-8 lose the thread.")).toBeInTheDocument();
    expect(screen.getByText("81/100")).toBeInTheDocument();
    expect(screen.getByText("86/100")).toBeInTheDocument();
    expect(screen.getByText("Song")).toBeInTheDocument();
  });

  it("can't open a step with nothing to show", () => {
    render(
      <ol>
        <StepRow step={stepView(9, "pending")} last files={[]} asks={0} open={false} onToggle={vi.fn()} />
      </ol>,
    );
    expect(screen.getByRole("button", { name: /Step 9/ })).toBeDisabled();
  });
});
