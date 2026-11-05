import { AreaField, NumberField } from "@/components/app/fields";
import { AFTER_DELAY_MAX_MINUTES, clampAfterDelay } from "@/agent/logic/after-delay";
import type { FunnelFieldsProps } from "./types";

/** Step 3: the optional last message, and how long to wait after the delivery before sending it. */
export function AfterFields({ funnel, set }: FunnelFieldsProps) {
  return (
    <div className="space-y-3">
      <AreaField
        label="3 · Last message (optional)"
        hint="Open a conversation, e.g. a question about what they need. Only with the tap button."
        max={1000}
        rows={2}
        optional
        value={funnel["after"]}
        onChange={(v) => set(["after"], v)}
      />
      {funnel["after"] && (
        <div className="sm:max-w-xs">
          <NumberField
            label="Wait before sending it (minutes)"
            hint={`0 sends it right after the delivery. A qualifying question lands better 10 to 60 minutes later (up to ${AFTER_DELAY_MAX_MINUTES}). It is skipped if the person writes back first or the 24-hour chat window has closed.`}
            value={funnel["after_delay_minutes"] ?? 0}
            min={0}
            max={AFTER_DELAY_MAX_MINUTES}
            // 0 is the default, so it is left out of the saved funnel.
            onChange={(v) => set(["after_delay_minutes"], clampAfterDelay(v) || undefined)}
          />
        </div>
      )}
    </div>
  );
}
