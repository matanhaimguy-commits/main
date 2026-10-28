import { AreaField, SwitchField, TextField } from "@/components/app/fields";
import type { FunnelFieldsProps } from "./types";

/** The optional "follow us first" step (Instagram). */
export function FollowGateFields({ funnel, set }: FunnelFieldsProps) {
  return (
    <div className="space-y-3">
      <SwitchField
        label="Ask to follow first (Instagram)"
        hint="Costs one extra tap. People who already follow skip it."
        checked={!!funnel["follow_gate"]?.["enabled"] && !!funnel["follow_gate"]}
        onChange={(v) =>
          set(
            ["follow_gate"],
            v ? { enabled: true, text: funnel["follow_gate"]?.["text"] || "Follow us first, then tap again 👇", button: funnel["follow_gate"]?.["button"] || "I followed" } : undefined,
          )
        }
      />
      {funnel["follow_gate"]?.["enabled"] && (
        <div className="grid gap-4 sm:grid-cols-[2fr_1fr]">
          <AreaField label="Follow request text" max={640} rows={2} value={funnel["follow_gate"]?.["text"]} onChange={(v) => set(["follow_gate", "text"], v ?? "")} />
          <TextField label="Button" max={20} value={funnel["follow_gate"]?.["button"]} onChange={(v) => set(["follow_gate", "button"], v ?? "")} />
        </div>
      )}
    </div>
  );
}
