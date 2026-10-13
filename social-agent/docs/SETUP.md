# Setup: from zero to live

Plan on about two hours for the first business. A client after that takes about 20 minutes, plus
their Page access. Do the steps in order: Meta checks your endpoint the moment you register it, so
the server must be deployed first.

## 0. What you need

- An **Instagram professional account** (business or creator) **linked to a Facebook Page** you
  admin. This applies to every business, yours and each client's. A personal Instagram account gets
  no API access to comments or DMs.
- A **Meta developer account** (developers.facebook.com) and ideally a **Meta Business portfolio**.
  Business verification is needed for Advanced Access (see step 6).
- **Hosting** for one small Node service plus **Postgres**. Railway is the simplest: about $5/month
  with Postgres included. Render with Neon or Supabase also works.
- An **Anthropic API key** (console.anthropic.com) for the AI. Without it the funnels still run.
- A **second Instagram/Facebook account** for testing. It must never be the brand account, because
  the brand's own comments are skipped by design.

## 1. Deploy the server

**Railway:**
1. New Project → Deploy from GitHub repo → pick this repo. In the service settings set
   **Root Directory** to `social-agent`. Railway detects the Dockerfile.
2. Add a **Postgres** database to the project. Railway sets `DATABASE_URL` for you if you
   reference it from the service variables.
3. Set the variables from `.env.example`. For now: `META_VERIFY_TOKEN` (any string you invent),
   `ADMIN_PASSWORD`, `OPERATOR_NAME`, `OPERATOR_EMAIL`, and `LIVE_SENDING=false`.
4. Generate a public domain (Settings → Networking). Your webhook URL is `https://<domain>/webhook`.
5. Check `https://<domain>/health` shows `"ok": true`.

On start the server creates its tables and logs every business with its LIVE / dry-run status and
its audit findings.

**Locally:** `cp .env.example .env`, fill in `DATABASE_URL`, then `npm install && npm run dev`.

## 2. Create the Meta app

1. developers.facebook.com → My Apps → **Create App**. Choose the business use case and connect your
   Business portfolio.
2. Add the products **Messenger**, **Instagram** (the "API setup with Facebook login" flavour) and
   **Webhooks**.
3. **App settings → Basic:** fill in the app icon, category and contact email. Use these URLs, which
   this server provides:
   - Privacy Policy URL: `https://<domain>/privacy`
   - User data deletion: `https://<domain>/data-deletion` (as "instructions URL")
4. Copy the **App ID** and **App Secret** into the host's variables as `META_APP_ID` and
   `META_APP_SECRET`, then redeploy.
5. Prove the endpoint before registering it with Meta:
   ```bash
   npm run cli -- verify-endpoint https://<domain>/webhook
   ```
   All five checks must pass. They test the right token, a wrong token, an unsigned request, a forged
   request, and a correctly signed request.

## 3. Register the webhooks

App Dashboard → **Webhooks**:

- Object **Page**: callback `https://<domain>/webhook`, verify token = your `META_VERIFY_TOKEN`.
  Subscribe to `feed`, `messages`, `messaging_postbacks`, `message_deliveries`, `message_reads`,
  `message_echoes`.
- Object **Instagram**: same callback and token. Subscribe to `comments`, `messages`,
  `messaging_postbacks`, `messaging_seen`.

Registering the app-level webhook is only half of it. Each Page must also be activated (step 4).

## 4. Tokens and IDs for each business

1. Open the Graph API Explorer (developers.facebook.com/tools/explorer) and select your app.
2. Get a **User token** with these permissions: `pages_show_list`, `pages_manage_metadata`,
   `pages_messaging`, `pages_read_engagement`, `pages_manage_engagement`, `instagram_basic`,
   `instagram_manage_messages`, `instagram_manage_comments`, `business_management`.
3. Locally, with `META_APP_ID` and `META_APP_SECRET` in `.env`, run:
   ```bash
   npm run cli -- meta:pages <that-user-token>
   ```
   It prints, for every Page you manage, the `page_id`, the linked `instagram_id`, and a **Page token
   that does not expire**. The token stops working only if the password changes or the role is removed.
4. Put each Page token in the host's variables (and your local `.env`) under the name you will use
   as `page_token_env`, e.g. `PAGE_TOKEN_MY_BUSINESS`. Never put a token in a YAML file or in git.
5. For a client's Page: they add you to their Page and Instagram through their Business portfolio
   (Page access with full control), or you run the same flow with their login.

## 5. Write the business file

```bash
cp businesses/_template.yaml businesses/my-business.yaml
```

Fill in `meta`, `profile` (the AI sells only what is written here), `links` (full URLs, no
shorteners) and `funnels`. Get post IDs with `npm run cli -- meta:posts my-business`. Then:

```bash
npm run audit                                        # must end with no errors for this business
npm run cli -- preview my-business <funnel-id>       # read every message as the customer will
npm run cli -- match my-business instagram <post-id> "send me the guide"
npm run cli -- chat my-business                      # role-play customers; fix the profile until it sells well
```

Commit the YAML (it has no secrets) and redeploy. Then activate the Page and check everything:

```bash
npm run cli -- meta:subscribe my-business
npm run cli -- meta:check my-business
```

## 6. Access level and App Review

This is where it usually stalls.

- **Live mode.** Switch the app from Development to Live (top of the App Dashboard). Nothing arrives
  from the public until you do.
- **Standard Access.** Meta delivers events and allows sends only for people who have a **role on the
  app** (admin, developer, tester). Anyone else gets error `200/2018028`. Instagram `comments`
  webhooks need Advanced Access.
- **Advanced Access.** To serve the general public, request Advanced Access in App Review for the
  permissions in step 4 and complete **Business Verification**. Meta's own pages contradict each other
  on whether your own Page needs review, so plan on it.
  - The review asks for a screencast of the flow. Record it with a tester account: comment, DM
    arrives, tap, link, AI reply.
- **While you wait:** add your test person as a **Tester** role on the app (App roles → Roles) and
  test with them. Keep `testers:` set in the business file so only they get messages.
- **Not needed:** WhatsApp, the Human Agent tag, or Handover protocol.

## 7. Go live, safely

Test in this order. Silence is not success: Meta can return success and nothing arrives.

1. In the business file set `live: true` and `testers: ["@your_second_account"]`. On the host set
   `LIVE_SENDING=true`. Redeploy. The startup log should show the business as LIVE.
2. **Comment from the second account** on a pinned post. In `/admin`, check that:
   - Comments shows the comment matched to the funnel.
   - Sends shows `private_reply … sent`.
   - The DM arrived (look in Message Requests).
3. Tap the button and check that the link and the follow-up message arrive.
4. **Open the link in a private window, logged out.** A lead magnet behind a "request access" wall is
   the most common silent failure.
5. Reply to the DM and check that the AI answers. Then reply yourself from the Instagram app or Meta
   Business Suite, and check that the conversation shows "paused" in `/admin`.
6. Set up alerts. Create a Telegram bot with @BotFather and set `TELEGRAM_BOT_TOKEN`. Send the bot a
   message, open `https://api.telegram.org/bot<token>/getUpdates`, copy `chat.id` into
   `TELEGRAM_CHAT_ID`, and redeploy.
7. **The stranger test.** Empty `testers`, redeploy, and ask someone with no connection to your app
   to comment. Only a stranger's comment proves it works for the public.

The quiet-funnel alert covers the rest. It fires when a funnel sends at least 5 DMs in 72h and none
is read, tapped or clicked.

## Day to day

- **New reel with a funnel:** add the post ID to a funnel's `posts` (or add a new funnel), run
  `npm run audit`, commit, redeploy.
- **Stop a funnel:** set `status: paused`. Matching comments are skipped and recorded as
  `funnel_paused`. They never fall through to another funnel.
- **Take over a conversation:** just reply from the Meta inbox. The AI pauses there for
  `pause_hours_after_human` hours. Resume or pause any thread from `/admin`.
- **Hot lead / handoff alerts** carry what the AI collected. The full thread is in `/admin/leads`.
- **Running next to ManyChat is safe.** Meta allows one private reply per comment, so whichever tool
  answers first wins and the other logs a harmless failure. Move one funnel at a time and remove its
  ManyChat automation after this one is proven.

## Costs

- **Meta:** $0 per message on Instagram and Messenger.
- **Hosting + Postgres:** about $0–20/month.
- **Claude:** with the default model (`claude-opus-5-5`, $4 / $20 per million input / output tokens,
  business facts cached), an AI reply typically costs about 1–3 cents. Set `ai.effort: low` or a
  cheaper `CLAUDE_MODEL` to lower it. `/admin` shows weekly token totals.
- **Dry run still costs AI tokens.** In dry-run mode the AI still writes replies (they are logged, not
  sent), so test on a quiet account or keep `ai.enabled: false` until you are ready.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Nothing arrives at all | App not Live; Page not activated (`meta:subscribe`); Instagram fields not ticked in the dashboard; or Meta disabled delivery after an hour of failures (`meta:check`, and the hourly subscription alert). |
| Comments from your own account do nothing | By design. Test from a second account. |
| `200/2018028` on sends | Standard Access: the person has no role on the app. Add them as a tester or get Advanced Access. |
| `100/2534025` on a private reply | Comment older than 7 days, deleted, already answered by another tool, or the person's settings block it. |
| `10900` / "already replied" | Another tool (e.g. ManyChat) used the one private reply first. Harmless. |
| `190` | Page token invalid (password change, role removed). Mint a new one with `meta:pages`. |
| `368` | Meta flagged messages as spam. Sending pauses for 24h automatically. Fix keywords and copy. |
| Funnel didn't fire | `/admin/comments` shows the reason, or run `npm run cli -- match ...`. |
