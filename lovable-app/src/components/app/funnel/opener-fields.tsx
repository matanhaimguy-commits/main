import { AreaField, SelectField, TextField } from "@/components/app/fields";
import type { FunnelFieldsProps } from "./types";

/** Step 1: the first message, with its button. */
export function OpenerFields({ funnel, set }: FunnelFieldsProps) {
  return (
    <div className="space-y-3">
      <div className="text-sm font-semibold">1 · First message</div>
      <AreaField label="Text" max={640} value={funnel["opener"]?.["text"]} onChange={(v) => set(["opener", "text"], v ?? "")} />
      <div className="grid gap-4 sm:grid-cols-2">
        <TextField label="Button" max={20} value={funnel["opener"]?.["button"]} onChange={(v) => set(["opener", "button"], v ?? "")} />
        <SelectField
          label="Button does"
          value={funnel["opener"]?.["mode"] ?? "tap"}
          options={[
            { value: "tap", label: "Tap to receive (recommended: opens the chat for the AI)" },
            { value: "link", label: "Opens the link directly" },
          ]}
          onChange={(v) => set(["opener", "mode"], v)}
        />
      </div>
    </div>
  );
}
