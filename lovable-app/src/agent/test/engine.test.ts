// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import type { Sql } from '../db/sql';
import { runFollowups } from '../engine/reply';
import { checkDmAccess, checkQuietFunnels, checkStuckSends } from '../engine/health';
import { LeadError, submitLead } from '../engine/leads';
import { PAGE_INBOX_APP_ID } from '../engine/process';
import { insertWebhookEvent } from '../db/repo';
import { tick } from '../engine/tick';
import { PAGE_ID, makeBusiness } from './fixtures';
import {
  APP_ID,
  apiError,
  dbAvailable,
  fbComment,
  freshDb,
  igComment,
  igEcho,
  igMessaging,
  igPostback,
  igText,
  makeHarness,
  networkError,
  truncate,
  type Harness,
} from './harness';

const hasDb = await dbAvailable();

describe.skipIf(!hasDb)('engine (Postgres)', () => {
  let sql: Sql;
  let h: Harness;

  const business = (overrides: Record<string, unknown> = {}) =>
    makeBusiness({ ai: { reply_delay_seconds: 0, comment_replies: false, comment_dms: false }, ...overrides });

  async function deliver(payload: unknown) {
    await insertWebhookEvent(sql, (payload as any).object, payload);
    while ((await tick(h.deps)) > 0) {
      /* drain */
    }
  }
  const one = async <T>(q: Promise<T[]>) => (await q)[0]!;

  beforeAll(async () => {
    sql = await freshDb();
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await truncate(sql);
    h = await makeHarness(sql, [business()]);
  });

  describe('comment funnels', () => {
    it('keyword on a pinned Facebook post: one private reply with a tap button, then the public reply', async () => {
      await deliver(fbComment({ id: 'C1', text: 'Guide please!' }));

      const sends = h.meta.sends();
      expect(sends).toHaveLength(1);
      expect(sends[0].recipient).toEqual({ comment_id: 'C1' });
      expect(sends[0].pageId).toBe(PAGE_ID);
      expect(sends[0].message.attachment.payload.buttons[0]).toEqual({ type: 'postback', title: 'Send it to me', payload: 'F|guide-reel|deliver' });
      expect(h.meta.calls.find((c) => c.method === 'replyToComment')?.args).toEqual(['facebook', 'C1', 'Sent you a DM 🙌']);

      const comment = await one(sql`SELECT * FROM comments WHERE comment_id = 'C1'`);
      expect(comment).toMatchObject({ outcome: 'funnel', funnel_id: 'guide-reel', skip_reason: null });
      const contact = await one(sql`SELECT * FROM contacts`);
      expect(contact).toMatchObject({ external_id: 'PSID_FOR_C1', source: 'funnel:guide-reel', name: 'Dana Levi' });
      const msgs = await sql`SELECT direction, source FROM messages ORDER BY id`;
      expect(msgs.map((m) => `${m.direction}:${m.source}`)).toEqual(['in:comment', 'out:funnel']);
      // A comment alone does not open the 24h messaging window.
      expect(contact.last_inbound_at).toBeNull();
    });

    it('the same webhook delivered twice sends once', async () => {
      await deliver(fbComment({ id: 'C1', text: 'guide' }));
      await deliver(fbComment({ id: 'C1', text: 'guide' }));
      expect(h.meta.sends()).toHaveLength(1);
      expect((await sql`SELECT * FROM comments`).length).toBe(1);
    });

    it('every skipped comment gets a row with the reason', async () => {
      h = await makeHarness(sql, [business({ funnels: [{ ...makeBusiness().funnels[0], id: 'paused', status: 'paused', posts: [`${PAGE_ID}_POST_B`] }, makeBusiness().funnels[0]] })]);
      await deliver(fbComment({ id: 'C1', text: 'guide', post: `${PAGE_ID}_POST_Z` }));
      await deliver(fbComment({ id: 'C2', text: 'nice post', post: `${PAGE_ID}_POST_A` }));
      await deliver(fbComment({ id: 'C3', text: 'guide', from: PAGE_ID }));
      await deliver(fbComment({ id: 'C4', text: 'guide', parent: 'SOME_COMMENT' }));
      await deliver(fbComment({ id: 'C5', text: 'guide', post: `${PAGE_ID}_POST_B` }));
      await deliver(fbComment({ id: 'C6', text: 'guide', verb: 'edited' }));
      const rows = await sql`SELECT comment_id, skip_reason FROM comments ORDER BY comment_id`;
      expect(rows.map((r) => `${r.comment_id}:${r.skip_reason}`)).toEqual([
        'C1:no_funnel_for_post',
        'C2:keyword_not_matched',
        'C3:own_comment',
        'C4:is_reply',
        'C5:funnel_paused',
      ]);
      expect(h.meta.sends()).toHaveLength(0);
    });

    it('a failed private reply is recorded, never retried, and gets no public "check your DMs"', async () => {
      h.meta.failNext.push(apiError(10900, undefined, 'Activity already replied to'));
      await deliver(igComment({ id: 'IGC1', text: 'מדריך' }));
      await deliver(igComment({ id: 'IGC1', text: 'מדריך' }));
      expect(h.meta.sends()).toHaveLength(1);
      expect(h.meta.calls.some((c) => c.method === 'replyToComment')).toBe(false);
      const send = await one(sql`SELECT * FROM sends`);
      expect(send).toMatchObject({ status: 'failed', error_code: 10900, kind: 'private_reply' });
      expect(h.alerts).toEqual([]); // another tool replied first: harmless
    });

    it('a timeout is "unknown", alerts, and is not retried', async () => {
      h.meta.failNext.push(networkError());
      await deliver(igComment({ id: 'IGC2', text: 'guide' }));
      await deliver(igComment({ id: 'IGC2', text: 'guide' }));
      expect(h.meta.sends()).toHaveLength(1);
      expect(await one(sql`SELECT status FROM sends`)).toMatchObject({ status: 'unknown' });
      expect(h.alerts.some((a) => a.includes('NOT retried'))).toBe(true);
    });

    it('a spam block pauses all sending for the business', async () => {
      h.meta.failNext.push(apiError(368, 1404169, 'blocked'));
      await deliver(igComment({ id: 'IGC3', text: 'guide' }));
      await deliver(igComment({ id: 'IGC4', text: 'guide' }));
      expect(h.meta.sends()).toHaveLength(1);
      expect(await one(sql`SELECT status, error_message FROM sends WHERE comment_id = 'IGC4'`)).toMatchObject({ status: 'skipped' });
      expect(h.alerts.some((a) => a.includes('paused for 24 hours'))).toBe(true);
    });

    it('dry run records everything and calls nothing', async () => {
      h.live.clear();
      await deliver(igComment({ id: 'IGC5', text: 'guide' }));
      expect(h.meta.calls.filter((c) => c.method !== 'getUserProfile')).toEqual([]);
      const sends = await sql`SELECT kind, status FROM sends ORDER BY id`;
      expect(sends.map((s) => `${s.kind}:${s.status}`)).toEqual(['private_reply:dry_run', 'public_reply:dry_run']);
    });

    it('while testers are set, only testers are messaged', async () => {
      h = await makeHarness(sql, [business({ testers: ['@my_test_account'] })]);
      await deliver(igComment({ id: 'IGC6', text: 'guide', username: 'stranger' }));
      await deliver(igComment({ id: 'IGC7', text: 'guide', username: 'my_test_account', from: 'IG_TESTER' }));
      expect(await one(sql`SELECT skip_reason FROM comments WHERE comment_id = 'IGC6'`)).toMatchObject({ skip_reason: 'not_a_tester' });
      expect(h.meta.sends().map((s) => s.recipient)).toEqual([{ comment_id: 'IGC7' }]);
    });
  });

  describe('button tap -> delivery', () => {
    it('tap delivers the link and the conversation opener, and opens the 24h window', async () => {
      await deliver(igComment({ id: 'IGC1', text: 'guide' }));
      await deliver(igMessaging([igPostback('PSID_FOR_IGC1', 'pb1', 'F|guide-reel|deliver')]));
      const sends = h.meta.sends();
      expect(sends).toHaveLength(3);
      expect(sends[1].recipient).toEqual({ id: 'PSID_FOR_IGC1' });
      expect(sends[1].message.attachment.payload.buttons[0]).toEqual({ type: 'web_url', url: 'https://acme.studio/guide.pdf', title: 'Open the guide' });
      expect(sends[2].message).toEqual({ text: 'Stuck or have a question? Just reply here.' });
      const contact = await one(sql`SELECT * FROM contacts`);
      expect(contact.last_inbound_at).not.toBeNull();
      expect(contact.stage).toBe('engaged');
      expect((await sql`SELECT * FROM taps`).length).toBe(1);
      // Same tap redelivered: nothing new.
      await deliver(igMessaging([igPostback('PSID_FOR_IGC1', 'pb1', 'F|guide-reel|deliver')]));
      expect(h.meta.sends()).toHaveLength(3);
    });

    it('follow gate: asks non-followers to follow, delivers after they do', async () => {
      const base = makeBusiness().funnels[0]!;
      h = await makeHarness(sql, [
        business({
          funnels: [{ ...base, follow_gate: { text: 'Follow us first, then tap below', button: 'I followed ✅' } }],
        }),
      ]);
      await deliver(igMessaging([igPostback('U1', 'pb1', 'F|guide-reel|deliver')]));
      expect(h.meta.sends()[0].message.attachment.payload.buttons[0].payload).toBe('F|guide-reel|gate');
      h.meta.follows.set('U1', true);
      await deliver(igMessaging([igPostback('U1', 'pb2', 'F|guide-reel|gate', 'I followed ✅')]));
      const last = h.meta.sends().slice(1);
      expect(last[0].message.attachment.payload.buttons[0].type).toBe('web_url');
      expect((await one(sql`SELECT follows_business FROM contacts`)).follows_business).toBe(true);
    });
  });

  describe('AI conversation', () => {
    it('answers a DM, attaches the link, saves the lead and alerts on a hot lead', async () => {
      h.ai.nextReply = { text: 'Here is the booking page 👇', linkId: 'book_call', lead: { stage: 'hot', interest: 'ads for a shoe store', phone: '050-1234567' } };
      await deliver(igMessaging([igText('U9', 'm1', 'How much for ads management? I want to start this month')]));
      expect(h.ai.replies).toHaveLength(1);
      expect(h.ai.replies[0]!.transcript.map((m) => m.text)).toEqual(['How much for ads management? I want to start this month']);
      const sends = h.meta.sends();
      expect(sends).toHaveLength(1);
      expect(sends[0].message.attachment.payload.buttons[0]).toEqual({ type: 'web_url', url: 'https://cal.com/acme/strategy', title: 'Book a call' });
      const contact = await one(sql`SELECT * FROM contacts`);
      expect(contact).toMatchObject({ stage: 'hot', interest: 'ads for a shoe store', phone: '050-1234567', needs_reply: false });
      expect(h.alerts.some((a) => a.includes('HOT'))).toBe(true);
    });

    it('a burst of messages gets one answer', async () => {
      await deliver(igMessaging([igText('U9', 'm1', 'hi'), igText('U9', 'm2', 'quick question'), igText('U9', 'm3', 'do you do tiktok ads?')]));
      expect(h.ai.replies).toHaveLength(1);
      expect(h.ai.replies[0]!.transcript).toHaveLength(3);
      expect(h.meta.sends()).toHaveLength(1);
    });

    it('a person replying from the inbox pauses the AI in that thread', async () => {
      await deliver(igMessaging([igText('U9', 'm1', 'hi')]));
      expect(h.meta.sends()).toHaveLength(1);
      await deliver(igMessaging([igEcho('U9', 'human-1', 'Hey, Matan here!', PAGE_INBOX_APP_ID)]));
      const contact = await one(sql`SELECT * FROM contacts`);
      expect(contact.ai_paused_until).not.toBeNull();
      await deliver(igMessaging([igText('U9', 'm2', 'thanks Matan')]));
      expect(h.ai.replies).toHaveLength(1);
      expect(h.meta.sends()).toHaveLength(1);
    });

    it('echoes of our own sends are ignored (by app id and by message id)', async () => {
      await deliver(igMessaging([igText('U9', 'm1', 'hi')]));
      await deliver(igMessaging([igEcho('U9', 'mid.1', 'Happy to help!'), igEcho('U9', 'mid.x', 'Happy to help!', APP_ID)]));
      const contact = await one(sql`SELECT * FROM contacts`);
      expect(contact.ai_paused_until).toBeNull();
      expect((await sql`SELECT * FROM messages WHERE source = 'human'`).length).toBe(0);
    });

    it('STOP opts out, confirms once, and the AI stays quiet', async () => {
      await deliver(igMessaging([igText('U9', 'm1', 'STOP')]));
      expect(h.meta.sends()).toHaveLength(1);
      expect(h.meta.sends()[0].message.text).toMatch(/won't get any more/);
      expect(await one(sql`SELECT opted_out FROM contacts`)).toMatchObject({ opted_out: true });
      expect(h.ai.replies).toHaveLength(0);
    });

    it('handoff pauses the AI and alerts the team', async () => {
      h.ai.nextReply = { text: 'Let me get someone from the team for you.', handoff: { reason: 'refund request', summary: 'Wants a refund for October', urgent: true } };
      await deliver(igMessaging([igText('U9', 'm1', 'I want a refund')]));
      expect(await one(sql`SELECT ai_pause_reason FROM contacts`)).toMatchObject({ ai_pause_reason: 'handoff: refund request' });
      expect(h.alerts.some((a) => a.includes('needs a person'))).toBe(true);
    });

    it('a story reply with a keyword runs the story funnel instead of the AI', async () => {
      const base = makeBusiness().funnels[0]!;
      h = await makeHarness(sql, [business({ funnels: [{ ...base, id: 'story', trigger: 'story_reply', posts: [] }] })]);
      await deliver(igMessaging([igText('U9', 'm1', 'guide', { reply_to: { story: { id: 'S1', url: 'https://x' } } })]));
      expect(h.ai.replies).toHaveLength(0);
      expect(h.meta.sends()[0].message.attachment.payload.buttons[0].payload).toBe('F|story|deliver');
    });

    it('one follow-up for a warm lead that went quiet, inside the 24h window', async () => {
      await deliver(igMessaging([igText('U9', 'm1', 'interested in the course')]));
      await sql`UPDATE contacts SET last_inbound_at = now() - interval '6 hours', last_outbound_at = now() - interval '5 hours'`;
      h.ai.nextReply = { text: 'Did you get a chance to look at the course page?' };
      expect(await runFollowups(h.deps)).toBe(1);
      expect(h.ai.replies[1]!.mode).toBe('followup');
      expect(await runFollowups(h.deps)).toBe(0);
      // Outside the window: nothing.
      await sql`UPDATE contacts SET last_inbound_at = now() - interval '23.5 hours', followup_for = NULL`;
      expect(await runFollowups(h.deps)).toBe(0);
      expect(h.meta.sends()).toHaveLength(2);
      // A team member spoke after the customer: no automated nudge.
      await sql`UPDATE contacts SET last_inbound_at = now() - interval '6 hours', followup_for = NULL, ai_paused_until = NULL`;
      await sql`INSERT INTO messages (contact_id, direction, source, text, created_at) VALUES (1, 'out', 'human', 'hi from Matan', now() - interval '5 hours')`;
      expect(await runFollowups(h.deps)).toBe(0);
    });

    it('comments no funnel owns can get an AI private reply and public reply', async () => {
      h = await makeHarness(sql, [business({ ai: { reply_delay_seconds: 0, comment_replies: true, comment_dms: true } })]);
      await deliver(igComment({ id: 'IGC9', text: 'how much is it?', media: 'OTHER_MEDIA' }));
      const comment = await one(sql`SELECT * FROM comments`);
      expect(comment).toMatchObject({ outcome: 'ai', ai_intent: 'pricing', skip_reason: 'no_funnel_for_post' });
      expect(h.meta.sends()[0]).toMatchObject({ recipient: { comment_id: 'IGC9' }, message: { text: expect.stringContaining('4,000') } });
      expect(h.meta.calls.some((c) => c.method === 'replyToComment')).toBe(true);
    });
  });

  describe('receipts and health', () => {
    it('Instagram reads mark sends read; delivered stays empty', async () => {
      await deliver(igMessaging([igText('U9', 'm1', 'hi')]));
      await deliver(igMessaging([{ sender: { id: 'U9' }, recipient: { id: 'x' }, timestamp: Date.now(), read: { mid: 'mid.1' } }]));
      const send = await one(sql`SELECT * FROM sends`);
      expect(send.read_at).not.toBeNull();
      expect(send.delivered_at).toBeNull();
    });

    it('alerts when a funnel sends but nothing lands', async () => {
      for (let i = 0; i < 6; i++) await deliver(igComment({ id: `Q${i}`, text: 'guide', from: `U${i}` }));
      await sql`UPDATE sends SET sent_at = now() - interval '3 hours'`;
      expect(await checkQuietFunnels(h.deps)).toEqual(['acme/guide-reel/instagram']);
      expect(h.alerts.some((a) => a.includes('not one was read'))).toBe(true);
      await sql`INSERT INTO taps (business, funnel_id, payload) VALUES ('acme', 'guide-reel', 'x')`;
      expect(await checkQuietFunnels(h.deps)).toEqual([]);
    });

    it('records whether Meta passes DMs from people without a role, and alerts when it opens', async () => {
      await sql`INSERT INTO contacts (business, platform, external_id, username) VALUES ('acme', 'instagram', 'TESTER', 'tester')`;
      expect((await checkDmAccess(h.deps)).acme).toMatchObject({ status: 'unknown' });

      await sql`INSERT INTO contacts (business, platform, external_id, username, updated_at)
        VALUES ('acme', 'instagram', 'STRANGER', 'stranger', now() + interval '1 minute')`;
      h.meta.refused.add('STRANGER');
      expect((await checkDmAccess(h.deps)).acme).toMatchObject({ status: 'roles_only', probe: 'stranger', refusedId: 'STRANGER' });
      expect(h.alerts.some((a) => a.includes('only passes Instagram DMs'))).toBe(true);

      // The tester writes again: they have a role, so they prove nothing. The stranger is asked first.
      await sql`UPDATE contacts SET updated_at = now() + interval '1 hour' WHERE external_id = 'TESTER'`;
      expect((await checkDmAccess(h.deps)).acme).toMatchObject({ status: 'roles_only' });
      h.meta.refused.clear();
      expect((await checkDmAccess(h.deps)).acme).toMatchObject({ status: 'everyone', probe: 'stranger' });
      expect(h.alerts.some((a) => a.includes('passes every Instagram DM'))).toBe(true);
    });

    it('lead form: one contact per phone, qualified, notes kept, an alert each time, never queued for the AI', async () => {
      const b = h.deps.registry.bySlug('acme')!;
      const first = await submitLead(h.deps, b, { name: 'Ana', phone: '+355 69 123 4567', instagram: '@ana.k', need: 'More clients', source: 'analiza' });
      const again = await submitLead(h.deps, b, { name: 'Ana Kola', phone: '+355691234567', need: 'Call after 5' });
      expect(again.contactId).toBe(first.contactId);
      expect(again.repeat).toBe(true);
      const c = await one(sql`SELECT * FROM contacts WHERE id = ${first.contactId}`);
      expect(c).toMatchObject({ platform: 'web', name: 'Ana Kola', phone: '+355691234567', username: 'ana.k', stage: 'qualified', source: 'form:analiza', needs_reply: false });
      expect(c.notes).toBe('More clients\nCall after 5');
      expect((await sql`SELECT * FROM messages WHERE contact_id = ${first.contactId}`).length).toBe(2);
      expect(h.alerts.filter((a) => a.includes('lead from the form'))).toHaveLength(2);
      await expect(submitLead(h.deps, b, { name: 'X', phone: '12' })).rejects.toThrow(LeadError);
    });

    it('marks sends stuck in pending as unknown without retrying', async () => {
      await sql`INSERT INTO sends (business, platform, kind, idempotency_key, status, created_at)
        VALUES ('acme', 'instagram', 'message', 'k1', 'pending', now() - interval '10 minutes')`;
      expect(await checkStuckSends(h.deps)).toBe(1);
      expect(await one(sql`SELECT status FROM sends`)).toMatchObject({ status: 'unknown' });
    });
  });
});
