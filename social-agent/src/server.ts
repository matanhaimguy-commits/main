import { Hono } from 'hono';
import { adminRoutes } from './admin.js';
import { insertWebhookEvent, recordClick } from './db/repo.js';
import type { Deps } from './engine/deps.js';
import { html, page } from './html.js';
import { verifyHandshake, verifySignature } from './meta/webhook.js';

export function createApp(deps: Deps, hooks: { onEvent?: () => void } = {}): Hono {
  const app = new Hono();
  const { env, log } = deps;

  // Meta calls this once when you register the callback URL. Deploy before registering.
  app.get('/webhook', (c) => {
    if (!env.META_VERIFY_TOKEN) return c.text('META_VERIFY_TOKEN is not set', 503);
    const challenge = verifyHandshake(c.req.query(), env.META_VERIFY_TOKEN);
    if (challenge === undefined) {
      log.warn('webhook verification rejected');
      return c.text('Forbidden', 403);
    }
    return c.text(challenge);
  });

  // Verify, store, answer. Processing happens in the worker, so Meta gets its 200 in
  // milliseconds and never re-sends a batch because our code was slow or failed.
  app.post('/webhook', async (c) => {
    if (!env.META_APP_SECRET) return c.text('META_APP_SECRET is not set', 503);
    const raw = new Uint8Array(await c.req.arrayBuffer());
    if (!verifySignature(raw, c.req.header('x-hub-signature-256'), env.META_APP_SECRET)) {
      log.warn('webhook signature rejected', { ip: c.req.header('x-forwarded-for') });
      return c.text('Invalid signature', 401);
    }
    let body: { object?: string };
    try {
      body = JSON.parse(new TextDecoder().decode(raw));
    } catch {
      return c.text('Invalid JSON', 400);
    }
    try {
      await insertWebhookEvent(deps.sql, body.object, body);
    } catch (err) {
      // Not stored = would be lost. A 500 makes Meta redeliver; the ledger makes that safe.
      log.error('could not store webhook event', { err });
      return c.text('Storage error', 500);
    }
    hooks.onEvent?.();
    return c.text('EVENT_RECEIVED');
  });

  app.get('/health', async (c) => {
    try {
      await deps.sql`SELECT 1`;
    } catch {
      return c.json({ ok: false, db: false }, 503);
    }
    return c.json({
      ok: true,
      businesses: deps.registry.businesses.map((b) => ({ slug: b.slug, live: deps.isLive(b) })),
      ai: !!deps.ai,
    });
  });

  // Tracked links (only when track_clicks is on for a business).
  app.get('/r/:token', async (c) => {
    const url = await recordClick(deps.sql, c.req.param('token'));
    return url ? c.redirect(url, 302) : c.text('Link not found', 404);
  });

  // Meta requires a privacy policy URL and data deletion instructions for a Live app.
  const operator = env.OPERATOR_NAME ?? 'the business operating this page';
  const contact = env.OPERATOR_EMAIL ? html`<a href="mailto:${env.OPERATOR_EMAIL}">${env.OPERATOR_EMAIL}</a>` : html`a direct message to the page`;
  app.get('/privacy', (c) =>
    c.html(
      page(
        'Privacy policy',
        html`<main><h1>Privacy policy</h1>
        <p>This service is operated by ${operator}. It answers comments and direct messages sent to the Facebook Pages and Instagram accounts it manages, through Meta's official APIs.</p>
        <p><b>What we store:</b> messages and comments you send to these accounts, your public name or username, and details you choose to share in the conversation (such as your email or phone number).</p>
        <p><b>Why:</b> to reply to you, to send what you asked for, and to follow up on your request. Replies may be written by an automated assistant; a person on the team can step in at any time.</p>
        <p><b>Sharing:</b> we do not sell your data. Message text is processed by our hosting, database and AI providers only to produce replies.</p>
        <p><b>Retention and deletion:</b> see <a href="/data-deletion">data deletion</a>. Contact: ${contact}.</p></main>`,
      ),
    ),
  );
  app.get('/data-deletion', (c) =>
    c.html(
      page(
        'Data deletion',
        html`<main><h1>Data deletion</h1><p>To delete the data we hold about you, send "delete my data" to the account you messaged, or write to ${contact}. We delete your conversation and profile details within 30 days and confirm when it is done.</p>
        <p>To stop automated messages at any time, reply STOP.</p></main>`,
      ),
    ),
  );

  app.get('/', (c) => c.text('ok'));
  app.route('/admin', adminRoutes(deps));
  return app;
}
