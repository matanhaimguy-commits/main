import "@tanstack/react-start/server-only";
import { createAlerter } from "@/agent/alerts";
import { resolveLink } from "@/agent/engine/funnel";
import { LeadError, submitLead, type LeadInput } from "@/agent/engine/leads";
import { log } from "@/agent/log";
import { getDb } from "./db.server";
import { recordServerError } from "./error-log.server";
import { loadBusinesses } from "./runtime.server";
import { loadRuntimeEnv } from "./settings.server";

export interface LeadFormInfo {
  slug: string;
  name: string;
  language: "en" | "sq" | "he";
  title: string | null;
  intro: string | null;
  afterUrl: string | null;
  afterTitle: string | null;
}

async function findBusiness(slug: string) {
  const { businesses } = await loadBusinesses(getDb());
  const b = businesses.find((x) => x.slug === slug);
  return b && b.enabled && b.lead_form.enabled ? b : undefined;
}

/** What the public form page needs; nothing private (no profile, no settings). */
export async function leadFormInfo(slug: string): Promise<LeadFormInfo | null> {
  const b = await findBusiness(slug);
  if (!b) return null;
  const f = b.lead_form;
  const link = f.after_link ? b.links.find((l) => l.id === f.after_link) : undefined;
  return {
    slug: b.slug,
    name: b.name,
    language: f.language,
    title: f.title ?? null,
    intro: f.intro ?? null,
    afterUrl: f.after_link ? resolveLink(b, f.after_link) : null,
    afterTitle: link?.title ?? null,
  };
}

export type LeadResult = { ok: true } | { ok: false; reason: "unknown" | "phone" | "name" | "busy" | "error" };

export async function submitLeadForm(slug: string, input: LeadInput & { website?: string }): Promise<LeadResult> {
  // The hidden "website" field is only ever filled by bots.
  if (input.website) return { ok: true };
  const b = await findBusiness(slug);
  if (!b) return { ok: false, reason: "unknown" };
  const sql = getDb();
  try {
    const { env } = await loadRuntimeEnv(sql);
    await submitLead({ sql, alert: createAlerter(env, sql, log) }, b, input);
    return { ok: true };
  } catch (err) {
    if (err instanceof LeadError) return { ok: false, reason: err.message as "phone" | "name" | "busy" };
    await recordServerError("lead form", err);
    return { ok: false, reason: "error" };
  }
}
