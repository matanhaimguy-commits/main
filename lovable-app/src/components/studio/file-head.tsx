import { ExternalLink, FileText, Film, ImageIcon, Music } from "lucide-react";
import type { StudioFileView } from "@/lib/api/studio";

const ICON = { doc: FileText, audio: Music, image: ImageIcon, video: Film };

/** A file's icon, label and "open in a new tab" link. */
export function FileHead({ file }: { file: StudioFileView }) {
  const Icon = ICON[file.kind];
  return (
    <div className="flex items-center gap-2 text-sm">
      <Icon className="h-4 w-4 shrink-0 text-muted-foreground" />
      <span dir="auto" className="min-w-0 flex-1 font-medium">
        {file.label}
      </span>
      {file.url && (
        <a href={file.url} target="_blank" rel="noreferrer" className="shrink-0 p-1 text-muted-foreground hover:text-foreground" aria-label="Open the file">
          <ExternalLink className="h-4 w-4" />
        </a>
      )}
    </div>
  );
}
