# Social Agent on Lovable

Instagram and Facebook comment-to-DM funnels and an AI sales assistant. It runs as a Lovable
project (TanStack Start on Cloudflare Workers, Lovable Cloud database). The code is written
outside Lovable and pushed to the project's GitHub repository; every push to `main` syncs to
Lovable and rebuilds the app, so changes cost no Lovable credits.

- Lovable editor: https://lovable.dev/projects/239a3368-f157-4af9-9f3c-129789693927
- Code: github.com/matanhaimguy-commits/agent-start-spark (synced with Lovable). A copy lives in
  `lovable-app/` of matanhaimguy-commits/main.
- Setup steps for a new person: [docs/SETUP.md](docs/SETUP.md).

## Where things are

| Path | What |
|---|---|
| `src/agent/` | The engine: business config, keyword matching, funnels, the Meta API client, the Claude sales agent, the send ledger. Ported from `social-agent/` in matanhaimguy-commits/main. |
| `src/agent/db/sql.ts` | Database access. Workers cannot hold a Postgres connection, so each query is sent to the `agent_sql()` database function over Supabase's REST API with the service-role key. |
| `src/server/` | Server-only glue: settings and secrets, login, the webhook/tick/connect handlers. |
| `src/routes/api/` | Endpoints Meta and the scheduler call: `/api/meta/webhook`, `/api/tick`, `/api/connect/start`, `/api/connect/callback`. |
| `src/routes/` | The dashboard: overview, inbox, businesses, activity, test the bot, connect, settings, and the public `/privacy` and `/data-deletion` pages. |
| `src/lib/api/` | Server functions the dashboard calls. |
| `src/server/content*.server.ts`, `src/routes/api/content/` | Growth Engine hub: the content calendar, media uploads, keyword funnels and post results the studio uses (`/api/content/*`, studio token from Settings). |
| `src/routes/content.tsx` | The Content page: review, approve, schedule and mark posts as posted. |
| `src/routes/studio/`, `src/components/studio/`, `src/server/studio/`, `src/routes/api/studio/` | The Studio page: every piece's production steps, gates, files and the owner's checkpoints (below). |
| `supabase/migrations/` | The database schema. Safe to re-run. |

## How it runs

- **Meta → `/api/meta/webhook`.** The signature is checked, the event is stored, Meta gets its
  200, and processing continues after the response (Workers `waitUntil`). A burst of DMs gets one
  AI answer after `reply_delay_seconds`.
- **Every minute** the database (`pg_cron` + `pg_net`) calls `/api/tick` with a shared secret, for
  follow-ups, health checks and anything left over. The app records its own address and the secret
  in `app_state('tick_target')` the first time the dashboard is opened on the published site.
- **Funnel wait:** a funnel's last message (`after`) goes out right after the delivery unless the funnel sets `after_delay_minutes` (0 to 60, default 0); then it is queued and the minute tick sends it once the wait is over, only if the person has not written back and their 24-hour window is still open (needs migration `20261028090000_funnel_followups.sql`, applied by hand).
- **Settings** (Meta App ID/Secret, Claude key, alerts) are entered on the Settings page and stored
  encrypted. A Lovable Cloud secret with the same name (e.g. `META_APP_SECRET`) overrides them.
- **Real sending** is off until it is switched on in Settings *and* the business is set to Live
  with no blocking problems. Until then everything is a dry run, recorded on the Activity page.
- **Login:** one dashboard password, created on the first visit (or set with an `ADMIN_PASSWORD` secret).
- **Reviewer login:** Settings → Reviewer access makes a second password for Meta's App Review. It can view
  everything, connect a Page and use Test the bot, but cannot change settings, businesses or sending.

## Studio page

`/studio` follows every content piece through the studio's 16 production steps (the run ledger
`clients/<slug>/runs/<post_id>/ledger.json` of `growth-engine/tools/pipeline.py`), so the owner sees progress
on his phone instead of reading long chat messages. The list puts pieces waiting on the owner first; a piece
opens to a timeline of its steps (done, now, next, blocked, not needed) with each gate's PASS/FAIL and score,
notes, and files (docs rendered, audio players, images and video inline). Checkpoint questions sit on top as
cards with options and a note; the owner's answer is stored as `answered` until the studio takes it in
(`synced`). Reviewer logins see everything but cannot answer. The page only shows what the studio pushed.

The studio talks to it with the same studio token as `/api/content/*` (`Authorization: Bearer <token>`),
through `growth-engine/tools/hub.py studio-push | studio-ask | studio-answers | studio-synced`:

| Endpoint | What |
|---|---|
| `POST /api/studio/runs` | Create or update a run (key: business + post_id) with its steps, ledger and, when given, its whole file list. |
| `GET /api/studio/runs[?business=B&post_id=P]` | All runs, or one with its files and questions. |
| `POST /api/studio/decisions` | Ask a checkpoint question (one per `key`; re-asking an open key updates it). |
| `GET /api/studio/decisions?status=answered[&business=B]` | Answers the studio has not taken in yet. |
| `POST /api/studio/synced` | `{"ids": [...]}`: the studio took these answers in. |

Media are uploaded through `/api/content/upload` (the public `content` bucket); docs travel as inline markdown.
Tables: `studio_runs`, `studio_files`, `studio_decisions` (migration `20261027090000_studio.sql`). The code is
one job per file: `src/server/studio/` (schema, validation, one file per query, one per endpoint, re-exported by
`index.server.ts`), `src/lib/api/studio/` (server functions), `src/components/studio/` (one component per file).

## Changing the database

Add a new file to `supabase/migrations/` and apply it to Lovable Cloud (Cloud → Database → SQL, or
through the Lovable MCP `query_database`). Lovable does not apply migrations that arrive through GitHub.

## Working locally

```sh
bun install
bun run test        # unit tests; the database tests need a local Postgres (TEST_DATABASE_URL)
bun run build
npx tsc --noEmit -p .
```

The database tests run every query through the same `agent_sql()` function and literal encoding the
hosted app uses, against a local Postgres loaded with the migration.
