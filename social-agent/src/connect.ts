import { randomBytes } from 'node:crypto';
import type { Context, Hono } from 'hono';
import { getSignedCookie, setSignedCookie, deleteCookie } from 'hono/cookie';
import { configuredPublicUrl, verifyToken } from './config/env.js';
import {
  assignConnection,
  decryptToken,
  deleteConnection,
  encryptToken,
  listConnections,
  markSubscribed,
  setState,
  upsertConnection,
} from './db/connections.js';
import type { Deps } from './engine/deps.js';
import { html, type Raw } from './html.js';
import { MetaApiError } from './meta/client.js';
import { LOGIN_SCOPES, subscribeApp, subscribePage } from './meta/subscriptions.js';

/** https://host of this server, from config or from the request (Railway/Render proxies set the headers). */
export function publicBase(deps: Deps, c: Context): string {
  const configured = configuredPublicUrl(deps.env);
  if (configured) return configured;
  const proto = c.req.header('x-forwarded-proto')?.split(',')[0] ?? new URL(c.req.url).protocol.replace(':', '');
  const host = c.req.header('x-forwarded-host') ?? c.req.header('host') ?? new URL(c.req.url).host;
  return `${proto}://${host}`;
}

export const redirectUri = (deps: Deps, c: Context) => `${publicBase(deps, c)}/admin/connect/callback`;

const describe = (err: unknown) =>
  err instanceof MetaApiError ? `${err.message} (code ${err.code ?? '?'}${err.subcode ? `/${err.subcode}` : ''})` : (err as Error).message;

type Layout = (title: string, body: Raw) => string;

export function mountConnect(app: Hono, deps: Deps, layout: Layout) {
  const { env, sql } = deps;
  const cookieSecret = () => env.META_APP_SECRET ?? env.ADMIN_PASSWORD ?? 'unset';

  app.get('/connect', async (c) => {
    const connections = await listConnections(sql);
    const missing = (['META_APP_ID', 'META_APP_SECRET'] as const).filter((k) => !env[k]);
    const msg = c.req.query('msg');
    const err = c.req.query('err');
    // A business whose own file names a Page owns that Page; the others can be picked here.
    const viaConnection = new Set(connections.map((x) => x.business).filter(Boolean));
    const fileOwner = (pageId: string) =>
      deps.registry.businesses.find((b) => b.meta.page_id === pageId && !viaConnection.has(b.slug))?.slug;
    const choosable = (pageId: string) =>
      deps.registry.businesses.filter((b) => !b.meta.page_id || b.meta.page_id === pageId || viaConnection.has(b.slug));

    return c.html(
      layout(
        'Connect Facebook & Instagram',
        html`${msg ? html`<p class="card ok">${msg}</p>` : ''}${err ? html`<p class="card bad">${err}</p>` : ''}
        <section class="card">
          <h2>1. Connect your Pages</h2>
          <p>Log in with the Facebook account that manages the Page. Meta asks which Pages and Instagram accounts to share. Pick the ones this system should answer for. The Instagram account must be a professional account linked to the Page.</p>
          ${
            missing.length
              ? html`<p class="bad">Set ${missing.join(' and ')} on the server first (Meta app → App settings → Basic), then reload.</p>`
              : html`<p><a class="button" href="/admin/connect/start">Connect Facebook &amp; Instagram</a></p>
                <p class="muted">If Meta says the URL is blocked, add this to Meta app → Facebook Login → Settings → Valid OAuth Redirect URIs:<br><code>${redirectUri(deps, c)}</code></p>`
          }
        </section>
        <section class="card table">
          <h2>2. Choose which business each Page belongs to</h2>
          ${
            connections.length === 0
              ? html`<p class="muted">No Pages connected yet.</p>`
              : html`<table><tr><th>Page</th><th>Instagram</th><th>Business</th><th>Webhooks</th><th></th></tr>
              ${connections.map(
                (p) => html`<tr>
                  <td><b>${p.page_name}</b><div class="meta">${p.page_id}</div></td>
                  <td>${p.instagram_id ? html`@${p.instagram_username ?? p.instagram_id}<div class="meta">${p.instagram_id}</div>` : html`<span class="bad">none linked</span>`}</td>
                  <td>${
                    fileOwner(p.page_id)
                      ? html`${fileOwner(p.page_id)} <span class="meta">(set in its file)</span>`
                      : html`<form method="post" action="/admin/connect/${p.page_id}/assign">
                    <select name="business"><option value="">— not used —</option>
                    ${choosable(p.page_id).map(
                      (b) => html`<option value="${b.slug}" ${p.business === b.slug ? 'selected' : ''}>${b.name} (${b.slug})</option>`,
                    )}
                    </select> <button>Save</button></form>`
                  }</td>
                  <td>${p.subscribed_at ? html`<span class="live">✓ subscribed</span>` : html`<span class="dry">not yet</span>`}
                    <form class="inline" method="post" action="/admin/connect/${p.page_id}/subscribe"><button>Subscribe${p.subscribed_at ? ' again' : ''}</button></form></td>
                  <td><form class="inline" method="post" action="/admin/connect/${p.page_id}/remove"><button>Remove</button></form></td>
                </tr>`,
              )}</table>
              <p class="muted">Businesses come from the files in businesses/. Saving a business subscribes that Page to this app's webhooks.</p>`
          }
        </section>
        <section class="card">
          <h2>3. App webhooks</h2>
          <p>Registers this server's webhook URL with your Meta app, for Facebook and Instagram. It is the same as filling in App Dashboard → Webhooks by hand, and you only need to do it once.</p>
          <form method="post" action="/admin/connect/app-webhooks"><button ${missing.length ? 'disabled' : ''}>Register webhooks automatically</button></form>
          <p class="muted">By hand: callback URL <code>${publicBase(deps, c)}/webhook</code>, verify token <code>${verifyToken(env) ?? '(set META_APP_SECRET)'}</code>.</p>
        </section>`,
      ),
    );
  });

  app.get('/connect/start', async (c) => {
    if (!env.META_APP_ID || !env.META_APP_SECRET) return c.redirect('/admin/connect?err=' + encodeURIComponent('META_APP_ID and META_APP_SECRET are not set'));
    const state = randomBytes(16).toString('hex');
    const secure = publicBase(deps, c).startsWith('https://');
    await setSignedCookie(c, 'connect_state', state, cookieSecret(), { path: '/admin/connect', httpOnly: true, secure, sameSite: 'Lax', maxAge: 900 });
    const url = new URL(`https://www.facebook.com/${env.META_GRAPH_VERSION}/dialog/oauth`);
    url.searchParams.set('client_id', env.META_APP_ID);
    url.searchParams.set('redirect_uri', redirectUri(deps, c));
    url.searchParams.set('state', state);
    url.searchParams.set('response_type', 'code');
    if (env.META_LOGIN_CONFIG_ID) url.searchParams.set('config_id', env.META_LOGIN_CONFIG_ID);
    else url.searchParams.set('scope', LOGIN_SCOPES.join(','));
    return c.redirect(url.toString());
  });

  app.get('/connect/callback', async (c) => {
    const back = (key: 'msg' | 'err', text: string) => c.redirect(`/admin/connect?${key}=${encodeURIComponent(text)}`);
    const q = c.req.query();
    if (q.error) return back('err', `Facebook login was cancelled or failed: ${q.error_description ?? q.error}`);
    const expected = await getSignedCookie(c, cookieSecret(), 'connect_state');
    deleteCookie(c, 'connect_state', { path: '/admin/connect' });
    if (!q.state || !expected || q.state !== expected) return back('err', 'The login expired or came from somewhere else. Press Connect again.');
    if (!q.code || !env.META_APP_ID || !env.META_APP_SECRET) return back('err', 'Missing login code.');

    try {
      const anon = deps.graph('');
      const short = await anon.get<{ access_token: string }>('oauth/access_token', {
        client_id: env.META_APP_ID,
        client_secret: env.META_APP_SECRET,
        redirect_uri: redirectUri(deps, c),
        code: q.code,
      });
      // Page tokens made from a long-lived user token do not expire.
      const long = await anon.get<{ access_token: string }>('oauth/access_token', {
        grant_type: 'fb_exchange_token',
        client_id: env.META_APP_ID,
        client_secret: env.META_APP_SECRET,
        fb_exchange_token: short.access_token,
      });
      const pages = await deps.graph(long.access_token).get<{
        data: { id: string; name: string; access_token?: string; instagram_business_account?: { id: string; username?: string } }[];
      }>('me/accounts', { fields: 'id,name,access_token,instagram_business_account{id,username}', limit: '100' });

      const usable = pages.data.filter((p) => p.access_token);
      for (const p of usable) {
        await upsertConnection(sql, {
          pageId: p.id,
          pageName: p.name,
          instagramId: p.instagram_business_account?.id,
          instagramUsername: p.instagram_business_account?.username,
          tokenEnc: encryptToken(p.access_token!, env.META_APP_SECRET),
        });
      }
      await setState(sql, 'last_connect', { pages: usable.map((p) => p.name), at: new Date() });
      await deps.reloadConnections();
      if (usable.length === 0) {
        return back('err', 'Logged in, but Meta shared no Pages. Press Connect again and make sure you tick your Page (and its Instagram account) in the Meta dialog.');
      }
      return back('msg', `Connected ${usable.length} Page(s): ${usable.map((p) => p.name).join(', ')}. Now choose the business for each one below.`);
    } catch (err) {
      deps.log.error('connect failed', { err });
      return back('err', `Meta refused the connection: ${describe(err)}`);
    }
  });

  const withPage = async (pageId: string) => (await listConnections(sql)).find((p) => p.page_id === pageId);

  async function subscribe(pageId: string): Promise<string | undefined> {
    const page = await withPage(pageId);
    const token = page && env.META_APP_SECRET ? decryptToken(page.token_enc, env.META_APP_SECRET) : undefined;
    if (!token) return 'No usable token for this Page. Connect it again.';
    try {
      await subscribePage(deps.graph(token), pageId);
      await markSubscribed(sql, pageId);
      return undefined;
    } catch (err) {
      return describe(err);
    }
  }

  app.post('/connect/:pageId/assign', async (c) => {
    const pageId = c.req.param('pageId');
    const business = String((await c.req.parseBody()).business ?? '') || null;
    if (business && !deps.registry.bySlug(business)) return c.redirect('/admin/connect?err=' + encodeURIComponent('Unknown business'));
    await assignConnection(sql, pageId, business);
    const problem = business ? await subscribe(pageId) : undefined;
    await deps.reloadConnections();
    if (problem) return c.redirect('/admin/connect?err=' + encodeURIComponent(`Saved, but subscribing the Page failed: ${problem}`));
    return c.redirect('/admin/connect?msg=' + encodeURIComponent(business ? `Saved. ${business} now answers for this Page, and the Page is subscribed.` : 'Saved.'));
  });

  app.post('/connect/:pageId/subscribe', async (c) => {
    const problem = await subscribe(c.req.param('pageId'));
    return c.redirect(problem ? '/admin/connect?err=' + encodeURIComponent(`Subscribing failed: ${problem}`) : '/admin/connect?msg=Subscribed.');
  });

  app.post('/connect/:pageId/remove', async (c) => {
    await deleteConnection(sql, c.req.param('pageId'));
    await deps.reloadConnections();
    return c.redirect('/admin/connect?msg=Removed.');
  });

  app.post('/connect/app-webhooks', async (c) => {
    const vt = verifyToken(env);
    if (!env.META_APP_ID || !env.META_APP_SECRET || !vt) return c.redirect('/admin/connect?err=' + encodeURIComponent('Set META_APP_ID and META_APP_SECRET first.'));
    const results = await subscribeApp(deps.graph(`${env.META_APP_ID}|${env.META_APP_SECRET}`), env.META_APP_ID, `${publicBase(deps, c)}/webhook`, vt);
    await setState(sql, 'app_webhooks', { results, at: new Date() });
    const failed = results.filter((r) => !r.ok);
    if (failed.length === 0) return c.redirect('/admin/connect?msg=' + encodeURIComponent('Webhooks registered for Facebook Pages and Instagram.'));
    return c.redirect(
      '/admin/connect?err=' +
        encodeURIComponent(`${failed.map((f) => `${f.object}: ${f.error}`).join(' · ')}. Register them by hand in App Dashboard → Webhooks with the values below.`),
    );
  });
}
