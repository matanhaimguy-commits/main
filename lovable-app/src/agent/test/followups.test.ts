// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import {
  claimDueFollowups,
  finishFollowup,
  FOLLOWUP_LEASE_MS,
  FOLLOWUP_MAX_ATTEMPTS,
  isMissingTable,
  queueFollowup,
  threadActivitySince,
} from '../db/followups';
import { insertMessage, upsertContact } from '../db/repo';
import type { Sql } from '../db/sql';
import { dbAvailable, freshDb, truncate } from './harness';

const hasDb = await dbAvailable();
const T0 = new Date('2026-10-28T10:00:00Z');
const at = (minutes: number) => new Date(T0.getTime() + minutes * 60_000);

describe('isMissingTable', () => {
  it('recognises Postgres "undefined_table" and nothing else', () => {
    expect(isMissingTable({ code: '42P01' })).toBe(true);
    expect(isMissingTable({ code: '23505' })).toBe(false);
    expect(isMissingTable(new Error('x'))).toBe(false);
    expect(isMissingTable(null)).toBe(false);
  });
});

describe.skipIf(!hasDb)('funnel follow-up queue (Postgres)', () => {
  let sql: Sql;
  let contactId: number;

  beforeAll(async () => {
    sql = await freshDb();
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await truncate(sql);
    contactId = (await upsertContact(sql, { business: 'acme', platform: 'instagram', externalId: 'U1' })).id;
  });

  // Plain arrays (the shim's result carries a `count` that toEqual would trip over).
  const claim = async (now: Date) => [...(await claimDueFollowups(sql, now, 10))];
  const queue = (over: Partial<Parameters<typeof queueFollowup>[1]> = {}) =>
    queueFollowup(sql, { key: 'funnel:f:after:t1', business: 'acme', funnelId: 'f', contactId, dueAt: at(15), dryRun: false, ...over });
  const message = (mid: string, source: 'user' | 'human' | 'comment' | 'funnel', direction: 'in' | 'out' = 'in', contact = contactId) =>
    insertMessage(sql, { contactId: contact, direction, source, mid, text: mid });

  it('keeps the table private: row level security on, no policies, nothing for the browser keys', async () => {
    const [t] = await sql<{ rls: boolean }[]>`SELECT relrowsecurity AS rls FROM pg_class WHERE relname = 'funnel_followups'`;
    expect(t!.rls).toBe(true);
    const policies = await sql`SELECT 1 FROM pg_policies WHERE tablename = 'funnel_followups'`;
    expect(policies).toHaveLength(0);
    const [p] = await sql<{ anon: boolean; auth: boolean }[]>`
      SELECT has_table_privilege('anon', 'funnel_followups', 'SELECT') AS anon,
             has_table_privilege('authenticated', 'funnel_followups', 'SELECT') AS auth`;
    expect(p).toEqual({ anon: false, auth: false });
  });

  it('queues a message once per key', async () => {
    expect(await queue()).toBe(true);
    expect(await queue({ dueAt: at(30) })).toBe(false);
    const rows = await sql`SELECT status, due_at FROM funnel_followups`;
    expect(rows).toHaveLength(1);
    expect(rows[0]).toMatchObject({ status: 'pending' });
    expect(rows[0]!['due_at'].getTime()).toBe(at(15).getTime());
  });

  it('notes the newest message of the thread as it was when queued', async () => {
    await queue({ key: 'k-empty' });
    const first = (await message('m1', 'user'))!;
    const second = (await message('m2', 'funnel', 'out'))!;
    await message('other-person', 'user', 'in', (await upsertContact(sql, { business: 'acme', platform: 'instagram', externalId: 'U2' })).id);
    await queue({ key: 'k-later' });
    const rows = await sql<{ key: string; watermark: number }[]>`SELECT key, watermark FROM funnel_followups ORDER BY id`;
    expect(rows.map((r) => [r.key, r.watermark])).toEqual([
      ['k-empty', 0],
      ['k-later', second],
    ]);
    expect(first).toBeLessThan(second);
  });

  it('hands out only what is due, to one worker at a time', async () => {
    await queue({ key: 'soon', dueAt: at(10) });
    await queue({ key: 'later', dueAt: at(40) });
    expect(await claim(at(5))).toEqual([]);

    const first = await claim(at(12));
    expect(first.map((r) => r.key)).toEqual(['soon']);
    expect(first[0]).toMatchObject({ attempts: 1, business: 'acme', funnel_id: 'f', contact_id: contactId, dry_run: false });
    // Leased: nobody else gets it while the lease lasts.
    expect(await claim(at(13))).toEqual([]);

    // A worker that died lets it go; it is handed out again, but never more than the attempt limit.
    const lease = FOLLOWUP_LEASE_MS / 60_000;
    let t = 12;
    for (let attempt = 2; attempt <= FOLLOWUP_MAX_ATTEMPTS; attempt++) {
      t += lease + 1;
      const again = await claim(at(t));
      expect(again.map((r) => [r.key, r.attempts])).toEqual([['soon', attempt]]);
    }
    expect(await claim(at(t + lease + 1))).toEqual([]);
  });

  it('stops handing out a message once it is finished', async () => {
    await queue({ dueAt: at(10) });
    const [row] = await claim(at(11));
    await finishFollowup(sql, row!.id, 'done', 'sent', at(11));
    expect([...(await sql`SELECT status, result, locked_until, finished_at FROM funnel_followups`)]).toMatchObject([
      { status: 'done', result: 'sent', locked_until: null },
    ]);
    expect(await claim(at(60))).toEqual([]);
  });

  it('sees a reply from the person, or from the team, after the watermark and nothing else', async () => {
    await message('before', 'user');
    await queue();
    const [row] = await sql<{ watermark: number }[]>`SELECT watermark FROM funnel_followups`;
    const watermark = row!.watermark;
    expect(await threadActivitySince(sql, contactId, watermark)).toEqual({ personReplied: false, teamReplied: false });

    // Not replies: our own message, a new comment, someone else's thread.
    await message('ours', 'funnel', 'out');
    await message('a-comment', 'comment');
    await message('their-thread', 'user', 'in', (await upsertContact(sql, { business: 'acme', platform: 'instagram', externalId: 'U2' })).id);
    expect(await threadActivitySince(sql, contactId, watermark)).toEqual({ personReplied: false, teamReplied: false });

    await message('team', 'human', 'out');
    expect(await threadActivitySince(sql, contactId, watermark)).toEqual({ personReplied: false, teamReplied: true });
    await message('reply', 'user');
    expect(await threadActivitySince(sql, contactId, watermark)).toEqual({ personReplied: true, teamReplied: true });
  });
});
