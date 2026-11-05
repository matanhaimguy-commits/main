import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { AnswerForm } from "./answer-form";
import { AnswerSummary } from "./answer-summary";
import { decisionView } from "./test-fixtures";

describe("AnswerForm", () => {
  it("sends the picked option and the note", async () => {
    const onSend = vi.fn(async () => true);
    render(<AnswerForm decision={decisionView(1)} canAnswer onSend={onSend} />);
    const send = screen.getByRole("button", { name: "Send answer" });
    expect(send).toBeDisabled();
    fireEvent.click(screen.getByRole("radio", { name: /Atlas Suno/ }));
    expect(screen.getByRole("radio", { name: /Atlas Suno/ })).toHaveAttribute("aria-checked", "true");
    fireEvent.change(screen.getByPlaceholderText("Anything to add? (optional)"), { target: { value: "name the model" } });
    fireEvent.click(send);
    await waitFor(() => expect(onSend).toHaveBeenCalledWith(["Atlas Suno"], "name the model"));
  });

  it("lets a reviewer look but not answer", () => {
    render(<AnswerForm decision={decisionView(1)} canAnswer={false} onSend={vi.fn()} />);
    expect(screen.getByRole("radio", { name: /Suno by hand/ })).toBeDisabled();
    expect(screen.queryByRole("button", { name: "Send answer" })).toBeNull();
    expect(screen.getByText("Only the owner can answer this.")).toBeInTheDocument();
  });

  it("asks for the answer in the note when there are no options", () => {
    render(<AnswerForm decision={decisionView(1, { options: [] })} canAnswer onSend={vi.fn()} />);
    expect(screen.getByPlaceholderText("Your answer")).toBeInTheDocument();
  });
});

describe("AnswerSummary", () => {
  const answer = { choices: ["Suno by hand"], note: "slower chorus", by: "owner", at: "2026-10-27T11:00:00Z" };

  it("shows the answer and offers to change it until the studio takes it in", () => {
    const onChange = vi.fn();
    render(<AnswerSummary decision={decisionView(1, { status: "answered", answer })} onChange={onChange} />);
    expect(screen.getByText("Suno by hand")).toBeInTheDocument();
    expect(screen.getByText("slower chorus")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Change answer" }));
    expect(onChange).toHaveBeenCalled();
  });

  it("can't be changed once synced", () => {
    render(<AnswerSummary decision={decisionView(1, { status: "synced", answer, synced_at: "2026-10-27T12:00:00Z" })} onChange={vi.fn()} />);
    expect(screen.getByText("Decided")).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Change answer" })).toBeNull();
  });
});
