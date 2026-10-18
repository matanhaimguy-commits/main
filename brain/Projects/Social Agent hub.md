---
type: project
updated: 2026-10-18
tags: [project, social-agent, hub, instagram, facebook, lovable]
aliases: [Social Agent, the hub, hub]
---

# Social Agent hub

The always-on app that answers Instagram and Facebook comments and DMs for each business, and holds the content
calendar that posts go out from. It is the "hub" half of [[Growth Engine]]; the studio half (this repo, Claude
sessions) makes the posts through the [[Production layer]] and [[Motion Studio]]. First client: [[StraightScale]].
Rules that apply here: [[Standing rules]]. Back to [[00 Index]].

## What it does

- **Comment-to-DM funnels.** Someone comments a keyword on a post or reel and gets a private reply with a button;
  a tap delivers the link. Story-reply and DM-keyword funnels work the same way. One comment goes to exactly one
  funnel, because Meta allows one private reply per comment.
- **AI sales DMs (Claude).** Every DM is answered from the business's own facts (offers, prices, FAQ, never-say
  list). It qualifies the lead, sends the right link, saves name, phone, interest and stage, and hands off to a
  person. Default model `claude-haiku-5-5`; a stronger one can be set in Settings → AI.
- **Human takeover.** A reply from Instagram or Meta Business Suite pauses the AI in that thread (12 hours by
  default). Pause and resume from the conversation in the Inbox.
- **Lead form.** Every business has a public form at `/l/<business slug>`. Submissions land in the Inbox as leads
  (marked FORM), with an alert. The AI never messages them; a person calls.
- **Content page and publisher.** Drafts from the studio are reviewed, approved, timed and posted to Instagram
  (see "How a post flows" below).
- **Alerts** go to Telegram and/or a generic webhook (Slack, Discord): hot leads, handoffs, problems (token, spam
  block, lost webhook subscription), a post published (with its link), a post that failed, a timed post still in
  draft within 24 hours, and Auto-publish on without the publishing permission. Set up in Settings → Alerts.
- **Dashboard pages:** Overview (setup checklist with the values to paste into Meta), Inbox, Businesses, Activity
  (every comment and what the bot did or would have done), Test the bot, Content, Connect, Settings, plus the
  public `/privacy` and `/data-deletion` pages.

Source: lovable-app/README.md, lovable-app/docs/SETUP.md, social-agent/README.md, lovable-app/src/agent/engine/publish.ts, lovable-app/src/agent/alerts.ts

## Where it runs and how it deploys

- **Lovable project** `239a3368-f157-4af9-9f3c-129789693927`
  (editor: https://lovable.dev/projects/239a3368-f157-4af9-9f3c-129789693927).
- **Published app:** https://matan-social-agent.lovable.app. Meta can only talk to the published address, not the
  editor preview.
- **Stack:** TanStack Start on Cloudflare Workers, Lovable Cloud database (Postgres via Supabase).
- **Code that runs:** GitHub `matanhaimguy-commits/agent-start-spark`. Every push to its `main` syncs to Lovable and
  rebuilds the app, so code changes cost no Lovable credits. Do not force-push or rewrite pushed history there: it
  rewrites Lovable's project history.
- **Mirror:** a copy lives in `lovable-app/` of `matanhaimguy-commits/main` (working branch
  `claude/ig-fb-chatbot-automation-zk8w44`). Mirror commits name the agent-start-spark commit they copy
  (e.g. "deployed as agent-start-spark e8bcd77"). When the two differ, agent-start-spark is what is live.
- **Database changes:** add a file under `supabase/migrations/` and apply it by hand (Lovable Cloud → Database →
  SQL, or the Lovable connector's `query_database`). Lovable does not apply migrations that arrive through GitHub.
- **Every minute** the database (`pg_cron` + `pg_net`) calls `/api/tick`: queued webhook events, due AI replies,
  then periodic jobs: follow-ups and the publisher (every minute), health checks (10 min), approval reminders
  (30 min), webhook subscription, DM access and publish access checks (hourly).
- **Secrets and settings** (Meta app id and secret, Claude key, alert channels, studio token) are entered in the hub
  Settings page (stored encrypted) or set as Lovable Cloud Secrets, which override them. Never in git or chat.
- **Before pushing:** `npx tsc --noEmit -p .`, `bun run test`, `bun run build`.
- **Predecessor:** `social-agent/` is the original Node/Railway version the engine was ported from. There, each
  business was a YAML file. It is not the running app.

Source: lovable-app/README.md, lovable-app/AGENTS.md, lovable-app/src/agent/engine/tick.ts, growth-engine/DAILY.md, CLAUDE.md, git log of lovable-app/

## Database tables (names only)

`ai_runs`, `alerts`, `app_state`, `business_state`, `businesses`, `comments`, `contacts`, `content_items`, `links`,
`messages`, `meta_connections`, `sends`, `taps`, `webhook_events`. Media files sit in a public storage bucket named
`content` (Instagram fetches them from there when posting).

- Businesses are rows in `businesses` (slug plus a config), edited in the dashboard.
- All server access goes through `src/agent/db/sql.ts` (the `agent_sql()` database function). Every table has RLS
  on with no policies; never query them from the browser.
- Never print or copy the `app_state` rows `settings` or `tick_target`.

Source: lovable-app/supabase/migrations/, lovable-app/AGENTS.md, growth-engine/DAILY.md

## How a post flows

1. **Draft.** The studio ships each finished post to `content_items` as a `draft` with its time, caption, keyword
   and media. Two ways: `growth-engine/tools/hub.py push` (the hub's Content API, `/api/content/*`, authorised by
   the studio token from Settings), or, from cloud sessions where the hub host is blocked, a SQL insert through the
   Lovable connector. Never insert as `scheduled` or `published`: only a person approves.
2. **Review on the Content page.** A person checks it, then:
   - **Approve** with a time set → `scheduled`; it posts itself at that time. Approve without a time → `approved`,
     and nothing posts until a time is set.
   - **Post now** (asks for confirmation) → `scheduled` for now; it goes out at the next publisher run, within a
     few minutes.
   - **Reject** → `rejected`.
3. **Publisher** (`src/agent/engine/publish.ts`, every minute). Only for businesses with **Auto-publish** on
   (Businesses → AI & rules; default off) and a connected Instagram account. It moves the item to `publishing`,
   creates the Instagram media container(s), waits for processing (a reel may take minutes; it gives up after 45),
   then sets `published` with `ig_media_id` and the **permalink**, posts the first comment if there is one, and
   sends a "posted" alert with the link. Temporary errors retry up to 5 times; anything else sets `failed` with the
   reason and an alert. A failed item can be approved again.
4. **Reminder.** A draft whose time is within 24 hours triggers an alert (at most every 12 hours) saying it will not
   go out unless approved.
5. **"Already posted by hand?"** only records a post someone made on Instagram themselves. It requires the post's
   Instagram link (`instagram.com/...`), marks the item `published` and matches the media id. It never posts.

Statuses: `draft`, `approved`, `scheduled`, `publishing`, `published`, `rejected`, `failed`. Instagram's API
accepts feed images from 4:5 to 1.91:1, and the hub refuses images outside that range (carousels are 1080x1350).

**Change on 16 Oct 2026** (commit 07cc0c3): the old "I posted it" button, where the link was optional, was replaced
by **Post now** plus **Already posted by hand?**, which needs the Instagram link. The code comment gives the reason:
so a post cannot be marked as live by mistake. Background from the working session (not written in any repo file):
a reel had been marked posted when it was not live.

Source: lovable-app/src/server/content.server.ts, lovable-app/src/routes/content.tsx, lovable-app/src/agent/engine/publish.ts, lovable-app/supabase/migrations/20261015090000_content.sql, growth-engine/tools/hub.py, growth-engine/DAILY.md, git commits 07cc0c3 and dd369dd

## Real customer messages: dry run by default

- Nothing is sent to customers until **both** Settings → Real sending is on **and** the business is set to **Live**
  with no blocking problems (any TODO left in its profile blocks it). Until then every action is a dry run,
  recorded on the Activity page.
- **Testers only** on a business limits real messages to the listed accounts; empty it to answer everyone.
- Do not change the dry-run default in code.
- The current on/off state of these switches for each business is in the hub, not in the repo.
  growth-engine/DAILY.md says Auto-publish is on for StraightScale.

Source: lovable-app/README.md, lovable-app/AGENTS.md, lovable-app/docs/SETUP.md, growth-engine/DAILY.md

## Meta App Review status

- Until the app has **Advanced Access** for `instagram_manage_messages` (and `pages_messaging` for Messenger), Meta
  only delivers DMs, button taps and replies from people with a role on the app (admins, developers, testers).
  Comments and the first private reply work for everyone. The Overview (step 11) checks this hourly and alerts
  when Meta opens access.
- growth-engine/PLAN.md (written 14 Oct) lists: messaging permissions "App Review in progress"; comment permissions
  "Working (Standard)"; `instagram_content_publish` and `pages_manage_posts` "To add to the Login configuration +
  App Review"; insights permissions "To add + App Review"; Business Verification and managing other businesses'
  accounts after our own account is approved; ads permissions later.
- `lovable-app/docs/APP_REVIEW_RECORDING.md` holds the screen-recording shot list and form text for
  `instagram_manage_messages` and `instagram_basic`. Meta's reviewer uses the read-only **Reviewer access** login
  (Settings → Reviewer access). Its password goes only in the submission notes.
- An hourly check asks Instagram for the publishing quota. It shows whether `instagram_content_publish` really
  works, and it is the test call Meta wants before Advanced Access can be requested.
- Meanwhile: the lead form catches people Meta's limits would lose, and keyword funnels use the "link" opener
  until Advanced Access, then "tap".
- **Unknown from the repo:** whether the review was submitted or approved after 15 Oct. Check the Meta App
  Dashboard or the hub Overview.

Source: lovable-app/docs/SETUP.md, lovable-app/docs/APP_REVIEW_RECORDING.md, growth-engine/PLAN.md, .claude/skills/growth-engine/SKILL.md, lovable-app/src/agent/engine/publish.ts

## Adding a new business

Done in the hub dashboard (no YAML files here).

1. **Businesses → New business**: a name and a short id (slug). This creates a starter config with TODO fields,
   Live off, AI on for DMs. The starter timezone is `Asia/Jerusalem`; change it if the business is elsewhere.
2. Fill in who they are, offers and prices, audience, the goal of every conversation, qualifying questions, FAQ,
   voice and the never-say list, plus links and the lead form. Every TODO must go: it blocks real sending.
3. **Connect → Connect Facebook & Instagram**, tick the Page and its Instagram account, choose which business it
   belongs to, then **Register webhooks**. On Instagram, "Allow access to messages" must be on.
4. **Funnels tab → Add a funnel → Pick from recent posts.**
5. **Test the bot**, then comment or DM from a second account and read the Activity page (dry run).
6. Real sending: Settings on, business Live with a tester in Testers only first; empty it when it looks right.
7. For content: switch on Auto-publish and start the client's folder `clients/<slug>/` with a brain from
   [[Client brain template]].

Planned, not built: a self-serve onboarding link (`/join/<code>`) with a brief form (PLAN.md phase 2; no such
route in the lovable-app mirror). Clients' own accounts also need the Meta permissions above and Business
Verification.

Source: lovable-app/docs/SETUP.md, lovable-app/src/routes/businesses/index.tsx, lovable-app/src/agent/config/starter.ts, growth-engine/PLAN.md

## Where to read more

| File | What |
|---|---|
| `lovable-app/README.md` | Layout of the code and how it runs |
| `lovable-app/AGENTS.md` | Rules for working on the app |
| `lovable-app/docs/SETUP.md` | Setup from zero, Meta review, lead form, alerts, troubleshooting, costs |
| `lovable-app/docs/APP_REVIEW_RECORDING.md` | App Review recording and form text |
| `growth-engine/PLAN.md` | How the hub and the studio fit together |
| `growth-engine/DAILY.md` | The daily run that fills the hub with drafts |
| `social-agent/README.md` | The original version and the rules the engine is built on |

Posts that went out are tracked in [[StraightScale content log]]; owner decisions in [[StraightScale decisions]].
