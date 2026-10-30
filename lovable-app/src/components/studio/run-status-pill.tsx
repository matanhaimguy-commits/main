import { cn } from "@/lib/utils";
import { RUN_LABEL, type RunStatus } from "./labels";

const TONE: Record<RunStatus, string> = {
  active: "bg-sky-100 text-sky-800",
  blocked: "bg-rose-100 text-rose-800",
  done: "bg-emerald-100 text-emerald-800",
  paused: "bg-muted text-muted-foreground",
};

export function RunStatusPill({ status }: { status: RunStatus }) {
  return <span className={cn("inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium", TONE[status])}>{RUN_LABEL[status]}</span>;
}
