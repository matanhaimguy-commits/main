import { Card, CardContent } from "@/components/ui/card";
import type { StudioFileView } from "@/lib/api/studio";
import { FileView } from "./file-view";

/** Files of the whole run (not tied to a step). */
export function RunFiles({ files }: { files: StudioFileView[] }) {
  if (files.length === 0) return null;
  return (
    <section className="space-y-2">
      <h2 className="text-base font-semibold">Files</h2>
      <Card>
        <CardContent className="space-y-3 p-4">
          {files.map((f) => (
            <FileView key={f.id} file={f} />
          ))}
        </CardContent>
      </Card>
    </section>
  );
}
