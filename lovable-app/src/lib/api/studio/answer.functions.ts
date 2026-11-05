import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import { asAdmin } from "@/server/admin.server";
import { AnswerInput, answerDecision, StudioError } from "@/server/studio/index.server";

/** The owner answers a checkpoint. Reviewers can look but not answer (asAdmin refuses them). */
export const answerStudioDecisionFn = createServerFn({ method: "POST" })
  .validator(z.object({ id: z.number().int().positive(), answer: AnswerInput }))
  .handler(async ({ data }) =>
    asAdmin(async (sql): Promise<{ ok: boolean; error?: string }> => {
      try {
        await answerDecision(sql, data.id, data.answer, "owner");
        return { ok: true };
      } catch (err) {
        if (err instanceof StudioError) return { ok: false, error: err.message };
        throw err;
      }
    }),
  );
