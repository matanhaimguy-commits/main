import type { ReactNode } from "react";

export function EmptyState({ children }: { children: ReactNode }) {
  return <div className="rounded-xl border bg-background p-10 text-center text-sm text-muted-foreground">{children}</div>;
}
