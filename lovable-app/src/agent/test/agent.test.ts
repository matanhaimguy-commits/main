// @vitest-environment node
import { describe, expect, it } from 'vitest';
import type Anthropic from '@anthropic-ai/sdk';
import { cleanReply, createClaudeAi, toApiMessages } from '../ai/agent';
import { businessKnowledge, dmSystemPrompt } from '../ai/prompts';
import type { Contact, MessageRow } from '../db/repo';
import { makeBusiness } from './fixtures';

const b = makeBusiness();
const contact: Contact = {
  id: 1, business: 'acme', platform: 'instagram', external_id: 'U1', username: 'dana', name: null, phone: null, email: null,
  stage: 'engaged', interest: null, budget: null, timeline: null, notes: null, source: null, follows_business: null,
  opted_out: false, ai_paused_until: null, ai_pause_reason: null, needs_reply: true, reply_due_at: null,
  last_inbound_at: new Date(), last_outbound_at: null, followup_for: null, created_at: new Date(),
};
const row = (direction: 'in' | 'out', text: string, source: MessageRow['source'] = direction === 'in' ? 'user' : 'ai'): MessageRow => ({
  id: 0, contact_id: 1, direction, source, mid: null, text, payload: null, created_at: new Date(),
});

function message(content: unknown[], stop_reason: string): Anthropic.Beta.BetaMessage {
  return {
    id: 'msg', type: 'message', role: 'assistant', model: 'claude-opus-5-5', content, stop_reason,
    usage: { input_tokens: 100, output_tokens: 20, cache_read_input_tokens: 80 },
  } as unknown as Anthropic.Beta.BetaMessage;
}

/** Scripted stand-in for the SDK client: returns queued responses and records requests. */
function fakeClient(responses: Anthropic.Beta.BetaMessage[]) {
  const requests: any[] = [];
  const client = {
    beta: {
      messages: {
        create: async (params: any) => {
          requests.push(structuredClone(params));
          return responses.shift();
        },
        parse: async (params: any) => {
          requests.push(params);
          return { ...message([], 'end_turn'), parsed_output: null };
        },
      },
    },
  } as unknown as Anthropic;
  return { client, requests };
}

describe('prompts', () => {
  it('system prompt is deterministic (cacheable) and carries the business facts and links', () => {
    expect(dmSystemPrompt(b)).toBe(dmSystemPrompt(b));
    expect(businessKnowledge(b)).toContain('4,000 ILS');
    expect(businessKnowledge(b)).toContain('book_call');
    expect(dmSystemPrompt(b)).toContain('Never claim to be a human');
  });
});

describe('toApiMessages / cleanReply', () => {
  it('starts with a user turn and merges consecutive turns', () => {
    const msgs = toApiMessages([row('out', 'opener', 'funnel'), row('in', 'hi'), row('in', 'question?')]);
    expect(msgs.map((m) => m.role)).toEqual(['user', 'assistant', 'user']);
    expect(msgs[2]!.content).toBe('hi\nquestion?');
  });

  it('shows comments as comments', () => {
    expect(toApiMessages([row('in', 'guide', 'comment')])[0]!.content).toBe('[They commented on our post: "guide"]');
  });

  it('strips markdown and any URL that is not one of the business links', () => {
    const out = cleanReply('**Sure!** see https://evil.example/x and https://cal.com/acme/strategy', b);
    expect(out).toBe('Sure! see  and https://cal.com/acme/strategy');
  });
});

describe('createClaudeAi.reply', () => {
  it('runs tools, then returns the final text with the link and lead update', async () => {
    const { client, requests } = fakeClient([
      message(
        [
          { type: 'tool_use', id: 't1', name: 'update_lead', input: { name: 'Dana', phone: null, email: null, interest: 'shoe store ads', budget: null, timeline: 'this month', note: null, stage: 'hot' } },
          { type: 'tool_use', id: 't2', name: 'attach_link', input: { link_id: 'book_call' } },
        ],
        'tool_use',
      ),
      message([{ type: 'text', text: 'Perfect, Dana! Grab a slot here and we will plan it together.' }], 'end_turn'),
    ]);
    const ai = createClaudeAi({ model: 'claude-opus-5-5', client });
    const res = await ai.reply({ business: b, contact, transcript: [row('in', 'I want ads for my shoe store this month')], mode: 'reply', now: new Date() });

    expect(res.text).toBe('Perfect, Dana! Grab a slot here and we will plan it together.');
    expect(res.linkId).toBe('book_call');
    expect(res.lead).toMatchObject({ name: 'Dana', interest: 'shoe store ads', timeline: 'this month', stage: 'hot' });
    expect(res.usage).toMatchObject({ inputTokens: 200, outputTokens: 40, cacheReadTokens: 160 });

    const first = requests[0];
    expect(first).toMatchObject({ model: 'claude-opus-5-5', fallbacks: 'default', betas: ['server-side-fallback-2026-07-01'], output_config: { effort: 'medium' } });
    expect(first.system[0].cache_control).toEqual({ type: 'ephemeral' });
    expect(first.tools.map((t: any) => t.name)).toEqual(['attach_link', 'update_lead', 'handoff_to_human', 'opt_out']);
    expect(first.tools.every((t: any) => t.strict && t.input_schema.additionalProperties === false)).toBe(true);
    expect(first.tool_choice).toBeUndefined(); // forced tool use is a 400 on this model
    // Second call carries the tool results after the assistant turn.
    const last = requests[1].messages.at(-1);
    expect(last.content.map((c: any) => c.tool_use_id)).toEqual(['t1', 't2']);
  });

  it('takes the reply from the same response as the tool calls: one model call per reply', async () => {
    const { client, requests } = fakeClient([
      message(
        [
          { type: 'thinking', thinking: '', signature: 's' },
          { type: 'text', text: 'Shoe stores are our thing. Want the link to book a free call?' },
          { type: 'tool_use', id: 't1', name: 'update_lead', input: { name: null, phone: null, email: null, interest: 'shoe store ads', budget: null, timeline: null, note: null, stage: 'engaged' } },
          { type: 'tool_use', id: 't2', name: 'attach_link', input: { link_id: 'book_call' } },
        ],
        'tool_use',
      ),
    ]);
    const res = await createClaudeAi({ model: 'claude-haiku-5-5', client }).reply({ business: b, contact, transcript: [row('in', 'I have a shoe store')], mode: 'reply', now: new Date() });
    expect(requests).toHaveLength(1);
    expect(res.text).toBe('Shoe stores are our thing. Want the link to book a free call?');
    expect(res.linkId).toBe('book_call');
    expect(res.lead).toMatchObject({ interest: 'shoe store ads', stage: 'engaged' });
    // Claude Haiku 5.5 has no server-side fallback, so the request carries none.
    expect(requests[0].fallbacks).toBeUndefined();
    expect(requests[0].betas).toBeUndefined();
  });

  it('a refusal sends nothing and hands off', async () => {
    const { client } = fakeClient([message([], 'refusal')]);
    const res = await createClaudeAi({ model: 'm', client }).reply({ business: b, contact, transcript: [row('in', 'x')], mode: 'reply', now: new Date() });
    expect(res.text).toBeNull();
    expect(res.handoff).toBeDefined();
  });

  it('does not answer when the last message is ours', async () => {
    const { client, requests } = fakeClient([]);
    const res = await createClaudeAi({ model: 'm', client }).reply({ business: b, contact, transcript: [row('in', 'hi'), row('out', 'hello')], mode: 'reply', now: new Date() });
    expect(res.text).toBeNull();
    expect(requests).toHaveLength(0);
  });

  it('follow-up mode sends one user turn with the transcript and honours SKIP', async () => {
    const { client, requests } = fakeClient([message([{ type: 'text', text: 'SKIP' }], 'end_turn')]);
    const res = await createClaudeAi({ model: 'm', client }).reply({
      business: b, contact: { ...contact, last_outbound_at: new Date(Date.now() - 5 * 3600_000) },
      transcript: [row('in', 'thanks, I will think about it'), row('out', 'Sure!')], mode: 'followup', now: new Date(),
    });
    expect(res.text).toBeNull();
    expect(requests[0].messages).toHaveLength(1);
    expect(requests[0].messages[0].content).toContain('Customer: thanks, I will think about it');
  });

  it('rejects unknown link ids from the model', async () => {
    const { client } = fakeClient([
      message([{ type: 'tool_use', id: 't1', name: 'attach_link', input: { link_id: 'made_up' } }], 'tool_use'),
      message([{ type: 'text', text: 'ok' }], 'end_turn'),
    ]);
    const res = await createClaudeAi({ model: 'm', client }).reply({ business: b, contact, transcript: [row('in', 'link?')], mode: 'reply', now: new Date() });
    expect(res.linkId).toBeUndefined();
  });
});
