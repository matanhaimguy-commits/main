import "@tanstack/react-start/server-only";

/**
 * The Studio: every content piece's production run (the studio's clients/<slug>/runs/<post_id>/ledger.json), step
 * by step, with its gates, files and the owner's checkpoints. The studio pushes through /api/studio/*
 * (growth-engine/tools/hub.py studio-*); the Studio page shows it and takes the owner's answers. Nothing here is
 * invented: steps, gates, scores and files are what the studio pushed. One job per file; this file only re-exports.
 */

export * from "./schema";
export type * from "./types";
export { StudioError } from "./errors";
export { currentStepOf, progressOf, runStatusOf } from "./steps";
export { sortRuns } from "./order";
export { openQueueItems } from "./queue";
export { answerProblem, decisionInputProblems, runInputProblems } from "./validate";
export { upsertRun } from "./runs-upsert.server";
export { findRun, listRuns } from "./runs-read.server";
export { runDetail } from "./run-detail.server";
export { fileMarkdown, listFiles, replaceFiles } from "./files.server";
export { createDecision } from "./decisions-create.server";
export { listDecisions } from "./decisions-list.server";
export { answerDecision } from "./decisions-answer.server";
export { markSynced } from "./decisions-synced.server";
export { getRuns, postRun } from "./api-runs.server";
export { getDecisions, postDecisions } from "./api-decisions.server";
export { postSynced } from "./api-synced.server";
export { withStudioToken } from "./api-common.server";
