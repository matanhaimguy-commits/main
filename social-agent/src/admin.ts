import { Hono } from 'hono';
import { basicAuth } from 'hono/basic-auth';
import { csrf } from 'hono/csrf';
import { getContact, pauseAi, recentMessages, resumeAi, STAGES, updateLead, type Contact, type Stage } from './db/repo.js';
import { mountConnect } from './connect.js';
import type { Deps } from './engine/deps.js';
import { html, page, type Raw } from './html.js';
import { mountSetup } from './setup.js';
import { explainReason } from './logic/funnels.js';

const nav = (title: string, body: Raw) =>
  page(
    title,
    html`<header><b>Social Agent</b><a href="/admin/setup">Setup</a><a href="/admin/connect">Connect</a><a href="/admin/test">Test the bot</a><a href="/admin">Overview</a><a href="/admin/leads">Leads</a><a href="/admin/comments">Comments</a><a href="/admin/sends">Sends</a></header><main><h1>${title}</h1>${body}</main>`,
  );

const who = (c: Pick<Contact, 'name' | 'username' | 'external_id'>) => c.name ?? (c.username ? `@${c.username}` : c.external_id);

export function adminRoutes(deps: Deps): Hono {
  const app = new Hono();
  const password = deps.env.ADMIN_PASSWORD;
  if (!password) {
    app.all('*', (c) => c.text('Admin is disabled. Set ADMIN_PASSWORD to enable it.', 404));
    return app;
  }
  app.use('*', basicAuth({ username: 'admin', password }));
  app.use('*', csrf());
  const sql = deps.sql;
  mountSetup(app, deps, nav);
  mountConnect(app, deps, nav);

  app.get('/', async (c) => {
    const cards: Raw[] = [];
    for (const b of deps.registry.businesses) {
      const [k] = await sql<Record<string, number>[]>`
        SELECT
          (SELECT count(*) FROM comments WHERE business = ${b.slug} AND received_at > now() - interval '7 days')::int AS comments,
          (SELECT count(*) FROM comments WHERE business = ${b.slug} AND outcome = 'funnel' AND received_at > now() - interval '7 days')::int AS funnel,
          (SELECT count(*) FROM comments WHERE business = ${b.slug} AND outcome = 'ai' AND received_at > now() - interval '7 days')::int AS ai_comments,
          (SELECT count(*) FROM sends WHERE business = ${b.slug} AND step = 'opener' AND status IN ('sent','dry_run') AND created_at > now() - interval '7 days')::int AS openers,
          (SELECT count(*) FROM taps WHERE business = ${b.slug} AND created_at > now() - interval '7 days')::int AS taps,
          (SELECT count(*) FROM sends WHERE business = ${b.slug} AND read_at IS NOT NULL AND created_at > now() - interval '7 days')::int AS reads,
          (SELECT count(*) FROM sends WHERE business = ${b.slug} AND delivered_at IS NOT NULL AND created_at > now() - interval '7 days')::int AS delivered,
          (SELECT coalesce(sum(clicks),0) FROM links WHERE business = ${b.slug} AND created_at > now() - interval '7 days')::int AS clicks,
          (SELECT count(*) FROM sends WHERE business = ${b.slug} AND step IN ('ai','followup') AND status IN ('sent','dry_run') AND created_at > now() - interval '7 days')::int AS ai_msgs,
          (SELECT count(*) FROM sends WHERE business = ${b.slug} AND status IN ('failed','unknown') AND created_at > now() - interval '7 days')::int AS failed,
          (SELECT count(*) FROM contacts WHERE business = ${b.slug} AND stage IN ('hot','booked'))::int AS hot,
          (SELECT count(*) FROM contacts WHERE business = ${b.slug} AND ai_paused_until > now())::int AS paused,
          (SELECT coalesce(sum(input_tokens + output_tokens),0) FROM ai_runs WHERE business = ${b.slug} AND created_at > now() - interval '7 days')::int AS tokens`;
      const reasons = await sql<{ skip_reason: string; n: number }[]>`
        SELECT skip_reason, count(*)::int AS n FROM comments
        WHERE business = ${b.slug} AND outcome = 'skipped' AND received_at > now() - interval '7 days'
        GROUP BY 1 ORDER BY 2 DESC LIMIT 6`;
      const live = deps.isLive(b);
      const kpis: [string, number][] = [
        ['comments', k!.comments!],
        ['funnel matches', k!.funnel!],
        ['AI-handled comments', k!.ai_comments!],
        ['opener DMs', k!.openers!],
        ['button taps', k!.taps!],
        ['reads', k!.reads!],
        ['delivered (FB only)', k!.delivered!],
        ['link clicks', k!.clicks!],
        ['AI messages', k!.ai_msgs!],
        ['hot / booked leads', k!.hot!],
        ['AI paused threads', k!.paused!],
        ['failed sends', k!.failed!],
      ];
      cards.push(html`<section class="card">
        <h2>${b.name} <span class="pill ${live ? 'live' : 'dry'}">${live ? 'LIVE' : 'DRY RUN'}</span>
          ${b.testers.length ? html`<span class="pill">testers only</span>` : ''}</h2>
        <div class="grid">${kpis.map(([l, n]) => html`<div class="kpi"><div class="n ${l === 'failed sends' && n > 0 ? 'bad' : ''}">${n}</div><div class="l">${l}</div></div>`)}</div>
        <p class="muted">Last 7 days. Instagram has no delivery receipts: judge Instagram funnels by reads, taps and clicks. AI tokens: ${k!.tokens!.toLocaleString()}.</p>
        ${reasons.length ? html`<p>Skipped comments: ${reasons.map((r) => html`<span class="pill">${r.skip_reason ?? 'unknown'}: ${r.n}</span> `)}</p>` : ''}
        <p><a href="/admin/leads?b=${b.slug}">Leads</a> · <a href="/admin/comments?b=${b.slug}">Comments</a> · <a href="/admin/sends?b=${b.slug}">Sends</a></p>
      </section>`);
    }
    const notReady = deps.registry.businesses.length === 0 || deps.registry.businesses.some((b) => !b.meta.page_id);
    return c.html(
      nav(
        'Overview',
        html`${notReady ? html`<p class="card">Not fully set up yet. <a href="/admin/setup">Open Setup</a> to see what's left.</p>` : ''}
        ${cards.length ? cards : html`<p>No businesses configured. Add a file to businesses/.</p>`}`,
      ),
    );
  });

  app.get('/leads', async (c) => {
    const b = c.req.query('b');
    const stage = c.req.query('stage');
    const rows = await sql<Contact[]>`
      SELECT * FROM contacts
      WHERE (${b ?? null}::text IS NULL OR business = ${b ?? null})
        AND (${stage ?? null}::text IS NULL OR stage = ${stage ?? null})
      ORDER BY GREATEST(last_inbound_at, last_outbound_at, created_at) DESC NULLS LAST LIMIT 200`;
    return c.html(
      nav(
        'Leads',
        html`<p>${['', ...STAGES].map((s) => html`<a class="pill" href="?${b ? `b=${b}&` : ''}${s ? `stage=${s}` : ''}">${s || 'all'}</a> `)}</p>
        <div class="card table"><table><tr><th>Who</th><th>Business</th><th>Stage</th><th>Wants</th><th>Contact</th><th>Last activity</th><th>AI</th></tr>
        ${rows.map(
          (r) => html`<tr><td><a href="/admin/contacts/${r.id}">${who(r)}</a><div class="meta">${r.platform}${r.source ? ` · ${r.source}` : ''}</div></td>
          <td>${r.business}</td><td><span class="pill">${r.stage}</span></td><td>${r.interest}</td>
          <td>${r.phone}${r.phone && r.email ? html`<br>` : ''}${r.email}</td>
          <td>${r.last_inbound_at ?? r.created_at}</td>
          <td>${r.opted_out ? html`<span class="bad">opted out</span>` : r.ai_paused_until && r.ai_paused_until > new Date() ? html`<span class="pill dry">paused</span>` : 'on'}</td></tr>`,
        )}</table></div>`,
      ),
    );
  });

  app.get('/contacts/:id', async (c) => {
    const contact = await getContact(sql, Number(c.req.param('id')));
    if (!contact) return c.notFound();
    const msgs = await recentMessages(sql, contact.id, 200);
    const paused = contact.ai_paused_until && contact.ai_paused_until > new Date();
    return c.html(
      nav(
        who(contact),
        html`<section class="card">
          <p><span class="pill">${contact.platform}</span> <span class="pill">${contact.stage}</span> ${contact.business}
            ${contact.username ? html` · @${contact.username}` : ''}</p>
          <p>${[
            contact.phone && `Phone: ${contact.phone}`,
            contact.email && `Email: ${contact.email}`,
            contact.interest && `Wants: ${contact.interest}`,
            contact.budget && `Budget: ${contact.budget}`,
            contact.timeline && `Timeline: ${contact.timeline}`,
            contact.follows_business !== null && `Follows: ${contact.follows_business ? 'yes' : 'no'}`,
            contact.source && `Source: ${contact.source}`,
          ]
            .filter(Boolean)
            .join(' · ')}</p>
          ${contact.notes ? html`<p class="muted">${contact.notes}</p>` : ''}
          <p>AI in this thread: ${contact.opted_out ? html`<b class="bad">opted out</b>` : paused ? html`<b>paused</b> until ${contact.ai_paused_until} (${contact.ai_pause_reason})` : html`<b>on</b>`}</p>
          <form class="inline" method="post" action="/admin/contacts/${contact.id}/pause"><button>Pause AI 24h</button></form>
          <form class="inline" method="post" action="/admin/contacts/${contact.id}/resume"><button>Resume AI</button></form>
          <form class="inline" method="post" action="/admin/contacts/${contact.id}/stage">
            <select name="stage">${STAGES.map((s) => html`<option ${s === contact.stage ? 'selected' : ''}>${s}</option>`)}</select><button>Set stage</button></form>
        </section>
        <section class="card msgs">${msgs.map(
          (m) => html`<div class="msg ${m.direction}">${m.text}<div class="meta">${m.source} · ${m.created_at}</div></div>`,
        )}</section>`,
      ),
    );
  });

  app.post('/contacts/:id/pause', async (c) => {
    const id = Number(c.req.param('id'));
    await pauseAi(sql, id, new Date(Date.now() + 24 * 3_600_000), 'paused from admin');
    return c.redirect(`/admin/contacts/${id}`);
  });
  app.post('/contacts/:id/resume', async (c) => {
    const id = Number(c.req.param('id'));
    await resumeAi(sql, id);
    return c.redirect(`/admin/contacts/${id}`);
  });
  app.post('/contacts/:id/stage', async (c) => {
    const id = Number(c.req.param('id'));
    const stage = String((await c.req.parseBody()).stage ?? '');
    if (STAGES.includes(stage as Stage)) await updateLead(sql, id, { stage: stage as Stage });
    return c.redirect(`/admin/contacts/${id}`);
  });

  app.get('/comments', async (c) => {
    const b = c.req.query('b');
    const rows = await sql<Record<string, any>[]>`
      SELECT * FROM comments WHERE (${b ?? null}::text IS NULL OR business = ${b ?? null})
      ORDER BY received_at DESC LIMIT 200`;
    return c.html(
      nav(
        'Comments',
        html`<p class="muted">Every comment gets a row, matched or not.</p><div class="card table"><table>
        <tr><th>When</th><th>Business</th><th>From</th><th>Comment</th><th>Outcome</th></tr>
        ${rows.map(
          (r) => html`<tr><td>${r.received_at}</td><td>${r.business}<div class="meta">${r.platform} · post ${r.post_id}</div></td>
          <td>${r.contact_id ? html`<a href="/admin/contacts/${r.contact_id}">${r.author_name ?? r.author_id}</a>` : r.author_name ?? r.author_id}</td>
          <td>${r.text}</td>
          <td><span class="pill">${r.outcome}</span> ${r.funnel_id ?? ''} ${r.skip_reason ? html`<div class="meta">${explainReason(r.skip_reason)}</div>` : ''}${r.ai_intent ? html`<div class="meta">AI: ${r.ai_intent}</div>` : ''}</td></tr>`,
        )}</table></div>`,
      ),
    );
  });

  app.get('/sends', async (c) => {
    const b = c.req.query('b');
    const rows = await sql<Record<string, any>[]>`
      SELECT * FROM sends WHERE (${b ?? null}::text IS NULL OR business = ${b ?? null})
      ORDER BY created_at DESC LIMIT 200`;
    return c.html(
      nav(
        'Sends',
        html`<p class="muted">The send ledger. Nothing is ever retried. "delivered" exists only on Facebook; Instagram publishes no delivery receipts.</p>
        <div class="card table"><table><tr><th>When</th><th>Business</th><th>What</th><th>Status</th><th>Receipts</th></tr>
        ${rows.map(
          (r) => html`<tr><td>${r.created_at}</td><td>${r.business}<div class="meta">${r.platform}</div></td>
          <td>${r.kind} · ${r.step ?? ''} ${r.funnel_id ? html`· ${r.funnel_id}` : ''}${r.contact_id ? html` · <a href="/admin/contacts/${r.contact_id}">contact</a>` : ''}</td>
          <td><span class="pill ${r.status === 'sent' ? 'live' : r.status === 'dry_run' ? 'dry' : r.status === 'failed' || r.status === 'unknown' ? 'bad' : ''}">${r.status}</span>
            ${r.error_message ? html`<div class="meta">${r.error_code ?? ''} ${r.error_message}</div>` : ''}</td>
          <td>${r.platform === 'facebook' ? (r.delivered_at ? 'delivered ' : '') : ''}${r.read_at ? 'read' : ''}</td></tr>`,
        )}</table></div>`,
      ),
    );
  });

  return app;
}
