# Social Agent

Your own ManyChat replacement plus an AI sales rep, for Instagram and Facebook, on Meta's official API.
Meta charges nothing per message, so there is no per-contact bill, and the contacts live in your own database.

- **Comment-to-DM funnels.** Someone comments a keyword on a pinned post or reel and gets a private
  reply with a button. They tap, get the link, and the conversation is open. Story-reply and DM-keyword
  funnels work the same way, plus an optional follow gate.
- **AI sales conversations (Claude).** Every DM is answered from the business's own facts (offers,
  prices, FAQ, policies). The agent qualifies the lead, sends the right link as a button, saves name /
  phone / interest / stage, and hands off to a person when needed. Warm leads that go quiet get one
  follow-up, always inside Meta's 24-hour window.
- **AI comment handling (optional).** For comments no funnel owns, it gives a short public answer to
  questions and a private reply to buying intent. It can also hide spam.
- **Multi-business.** One deployment serves you and your clients. Each business is one YAML file in
  `businesses/` with its own knowledge, links and funnels. Its Page and Instagram account are
  connected with a button in `/admin/connect`.
- **Human takeover.** When anyone replies from the Meta inbox, the AI steps back in that thread.
  The `/admin` dashboard shows leads, conversations, the comment ledger and the send ledger, with
  pause / resume / stage controls.
- **Alerts** go to Telegram or Slack/Discord: hot leads, handoffs, a funnel that sends but nothing
  lands, token problems, a spam block, a lost webhook subscription.

Setup, from zero to live, all in the browser: **[docs/SETUP.md](docs/SETUP.md)**.

## The admin pages (`/admin`, user `admin` + `ADMIN_PASSWORD`)

| Page | What it's for |
|---|---|
| **Setup** | Green/red checklist of every setup step, with the exact URLs and tokens to paste into Meta. |
| **Connect** | "Connect Facebook & Instagram" button. You log in with Facebook and pick the Page. The token is stored encrypted, and the Page and app webhooks are subscribed for you. |
| **Test the bot** | Chat with the AI as a customer, and simulate a comment to see which funnel fires and exactly what gets sent. Nothing goes to Meta. |
| **Overview / Leads / Comments / Sends** | Results, every lead and conversation (pause / resume the AI, set a stage), every comment with the reason it did or didn't fire, and the send ledger. |

## How it works

```
Meta webhook ─► POST /webhook ─► verify signature ─► store raw event ─► 200 (milliseconds)
                                                          │
worker ◄──────────────────────────────────────────────────┘
  ├─ comment  ─► skip own / replies / old ─► pick exactly ONE funnel ─► claim ledger key ─► private reply (+ public reply)
  │                                         └─ no funnel: AI triage (optional)
  ├─ tap      ─► follow gate (IG) ─► link button ─► "questions? reply here"
  ├─ DM       ─► STOP / keyword funnel / else schedule AI reply (debounced)
  ├─ echo     ─► sent by a person, not us ─► pause AI in that thread
  └─ receipts ─► read (IG + FB), delivered (FB only)
AI reply job ─► Claude (business facts + transcript + tools) ─► claim ledger key ─► DM ─► lead update / alerts
```

## The rules it is built on

Each of these exists because breaking it fails silently.

1. **Sent and delivered are different facts.** Instagram has no delivery receipts, so `delivered_at`
   stays empty for Instagram and Instagram funnels are judged on reads, taps and clicks.
2. **One comment goes to exactly one funnel**, decided before any API call, because Meta allows one
   private reply per comment, ever, across every app. A pinned post beats a catch-all. A paused funnel
   stops instead of falling through to another one.
3. **Never auto-retry a send.** Every send claims a unique key in the `sends` ledger before calling
   Meta. A timeout is recorded as `unknown` and raises an alert. It is never re-sent.
4. **Every skipped comment gets a row** with the reason (`keyword_not_matched`, `funnel_paused`,
   `own_comment`, ...), so "why didn't my funnel fire" is a query, not an investigation.

It also handles the known traps:

- Facebook top-level comments have `parent_id == post_id`, so they are not treated as replies.
- The bot's own comments are skipped, which prevents DM loops.
- Follow status is re-checked to cover Meta's lag.
- Meta always gets its 200, and redelivery is safe.
- A per-business audit refuses risky keywords, unpinned funnels and link shorteners.

## Commands

```bash
npm install
npm test                      # unit + integration tests (integration needs TEST_DATABASE_URL or local Postgres)
npm run dev                   # server + worker with reload (reads .env)
npm run audit                 # check every business config, after every change
npm run cli -- help           # all commands
npm run cli -- preview <business> <funnel>          # exactly what people receive
npm run cli -- match <business> instagram <post> "text"   # would this comment fire, and why
npm run cli -- chat <business>                       # talk to the AI agent locally before going live
npm run cli -- meta:subscribe <business>             # activate webhooks on the Page (the Connect page does this too)
npm run cli -- meta:check <business>                 # token, permissions, subscription
npm run cli -- meta:posts <business>                 # post IDs to pin funnels to
npm run cli -- verify-endpoint https://.../webhook   # prove the endpoint accepts/rejects correctly
npm run cli -- stats [business] [days]
```

## Layout

| Path | What |
|---|---|
| `businesses/*.yaml` | One file per business. `_template.yaml` is annotated; `_example-agency.yaml` is a filled-in example. |
| `migrations/` | Postgres schema (applied automatically on start). |
| `src/logic/` | Pure rules: keyword matching (with Hebrew prefixes), funnel selection, comment screening, audit. |
| `src/meta/` | Webhook signature + parsing, Graph API client and error categories, message templates. |
| `src/ai/` | Claude sales agent: prompts, tools (`attach_link`, `update_lead`, `handoff_to_human`, `opt_out`), comment triage. |
| `src/engine/` | Orchestration: send ledger, funnel steps, event processing, AI replies and follow-ups, health checks. |
| `src/server.ts`, `src/admin.ts` | Webhook endpoint, `/admin` dashboard, `/privacy`, `/data-deletion`, `/r/:token`. |
| `src/worker.ts` | Queue loop (lease-based, safe to run more than one). |
