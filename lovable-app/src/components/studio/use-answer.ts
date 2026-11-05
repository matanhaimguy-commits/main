import { useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { answerStudioDecisionFn } from "@/lib/api/studio";
import { errorText } from "@/lib/format";

/** Saves the owner's answer to a question of run `runId`, says how it went, and refreshes the Studio pages. */
export function useAnswer(runId: number) {
  const qc = useQueryClient();
  return async (decisionId: number, choices: string[], note: string): Promise<boolean> => {
    try {
      const res = await answerStudioDecisionFn({ data: { id: decisionId, answer: { choices, note } } });
      if (!res.ok) toast.error(res.error ?? "That did not work.");
      else toast.success("Answer saved. The studio picks it up next.");
      return res.ok;
    } catch (err) {
      toast.error(errorText(err));
      return false;
    } finally {
      await qc.invalidateQueries({ queryKey: ["studio-run", runId] });
      await qc.invalidateQueries({ queryKey: ["studio"] });
    }
  };
}
