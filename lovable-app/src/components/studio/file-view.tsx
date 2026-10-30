import type { StudioFileView } from "@/lib/api/studio";
import { AudioFile } from "./audio-file";
import { DocFile } from "./doc-file";
import { ImageFile } from "./image-file";
import { VideoFile } from "./video-file";

/** Shows a file the way its kind needs: docs readable, audio with a player, images and video inline. */
export function FileView({ file, compact }: { file: StudioFileView; compact?: boolean }) {
  switch (file.kind) {
    case "doc":
      return <DocFile file={file} />;
    case "audio":
      return <AudioFile file={file} />;
    case "image":
      return <ImageFile file={file} compact={compact} />;
    case "video":
      return <VideoFile file={file} compact={compact} />;
  }
}
