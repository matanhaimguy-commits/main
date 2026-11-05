import type { DecisionStatus, FileKind, RunStatus, StudioStep } from "./schema";

/** Rows as the database hands them back (timestamps as Dates, jsonb as objects). */

export interface StudioRunRow {
  id: number;
  business: string;
  post_id: string;
  title: string | null;
  format: string | null;
  family: string | null;
  current_step: number | null;
  status: RunStatus;
  waiting_on_owner: boolean;
  summary: string | null;
  steps: StudioStep[];
  pushed_at: Date;
  created_at: Date;
  updated_at: Date;
}

export interface RunListRow extends StudioRunRow {
  business_name: string;
  open_decisions: number;
  /** An open question, or the studio's own "waiting on the owner" flag. */
  waiting: boolean;
}

export interface StudioFileRow {
  id: number;
  run_id: number;
  key: string;
  step: number | null;
  label: string;
  kind: FileKind;
  url: string | null;
  sha256: string | null;
  position: number;
  has_markdown: boolean;
  markdown_chars: number;
  updated_at: Date;
}

export interface DecisionAnswer {
  choices: string[];
  note: string;
  by: string;
  at: string;
}

export interface StudioDecisionRow {
  id: number;
  run_id: number;
  key: string;
  checkpoint: string;
  step: number | null;
  question: string;
  context: string | null;
  options: { label: string; description?: string }[];
  multi: boolean;
  status: DecisionStatus;
  answer: DecisionAnswer | null;
  answered_at: Date | null;
  synced_at: Date | null;
  created_at: Date;
  updated_at: Date;
}

export interface DecisionListRow extends StudioDecisionRow {
  business: string;
  post_id: string;
  run_title: string | null;
}

/** An open item of the run's ledger queue (the studio's own list of what waits on the owner). */
export interface QueueItem {
  id: string;
  checkpoint: string;
  asset: string | null;
  note: string;
  asked_at: string | null;
}

export interface RunDetail {
  run: StudioRunRow & { business_name: string };
  files: StudioFileRow[];
  decisions: DecisionListRow[];
  queue: QueueItem[];
}
