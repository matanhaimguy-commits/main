import { progressOf } from "@/server/studio/steps";
import type { RunDetail, RunListRow, StudioDecisionRow, StudioFileRow } from "@/server/studio/types";
import type { StudioDecisionView, StudioFileView, StudioRunCard, StudioRunView } from "./views";

/** Database rows to what the pages get. */

const iso = (d: Date | string | null | undefined) => (d ? new Date(d).toISOString() : null);
const stepsOf = <T>(v: T[] | null | undefined): T[] => (Array.isArray(v) ? v : []);

export function toRunCard(r: RunListRow): StudioRunCard {
  const steps = stepsOf(r.steps);
  return {
    id: Number(r.id),
    business: r.business,
    business_name: r.business_name,
    post_id: r.post_id,
    title: r.title,
    format: r.format,
    family: r.family,
    status: r.status,
    waiting: r.waiting,
    open_decisions: r.open_decisions,
    summary: r.summary,
    current_step: r.current_step,
    steps: steps.map((s) => ({ n: s.n, name: s.name, status: s.status })),
    progress: progressOf(steps),
    updated_at: iso(r.updated_at)!,
  };
}

export function toFileView(f: StudioFileRow): StudioFileView {
  return {
    id: Number(f.id),
    key: f.key,
    step: f.step,
    label: f.label,
    kind: f.kind,
    url: f.url,
    has_markdown: f.has_markdown,
    markdown_chars: f.markdown_chars,
    updated_at: iso(f.updated_at)!,
  };
}

export function toDecisionView(d: StudioDecisionRow): StudioDecisionView {
  return {
    id: Number(d.id),
    key: d.key,
    checkpoint: d.checkpoint,
    step: d.step,
    question: d.question,
    context: d.context,
    options: stepsOf(d.options),
    multi: d.multi,
    status: d.status,
    answer: d.answer,
    answered_at: iso(d.answered_at),
    synced_at: iso(d.synced_at),
    created_at: iso(d.created_at)!,
  };
}

export function toRunView(d: RunDetail): StudioRunView {
  const r = d.run;
  const steps = stepsOf(r.steps);
  return {
    run: {
      id: Number(r.id),
      business: r.business,
      business_name: r.business_name,
      post_id: r.post_id,
      title: r.title,
      format: r.format,
      family: r.family,
      status: r.status,
      waiting_on_owner: r.waiting_on_owner,
      summary: r.summary,
      current_step: r.current_step,
      steps: steps.map((s) => ({ n: s.n, name: s.name, status: s.status, note: s.note ?? null, at: s.at ?? null, gates: s.gates ?? [] })),
      progress: progressOf(steps),
      updated_at: iso(r.updated_at)!,
      pushed_at: iso(r.pushed_at)!,
    },
    files: d.files.map(toFileView),
    decisions: d.decisions.map(toDecisionView),
    queue: d.queue,
  };
}
