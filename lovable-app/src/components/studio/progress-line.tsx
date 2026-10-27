/** "Step 4 · Audio" and "4 of 16 done", under a progress bar. */
export function ProgressLine({
  status,
  current,
  progress,
}: {
  status: string;
  current: { n: number; name: string } | undefined;
  progress: { done: number; total: number };
}) {
  return (
    <div className="flex flex-wrap items-baseline justify-between gap-x-3 text-sm">
      <span className="font-medium">{status === "done" ? "All steps done" : current ? `Step ${current.n} · ${current.name}` : "No current step"}</span>
      <span className="text-xs tabular-nums text-muted-foreground">
        {progress.done} of {progress.total} done
      </span>
    </div>
  );
}
