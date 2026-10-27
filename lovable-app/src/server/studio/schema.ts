import { z } from "zod/v4";

/** What the studio may send: runs with their steps and gates, files, questions, and the owner's answers. */

export const STEP_STATUSES = ["done", "active", "blocked", "na", "pending"] as const;
export const GATE_STATUSES = ["PASS", "FAIL", "OVERRIDE", "PENDING"] as const;
export const RUN_STATUSES = ["active", "blocked", "done", "paused"] as const;
export const FILE_KINDS = ["doc", "audio", "image", "video"] as const;
export const DECISION_STATUSES = ["open", "answered", "synced"] as const;

export type StepStatus = (typeof STEP_STATUSES)[number];
export type GateStatus = (typeof GATE_STATUSES)[number];
export type RunStatus = (typeof RUN_STATUSES)[number];
export type FileKind = (typeof FILE_KINDS)[number];
export type DecisionStatus = (typeof DECISION_STATUSES)[number];

const HttpUrl = z.url({ protocol: /^https?$/ }).max(2000);
const StepNo = z.number().int().min(0).max(99);
const When = z.string().max(40);

export const GateInput = z.object({
  /** The gate code, e.g. G-SCRIPT. */
  gate: z.string().trim().min(1).max(60),
  /** A human name, e.g. "Script Lab". */
  label: z.string().max(120).optional(),
  status: z.enum(GATE_STATUSES),
  score: z.number().finite().optional(),
  /** The scale of the score (100 when left out). */
  max: z.number().positive().finite().optional(),
  by: z.string().max(120).optional(),
  at: When.optional(),
  note: z.string().max(4000).optional(),
  /** For a per-asset gate: the asset version, e.g. SB-H01@v2. */
  asset: z.string().max(100).optional(),
});
export type StudioGate = z.infer<typeof GateInput>;

export const StepInput = z.object({
  n: StepNo,
  name: z.string().trim().min(1).max(120),
  status: z.enum(STEP_STATUSES),
  note: z.string().max(4000).optional(),
  at: When.optional(),
  gates: z.array(GateInput).max(200).default([]),
});
export type StudioStep = z.infer<typeof StepInput>;

export const FileInput = z
  .object({
    /** The studio's id for the file (by default its path); a re-push with the same key updates it. */
    key: z.string().trim().min(1).max(300),
    step: StepNo.nullable().optional(),
    label: z.string().trim().min(1).max(200),
    kind: z.enum(FILE_KINDS),
    url: HttpUrl.optional(),
    markdown: z.string().max(300_000).optional(),
    sha256: z
      .string()
      .regex(/^[0-9a-f]{64}$/)
      .optional(),
  })
  .refine((f) => f.url !== undefined || f.markdown !== undefined, { message: "A file needs a url or inline markdown." })
  .refine((f) => f.kind === "doc" || f.url !== undefined, { message: "Audio, images and video need a url (upload them first)." });
export type FileInput = z.infer<typeof FileInput>;

export const RunInput = z.object({
  business: z.string().min(1).max(64),
  post_id: z.string().trim().min(1).max(120),
  title: z.string().max(200).optional(),
  format: z.string().max(60).optional(),
  family: z.string().max(60).optional(),
  /** Left out: the first step not done or skipped. */
  current_step: StepNo.nullable().optional(),
  /** Left out: worked out from the steps. */
  status: z.enum(RUN_STATUSES).optional(),
  waiting_on_owner: z.boolean().default(false),
  summary: z.string().max(300).optional(),
  steps: z.array(StepInput).max(40).default([]),
  ledger: z.record(z.string(), z.unknown()).default({}),
  /** When given, these are the run's files: missing keys are removed. Left out, the files stay as they are. */
  files: z.array(FileInput).max(100).optional(),
});
export type RunInput = z.infer<typeof RunInput>;

export const OptionInput = z.object({
  label: z.string().trim().min(1).max(120),
  description: z.string().max(2000).optional(),
});

export const DecisionInput = z.object({
  business: z.string().min(1).max(64),
  post_id: z.string().trim().min(1).max(120),
  /** One question per key and run; by default the checkpoint code. */
  key: z.string().trim().min(1).max(200).optional(),
  checkpoint: z.string().trim().min(1).max(60),
  step: StepNo.nullable().optional(),
  question: z.string().trim().min(1).max(2000),
  context: z.string().max(50_000).optional(),
  options: z.array(OptionInput).max(12).default([]),
  multi: z.boolean().default(false),
});
export type DecisionInput = z.infer<typeof DecisionInput>;

export const AnswerInput = z.object({
  choices: z.array(z.string().max(120)).max(12).default([]),
  note: z.string().max(4000).default(""),
});
export type AnswerInput = z.infer<typeof AnswerInput>;

export const SyncedInput = z.object({ ids: z.array(z.number().int().positive()).min(1).max(200) });
