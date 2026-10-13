import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { configuredPublicUrl, loadEnv, verifyToken } from '../src/config/env.js';
import { buildRegistry } from '../src/config/load.js';
import type { Sql } from '../src/db/index.js';
import { decryptToken, encryptToken, listConnections } from '../src/db/connections.js';
import { insertWebhookEvent } from '../src/db/repo.js';
import { createApp } from '../src/server.js';
import { tick } from '../src/worker.js';
import { APP_SECRET, makeBusiness } from './fixtures.js';
import { APP_ID, dbAvailable, freshDb, igComment, makeHarness, truncate, type Harness } from './harness.js';

describe('token encryption and helpers', () => {
  it('round-trips, and a different secret cannot read it', () => {
    const blob = encryptToken('EAAG-page-token', 'secret-1');
    expect(blob).not.toContain('EAAG');
    expect(decryptToken(blob, 'secret-1')).toBe('EAAG-page-token');
    expect(decryptToken(blob, 'secret-2')).toBeUndefined();
  });

  it('derives a stable verify token from the app secret when none is set', () => {
    const a = verifyToken(loadEnv({ META_APP_SECRET: 's' }));
    expect(a).toMatch(/^[0-9a-f]{32}$/);
    expect(verifyToken(loadEnv({ META_APP_SECRET: 's' }))).toBe(a);
    expect(verifyToken(loadEnv({ META_APP_SECRET: 's', META_VERIFY_TOKEN: 'mine' }))).toBe('mine');
  });

  it('finds the public URL on Railway', () => {
    expect(configuredPublicUrl(loadEnv({ RAILWAY_PUBLIC_DOMAIN: 'x.up.railway.app' }))).toBe('https://x.up.railway.app');
    expect(configuredPublicUrl(loadEnv({ PUBLIC_URL: 'https://a.io/' }))).toBe('https://a.io');
  });

  it('a business without IDs in its file takes the Page assigned to it', () => {
    const reg = buildRegistry([makeBusiness({ meta: {} })]);
    expect(reg.byAccount('facebook', '555')).toBeUndefined();
    reg.refresh([{ page_id: '555', instagram_id: '1784', business: 'acme' }]);
    expect(reg.byAccount('facebook', '555')?.slug).toBe('acme');
    expect(reg.byAccount('instagram', '1784')?.slug).toBe('acme');
    reg.refresh([{ page_id: '555', instagram_id: '1784', business: null }]);
    expect(reg.byAccount('facebook', '555')).toBeUndefined();
  });
});

const hasDb = await dbAvailable();

describe.skipIf(!hasDb)('Connect Facebook & Instagram (admin)', () => {
  let sql: Sql;
  let h: Harness;
  let app: ReturnType<typeof createApp>;
  const auth = { Authorization: `Basic ${Buffer.from('admin:pw').toString('base64')}` };
  const post = (path: string, body: Record<string, string> = {}) =>
    app.request(path, {
      method: 'POST',
      headers: { ...auth, Origin: 'http://localhost', 'content-type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(body).toString(),
    });

  beforeAll(async () => {
    sql = await freshDb();
  });
  afterAll(async () => {
    await sql?.end({ timeout: 2 });
  });
  beforeEach(async () => {
    await truncate(sql);
    // A business file with no Page IDs and no token: everything comes from the Connect button.
    h = await makeHarness(sql, [makeBusiness({ meta: {} })], { PUBLIC_URL: 'https://agent.example.app' });
    h.meta.pages = [
      { id: '9001', name: 'Acme Studio', access_token: 'PAGE_TOKEN_9001', instagram_business_account: { id: '178400009001', username: 'acme.studio' } },
      { id: '9002', name: 'Side Project', access_token: 'PAGE_TOKEN_9002' },
    ];
    app = createApp(h.deps);
  });

  async function connect() {
    const start = await app.request('/admin/connect/start', { headers: auth });
    expect(start.status).toBe(302);
    const dialog = new URL(start.headers.get('location')!);
    const cookie = start.headers.get('set-cookie')!.split(';')[0]!;
    const state = dialog.searchParams.get('state')!;
    const cb = await app.request(`/admin/connect/callback?code=CODE123&state=${state}`, { headers: { ...auth, Cookie: cookie } });
    return { dialog, cb };
  }

  it('the button sends you to Facebook login with the right app, redirect and permissions', async () => {
    const { dialog } = await connect();
    expect(dialog.origin + dialog.pathname).toBe('https://www.facebook.com/v26.0/dialog/oauth');
    expect(dialog.searchParams.get('client_id')).toBe(APP_ID);
    expect(dialog.searchParams.get('redirect_uri')).toBe('https://agent.example.app/admin/connect/callback');
    expect(dialog.searchParams.get('scope')).toContain('instagram_manage_messages');
  });

  it('the callback stores every shared Page with an encrypted token', async () => {
    const { cb } = await connect();
    expect(cb.status).toBe(302);
    expect(decodeURIComponent(cb.headers.get('location')!)).toContain('Connected 2 Page(s): Acme Studio, Side Project');
    const exchange = h.meta.calls.filter((c) => c.method === 'get' && c.args[0] === 'oauth/access_token');
    expect(exchange[0]!.args[1]).toMatchObject({ code: 'CODE123', client_id: APP_ID, redirect_uri: 'https://agent.example.app/admin/connect/callback' });
    expect(exchange[1]!.args[1]).toMatchObject({ grant_type: 'fb_exchange_token', fb_exchange_token: 'SHORT_USER_TOKEN' });
    const rows = await listConnections(sql);
    expect(rows.map((r) => r.page_name)).toEqual(['Acme Studio', 'Side Project']);
    expect(rows[0]!.token_enc).not.toContain('PAGE_TOKEN');
    expect(decryptToken(rows[0]!.token_enc, APP_SECRET)).toBe('PAGE_TOKEN_9001');
  });

  it('rejects a callback whose state does not match', async () => {
    await app.request('/admin/connect/start', { headers: auth });
    const cb = await app.request('/admin/connect/callback?code=X&state=forged', { headers: auth });
    expect(decodeURIComponent(cb.headers.get('location')!)).toContain('expired');
    expect(await listConnections(sql)).toEqual([]);
  });

  it('choosing the business subscribes the Page and makes it work end to end', async () => {
    await connect();
    const b = h.deps.registry.bySlug('acme')!;
    expect(h.deps.isLive(b)).toBe(false); // not connected yet

    const res = await post('/admin/connect/9001/assign', { business: 'acme' });
    expect(decodeURIComponent(res.headers.get('location')!)).toContain('now answers for this Page');
    expect(h.meta.calls.some((c) => c.method === 'post' && c.args[0] === '9001/subscribed_apps')).toBe(true);
    expect((await listConnections(sql)).find((c) => c.page_id === '9001')).toMatchObject({ business: 'acme', subscribed_at: expect.any(Date) });

    const connected = h.deps.registry.bySlug('acme')!;
    expect(connected.meta).toMatchObject({ page_id: '9001', instagram_id: '178400009001' });
    expect(h.deps.isLive(connected)).toBe(true);

    // A comment on the connected Instagram account now runs the funnel with the stored Page token.
    const payload = igComment({ id: 'C1', text: 'guide please' });
    (payload.entry[0] as any).id = '178400009001';
    await insertWebhookEvent(sql, 'instagram', payload);
    await tick(h.deps);
    expect(h.meta.sends()[0]).toMatchObject({ pageId: '9001', recipient: { comment_id: 'C1' } });
    expect(h.meta.tokens).toContain('PAGE_TOKEN_9001');
  });

  it('registers the app webhooks for Page and Instagram', async () => {
    const res = await post('/admin/connect/app-webhooks');
    expect(decodeURIComponent(res.headers.get('location')!)).toContain('Webhooks registered');
    const subs = h.meta.calls.filter((c) => c.method === 'post' && c.args[0] === `${APP_ID}/subscriptions`);
    expect(subs.map((s) => s.args[1].object)).toEqual(['page', 'instagram']);
    expect(subs[0]!.args[1]).toMatchObject({ callback_url: 'https://agent.example.app/webhook', verify_token: 'test-verify-token' });
    expect(h.meta.tokens).toContain(`${APP_ID}|${APP_SECRET}`);
  });

  it('setup, connect and test pages render; the test page simulates comments and chats', async () => {
    for (const path of ['/admin/setup', '/admin/connect', '/admin/test']) {
      expect((await app.request(path, { headers: auth })).status, path).toBe(200);
    }
    const setup = await (await app.request('/admin/setup', { headers: auth })).text();
    expect(setup).toContain('https://agent.example.app/webhook');
    expect(setup).toContain('Not connected');

    const sim = await (await post('/admin/test/comment?b=acme', { platform: 'instagram', post: 'MEDIA_A', text: 'send the guide' })).text();
    expect(sim).toContain('Funnel "guide-reel" fires');

    h.ai.nextReply = { text: 'We run ads for e-commerce brands. What do you sell?', lead: { interest: 'ads' } };
    const chat = await (await post('/admin/test/chat?b=acme', { text: 'hi, what do you do?', state: '' })).text();
    expect(chat).toContain('What do you sell?');
    expect(chat).toContain('Saved to the lead');
    expect(h.meta.sends()).toEqual([]); // nothing goes to Meta from the test page
  });
});
