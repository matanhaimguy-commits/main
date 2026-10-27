import type { StudioFileView } from "@/lib/api/studio";
import { cn } from "@/lib/utils";
import { FileHead } from "./file-head";

/** An image at its own proportions; tap to open it full size. `compact` keeps it small inside a question. */
export function ImageFile({ file, compact }: { file: StudioFileView; compact?: boolean }) {
  return (
    <div className="space-y-1.5">
      <FileHead file={file} />
      {file.url && (
        <a href={file.url} target="_blank" rel="noreferrer" className="block">
          <img
            src={file.url}
            alt={file.label}
            loading="lazy"
            className={cn("w-auto max-w-full rounded-lg border object-contain", compact ? "max-h-64" : "max-h-[28rem]")}
          />
        </a>
      )}
    </div>
  );
}
