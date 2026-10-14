import { Plus, Trash2 } from "lucide-react";
import type { ReactNode } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";

/** Immutable set at a path: setIn(obj, ["profile", "about"], "x"). `undefined` deletes the key. */
export function setIn<T>(obj: T, path: (string | number)[], value: unknown): T {
  if (path.length === 0) return value as T;
  const [head, ...rest] = path;
  const base: any = Array.isArray(obj) ? [...obj] : { ...(obj as object) };
  const next = setIn(base[head as any], rest, value);
  if (next === undefined && !Array.isArray(base)) delete base[head as any];
  else base[head as any] = next;
  return base;
}

export function Field({ label, hint, children, className }: { label: string; hint?: ReactNode; children: ReactNode; className?: string }) {
  return (
    <div className={cn("space-y-1.5", className)}>
      <Label>{label}</Label>
      {children}
      {hint && <p className="text-xs text-muted-foreground">{hint}</p>}
    </div>
  );
}

export function TextField({
  label,
  hint,
  value,
  onChange,
  max,
  placeholder,
  optional,
}: {
  label: string;
  hint?: ReactNode;
  value: string | undefined;
  onChange: (v: string | undefined) => void;
  max?: number;
  placeholder?: string;
  optional?: boolean;
}) {
  const v = value ?? "";
  return (
    <Field label={label} hint={<Counter hint={hint} length={v.length} max={max} />}>
      <Input value={v} placeholder={placeholder} onChange={(e) => onChange(optional && e.target.value === "" ? undefined : e.target.value)} />
    </Field>
  );
}

export function AreaField({
  label,
  hint,
  value,
  onChange,
  max,
  rows = 3,
  placeholder,
  optional,
}: {
  label: string;
  hint?: ReactNode;
  value: string | undefined;
  onChange: (v: string | undefined) => void;
  max?: number;
  rows?: number;
  placeholder?: string;
  optional?: boolean;
}) {
  const v = value ?? "";
  return (
    <Field label={label} hint={<Counter hint={hint} length={v.length} max={max} />}>
      <Textarea rows={rows} value={v} placeholder={placeholder} onChange={(e) => onChange(optional && e.target.value === "" ? undefined : e.target.value)} />
    </Field>
  );
}

function Counter({ hint, length, max }: { hint?: ReactNode; length: number; max?: number | undefined }) {
  if (!max) return <>{hint}</>;
  return (
    <span className="flex justify-between gap-3">
      <span>{hint}</span>
      <span className={cn("tabular-nums", length > max && "font-medium text-destructive")}>
        {length}/{max}
      </span>
    </span>
  );
}

/** A list of short strings, one per line. Committed when the field loses focus. */
export function LinesField({
  label,
  hint,
  value,
  onChange,
  rows = 3,
  placeholder,
}: {
  label: string;
  hint?: ReactNode;
  value: string[] | undefined;
  onChange: (v: string[]) => void;
  rows?: number;
  placeholder?: string;
}) {
  const text = (value ?? []).join("\n");
  return (
    <Field label={label} hint={hint ?? "One per line."}>
      <Textarea
        key={text}
        rows={rows}
        placeholder={placeholder}
        defaultValue={text}
        onBlur={(e) => onChange(e.target.value.split("\n").map((s) => s.trim()).filter(Boolean))}
      />
    </Field>
  );
}

/** Comma-separated chips-lite: keywords, testers, post IDs. */
export function CommaField({
  label,
  hint,
  value,
  onChange,
  placeholder,
}: {
  label: string;
  hint?: ReactNode;
  value: string[] | undefined;
  onChange: (v: string[]) => void;
  placeholder?: string;
}) {
  return (
    <Field label={label} hint={hint ?? "Separate with commas."}>
      <Input
        placeholder={placeholder}
        defaultValue={(value ?? []).join(", ")}
        key={(value ?? []).join("|")}
        onBlur={(e) => onChange(e.target.value.split(",").map((s) => s.trim()).filter(Boolean))}
      />
    </Field>
  );
}

export function SwitchField({ label, hint, checked, onChange }: { label: string; hint?: ReactNode; checked: boolean; onChange: (v: boolean) => void }) {
  return (
    <div className="flex items-start justify-between gap-4 rounded-lg border p-3">
      <div>
        <div className="text-sm font-medium">{label}</div>
        {hint && <div className="mt-0.5 text-xs text-muted-foreground">{hint}</div>}
      </div>
      <Switch checked={checked} onCheckedChange={onChange} />
    </div>
  );
}

export function SelectField({
  label,
  hint,
  value,
  options,
  onChange,
}: {
  label: string;
  hint?: ReactNode;
  value: string;
  options: { value: string; label: string }[];
  onChange: (v: string) => void;
}) {
  return (
    <Field label={label} hint={hint}>
      <select className="h-9 w-full rounded-md border bg-background px-2 text-sm" value={value} onChange={(e) => onChange(e.target.value)}>
        {options.map((o) => (
          <option key={o.value} value={o.value}>
            {o.label}
          </option>
        ))}
      </select>
    </Field>
  );
}

export function NumberField({
  label,
  hint,
  value,
  onChange,
  min,
  max,
  step,
}: {
  label: string;
  hint?: ReactNode;
  value: number | undefined;
  onChange: (v: number) => void;
  min?: number;
  max?: number;
  step?: number;
}) {
  return (
    <Field label={label} hint={hint}>
      <Input type="number" value={value ?? ""} min={min} max={max} step={step ?? 1} onChange={(e) => onChange(Number(e.target.value))} />
    </Field>
  );
}

/** Rows of objects with add/remove, e.g. FAQ pairs and links. */
export function RowsEditor<T>({
  items,
  onChange,
  render,
  make,
  addLabel,
}: {
  items: T[];
  onChange: (items: T[]) => void;
  render: (item: T, update: (next: T) => void) => ReactNode;
  make: () => T;
  addLabel: string;
}) {
  return (
    <div className="space-y-3">
      {items.map((item, i) => (
        <div key={i} className="flex gap-2 rounded-lg border p-3">
          <div className="min-w-0 flex-1">{render(item, (next) => onChange(items.map((x, j) => (j === i ? next : x))))}</div>
          <Button type="button" variant="ghost" size="icon" onClick={() => onChange(items.filter((_, j) => j !== i))} aria-label="Remove">
            <Trash2 />
          </Button>
        </div>
      ))}
      <Button type="button" variant="outline" size="sm" onClick={() => onChange([...items, make()])}>
        <Plus /> {addLabel}
      </Button>
    </div>
  );
}
