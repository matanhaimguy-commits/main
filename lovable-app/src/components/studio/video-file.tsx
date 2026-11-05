import type { StudioFileView } from "@/lib/api/studio";
import { cn } from "@/lib/utils";
import { FileHead } from "./file-head";

/** A video that plays inline on a phone. `compact` keeps it small inside a question. */
export function VideoFile({ file, compact }: { file: StudioFileView; compact?: boolean }) {
  return (
    <div className="space-y-1.5">
      <FileHead file={file} />
      {file.url && (
        <video
          src={file.url}
          controls
          playsInline
          preload="metadata"
          className={cn("w-full rounded-lg bg-black", compact ? "max-h-80" : "max-h-[32rem]")}
        />
      )}
    </div>
  );
}
