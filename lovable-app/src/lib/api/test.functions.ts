import { createServerFn } from "@tanstack/react-start";
import { z } from "zod/v4";
import type { ReplyResult } from "@/agent/ai/agent";
import type { Platform } from "@/agent/config/schema";
import { setState } from "@/agent/db/connections";
import type { Contact, LeadUpdate, MessageRow } from "@/agent/db/repo";
import type { Sql } from "@/agent/db/sql";
import { openerMessage, resolveLink } from "@/agent/engine/funnel";
import { screenComment } from "@/agent/logic/comments";
import { explainReason, selectCommentFunnel, selectMessageFunnel } from "@/agent/logic/funnels";
import { describeMessage } from "@/agent/meta/messages";
import { asAdmin } from "@/server/admin.server";
import { recordServerError } from "@/server/error-log.server";
import { createRuntimeDeps } from "@/server/runtime.server";

/** Chat with the bot as a customer. Nothing is sent to Meta and nothing is saved. */
export interface TestChatState {
  platform: Platform;
  msgs: { d: "in" | "out"; t: string }[];
  /** What the AI saved about the lead so far (a LeadUpdate). */
  lead: Record<string, any>;
  notes: string[];
}

const ChatState = z.object({
  platform: z.enum(["instagram", "facebook"]),
  msgs: z.array(z.object({ d: z.enum(["in", "out"]), t: z.string().max(4000) })).max(60),
  lead: z.record(z.string(), z.unknown()),
  notes: z.array(z.string()).max(100),
});

/** Answer before the hosting platform gives up on the request, with a clear message instead. */
const AI_TIME_LIMIT_MS = 45_000;

class TimeLimitError extends Error {}

function withTimeLimit<T>(work: Promise<T>, ms: number): Promise<T> {
  let timer: ReturnType<typeof setTimeout> | undefined;
  const limit = new Promise<never>((_, reject) => {
    timer = setTimeout(() => reject(new TimeLimitError(`no answer after ${ms / 1000}s`)), ms);
  });
  return Promise.race([work, limit]).finally(() => clearTimeout(timer));
}

export const testChatFn = createServerFn({ method: "POST" })
  .validator(z.object({ slug: z.string(), state: ChatState, text: z.string().min(1).max(1000) }))
  .handler(async ({ data }) =>
    asAdmin(async (sql): Promise<{ state: TestChatState; error: string | null }> => {
      try {
        return await testChat(sql, data);
      } catch (err) {
        await recordServerError("test chat", err);
        return { state: data.state as TestChatState, error: `Something went wrong: ${(err as Error).message}` };
      }
    }),
  );

async function testChat(
  sql: Sql,
  data: { slug: string; state: z.infer<typeof ChatState>; text: string },
): Promise<{ state: TestChatState; error: string | null }> {
  const chat = structuredClone(data.state) as TestChatState;
  const { deps } = await createRuntimeDeps(sql);
  const b = deps.registry.bySlug(data.slug);
  if (!b) return { state: chat, error: "This business has a problem in its details. Fix it on the business page first." };
  if (!deps.ai) return { state: chat, error: "Add the Claude API key in Settings to talk to the bot." };
  chat.msgs.push({ d: "in", t: data.text });
  const now = new Date();
  const lead = chat.lead as LeadUpdate;
  const contact: Contact = {
    id: 0,
    business: b.slug,
    platform: chat.platform,
    external_id: "admin-test",
    username: null,
    name: lead.name ?? null,
    phone: lead.phone ?? null,
    email: lead.email ?? null,
    stage: lead.stage ?? (chat.msgs.length > 1 ? "engaged" : "new"),
    interest: lead.interest ?? null,
    budget: lead.budget ?? null,
    timeline: lead.timeline ?? null,
    notes: lead.notes ?? null,
    source: "dashboard test",
    follows_business: null,
    opted_out: false,
    ai_paused_until: null,
    ai_pause_reason: null,
    needs_reply: true,
    reply_due_at: null,
    last_inbound_at: now,
    last_outbound_at: null,
    followup_for: null,
    created_at: now,
  };
  const transcript: MessageRow[] = chat.msgs.map((m, i) => ({
    id: i,
    contact_id: 0,
    direction: m.d,
    source: m.d === "in" ? "user" : "ai",
    mid: null,
    text: m.t,
    payload: null,
    created_at: now,
  }));
  let res: ReplyResult;
  const started = Date.now();
  // Kept in app_state so a slow or failed answer can be looked at afterwards.
  const record = (status: string, extra: Record<string, unknown> = {}) =>
    setState(sql, "last_test_chat", { at: new Date(started).toISOString(), status, ms: Date.now() - started, ...extra }).catch(() => {});
  await record("started");
  try {
    res = await withTimeLimit(deps.ai.reply({ business: b, contact, transcript, mode: "reply", now }), AI_TIME_LIMIT_MS);
  } catch (err) {
    chat.msgs.pop();
    if (err instanceof TimeLimitError) {
      await record("timeout");
      return { state: chat, error: `Claude did not answer within ${AI_TIME_LIMIT_MS / 1000} seconds. Try again; if it keeps happening, lower the thinking effort on the business page.` };
    }
    await record("failed", { error: (err as Error).message.slice(0, 500) });
    return { state: chat, error: `The AI call failed: ${(err as Error).message}` };
  }
  await record("done", { model: res.usage.model, input: res.usage.inputTokens, output: res.usage.outputTokens });
  const link = res.linkId ? b.links.find((l) => l.id === res.linkId) : undefined;
  if (res.text) chat.msgs.push({ d: "out", t: res.text + (link ? `\n[ ${link.title} → ${link.url} ]` : "") });
  for (const [k, v] of Object.entries(res.lead)) if (v) (chat.lead as Record<string, unknown>)[k] = v;
  if (Object.keys(res.lead).length) chat.notes.push(`Saved to the lead: ${JSON.stringify(res.lead)}`);
  if (res.handoff) chat.notes.push(`Handed to a person (${res.handoff.reason}). In real use the AI pauses here and you get an alert.`);
  if (res.optOut) chat.notes.push("The customer opted out.");
  if (!res.text) chat.notes.push("The AI chose not to reply.");
  chat.notes.push(`Answered in ${((Date.now() - started) / 1000).toFixed(1)} s by ${res.usage.model}.`);
  return { state: chat, error: null };
}

export interface CommentSimulation {
  fires: boolean;
  summary: string;
  publicReplies: string[];
  steps: { title: string; message: string }[];
  notes: string[];
}

/** Which funnel a comment would trigger and exactly what the person would receive. Nothing is sent. */
export const simulateCommentFn = createServerFn({ method: "POST" })
  .validator(
    z.object({ slug: z.string(), platform: z.enum(["instagram", "facebook"]), postId: z.string().max(100).optional(), text: z.string().max(2000) }),
  )
  .handler(async ({ data }) =>
    asAdmin(async (sql): Promise<CommentSimulation> => {
      const { deps } = await createRuntimeDeps(sql);
      const b = deps.registry.bySlug(data.slug);
      if (!b) return { fires: false, summary: "This business has a problem in its details.", publicReplies: [], steps: [], notes: [] };
      const postId = data.postId?.trim() || undefined;
      const skip = screenComment(
        {
          type: "comment",
          platform: data.platform,
          accountId: "",
          commentId: "test",
          ...(postId ? { postId } : {}),
          authorId: "someone",
          text: data.text,
          createdAt: new Date(),
          verb: "add",
        },
        b,
      );
      if (skip) return { fires: false, summary: `Skipped: ${explainReason(skip)}.`, publicReplies: [], steps: [], notes: [] };
      const d = selectCommentFunnel(b.funnels, { platform: data.platform, postId, text: data.text });
      if (d.kind === "matched") {
        const f = d.funnel;
        const steps = [{ title: "Private reply to the comment", message: describeMessage(openerMessage(b, f)) }];
        if (f.opener.mode === "tap") {
          steps.push({
            title: "After they tap the button",
            message: describeMessage({ text: f.deliver.text, button: { title: f.deliver.button, url: resolveLink(b, f.deliver.link) } }),
          });
          if (f.after) steps.push({ title: "Then", message: f.after });
        }
        return { fires: true, summary: `Funnel "${f.id}" fires (keyword "${d.keyword}").`, publicReplies: f.public_replies, steps, notes: [] };
      }
      const notes: string[] = [];
      if (b.ai.comment_replies || b.ai.comment_dms) notes.push("The AI would look at this comment and decide whether to answer it.");
      const story = selectMessageFunnel(b.funnels, { platform: data.platform, trigger: "story_reply", text: data.text });
      if (story.kind === "matched") notes.push(`As a story reply it would fire "${story.funnel.id}".`);
      return {
        fires: false,
        summary: `No DM: ${explainReason(d.reason)}${d.funnel ? ` (${d.funnel.id})` : ""}.`,
        publicReplies: [],
        steps: [],
        notes,
      };
    }),
  );
