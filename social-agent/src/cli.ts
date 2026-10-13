import { existsSync } from 'node:fs';
import path from 'node:path';
import { createInterface } from 'node:readline/promises';
import { createClaudeAi } from './ai/agent.js';
import { loadEnv, requireEnv, type Env } from './config/env.js';
import { ConfigError, loadRegistry, PROJECT_ROOT, type Registry } from './config/load.js';
import type { Business, Platform } from './config/schema.js';
import { connect, migrate } from './db/index.js';
import type { Contact, LeadUpdate, MessageRow } from './db/repo.js';
import { liveStatus } from './engine/deps.js';
import { openerMessage, resolveLink } from './engine/funnel.js';
import { screenComment } from './logic/comments.js';
import { selectCommentFunnel, selectMessageFunnel } from './logic/funnels.js';
import { createMetaClient, MetaApiError } from './meta/client.js';
import { describeMessage, toMetaMessage } from './meta/messages.js';
import { sign } from './meta/webhook.js';

const envFile = path.join(PROJECT_ROOT, '.env');
if (existsSync(envFile)) process.loadEnvFile(envFile);

const HELP = `Usage: npm run cli -- <command> [args]

Config and safety
  audit                                   Check every business config (run after every change)
  match <business> <platform> <post|-> "<text>"
                                          Which funnel would this comment fire, and why
  preview <business> <funnel>             Show exactly what the person receives, step by step
  chat <business> [instagram|facebook]    Talk to the AI sales agent locally (real Claude, no Meta)

Meta setup
  meta:pages <user-access-token>          Exchange a token, list your Pages, their IG accounts and Page tokens
  meta:check <business>                   Check the token, permissions, IG link and webhook subscription
  meta:subscribe <business>               Subscribe the app to the Page's webhooks (feed + messaging)
  meta:posts <business> [instagram|facebook]
                                          Recent posts with the IDs to pin funnels to
  verify-endpoint <https://.../webhook>   Prove the deployed endpoint accepts and rejects correctly

Database
  migrate                                 Create / update tables
  stats [business] [days]                 Funnel and send report from the ledger`;

const out = (s = '') => process.stdout.write(s + '\n');
const fail = (s: string): never => {
  process.stderr.write(`\n✖ ${s}\n`);
  process.exit(1);
};

function business(reg: Registry, slug: string | undefined): Business {
  if (!slug) fail(`Pass a business slug. Configured: ${reg.businesses.map((b) => b.slug).join(', ') || '(none)'}`);
  return reg.bySlug(slug!) ?? fail(`No business "${slug}". Configured: ${reg.businesses.map((b) => b.slug).join(', ')}`);
}

function metaFor(env: Env, b: Business) {
  const token = process.env[b.meta.page_token_env] ?? fail(`Set ${b.meta.page_token_env} (this Page's access token) in .env`);
  return createMetaClient({ accessToken: token, version: env.META_GRAPH_VERSION });
}

async function main() {
  const [cmd, ...args] = process.argv.slice(2);
  if (!cmd || cmd === 'help' || cmd === '--help') return out(HELP);
  const env = loadEnv();
  const reg = () => loadRegistry(env.BUSINESSES_DIR);

  switch (cmd) {
    case 'migrate': {
      const sql = connect(requireEnv(env, 'DATABASE_URL'), { max: 1 });
      const applied = await migrate(sql, out);
      out(applied.length ? `Applied ${applied.length} migration(s).` : 'Database is up to date.');
      await sql.end();
      return;
    }

    case 'audit': {
      const r = reg();
      if (r.businesses.length === 0) return out('No business configs in businesses/ (files starting with _ are templates).');
      let errors = 0;
      for (const b of r.businesses) {
        const s = liveStatus(b, env);
        out(`\n${b.slug} (${b.name}): ${s.live ? 'LIVE' : `dry run: ${s.reason}`}${b.testers.length ? `, testers only: ${b.testers.join(', ')}` : ''}`);
        if (s.issues.length === 0) out('  ✓ no issues');
        for (const i of s.issues) {
          if (i.level === 'error') errors++;
          out(`  ${i.level === 'error' ? '✖' : '!'} ${i.where ? `[${i.where}] ` : ''}${i.message}`);
        }
      }
      out(errors ? `\n${errors} error(s): affected businesses will not send live until fixed.` : '\nAll clear.');
      process.exitCode = errors ? 1 : 0;
      return;
    }

    case 'match': {
      const [slug, platform, post, ...words] = args;
      const b = business(reg(), slug);
      if (platform !== 'instagram' && platform !== 'facebook') fail('platform must be instagram or facebook');
      const text = words.join(' ');
      const postId = post === '-' ? undefined : post;
      const screen = screenComment(
        { type: 'comment', platform: platform as Platform, accountId: '', commentId: 'test', postId, parentId: undefined, authorId: 'someone', text, createdAt: new Date(), verb: 'add' },
        b,
      );
      if (screen) return out(`Skipped before matching: ${screen}`);
      const d = selectCommentFunnel(b.funnels, { platform: platform as Platform, postId, text });
      out(d.kind === 'matched' ? `✓ Funnel "${d.funnel.id}" fires (keyword "${d.keyword}", ${d.funnel.match})` : `✖ No DM: ${d.reason}${d.funnel ? ` (funnel ${d.funnel.id})` : ''}`);
      for (const trigger of ['story_reply', 'dm_keyword'] as const) {
        const m = selectMessageFunnel(b.funnels, { platform: platform as Platform, trigger, text });
        if (m.kind === 'matched') out(`  As a ${trigger.replace('_', ' ')} it would fire "${m.funnel.id}"`);
      }
      return;
    }

    case 'preview': {
      const [slug, funnelId] = args;
      const b = business(reg(), slug);
      const f = b.funnels.find((x) => x.id === funnelId) ?? fail(`No funnel "${funnelId}". Funnels: ${b.funnels.map((x) => x.id).join(', ')}`);
      out(`Funnel ${f.id} (${f.trigger}, ${f.status}) on ${f.platforms.join(' + ')}`);
      out(`Fires on: ${f.keywords.map((k) => `"${k}"`).join(', ')} (${f.match})${f.trigger === 'comment' ? `, posts: ${f.all_posts ? 'ALL' : f.posts.join(', ')}` : ''}\n`);
      const step = (n: string, m: Parameters<typeof describeMessage>[0]) => {
        out(`── ${n} ──\n${describeMessage(m)}\n`);
        out(`   JSON: ${JSON.stringify(toMetaMessage(m, f.platforms[0]!))}\n`);
      };
      if (f.public_replies.length) out(`── public reply under the comment (one of) ──\n${f.public_replies.join('\n')}\n`);
      step(f.trigger === 'comment' ? '1. private reply to the comment' : '1. reply', openerMessage(b, f));
      if (f.opener.mode === 'link') return out('(mode: link: the button opens the link; the flow ends here)');
      if (f.follow_gate?.enabled) step('2a. if they do not follow (Instagram)', { text: f.follow_gate.text, button: { title: f.follow_gate.button, payload: '…gate' } });
      step('2. after they tap', { text: f.deliver.text, button: { title: f.deliver.button, url: resolveLink(b, f.deliver.link) } });
      if (f.after) step('3. then', { text: f.after });
      out('Open the link in a private window, logged out, before going live.');
      return;
    }

    case 'chat': {
      const b = business(reg(), args[0]);
      const platform = (args[1] as Platform) ?? 'instagram';
      const ai = createClaudeAi({ model: env.CLAUDE_MODEL, apiKey: requireEnv(env, 'ANTHROPIC_API_KEY') });
      const rl = createInterface({ input: process.stdin, output: process.stdout });
      let contact: Contact = {
        id: 0, business: b.slug, platform, external_id: 'local-test', username: null, name: null, phone: null, email: null,
        stage: 'new', interest: null, budget: null, timeline: null, notes: null, source: 'cli chat', follows_business: null,
        opted_out: false, ai_paused_until: null, ai_pause_reason: null, needs_reply: false, reply_due_at: null,
        last_inbound_at: null, last_outbound_at: null, followup_for: null, created_at: new Date(),
      };
      const transcript: MessageRow[] = [];
      const add = (direction: 'in' | 'out', text: string) =>
        transcript.push({ id: transcript.length, contact_id: 0, direction, source: direction === 'in' ? 'user' : 'ai', mid: null, text, payload: null, created_at: new Date() });
      out(`Chatting with the ${b.name} agent as a customer on ${platform}. Model: ${b.ai.model ?? env.CLAUDE_MODEL}. Type /lead to see what it saved, /quit to stop.\n`);
      for (;;) {
        const line = (await rl.question('you › ')).trim();
        if (!line) continue;
        if (line === '/quit') break;
        if (line === '/lead') {
          out(JSON.stringify({ stage: contact.stage, name: contact.name, phone: contact.phone, email: contact.email, interest: contact.interest, budget: contact.budget, timeline: contact.timeline, notes: contact.notes }, null, 2));
          continue;
        }
        add('in', line);
        const res = await ai.reply({ business: b, contact, transcript, mode: 'reply', now: new Date() });
        const lead: LeadUpdate = res.lead;
        contact = {
          ...contact,
          ...Object.fromEntries(Object.entries(lead).filter(([k, v]) => v && k !== 'notes')),
          notes: lead.notes ? [contact.notes, lead.notes].filter(Boolean).join('\n') : contact.notes,
          stage: lead.stage ?? (contact.stage === 'new' ? 'engaged' : contact.stage),
        } as Contact;
        const link = res.linkId ? b.links.find((l) => l.id === res.linkId) : undefined;
        if (res.text) {
          add('out', res.text + (link ? `\n[button: ${link.title}]` : ''));
          out(`\n${b.name} › ${res.text}${link ? `\n   [ ${link.title} → ${link.url} ]` : ''}\n`);
        } else out('\n(no reply)\n');
        const notes = [
          Object.keys(lead).length && `lead: ${JSON.stringify(lead)}`,
          res.handoff && `HANDOFF: ${res.handoff.reason}`,
          res.optOut && 'OPTED OUT',
          `tokens in/out/cached: ${res.usage.inputTokens}/${res.usage.outputTokens}/${res.usage.cacheReadTokens}`,
        ].filter(Boolean);
        out(`   (${notes.join(' · ')})\n`);
      }
      rl.close();
      return;
    }

    case 'meta:pages': {
      const userToken = args[0] ?? fail('Pass a user access token from the Graph API Explorer (with your app selected).');
      const appId = requireEnv(env, 'META_APP_ID');
      const appSecret = requireEnv(env, 'META_APP_SECRET');
      const anon = createMetaClient({ accessToken: userToken, version: env.META_GRAPH_VERSION });
      const exchanged = await anon.get<{ access_token: string; expires_in?: number }>('oauth/access_token', {
        grant_type: 'fb_exchange_token',
        client_id: appId,
        client_secret: appSecret,
        fb_exchange_token: userToken,
      });
      const user = createMetaClient({ accessToken: exchanged.access_token, version: env.META_GRAPH_VERSION });
      const pages = await user.get<{ data: { id: string; name: string; access_token: string; instagram_business_account?: { id: string; username?: string } }[] }>(
        'me/accounts',
        { fields: 'id,name,access_token,instagram_business_account{id,username}', limit: '100' },
      );
      out('Page tokens made from a long-lived user token do not expire (until a password change or a removed role).');
      out('Put each token in .env (and your host) under the page_token_env name from its business file. Never commit it.\n');
      for (const p of pages.data) {
        out(`Page: ${p.name}`);
        out(`  page_id:      ${p.id}`);
        out(`  instagram_id: ${p.instagram_business_account?.id ?? '(no Instagram professional account linked)'}${p.instagram_business_account?.username ? ` (@${p.instagram_business_account.username})` : ''}`);
        out(`  page token:   ${p.access_token}\n`);
      }
      return;
    }

    case 'meta:check': {
      const b = business(reg(), args[0]);
      const api = metaFor(env, b);
      const check = async (label: string, fn: () => Promise<string>) => {
        try {
          out(`✓ ${label}: ${await fn()}`);
        } catch (err) {
          out(`✖ ${label}: ${err instanceof MetaApiError ? `${err.code}${err.subcode ? `/${err.subcode}` : ''} ${err.message}` : (err as Error).message}`);
        }
      };
      await check('Page token', async () => {
        const p = await api.get<{ id: string; name: string; instagram_business_account?: { id: string; username?: string } }>(b.meta.page_id, {
          fields: 'id,name,instagram_business_account{id,username}',
        });
        const ig = p.instagram_business_account;
        if (b.meta.instagram_id && ig?.id !== b.meta.instagram_id) throw new Error(`Page's linked IG is ${ig?.id ?? 'none'}, config says ${b.meta.instagram_id}`);
        return `${p.name}${ig ? `, Instagram @${ig.username ?? ig.id}` : ', no Instagram linked'}`;
      });
      if (env.META_APP_ID && env.META_APP_SECRET) {
        await check('Token permissions', async () => {
          const token = process.env[b.meta.page_token_env]!;
          const dbg = await createMetaClient({ accessToken: `${env.META_APP_ID}|${env.META_APP_SECRET}`, version: env.META_GRAPH_VERSION }).get<{
            data: { is_valid: boolean; scopes?: string[]; expires_at?: number };
          }>('debug_token', { input_token: token });
          const needed = ['pages_messaging', 'pages_manage_metadata', 'pages_read_engagement', 'pages_manage_engagement', 'instagram_basic', 'instagram_manage_messages', 'instagram_manage_comments'];
          const missing = needed.filter((s) => !dbg.data.scopes?.includes(s));
          if (!dbg.data.is_valid) throw new Error('token is not valid');
          return `valid, expires ${dbg.data.expires_at ? new Date(dbg.data.expires_at * 1000).toISOString() : 'never'}${missing.length ? `; MISSING: ${missing.join(', ')}` : '; all needed scopes present'}`;
        });
      }
      await check('Webhook subscription on the Page', async () => {
        const res = await api.get<{ data: { id: string; name?: string; subscribed_fields?: string[] }[] }>(`${b.meta.page_id}/subscribed_apps`);
        const ours = env.META_APP_ID ? res.data.find((a) => a.id === env.META_APP_ID) : res.data[0];
        if (!ours) throw new Error(`our app is not subscribed. Run: npm run cli -- meta:subscribe ${b.slug}`);
        return `fields: ${ours.subscribed_fields?.join(', ') ?? '?'}`;
      });
      return;
    }

    case 'meta:subscribe': {
      const b = business(reg(), args[0]);
      const api = metaFor(env, b);
      const fields = ['feed', 'messages', 'messaging_postbacks', 'message_deliveries', 'message_reads', 'message_echoes'];
      const res = await api.post(`${b.meta.page_id}/subscribed_apps?subscribed_fields=${fields.join(',')}`);
      out(`Page subscribed (${fields.join(', ')}): ${JSON.stringify(res)}`);
      out('Instagram fields (comments, messages, messaging_postbacks, messaging_seen) are set on the app: App Dashboard → Webhooks → Instagram.');
      return;
    }

    case 'meta:posts': {
      const b = business(reg(), args[0]);
      const api = metaFor(env, b);
      const which = args[1] ?? (b.meta.instagram_id ? 'instagram' : 'facebook');
      if (which === 'instagram') {
        if (!b.meta.instagram_id) fail('meta.instagram_id is not set for this business');
        const res = await api.get<{ data: { id: string; caption?: string; media_product_type?: string; timestamp: string; permalink?: string }[] }>(
          `${b.meta.instagram_id}/media`,
          { fields: 'id,caption,media_product_type,timestamp,permalink', limit: '25' },
        );
        for (const m of res.data) out(`${m.id}  ${m.timestamp.slice(0, 10)}  ${m.media_product_type ?? ''}  ${(m.caption ?? '').replace(/\s+/g, ' ').slice(0, 60)}\n    ${m.permalink ?? ''}`);
      } else {
        const res = await api.get<{ data: { id: string; message?: string; created_time: string; permalink_url?: string }[] }>(`${b.meta.page_id}/posts`, {
          fields: 'id,message,created_time,permalink_url',
          limit: '25',
        });
        for (const p of res.data) out(`${p.id}  ${p.created_time.slice(0, 10)}  ${(p.message ?? '').replace(/\s+/g, ' ').slice(0, 60)}\n    ${p.permalink_url ?? ''}`);
      }
      out('\nCopy the ID into the funnel\'s posts list.');
      return;
    }

    case 'verify-endpoint': {
      const url = args[0] ?? fail('Pass the full webhook URL, e.g. https://your-app.up.railway.app/webhook');
      const verifyToken = requireEnv(env, 'META_VERIFY_TOKEN');
      const secret = requireEnv(env, 'META_APP_SECRET');
      const results: [string, boolean][] = [];
      const get = (token: string) => fetch(`${url}?hub.mode=subscribe&hub.verify_token=${encodeURIComponent(token)}&hub.challenge=4242`);
      const good = await get(verifyToken);
      results.push(['correct verify token returns the challenge', good.status === 200 && (await good.text()) === '4242']);
      results.push(['wrong verify token is rejected', (await get('wrong-token')).status === 403]);
      const body = JSON.stringify({ object: 'page', entry: [] });
      const post = (headers: Record<string, string>) => fetch(url, { method: 'POST', body, headers: { 'content-type': 'application/json', ...headers } });
      results.push(['unsigned POST is rejected', (await post({})).status === 401]);
      results.push(['forged signature is rejected', (await post({ 'x-hub-signature-256': sign(body, 'forged') })).status === 401]);
      results.push(['correctly signed POST is accepted', (await post({ 'x-hub-signature-256': sign(body, secret) })).status === 200]);
      for (const [label, ok] of results) out(`${ok ? '✓' : '✖'} ${label}`);
      process.exitCode = results.every(([, ok]) => ok) ? 0 : 1;
      return;
    }

    case 'stats': {
      const [slug, daysArg] = args;
      const days = Number(daysArg ?? 7);
      const sql = connect(requireEnv(env, 'DATABASE_URL'), { max: 1 });
      const filter = slug ? sql`AND business = ${slug}` : sql``;
      const comments = await sql`
        SELECT business, outcome, coalesce(skip_reason, funnel_id, ai_intent, '') AS detail, count(*)::int AS n
        FROM comments WHERE received_at > now() - make_interval(days => ${days}) ${filter}
        GROUP BY 1, 2, 3 ORDER BY 1, 2, 4 DESC`;
      out(`Comments, last ${days} days`);
      for (const r of comments) out(`  ${r.business}  ${r.outcome.padEnd(8)} ${String(r.detail).padEnd(24)} ${r.n}`);
      const sends = await sql`
        SELECT business, platform, coalesce(funnel_id, '-') AS funnel, coalesce(step, '-') AS step, status, count(*)::int AS n,
          count(delivered_at)::int AS delivered, count(read_at)::int AS read
        FROM sends WHERE created_at > now() - make_interval(days => ${days}) ${filter}
        GROUP BY 1, 2, 3, 4, 5 ORDER BY 1, 2, 3, 4`;
      out(`\nSends (delivered is Facebook-only; Instagram has no delivery receipts)`);
      for (const r of sends) out(`  ${r.business}  ${r.platform.padEnd(9)} ${r.funnel.padEnd(16)} ${r.step.padEnd(10)} ${r.status.padEnd(8)} ${String(r.n).padStart(4)}  delivered ${r.delivered}  read ${r.read}`);
      await sql.end();
      return;
    }

    default:
      out(HELP);
      fail(`Unknown command "${cmd}"`);
  }
}

main().catch((err) => {
  if (err instanceof ConfigError) fail(err.message);
  if (err instanceof MetaApiError) fail(`Meta API error ${err.code ?? ''}${err.subcode ? `/${err.subcode}` : ''}: ${err.message}`);
  fail((err as Error).stack ?? String(err));
});
