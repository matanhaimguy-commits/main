import type { DecisionAnswer, DecisionStatus, FileKind, QueueItem, RunStatus, StepStatus, StudioGate } from "@/server/studio/index.server";

/** What the Studio pages receive: plain JSON, timestamps as ISO strings. */

export type { QueueItem, StudioGate };

export interface StudioStepView {
  n: number;
  name: string;
  status: StepStatus;
  note: string | null;
  at: string | null;
  gates: StudioGate[];
}

export interface StudioRunCard {
  id: number;
  business: string;
  business_name: string;
  post_id: string;
  title: string | null;
  format: string | null;
  family: string | null;
  status: RunStatus;
  /** An open question, or the studio's own "waiting on the owner" flag. */
  waiting: boolean;
  open_decisions: number;
  summary: string | null;
  current_step: number | null;
  steps: { n: number; name: string; status: StepStatus }[];
  progress: { done: number; total: number };
  updated_at: string;
}

export interface StudioFileView {
  id: number;
  key: string;
  step: number | null;
  label: string;
  kind: FileKind;
  url: string | null;
  has_markdown: boolean;
  markdown_chars: number;
  updated_at: string;
}

export interface StudioDecisionView {
  id: number;
  key: string;
  checkpoint: string;
  step: number | null;
  question: string;
  context: string | null;
  options: { label: string; description?: string }[];
  multi: boolean;
  status: DecisionStatus;
  answer: DecisionAnswer | null;
  answered_at: string | null;
  synced_at: string | null;
  created_at: string;
}

export interface StudioRunHeader {
  id: number;
  business: string;
  business_name: string;
  post_id: string;
  title: string | null;
  format: string | null;
  family: string | null;
  status: RunStatus;
  waiting_on_owner: boolean;
  summary: string | null;
  current_step: number | null;
  steps: StudioStepView[];
  progress: { done: number; total: number };
  updated_at: string;
  pushed_at: string;
}

export interface StudioRunView {
  run: StudioRunHeader;
  files: StudioFileView[];
  decisions: StudioDecisionView[];
  queue: QueueItem[];
}
