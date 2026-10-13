import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import type { Sql } from '../src/db/index.js';
import { createLink } from '../src/db/repo.js';
import { sign } from '../src/meta/webhook.js';
import { createApp } from '../src/server.js';
import { tick } from '../src/worker.js';
import { APP_SECRET, VERIFY_TOKEN, makeBusiness } from './fixtures.js';
import { dbAvailable, fbComment, freshDb, makeHarness, truncate, type Harness } from './harness.js';

const hasDb = await dbAvailable();

describe.skipIf(!hasDb)('HTTP endpoints', () => {
  let sql: Sql;
  let h: Harness;
  let app: ReturnType<typeof createApp>;
  let nudged = 0;

  beforeAll(async () => {
    sql = await freshDb();
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await truncate(sql);
    h = await makeHarness(sql, [makeBusiness()]);
    nudged = 0;
    app = createApp(h.deps, { onEvent: () => nudged++ });
  });

  it('verification: right token returns the challenge, wrong token is rejected', async () => {
    const ok = await app.request(`/webhook?hub.mode=subscribe&hub.verify_token=${VERIFY_TOKEN}&hub.challenge=1158201444`);
    expect(ok.status).toBe(200);
    expect(await ok.text()).toBe('1158201444');
    const bad = await app.request('/webhook?hub.mode=subscribe&hub.verify_token=guess&hub.challenge=1');
    expect(bad.status).toBe(403);
  });

  it('unsigned and forged posts are rejected and not stored', async () => {
    const body = JSON.stringify(fbComment({ id: 'C1', text: 'guide' }));
    const unsigned = await app.request('/webhook', { method: 'POST', body, headers: { 'content-type': 'application/json' } });
    expect(unsigned.status).toBe(401);
    const forged = await app.request('/webhook', { method: 'POST', body, headers: { 'x-hub-signature-256': sign(body, 'not-the-secret') } });
    expect(forged.status).toBe(401);
    expect((await sql`SELECT * FROM webhook_events`).length).toBe(0);
  });

  it('a correctly signed post is stored, acknowledged, and processed by the worker', async () => {
    const body = JSON.stringify(fbComment({ id: 'C1', text: 'guide' }));
    const res = await app.request('/webhook', { method: 'POST', body, headers: { 'x-hub-signature-256': sign(body, APP_SECRET) } });
    expect(res.status).toBe(200);
    expect(await res.text()).toBe('EVENT_RECEIVED');
    expect(nudged).toBe(1);
    expect((await sql`SELECT status FROM webhook_events`)[0]).toMatchObject({ status: 'pending' });
    await tick(h.deps);
    expect((await sql`SELECT status FROM webhook_events`)[0]).toMatchObject({ status: 'done' });
    expect(h.meta.sends()).toHaveLength(1);
  });

  it('health, privacy and data deletion pages', async () => {
    const health = await app.request('/health');
    expect(await health.json()).toMatchObject({ ok: true, businesses: [{ slug: 'acme', live: true }] });
    expect((await app.request('/privacy')).status).toBe(200);
    expect(await (await app.request('/data-deletion')).text()).toContain('STOP');
  });

  it('tracked links redirect and count clicks', async () => {
    await createLink(sql, { token: 'tok123', business: 'acme', url: 'https://acme.studio/guide.pdf' });
    const res = await app.request('/r/tok123');
    expect(res.status).toBe(302);
    expect(res.headers.get('location')).toBe('https://acme.studio/guide.pdf');
    expect((await sql`SELECT clicks FROM links`)[0]).toMatchObject({ clicks: 1 });
    expect((await app.request('/r/nope')).status).toBe(404);
  });

  it('admin needs the password and renders', async () => {
    expect((await app.request('/admin')).status).toBe(401);
    const auth = { Authorization: `Basic ${Buffer.from('admin:pw').toString('base64')}` };
    const body = JSON.stringify(fbComment({ id: 'C1', text: 'guide' }));
    await app.request('/webhook', { method: 'POST', body, headers: { 'x-hub-signature-256': sign(body, APP_SECRET) } });
    await tick(h.deps);
    for (const path of ['/admin', '/admin/leads', '/admin/comments', '/admin/sends', '/admin/contacts/1']) {
      const res = await app.request(path, { headers: auth });
      expect(res.status, path).toBe(200);
    }
    const overview = await (await app.request('/admin', { headers: auth })).text();
    expect(overview).toContain('Acme Studio');
    expect(overview).toContain('LIVE');
    const pause = await app.request('/admin/contacts/1/pause', {
      method: 'POST',
      headers: { ...auth, Origin: 'http://localhost', 'content-type': 'application/x-www-form-urlencoded' },
    });
    expect(pause.status).toBe(302);
    expect((await sql`SELECT ai_paused_until FROM contacts WHERE id = 1`)[0]!.ai_paused_until).not.toBeNull();
  });
});
