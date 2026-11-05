import type { StudioFileView, StudioStepView } from "@/lib/api/studio";
import { FileView } from "./file-view";
import { GateList } from "./gate-list";

/** An open step: its note, every gate record, and its files. */
export function StepDetails({ step, files }: { step: StudioStepView; files: StudioFileView[] }) {
  return (
    <div className="space-y-4 border-t px-3 py-3">
      {step.note && (
        <p dir="auto" className="whitespace-pre-wrap text-sm">
          {step.note}
        </p>
      )}
      {step.gates.length > 0 && <GateList gates={step.gates} />}
      {files.length > 0 && (
        <div className="space-y-3">
          <div className="text-xs font-medium uppercase tracking-wide text-muted-foreground">Files</div>
          {files.map((f) => (
            <FileView key={f.id} file={f} />
          ))}
        </div>
      )}
    </div>
  );
}
