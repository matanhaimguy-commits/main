import { Hand } from "lucide-react";
import type { ReactNode } from "react";

/** The prominent "Waiting on you" badge. */
export function WaitingBadge({ children }: { children?: ReactNode }) {
  return (
    <span className="inline-flex items-center gap-1.5 rounded-full bg-amber-500 px-3 py-1 text-sm font-semibold text-white shadow-sm">
      <Hand className="h-4 w-4" />
      {children ?? "Waiting on you"}
    </span>
  );
}
