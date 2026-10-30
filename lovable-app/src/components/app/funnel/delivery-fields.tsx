import { AreaField, Field, TextField } from "@/components/app/fields";
import { Input } from "@/components/ui/input";
import type { AnyObj, FunnelFieldsProps } from "./types";

/** Step 2: the message that hands over the link. */
export function DeliveryFields({ funnel, set, links }: FunnelFieldsProps & { links: AnyObj[] }) {
  const linkIds = links.map((l) => String(l["id"]));
  const deliverLink = String(funnel["deliver"]?.["link"] ?? "");
  const customLink = deliverLink !== "" && !linkIds.includes(deliverLink);
  return (
    <div className="space-y-3">
      <div className="text-sm font-semibold">2 · Delivery</div>
      <AreaField label="Text" max={640} value={funnel["deliver"]?.["text"]} onChange={(v) => set(["deliver", "text"], v ?? "")} />
      <div className="grid gap-4 sm:grid-cols-2">
        <Field label="Link" hint={linkIds.length ? "One of the business's links, or a full address." : "Add links on the Links tab, or paste a full address."}>
          <select
            className="h-9 w-full rounded-md border bg-background px-2 text-sm"
            value={customLink ? "__custom" : deliverLink}
            onChange={(e) => set(["deliver", "link"], e.target.value === "__custom" ? "https://" : e.target.value)}
          >
            <option value="">— choose —</option>
            {links.map((l) => (
              <option key={l["id"]} value={l["id"]}>
                {l["title"]} ({l["id"]})
              </option>
            ))}
            <option value="__custom">A full address…</option>
          </select>
          {customLink && <Input className="mt-2" value={deliverLink} onChange={(e) => set(["deliver", "link"], e.target.value)} />}
        </Field>
        <TextField label="Button" max={20} value={funnel["deliver"]?.["button"]} onChange={(v) => set(["deliver", "button"], v ?? "")} />
      </div>
    </div>
  );
}
