import { Check, Copy } from "lucide-react";
import { useState } from "react";

/** A value to paste somewhere else (Meta's dashboard), with a copy button. */
export function CopyField({ label, value }: { label: string; value: string | null | undefined }) {
  const [copied, setCopied] = useState(false);
  const copy = async () => {
    if (!value) return;
    await navigator.clipboard.writeText(value);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };
  return (
    <div className="grid gap-1 py-1.5 sm:grid-cols-[minmax(0,15rem)_1fr] sm:items-center sm:gap-3">
      <div className="text-xs text-muted-foreground">{label}</div>
      <div className="flex min-w-0 items-center gap-2">
        <code className="min-w-0 flex-1 truncate rounded bg-muted px-2 py-1 text-xs">{value ?? "—"}</code>
        <button
          type="button"
          onClick={copy}
          disabled={!value}
          className="shrink-0 rounded-md border p-1.5 text-muted-foreground hover:bg-accent hover:text-foreground disabled:opacity-40"
          aria-label={`Copy ${label}`}
        >
          {copied ? <Check className="h-3.5 w-3.5" /> : <Copy className="h-3.5 w-3.5" />}
        </button>
      </div>
    </div>
  );
}
