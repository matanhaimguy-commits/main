import type { StudioFileView } from "@/lib/api/studio";
import { FileHead } from "./file-head";

export function AudioFile({ file }: { file: StudioFileView }) {
  return (
    <div className="space-y-1.5">
      <FileHead file={file} />
      {file.url && <audio src={file.url} controls preload="metadata" className="w-full" />}
    </div>
  );
}
