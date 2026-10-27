import { Pill } from "@/components/app/shell";
import { Card, CardContent } from "@/components/ui/card";
import type { QueueItem } from "@/lib/api/studio";
import { timeAgo } from "@/lib/format";

/** What the studio's own queue says waits on the owner but has no question on the page yet. */
export function QueueCard({ items }: { items: QueueItem[] }) {
  if (items.length === 0) return null;
  return (
    <Card className="border-amber-200">
      <CardContent className="space-y-2 p-4">
        <div className="text-sm font-semibold">Also waiting on you in the studio's queue</div>
        <p className="text-xs text-muted-foreground">These have no question on this page yet; answer them in chat.</p>
        <ul className="space-y-2">
          {items.map((q) => (
            <li key={q.id} className="rounded-lg bg-muted/60 p-2.5 text-sm">
              <div className="flex flex-wrap items-center gap-2">
                <Pill tone="amber">{q.checkpoint}</Pill>
                {q.asset && <span className="text-xs text-muted-foreground">{q.asset}</span>}
                {q.asked_at && <span className="ml-auto text-xs text-muted-foreground">asked {timeAgo(q.asked_at)}</span>}
              </div>
              {q.note && (
                <p dir="auto" className="mt-1.5 whitespace-pre-wrap">
                  {q.note}
                </p>
              )}
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  );
}
