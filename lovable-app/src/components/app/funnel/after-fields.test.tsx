import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { AfterFields } from "./after-fields";

const DELAY_LABEL = "Wait before sending it (minutes)";

describe("AfterFields", () => {
  it("shows the wait only when the funnel has a last message", () => {
    const { rerender } = render(<AfterFields funnel={{}} set={vi.fn()} />);
    expect(screen.queryByText(DELAY_LABEL)).toBeNull();
    rerender(<AfterFields funnel={{ after: "One question: what do you sell?" }} set={vi.fn()} />);
    expect(screen.getByText(DELAY_LABEL)).toBeInTheDocument();
  });

  it("shows 0 for a funnel with no setting, and the saved wait otherwise", () => {
    const { rerender } = render(<AfterFields funnel={{ after: "Q?" }} set={vi.fn()} />);
    expect(screen.getByRole("spinbutton")).toHaveValue(0);
    rerender(<AfterFields funnel={{ after: "Q?", after_delay_minutes: 25 }} set={vi.fn()} />);
    expect(screen.getByRole("spinbutton")).toHaveValue(25);
  });

  it("limits the input to 0 to 60 whole minutes", () => {
    render(<AfterFields funnel={{ after: "Q?" }} set={vi.fn()} />);
    const input = screen.getByRole("spinbutton");
    expect(input).toHaveAttribute("min", "0");
    expect(input).toHaveAttribute("max", "60");
    expect(input).toHaveAttribute("step", "1");
  });

  it("saves the minutes typed", () => {
    const set = vi.fn();
    render(<AfterFields funnel={{ after: "Q?" }} set={set} />);
    fireEvent.change(screen.getByRole("spinbutton"), { target: { value: "15" } });
    expect(set).toHaveBeenCalledWith(["after_delay_minutes"], 15);
  });

  it("holds a number that is too big or too small to the limits", () => {
    const set = vi.fn();
    render(<AfterFields funnel={{ after: "Q?", after_delay_minutes: 10 }} set={set} />);
    fireEvent.change(screen.getByRole("spinbutton"), { target: { value: "90" } });
    expect(set).toHaveBeenLastCalledWith(["after_delay_minutes"], 60);
    fireEvent.change(screen.getByRole("spinbutton"), { target: { value: "-4" } });
    expect(set).toHaveBeenLastCalledWith(["after_delay_minutes"], undefined);
  });

  it("leaves the setting out of the funnel when it goes back to 0 (the default)", () => {
    const set = vi.fn();
    render(<AfterFields funnel={{ after: "Q?", after_delay_minutes: 10 }} set={set} />);
    fireEvent.change(screen.getByRole("spinbutton"), { target: { value: "0" } });
    expect(set).toHaveBeenCalledWith(["after_delay_minutes"], undefined);
  });
});
