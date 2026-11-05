import Anthropic from '@anthropic-ai/sdk';
import { betaZodOutputFormat } from '@anthropic-ai/sdk/helpers/beta/zod';
import { z } from 'zod/v4';
import type { Business, Platform } from '../config/schema';
import { STAGES, type Contact, type LeadUpdate, type MessageRow } from '../db/repo';
import { commentTriagePrompt, contactCard, describeRow, dmSystemPrompt, followupInstruction, renderTranscript } from './prompts';

export interface Usage {
  model: string;
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens: number;
  stopReason: string | null;
}

export interface ReplyInput {
  business: Business;
  contact: Contact;
  transcript: MessageRow[];
  mode: 'reply' | 'followup';
  now: Date;
}

export interface ReplyResult {
  /** null means: send nothing. */
  text: string | null;
  linkId?: string;
  lead: LeadUpdate;
  handoff?: { reason: string; summary: string; urgent: boolean };
  optOut: boolean;
  usage: Usage;
}

export const CommentDecisionSchema = z.object({
  intent: z.enum(['question', 'pricing', 'buying_intent', 'praise', 'complaint', 'tag_friend', 'spam', 'other']),
  public_reply: z.string().nullable(),
  send_dm: z.boolean(),
  dm_text: z.string().nullable(),
  hide: z.boolean(),
  alert_owner: z.boolean(),
  reason: z.string(),
});
export type CommentDecision = z.infer<typeof CommentDecisionSchema>;

export interface CommentInput {
  business: Business;
  platform: Platform;
  text: string;
  authorName?: string;
}

export interface SalesAi {
  reply(input: ReplyInput): Promise<ReplyResult>;
  triageComment(input: CommentInput): Promise<{ decision: CommentDecision; usage: Usage }>;
}

// ---- tools -------------------------------------------------------------------

const nullableString = (description: string) => ({ anyOf: [{ type: 'string' }, { type: 'null' }], description });

function toolDefs(b: Business): Anthropic.Beta.BetaTool[] {
  const tools: Anthropic.Beta.BetaTool[] = [
    {
      name: 'update_lead',
      description:
        'Save what you learned about this person and/or change their lead stage. Use null for anything you did not learn this turn; existing values are kept.',
      strict: true,
      input_schema: {
        type: 'object',
        properties: {
          name: nullableString('Their name'),
          phone: nullableString('Phone number, as given'),
          email: nullableString('Email address'),
          interest: nullableString('What they want, in a few words'),
          budget: nullableString('Budget, as given'),
          timeline: nullableString('When they want it'),
          note: nullableString('Anything else worth remembering, one line'),
          stage: { type: 'string', enum: ['unchanged', ...STAGES], description: 'New lead stage, or "unchanged"' },
        },
        required: ['name', 'phone', 'email', 'interest', 'budget', 'timeline', 'note', 'stage'],
        additionalProperties: false,
      },
    },
    {
      name: 'handoff_to_human',
      description:
        'Hand this conversation to a person on the team. The automated assistant stops replying in this thread until the team resumes it. Still write a short reply telling the customer the team will get back to them.',
      strict: true,
      input_schema: {
        type: 'object',
        properties: {
          reason: { type: 'string', description: 'Why a person is needed' },
          summary: { type: 'string', description: 'Two or three lines the team needs to pick this up' },
          urgent: { type: 'boolean', description: 'True for angry customers or hot leads ready to buy now' },
        },
        required: ['reason', 'summary', 'urgent'],
        additionalProperties: false,
      },
    },
    {
      name: 'opt_out',
      description: 'The person asked to stop receiving messages. Then reply with a one-line polite confirmation.',
      strict: true,
      input_schema: {
        type: 'object',
        properties: { reason: { type: 'string' } },
        required: ['reason'],
        additionalProperties: false,
      },
    },
  ];
  if (b.links.length > 0) {
    tools.unshift({
      name: 'attach_link',
      description: 'Attach one of the business links as a button under your reply. At most one link per reply.',
      strict: true,
      input_schema: {
        type: 'object',
        properties: { link_id: { type: 'string', enum: b.links.map((l) => l.id) } },
        required: ['link_id'],
        additionalProperties: false,
      },
    });
  }
  return tools;
}

const LeadInput = z.object({
  name: z.string().nullable(),
  phone: z.string().nullable(),
  email: z.string().nullable(),
  interest: z.string().nullable(),
  budget: z.string().nullable(),
  timeline: z.string().nullable(),
  note: z.string().nullable(),
  stage: z.enum(['unchanged', ...STAGES] as [string, ...string[]]),
});
const HandoffInput = z.object({ reason: z.string(), summary: z.string(), urgent: z.boolean() });
const LinkInput = z.object({ link_id: z.string() });

// ---- helpers -----------------------------------------------------------------

/** Transcript rows to alternating user/assistant turns that start with a user turn. */
export function toApiMessages(rows: MessageRow[]): Anthropic.Beta.BetaMessageParam[] {
  const out: { role: 'user' | 'assistant'; content: string }[] = [];
  for (const row of rows) {
    const role = row.direction === 'in' ? 'user' : 'assistant';
    const text = describeRow(row);
    const last = out[out.length - 1];
    if (last && last.role === role) last.content += `\n${text}`;
    else out.push({ role, content: text });
  }
  if (out[0]?.role === 'assistant') out.unshift({ role: 'user', content: '[The business started this conversation.]' });
  return out;
}

const URL_RE = /\bhttps?:\/\/[^\s)]+/gi;

/** DMs don't render markdown, and the model must never invent a URL. */
export function cleanReply(text: string, b: Business): string {
  const allowed = b.links.map((l) => l.url);
  return text
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/__(.+?)__/g, '$1')
    .replace(/^#{1,6}\s*/gm, '')
    .replace(URL_RE, (url) => (allowed.some((a) => url.startsWith(a)) ? url : ''))
    .replace(/[ \t]+\n/g, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

function emptyUsage(model: string): Usage {
  return { model, inputTokens: 0, outputTokens: 0, cacheReadTokens: 0, stopReason: null };
}

function addUsage(u: Usage, res: Anthropic.Beta.BetaMessage) {
  u.model = res.model;
  u.inputTokens += res.usage.input_tokens;
  u.outputTokens += res.usage.output_tokens;
  u.cacheReadTokens += res.usage.cache_read_input_tokens ?? 0;
  u.stopReason = res.stop_reason;
}

// ---- Claude implementation ---------------------------------------------------------

export interface ClaudeAiOptions {
  model: string;
  apiKey?: string;
  client?: Anthropic;
  maxToolRounds?: number;
}

// Safety classifiers can decline a benign request; "default" re-runs a declined request on
// Anthropic's recommended fallback model instead of failing. Only these models offer it
// (Claude Haiku 5.5 has no server-side fallback), so other models get a plain request.
const FALLBACK = { betas: ['server-side-fallback-2026-07-01'], fallbacks: 'default' as const };
export const fallbackFor = (model: string) => (/^claude-(opus-5|fable-5|sonnet-5-5)/.test(model) ? FALLBACK : {});

export function createClaudeAi(opts: ClaudeAiOptions): SalesAi {
  const client = opts.client ?? new Anthropic(opts.apiKey ? { apiKey: opts.apiKey } : {});
  const maxRounds = opts.maxToolRounds ?? 5;

  return {
    async reply({ business: b, contact, transcript, mode, now }) {
      const model = b.ai.model ?? opts.model;
      const usage = emptyUsage(model);
      const result: ReplyResult = { text: null, lead: {}, optOut: false, usage };

      let messages: Anthropic.Beta.BetaMessageParam[];
      if (mode === 'followup') {
        const last = contact.last_outbound_at ?? now;
        const hours = (now.getTime() - last.getTime()) / 3_600_000;
        messages = [{ role: 'user', content: `${followupInstruction(hours)}\n\n${renderTranscript(transcript)}` }];
      } else {
        messages = toApiMessages(transcript);
        if (messages.length === 0 || messages[messages.length - 1]!.role !== 'user') return result;
      }

      const system: Anthropic.Beta.BetaTextBlockParam[] = [
        { type: 'text', text: dmSystemPrompt(b), cache_control: { type: 'ephemeral' } },
        { type: 'text', text: contactCard(b, contact, now) },
      ];
      const tools = toolDefs(b);

      for (let round = 0; round < maxRounds; round++) {
        const res = await client.beta.messages.create({
          ...fallbackFor(model),
          model,
          max_tokens: 16000,
          output_config: { effort: b.ai.effort },
          system,
          tools,
          messages,
        });
        addUsage(usage, res);

        if (res.stop_reason === 'refusal') {
          result.text = null;
          result.handoff = {
            reason: 'The assistant declined to answer this conversation.',
            summary: 'Automated reply was declined by the model; please answer manually.',
            urgent: false,
          };
          return result;
        }

        const toolUses = res.content.filter((c): c is Anthropic.Beta.BetaToolUseBlock => c.type === 'tool_use');
        const text = res.content
          .filter((c): c is Anthropic.Beta.BetaTextBlock => c.type === 'text')
          .map((c) => c.text)
          .join('\n')
          .trim();
        if (res.stop_reason !== 'tool_use' || toolUses.length === 0) {
          if (mode === 'followup' && /^SKIP\.?$/i.test(text)) return result;
          result.text = text ? cleanReply(text, b) || null : null;
          return result;
        }

        const results: Anthropic.Beta.BetaToolResultBlockParam[] = toolUses.map((use) => {
          const content = runTool(use, b, result);
          return { type: 'tool_result', tool_use_id: use.id, content: content.text, is_error: content.error };
        });
        // The tools only record things. When the reply came with the calls and every call
        // worked, there is nothing to wait for: one model call per reply instead of two.
        if (text && results.every((r) => !r.is_error)) {
          result.text = cleanReply(text, b) || null;
          return result;
        }
        messages = [...messages, { role: 'assistant', content: res.content }, { role: 'user', content: results }];
      }
      // Ran out of tool rounds without a final answer: let a person take it.
      result.handoff ??= { reason: 'The assistant could not finish a reply.', summary: 'Tool loop limit reached.', urgent: false };
      return result;
    },

    async triageComment({ business: b, platform, text, authorName }) {
      const model = b.ai.model ?? opts.model;
      const usage = emptyUsage(model);
      const res = await client.beta.messages.parse({
        ...fallbackFor(model),
        model,
        max_tokens: 8000,
        output_config: { effort: 'low', format: betaZodOutputFormat(CommentDecisionSchema) },
        system: [{ type: 'text', text: commentTriagePrompt(b), cache_control: { type: 'ephemeral' } }],
        messages: [
          {
            role: 'user',
            content: `Platform: ${platform}\nCommenter: ${authorName ?? 'unknown'}\nComment:\n"""\n${text}\n"""`,
          },
        ],
      });
      addUsage(usage, res);
      const parsed = res.stop_reason === 'refusal' ? null : res.parsed_output;
      const decision: CommentDecision = parsed ?? {
        intent: 'other',
        public_reply: null,
        send_dm: false,
        dm_text: null,
        hide: false,
        alert_owner: false,
        reason: 'no decision returned',
      };
      if (decision.public_reply) decision.public_reply = cleanReply(decision.public_reply, { ...b, links: [] }) || null;
      if (decision.dm_text) decision.dm_text = cleanReply(decision.dm_text, b) || null;
      return { decision, usage };
    },
  };
}

function runTool(use: Anthropic.Beta.BetaToolUseBlock, b: Business, result: ReplyResult): { text: string; error?: boolean } {
  switch (use.name) {
    case 'attach_link': {
      const input = LinkInput.safeParse(use.input);
      if (!input.success || !b.links.some((l) => l.id === input.data.link_id)) {
        return { text: `Unknown link id. Valid ids: ${b.links.map((l) => l.id).join(', ')}`, error: true };
      }
      result.linkId = input.data.link_id;
      return { text: 'The link will be attached as a button under your reply. Do not type the URL.' };
    }
    case 'update_lead': {
      const input = LeadInput.safeParse(use.input);
      if (!input.success) return { text: 'Invalid input; nothing saved.', error: true };
      const { note, stage, ...fields } = input.data;
      for (const [k, v] of Object.entries(fields)) if (v) (result.lead as Record<string, string>)[k] = v;
      if (note) result.lead.notes = result.lead.notes ? `${result.lead.notes}\n${note}` : note;
      if (stage !== 'unchanged') result.lead.stage = stage as LeadUpdate['stage'];
      return { text: 'Saved.' };
    }
    case 'handoff_to_human': {
      const input = HandoffInput.safeParse(use.input);
      if (!input.success) return { text: 'Invalid input.', error: true };
      result.handoff = input.data;
      return { text: 'The team has been notified. Tell the customer briefly that someone will get back to them.' };
    }
    case 'opt_out':
      result.optOut = true;
      return { text: 'Opted out. Reply with a one-line polite confirmation and nothing else.' };
    default:
      return { text: `Unknown tool ${use.name}`, error: true };
  }
}
