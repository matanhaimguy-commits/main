import type { StudioDecisionView, StudioFileView, StudioRunCard, StudioRunView, StudioStepView } from "@/lib/api/studio";

/** Sample page data for the Studio component tests. */

export const stepView = (n: number, status: StudioStepView["status"], extra: Partial<StudioStepView> = {}): StudioStepView => ({
  n,
  name: `Step ${n}`,
  status,
  note: null,
  at: null,
  gates: [],
  ...extra,
});

export const fileView = (id: number, kind: StudioFileView["kind"], extra: Partial<StudioFileView> = {}): StudioFileView => ({
  id,
  key: `f${id}`,
  step: null,
  label: `File ${id}`,
  kind,
  url: kind === "doc" ? null : `https://cdn.example/f${id}`,
  has_markdown: kind === "doc",
  markdown_chars: kind === "doc" ? 10 : 0,
  updated_at: "2026-10-27T10:00:00.000Z",
  ...extra,
});

export const decisionView = (id: number, extra: Partial<StudioDecisionView> = {}): StudioDecisionView => ({
  id,
  key: "G-HUMAN-SONG",
  checkpoint: "G-HUMAN-SONG",
  step: 4,
  question: "How should we make the song?",
  context: null,
  options: [
    { label: "Suno by hand", description: "You make it in Suno." },
    { label: "Atlas Suno", description: "Claude makes it through the gated command." },
  ],
  multi: false,
  status: "open",
  answer: null,
  answered_at: null,
  synced_at: null,
  created_at: "2026-10-27T10:00:00.000Z",
  ...extra,
});

export const runCard = (id: number, extra: Partial<StudioRunCard> = {}): StudioRunCard => ({
  id,
  business: "acme",
  business_name: "Acme",
  post_id: `AC-${id}`,
  title: null,
  format: "reel_song",
  family: "song",
  status: "active",
  waiting: false,
  open_decisions: 0,
  summary: null,
  current_step: 0,
  steps: [],
  progress: { done: 0, total: 0 },
  updated_at: "2026-10-27T10:00:00.000Z",
  ...extra,
});

export const runView = (extra: { steps?: StudioStepView[]; files?: StudioFileView[]; decisions?: StudioDecisionView[]; current_step?: number | null } = {}): StudioRunView => ({
  run: {
    id: 1,
    business: "acme",
    business_name: "Acme",
    post_id: "AC-1",
    title: "Maya's quilt",
    format: "reel_song",
    family: "song",
    status: "active",
    waiting_on_owner: false,
    summary: null,
    current_step: extra.current_step === undefined ? 3 : extra.current_step,
    steps: extra.steps ?? [stepView(3, "active"), stepView(4, "pending")],
    progress: { done: 0, total: 2 },
    updated_at: "2026-10-27T10:00:00.000Z",
    pushed_at: "2026-10-27T10:00:00.000Z",
  },
  files: extra.files ?? [],
  decisions: extra.decisions ?? [],
  queue: [],
});
