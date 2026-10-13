import type { Hono } from 'hono';
import type { ReplyResult } from './ai/agent.js';
import { verifyToken } from './config/env.js';
import type { Platform } from './config/schema.js';
import { getState, listConnections } from './db/connections.js';
import type { Contact, LeadUpdate, MessageRow } from './db/repo.js';
import type { Deps } from './engine/deps.js';
import { openerMessage, resolveLink } from './engine/funnel.js';
import { publicBase } from './connect.js';
import { html, type Raw } from './html.js';
import { screenComment } from './logic/comments.js';
import { explainReason, selectCommentFunnel, selectMessageFunnel } from './logic/funnels.js';
import { describeMessage } from './meta/messages.js';

type Layout = (title: string, body: Raw) => string;
type Status = 'done' | 'todo' | 'info';

const mark = (s: Status) => (s === 'done' ? html`<span class="live">✓</span>` : s === 'todo' ? html`<span class="bad">✗</span>` : html`<span class="muted">•</span>`);
const ago = (d: Date) => {
  const m = Math.round((Date.now() - d.getTime()) / 60000);
  return m < 1 ? 'just now' : m < 60 ? `${m} min ago` : m < 48 * 60 ? `${Math.round(m / 60)} h ago` : `${Math.round(m / 1440)} days ago`;
};

export function mountSetup(app: Hono, deps: Deps, layout: Layout) {
  const { env, sql } = deps;

  app.get('/setup', async (c) => {
    const base = publicBase(deps, c);
    const verified = await getState(sql, 'webhook_verified_at');
    const lastEvent = await getState(sql, 'last_event_at');
    const connections = await listConnections(sql);
    const step = (s: Status, title: string, body: Raw | string = '') =>
      html`<div class="step"><div class="mark">${mark(s)}</div><div><b>${title}</b><div>${body}</div></div></div>`;

    const businesses = deps.registry.businesses.map((b) => {
      const st = deps.liveStatus(b);
      const conn = connections.find((x) => x.page_id === b.meta.page_id);
      const errors = st.issues.filter((i) => i.level === 'error');
      return html`<div class="card">
        <h2>${b.name} <span class="pill ${st.live ? 'live' : 'dry'}">${st.live ? 'LIVE' : `DRY RUN · ${st.reason}`}</span></h2>
        ${step(b.meta.page_id ? 'done' : 'todo', 'Facebook Page', b.meta.page_id ? `${conn?.page_name ?? b.meta.page_id}` : html`Not connected. <a href="/admin/connect">Connect it</a>.`)}
        ${step(b.meta.instagram_id ? 'done' : 'todo', 'Instagram', b.meta.instagram_id ? `${conn?.instagram_username ? `@${conn.instagram_username}` : b.meta.instagram_id}` : 'No Instagram professional account linked to the Page.')}
        ${conn ? step(conn.subscribed_at ? 'done' : 'todo', 'Page subscribed to webhooks', conn.subscribed_at ? ago(conn.subscribed_at) : html`<a href="/admin/connect">Subscribe it</a>.`) : ''}
        ${step(errors.length ? 'todo' : 'done', 'Business details and funnels', errors.length ? html`${errors.length} problem(s): ${errors.slice(0, 4).map((e) => html`<div class="meta">${e.where ? `[${e.where}] ` : ''}${e.message}</div>`)}` : 'Audit passes.')}
        ${step(b.testers.length ? 'info' : 'info', 'Who gets messages', b.testers.length ? `Only testers: ${b.testers.join(', ')}` : 'Everyone (no testers list).')}
        <p><a href="/admin/test?b=${b.slug}">Test this bot</a></p>
      </div>`;
    });

    return c.html(
      layout(
        'Setup',
        html`<section class="card">
          ${step('done', 'Server and database are running', base)}
          ${step(env.META_APP_ID && env.META_APP_SECRET ? 'done' : 'todo', 'Meta app keys on the server', env.META_APP_ID && env.META_APP_SECRET ? `App ID ${env.META_APP_ID}` : 'Set META_APP_ID and META_APP_SECRET (Meta app → App settings → Basic) on the host, then redeploy.')}
          ${step('info', 'Paste these into your Meta app', html`<table class="kv">
            <tr><td>App settings → Basic → Privacy Policy URL</td><td><code>${base}/privacy</code></td></tr>
            <tr><td>App settings → Basic → User data deletion (instructions URL)</td><td><code>${base}/data-deletion</code></td></tr>
            <tr><td>Facebook Login → Settings → Valid OAuth Redirect URIs</td><td><code>${base}/admin/connect/callback</code></td></tr>
            <tr><td>Webhooks → Callback URL</td><td><code>${base}/webhook</code></td></tr>
            <tr><td>Webhooks → Verify token</td><td><code>${verifyToken(env) ?? '(set META_APP_SECRET first)'}</code></td></tr></table>`)}
          ${step(verified ? 'done' : 'todo', 'Meta verified the webhook', verified ? ago(verified.updated_at) : html`On <a href="/admin/connect">Connect</a>, press "Register webhooks automatically" (or paste the values above into App Dashboard → Webhooks).`)}
          ${step(connections.length ? 'done' : 'todo', 'Facebook & Instagram connected', connections.length ? `${connections.length} Page(s): ${connections.map((x) => x.page_name).join(', ')}` : html`<a href="/admin/connect">Connect Facebook &amp; Instagram</a>.`)}
          ${step('info', 'Two switches Meta does not show here', html`In the Meta App Dashboard, switch the app from <b>Development</b> to <b>Live</b> (top bar).<br>
            In the Instagram app: Settings → Messages and story replies → Message controls → Connected tools → turn on <b>Allow access to messages</b>. Without it, Instagram DMs never reach the API.`)}
          ${step(lastEvent ? 'done' : 'todo', 'Events arriving from Meta', lastEvent ? `Last one ${ago(lastEvent.updated_at)}` : 'None yet. Comment on a post or send a DM from a second account. If nothing arrives: is the Meta app switched to Live?')}
          ${step(deps.ai ? 'done' : 'todo', 'AI (Claude) key', deps.ai ? html`Set. <a href="/admin/test">Chat with the bot</a>.` : 'Set ANTHROPIC_API_KEY on the host. Funnels work without it; AI replies do not.')}
          ${step(env.LIVE_SENDING ? 'done' : 'todo', 'Real sending switched on', env.LIVE_SENDING ? 'LIVE_SENDING=true. Each business also needs live: true in its file.' : 'LIVE_SENDING is off: everything is a dry run (recorded, not sent). Set LIVE_SENDING=true when the tests look right.')}
          ${step(env.TELEGRAM_BOT_TOKEN || env.ALERT_WEBHOOK_URL ? 'done' : 'info', 'Alerts', env.TELEGRAM_BOT_TOKEN || env.ALERT_WEBHOOK_URL ? 'Configured.' : 'Optional: TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID for hot-lead and problem alerts.')}
        </section>
        ${businesses.length ? businesses : html`<p class="card">No business files yet. Add one to businesses/ (see _template.yaml).</p>`}`,
      ),
    );
  });

  // ---- Test the bot (no Meta involved) -------------------------------------------------

  interface ChatState {
    platform: Platform;
    msgs: { d: 'in' | 'out'; t: string }[];
    lead: LeadUpdate;
    notes: string[];
  }
  const emptyState = (): ChatState => ({ platform: 'instagram', msgs: [], lead: {}, notes: [] });
  const parseState = (raw: unknown): ChatState => {
    try {
      const s = JSON.parse(String(raw ?? ''));
      return { ...emptyState(), ...s };
    } catch {
      return emptyState();
    }
  };

  const testPage = (slug: string | undefined, chat: ChatState, sim?: Raw, error?: string) => {
    const b = (slug && deps.registry.bySlug(slug)) || deps.registry.businesses[0];
    if (!b) return layout('Test the bot', html`<p class="card">No business files yet.</p>`);
    const picker = deps.registry.businesses.length > 1
      ? html`<p>${deps.registry.businesses.map((x) => html`<a class="pill ${x.slug === b.slug ? 'live' : ''}" href="/admin/test?b=${x.slug}">${x.name}</a> `)}</p>`
      : '';
    return layout(
      `Test the bot: ${b.name}`,
      html`${picker}
      <section class="card">
        <h2>Chat as a customer</h2>
        <p class="muted">This talks to the real AI with ${b.name}'s details. Nothing is sent to Instagram or Facebook and nothing is saved.</p>
        ${!deps.ai ? html`<p class="bad">ANTHROPIC_API_KEY is not set, so the AI is off.</p>` : ''}
        ${error ? html`<p class="bad">${error}</p>` : ''}
        <div class="msgs">${chat.msgs.map((m) => html`<div class="msg ${m.d}">${m.t}</div>`)}</div>
        ${chat.notes.length ? html`<p class="muted">${chat.notes.slice(-6).map((n) => html`<div class="meta">${n}</div>`)}</p>` : ''}
        <form method="post" action="/admin/test/chat?b=${b.slug}" class="row">
          <input type="hidden" name="state" value="${JSON.stringify(chat)}">
          <input name="text" placeholder="Write like a customer would…" autocomplete="off" autofocus>
          <button ${deps.ai ? '' : 'disabled'}>Send</button>
        </form>
        <form method="get" action="/admin/test"><input type="hidden" name="b" value="${b.slug}"><button>Start over</button></form>
      </section>
      <section class="card">
        <h2>Simulate a comment</h2>
        <p class="muted">Shows which funnel would fire and exactly what the person would receive. Nothing is sent.</p>
        <form method="post" action="/admin/test/comment?b=${b.slug}" class="row">
          <select name="platform"><option>instagram</option><option>facebook</option></select>
          <input name="post" placeholder="Post / reel ID">
          <input name="text" placeholder="Comment text">
          <button>Check</button>
        </form>
        ${sim ?? ''}
      </section>`,
    );
  };

  app.get('/test', (c) => c.html(testPage(c.req.query('b'), emptyState())));

  app.post('/test/chat', async (c) => {
    const slug = c.req.query('b');
    const b = slug ? deps.registry.bySlug(slug) : undefined;
    const form = await c.req.parseBody();
    const chat = parseState(form.state);
    const text = String(form.text ?? '').trim();
    if (!b || !deps.ai || !text) return c.html(testPage(slug, chat));
    chat.msgs.push({ d: 'in', t: text });
    const now = new Date();
    const contact: Contact = {
      id: 0, business: b.slug, platform: chat.platform, external_id: 'admin-test', username: null,
      name: chat.lead.name ?? null, phone: chat.lead.phone ?? null, email: chat.lead.email ?? null,
      stage: chat.lead.stage ?? (chat.msgs.length > 1 ? 'engaged' : 'new'), interest: chat.lead.interest ?? null,
      budget: chat.lead.budget ?? null, timeline: chat.lead.timeline ?? null, notes: chat.lead.notes ?? null,
      source: 'admin test', follows_business: null, opted_out: false, ai_paused_until: null, ai_pause_reason: null,
      needs_reply: true, reply_due_at: null, last_inbound_at: now, last_outbound_at: null, followup_for: null, created_at: now,
    };
    const transcript: MessageRow[] = chat.msgs.map((m, i) => ({
      id: i, contact_id: 0, direction: m.d, source: m.d === 'in' ? 'user' : 'ai', mid: null, text: m.t, payload: null, created_at: now,
    }));
    let res: ReplyResult;
    try {
      res = await deps.ai.reply({ business: b, contact, transcript, mode: 'reply', now });
    } catch (err) {
      chat.msgs.pop();
      return c.html(testPage(slug, chat, undefined, `The AI call failed: ${(err as Error).message}`));
    }
    const link = res.linkId ? b.links.find((l) => l.id === res.linkId) : undefined;
    if (res.text) chat.msgs.push({ d: 'out', t: res.text + (link ? `\n[ ${link.title} → ${link.url} ]` : '') });
    for (const [k, v] of Object.entries(res.lead)) if (v) (chat.lead as Record<string, unknown>)[k] = v;
    if (Object.keys(res.lead).length) chat.notes.push(`Saved to the lead: ${JSON.stringify(res.lead)}`);
    if (res.handoff) chat.notes.push(`Handed to a person (${res.handoff.reason}). In real use the AI now pauses here and you get an alert.`);
    if (res.optOut) chat.notes.push('Customer opted out.');
    if (!res.text) chat.notes.push('The AI chose not to reply.');
    return c.html(testPage(slug, chat));
  });

  app.post('/test/comment', async (c) => {
    const slug = c.req.query('b');
    const b = slug ? deps.registry.bySlug(slug) : undefined;
    if (!b) return c.html(testPage(slug, emptyState()));
    const form = await c.req.parseBody();
    const platform: Platform = form.platform === 'facebook' ? 'facebook' : 'instagram';
    const postId = String(form.post ?? '').trim() || undefined;
    const text = String(form.text ?? '');
    const screen = screenComment(
      { type: 'comment', platform, accountId: '', commentId: 'test', postId, authorId: 'someone', text, createdAt: new Date(), verb: 'add' },
      b,
    );
    let sim: Raw;
    if (screen) {
      sim = html`<p class="bad">Skipped: ${explainReason(screen)}.</p>`;
    } else {
      const d = selectCommentFunnel(b.funnels, { platform, postId, text });
      if (d.kind === 'matched') {
        const f = d.funnel;
        const steps = [
          ['Private reply to the comment', describeMessage(openerMessage(b, f))],
          ...(f.opener.mode === 'tap' ? [['After they tap', describeMessage({ text: f.deliver.text, button: { title: f.deliver.button, url: resolveLink(b, f.deliver.link) } })]] : []),
          ...(f.opener.mode === 'tap' && f.after ? [['Then', f.after]] : []),
        ];
        sim = html`<p class="live">✓ Funnel "${f.id}" fires (keyword "${d.keyword}").</p>
          ${f.public_replies.length ? html`<p class="muted">Public reply: ${f.public_replies.join(' / ')}</p>` : ''}
          ${steps.map(([t, m]) => html`<div class="meta">${t}</div><div class="msg out">${m}</div>`)}`;
      } else {
        const story = selectMessageFunnel(b.funnels, { platform, trigger: 'story_reply', text });
        sim = html`<p class="bad">No DM: ${explainReason(d.reason)}${d.funnel ? ` (${d.funnel.id})` : ''}.</p>
          ${b.ai.comment_replies || b.ai.comment_dms ? html`<p class="muted">The AI would look at this comment and decide whether to answer it.</p>` : ''}
          ${story.kind === 'matched' ? html`<p class="muted">As a story reply it would fire "${story.funnel.id}".</p>` : ''}`;
      }
    }
    return c.html(testPage(slug, emptyState(), sim));
  });
}
