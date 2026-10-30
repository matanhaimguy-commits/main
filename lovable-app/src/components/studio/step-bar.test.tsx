import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { GateChip } from "./gate-chip";
import { StepBar } from "./step-bar";

describe("StepBar and GateChip", () => {
  it("draws one segment per step and says how many are done", () => {
    render(
      <StepBar
        steps={[
          { n: 0, name: "Brief", status: "done" },
          { n: 1, name: "Idea", status: "active" },
          { n: 2, name: "Skip", status: "na" },
        ]}
      />,
    );
    const bar = screen.getByRole("img", { name: "1 of 2 steps done" });
    expect(bar.children).toHaveLength(3);
    expect(bar.children[1]).toHaveAttribute("title", "1 Idea: Now");
  });

  it("draws nothing for a run without steps", () => {
    const { container } = render(<StepBar steps={[]} />);
    expect(container).toBeEmptyDOMElement();
  });

  it("shows a gate's state, name and score", () => {
    render(<GateChip status="PASS" label="Script Lab" score={86} />);
    expect(screen.getByText("Pass").parentElement).toHaveTextContent("Pass· Script Lab86/100");
  });
});
