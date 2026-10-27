import { useQuery } from "@tanstack/react-query";
import { ChevronDown, ExternalLink, FileText } from "lucide-react";
import { useState } from "react";
import { Markdown } from "@/components/app/markdown";
import { ErrorBlock } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { getStudioFileFn, type StudioFileView } from "@/lib/api/studio";
import { cn } from "@/lib/utils";

/** A doc: inline markdown opens in place (loaded on first open); a doc with only a link opens in a new tab. */
export function DocFile({ file }: { file: StudioFileView }) {
  const [open, setOpen] = useState(false);
  const doc = useQuery({
    queryKey: ["studio-file", file.id, file.updated_at],
    queryFn: () => getStudioFileFn({ data: { id: file.id } }),
    enabled: open && file.has_markdown,
    staleTime: Infinity,
  });
  if (!file.has_markdown) {
    return (
      <a href={file.url ?? "#"} target="_blank" rel="noreferrer" className="flex min-h-11 items-center gap-2 rounded-lg border px-3 py-2 text-sm hover:bg-accent/40">
        <FileText className="h-4 w-4 shrink-0 text-muted-foreground" />
        <span dir="auto" className="min-w-0 flex-1 font-medium">
          {file.label}
        </span>
        <ExternalLink className="h-4 w-4 shrink-0 text-muted-foreground" />
      </a>
    );
  }
  return (
    <div className={cn("rounded-lg border", open && "bg-background")}>
      <button type="button" onClick={() => setOpen(!open)} aria-expanded={open} className="flex min-h-11 w-full items-center gap-2 px-3 py-2 text-left text-sm">
        <FileText className="h-4 w-4 shrink-0 text-muted-foreground" />
        <span dir="auto" className="min-w-0 flex-1 font-medium">
          {file.label}
        </span>
        <span className="shrink-0 text-xs text-muted-foreground">{open ? "Close" : "Read"}</span>
        <ChevronDown className={cn("h-4 w-4 shrink-0 text-muted-foreground transition-transform", open && "rotate-180")} />
      </button>
      {open && (
        <div className="border-t px-3 py-3">
          {doc.isLoading && <p className="text-sm text-muted-foreground">Loading…</p>}
          {doc.error && <ErrorBlock error={doc.error} />}
          {doc.data && <Markdown source={doc.data.markdown} />}
          {doc.data && (
            <Button variant="ghost" size="sm" className="mt-3" onClick={() => setOpen(false)}>
              Close
            </Button>
          )}
        </div>
      )}
    </div>
  );
}
