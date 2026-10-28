// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { insertWebhookEvent } from '../db/repo';
import type { Sql } from '../db/sql';
import { runDueAfters } from '../engine/after-run';
import { PAGE_INBOX_APP_ID } from '../engine/process';
import { scheduledRun, tick } from '../engine/tick';
import { makeBusiness } from './fixtures';
import { dbAvailable, freshDb, igEcho, igMessaging, igPostback, igText, makeHarness, truncate, type Harness } from './harness';

const hasDb = await dbAvailable();
const AFTER_TEXT = 'Stuck or have a question? Just reply here.';
const MIN = 60_000;
const HOUR = 60 * MIN;

/**
 * A funnel's last message (`after`) with and without `after_delay_minutes`: queued by the delivery,
 * sent by the scheduled tick when its time comes, and only when it is still right to send it.
 * The clock is ours, so "15 minutes later" is one line.
 */
describe.skipIf(!hasDb)('funnel last message wait (Postgres)', () => {
  let sql: Sql;
  let h: Harness;
  let clock: Date;

  const funnel = (over: Record<string, unknown> = {}) => ({ ...makeBusiness().funnels[0]!, ...over });
  const business = (funnelOver: Record<string, unknown> = {}) =>
    makeBusiness({ ai: { reply_delay_seconds: 0, comment_replies: false, comment_dms: false }, funnels: [funnel(funnelOver)] });

  async function start(funnelOver: Record<string, unknown> = {}) {
    h = await makeHarness(sql, [business(funnelOver)]);
    h.deps.now = () => clock;
  }
  const later = (ms: number) => {
    clock = new Date(clock.getTime() + ms);
  };
  async function deliver(payload: unknown) {
    await insertWebhookEvent(sql, (payload as { object?: string }).object, payload);
    while ((await tick(h.deps)) > 0) {
      /* drain */
    }
  }
  /** The person taps the first message's button; the funnel delivers the link. */
  const tap = (mid = 'pb1') => deliver(igMessaging([igPostback('U1', mid, 'F|guide-reel|deliver')]));
  // Plain arrays (the shim's result carries a `count` that toMatchObject would trip over).
  const queue = async () => [...(await sql<{ status: string; result: string | null; due_at: Date; dry_run: boolean }[]>`SELECT * FROM funnel_followups ORDER BY id`)];
  const afterSends = async () => [
    ...(await sql<{ status: string; error_message: string | null; request: { text?: string } | null }[]>`
      SELECT * FROM sends WHERE step = 'after' ORDER BY id`),
  ];
  const texts = () => h.meta.sends().map((s) => s.message.text ?? s.message.attachment?.payload?.text);

  beforeAll(async () => {
    sql = await freshDb();
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await truncate(sql);
    clock = new Date();
    await start({ after_delay_minutes: 15 });
  });

  describe('no delay (the default): as before', () => {
    it('sends the last message right after the delivery and queues nothing', async () => {
      await start();
      await tap();
      expect(h.meta.sends()).toHaveLength(2);
      expect(h.meta.sends()[1]).toMatchObject({ recipient: { id: 'U1' }, message: { text: AFTER_TEXT } });
      expect(await queue()).toHaveLength(0);
      expect((await afterSends()).map((s) => s.status)).toEqual(['sent']);
      expect(await runDueAfters(h.deps)).toBe(0);
    });

    it('treats an explicit 0 the same way', async () => {
      await start({ after_delay_minutes: 0 });
      await tap();
      expect(texts().at(-1)).toBe(AFTER_TEXT);
      expect(await queue()).toHaveLength(0);
    });
  });

  describe('with a delay', () => {
    it('queues the last message at delivery and sends nothing yet', async () => {
      await tap();
      expect(h.meta.sends()).toHaveLength(1); // the delivery only
      const rows = await queue();
      expect(rows).toHaveLength(1);
      expect(rows[0]).toMatchObject({ status: 'pending', dry_run: false });
      expect(rows[0]!.due_at.getTime()).toBe(clock.getTime() + 15 * MIN);
      expect(await afterSends()).toHaveLength(0);
    });

    it('does not send before the delay has passed', async () => {
      await tap();
      later(14 * MIN + 59_000);
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(h.meta.sends()).toHaveLength(1);
      expect((await queue())[0]).toMatchObject({ status: 'pending' });
    });

    it('sends it once the delay has passed, as a normal funnel DM in the ledger', async () => {
      await tap();
      later(15 * MIN);
      expect(await runDueAfters(h.deps)).toBe(1);
      expect(h.meta.sends()).toHaveLength(2);
      expect(h.meta.sends()[1]).toMatchObject({ recipient: { id: 'U1' }, message: { text: AFTER_TEXT } });
      expect(await queue()).toMatchObject([{ status: 'done', result: 'sent' }]);
      const [send] = await afterSends();
      expect(send).toMatchObject({ status: 'sent' });
      const [msg] = await sql`SELECT source, direction, text FROM messages WHERE send_id = (SELECT id FROM sends WHERE step = 'after')`;
      expect(msg).toMatchObject({ source: 'funnel', direction: 'out', text: AFTER_TEXT });
    });

    it('sends it from the scheduled tick', async () => {
      await tap();
      later(16 * MIN);
      const run = await scheduledRun(h.deps, Date.now() + 10_000);
      expect(run.ran).toContain('funnel_after');
      expect(texts().at(-1)).toBe(AFTER_TEXT);
    });

    it('never sends it twice', async () => {
      await tap();
      later(20 * MIN);
      expect(await runDueAfters(h.deps)).toBe(1);
      expect(await runDueAfters(h.deps)).toBe(0);
      // The same button tap arriving again queues and sends nothing new.
      await tap();
      // Even a queue row that is somehow pending again cannot send: the ledger key is used up.
      await sql`UPDATE funnel_followups SET status = 'pending', attempts = 0`;
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(h.meta.sends()).toHaveLength(2);
      expect(await afterSends()).toHaveLength(1);
      expect(await queue()).toMatchObject([{ status: 'done', result: 'duplicate' }]);
    });

    it('two workers running at the same moment send it once', async () => {
      await tap();
      later(20 * MIN);
      const [a, b] = await Promise.all([runDueAfters(h.deps), runDueAfters(h.deps)]);
      expect(a + b).toBe(1);
      expect(h.meta.sends()).toHaveLength(2);
    });

    it('waits separately for each tap', async () => {
      await tap('pb1');
      later(5 * MIN);
      await tap('pb2');
      expect(await queue()).toHaveLength(2);
    });

    it('does not send it when the person replied in the meantime', async () => {
      await tap();
      later(5 * MIN);
      await deliver(igMessaging([igText('U1', 'm2', 'what is this exactly?')]));
      const before = h.meta.sends().length;
      later(15 * MIN);
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(texts().slice(before)).not.toContain(AFTER_TEXT);
      expect(await queue()).toMatchObject([{ status: 'skipped', result: 'replied' }]);
      // Logged where the owner looks: a skipped send with the reason.
      expect(await afterSends()).toMatchObject([
        { status: 'skipped', error_message: 'not sent: the person wrote back while this was waiting', request: { text: AFTER_TEXT } },
      ]);
    });

    it('does not send it when a team member wrote to the person in the meantime', async () => {
      await tap();
      await deliver(igMessaging([igEcho('U1', 'human-1', 'Hey, Matan here!', PAGE_INBOX_APP_ID)]));
      later(20 * MIN);
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(await queue()).toMatchObject([{ status: 'skipped', result: 'team_replied' }]);
      expect(h.meta.sends()).toHaveLength(1);
    });

    it('does not send it to someone who said STOP', async () => {
      await tap();
      await deliver(igMessaging([igText('U1', 'm2', 'STOP')]));
      const before = h.meta.sends().length;
      later(20 * MIN);
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(await queue()).toMatchObject([{ status: 'skipped', result: 'opted_out' }]);
      expect(h.meta.sends()).toHaveLength(before);
    });

    it('does not send it outside the 24-hour window, and says why', async () => {
      await tap();
      later(25 * HOUR); // the person last wrote 25 hours ago
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(h.meta.sends()).toHaveLength(1);
      expect(await queue()).toMatchObject([{ status: 'skipped', result: 'window_closed' }]);
      const [send] = await afterSends();
      expect(send).toMatchObject({ status: 'skipped' });
      expect(send!.error_message).toContain('24-hour messaging window is closed');
    });

    it('still sends late while the 24-hour window is open, but not once it closes', async () => {
      await tap();
      later(23 * HOUR);
      expect(await runDueAfters(h.deps)).toBe(1);

      await tap('pb2');
      later(24 * HOUR - 4 * MIN); // inside the last five minutes, held back on purpose
      expect(await runDueAfters(h.deps)).toBe(0);
      expect((await queue())[1]).toMatchObject({ status: 'skipped', result: 'window_closed' });
    });

    it('is a dry run while sending is off: recorded, nothing reaches Meta', async () => {
      h.live.clear();
      await tap();
      expect(await queue()).toMatchObject([{ status: 'pending', dry_run: true }]);
      later(15 * MIN);
      expect(await runDueAfters(h.deps)).toBe(1);
      expect(h.meta.calls.filter((c) => c.method === 'sendMessage')).toHaveLength(0);
      expect((await afterSends()).map((s) => s.status)).toEqual(['dry_run']);
      expect(await queue()).toMatchObject([{ status: 'done', result: 'dry_run' }]);
    });

    it('does not send a question for a delivery that was only a dry run once sending goes live', async () => {
      h.live.clear();
      await tap();
      h.live.add('acme'); // the owner switches sending on during the wait
      later(15 * MIN);
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(h.meta.calls.filter((c) => c.method === 'sendMessage')).toHaveLength(0);
      expect(await queue()).toMatchObject([{ status: 'skipped', result: 'queued_in_dry_run' }]);
    });

    it('does not send it when the funnel lost its last message during the wait', async () => {
      await tap();
      await start({ after_delay_minutes: 15, after: undefined });
      later(15 * MIN);
      expect(await runDueAfters(h.deps)).toBe(0);
      expect(await queue()).toMatchObject([{ status: 'skipped', result: 'funnel_changed' }]);
    });

    it('sends the funnel\'s current text if it was edited during the wait', async () => {
      await tap();
      await start({ after_delay_minutes: 15, after: 'Quick one: what do you sell?' });
      later(15 * MIN);
      expect(await runDueAfters(h.deps)).toBe(1);
      expect(texts().at(-1)).toBe('Quick one: what do you sell?');
    });

    it('does not send early when the migration is missing: it says so instead', async () => {
      await sql`ALTER TABLE funnel_followups RENAME TO funnel_followups_off`;
      try {
        await tap();
        expect(h.meta.sends()).toHaveLength(1); // the delivery only; the question is not sent early
        expect(h.alerts.some((a) => a.includes('funnel_followups'))).toBe(true);
        later(20 * MIN);
        expect(await runDueAfters(h.deps)).toBe(0); // quiet, not an error
      } finally {
        await sql`ALTER TABLE funnel_followups_off RENAME TO funnel_followups`;
      }
    });
  });
});
