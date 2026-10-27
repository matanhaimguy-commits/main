import type { StudioRunCard } from "@/lib/api/studio";
import { cn } from "@/lib/utils";
import { businessesOf, LIST_VIEWS } from "./list-views";

/** The tabs (In progress, Done, All) with their counts, and a business picker when there is more than one. */
export function RunListFilters({
  runs,
  view,
  onView,
  business,
  onBusiness,
}: {
  runs: StudioRunCard[] | undefined;
  view: string;
  onView: (id: string) => void;
  business: string;
  onBusiness: (slug: string) => void;
}) {
  const businesses = businessesOf(runs ?? []);
  return (
    <div className="mb-4 flex flex-wrap items-center gap-2">
      {LIST_VIEWS.map((x) => (
        <button
          key={x.id}
          onClick={() => onView(x.id)}
          className={cn("min-h-9 rounded-full border px-3.5 py-1.5 text-sm", x.id === view ? "bg-primary text-primary-foreground" : "bg-background")}
        >
          {x.label} {runs ? <span className="opacity-70">({runs.filter(x.match).length})</span> : null}
        </button>
      ))}
      {businesses.length > 1 && (
        <select className="ml-auto h-9 rounded-md border bg-background px-2 text-sm" value={business} onChange={(e) => onBusiness(e.target.value)}>
          <option value="">All businesses</option>
          {businesses.map(([slug, name]) => (
            <option key={slug} value={slug}>
              {name}
            </option>
          ))}
        </select>
      )}
    </div>
  );
}
