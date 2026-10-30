import { Check } from "lucide-react";
import { cn } from "@/lib/utils";

/** One answer option: a full-width tap target with its label and description, a radio or a checkbox. */
export function OptionButton({
  label,
  description,
  multi,
  checked,
  disabled,
  onClick,
}: {
  label: string;
  description?: string;
  multi: boolean;
  checked: boolean;
  disabled: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      role={multi ? "checkbox" : "radio"}
      aria-checked={checked}
      disabled={disabled}
      onClick={onClick}
      className={cn(
        "flex min-h-12 w-full items-start gap-3 rounded-lg border px-3 py-2.5 text-left transition-colors disabled:cursor-not-allowed",
        checked ? "border-primary bg-primary/5 ring-1 ring-primary" : "bg-background hover:bg-accent/40",
      )}
    >
      <span
        className={cn(
          "mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center border",
          multi ? "rounded" : "rounded-full",
          checked ? "border-primary bg-primary text-primary-foreground" : "border-muted-foreground/40",
        )}
        aria-hidden
      >
        {checked && <Check className="h-3.5 w-3.5" />}
      </span>
      <span className="min-w-0 flex-1">
        <span dir="auto" className="block text-sm font-medium">
          {label}
        </span>
        {description && (
          <span dir="auto" className="mt-0.5 block whitespace-pre-wrap text-sm text-muted-foreground">
            {description}
          </span>
        )}
      </span>
    </button>
  );
}
