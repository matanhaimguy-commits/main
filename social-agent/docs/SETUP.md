# Setup: from zero to working

Everything happens in the browser. No terminal. Three parts:

1. **Put the server online** (Railway, about 10 minutes). Railway hosts the program and its database.
2. **Create the Meta app** (developers.facebook.com, about 20 minutes). This is what lets the
   program receive your comments and DMs and reply to them.
3. **Press "Connect Facebook & Instagram"** in the server's admin page and pick your Page (2 minutes).

The server's own **Setup page** (`/admin/setup`) shows what's done and what's left, and lists the
exact values to paste into Meta. Keep it open while you work.

Until you switch real sending on, nothing is ever sent. The system records what it *would* send,
so you can watch it work safely first.

## Before you start

- **Instagram professional account linked to a Facebook Page.** It can be a business or creator
  account, and you must be an admin of the Page.
  - Check in the Instagram app: Settings → Account type and tools.
  - Link it from Meta Business Suite → Settings → Instagram accounts.
- **Instagram setting:** in the Instagram app, open Settings → Messages and story replies → Message
  controls → Connected tools, and turn on **Allow access to messages**. Without it, Instagram DMs
  never reach the system.
- **A second Instagram/Facebook account** for testing. Comments from the business account itself are
  ignored on purpose, so you can't test with it.
- **An Anthropic API key** (console.anthropic.com → API keys) for the AI replies.

## Part 1: Put the server online (Railway)

1. Go to **railway.com**, sign in with GitHub, and choose **New Project → Deploy from GitHub repo →**
   `matanhaimguy-commits/main`.
2. Open the new service → **Settings**:
   - **Source → Branch:** `claude/ig-fb-chatbot-automation-zk8w44` (or `main`, once it is merged).
   - **Source → Root Directory:** `social-agent`.
3. In the project, click **+ New → Database → PostgreSQL**.
4. Open the service → **Variables** and add:
   | Name | Value |
   |---|---|
   | `DATABASE_URL` | `${{Postgres.DATABASE_URL}}` (Railway fills it in) |
   | `ADMIN_PASSWORD` | a password you choose for the admin pages |
   | `ANTHROPIC_API_KEY` | your Claude API key |
5. **Settings → Networking → Generate Domain.** You get an address like
   `https://social-agent-production.up.railway.app`.
6. Open `https://<your-address>/admin/setup` and log in with user `admin` and your password. The first
   step should be green.

## Part 2: Create the Meta app

1. Go to **developers.facebook.com → My Apps → Create App**.
   - If asked for a use case, pick **Other**, then app type **Business**.
   - Connect your Business portfolio if asked.
2. In the app, add these products (**Add product** in the left menu): **Facebook Login for
   Business**, **Messenger**, **Instagram** (the "API setup with Facebook login" option) and
   **Webhooks**.
3. Open **App settings → Basic** and fill in:
   - **Privacy Policy URL** and **User data deletion URL.** Copy both from your Setup page.
   - App icon, category and contact email.
   - Then **Save**.
4. On the same screen, copy the **App ID** and **App Secret** (click Show). In Railway → Variables, add
   them as `META_APP_ID` and `META_APP_SECRET`. Railway redeploys by itself.
5. Open **Facebook Login for Business → Settings → Valid OAuth Redirect URIs** and paste the redirect
   URI from your Setup page. It ends in `/admin/connect/callback`. Save.
   - Some apps use login **Configurations** instead of permissions. If yours shows a
     "Configurations" tab, create one with these settings:
     - Login variation **General**, token type **User access token**.
     - The permissions listed in Part 4.
     - Put its ID in Railway as `META_LOGIN_CONFIG_ID`.
6. **App roles → Roles:** add your second (test) Facebook account as a **Tester**, and accept the
   invite from that account.
7. Switch the app from **Development** to **Live** using the toggle at the top of the dashboard.

## Part 3: Connect your Facebook Page and Instagram

1. Open `https://<your-address>/admin/connect` and press **Connect Facebook & Instagram**.
2. Log in with the Facebook account that manages the Page. When Meta asks, select your **Page** and
   its **Instagram account**, and allow everything it asks for.
3. You land back on the Connect page with your Page listed. In **"Choose which business each Page
   belongs to"**, pick **our-business** and press **Save**. That also subscribes the Page to the
   webhooks.
4. Press **Register webhooks automatically**. This tells Meta where to send events, for Facebook and
   Instagram. If it shows an error, paste the callback URL and verify token from the Setup page into
   the App Dashboard → **Webhooks** by hand:
   - **Page** object: subscribe `feed`, `messages`, `messaging_postbacks`, `message_deliveries`,
     `message_reads`, `message_echoes`.
   - **Instagram** object: subscribe `comments`, `messages`, `messaging_postbacks`,
     `messaging_seen`.
5. The Setup page should now be green down to "Events arriving from Meta".

## Part 4: See it working

1. **Talk to your bot first.** Open `/admin/test` and write to it like a customer would. It answers
   using what `businesses/our-business.yaml` says about your business. Until that file has real
   details (the TODO lines), its answers will be generic.
2. **Send a DM or comment from your second account.**
   - Open `/admin` → **Comments** and **Sends**.
   - Every event shows up, along with what the bot decided and what it would have sent. While
     `LIVE_SENDING` is off, every send is marked `dry_run`.
3. **Switch on real sending:**
   - In Railway, set `LIVE_SENDING=true`.
   - In `businesses/our-business.yaml`, set `live: true` and `testers: ["@your_second_account"]`.
   - With the testers list set, only your test account gets real messages.
   - The business must also have no TODOs left (the Setup page lists any that remain).
4. Test the full flow from the second account:
   - The comment gets a DM. Look in Message Requests.
   - Tap the button and you get the link.
   - Reply and the AI answers.
   - Reply yourself from the Instagram app and the AI steps back.
5. Open your links in a private window, logged out, to make sure they open for strangers.
6. When it's all right, empty `testers` so it answers everyone.

## Meta's review (for strangers)

Meta only delivers messages from **people with a role on your app** (admins, developers, testers)
until your app has **Advanced Access**. Anyone else gets error `200/2018028`. Instagram comment
events also need Advanced Access.

- Meta's pages contradict each other on whether this applies to your own Page. The guide in the PDF
  says flipping to Live was enough for its author.
- Test with your tester account first. If strangers' messages don't arrive, go to **App Review →
  Permissions and features** and request Advanced Access for:
  - `pages_messaging`, `pages_manage_metadata`, `pages_read_engagement`, `pages_manage_engagement`
  - `instagram_basic`, `instagram_manage_messages`, `instagram_manage_comments`
  - `business_management`
- Complete **Business Verification**.
- Meta asks for a short screen recording of the flow. Record your tester account commenting,
  receiving the DM, tapping, and getting an answer.

## Alerts (optional, recommended)

Get a Telegram message for hot leads, handoffs and problems:

1. In Telegram, talk to **@BotFather** → `/newbot` and copy the token.
2. Send your new bot any message.
3. Open `https://api.telegram.org/bot<token>/getUpdates` and copy the number after `"chat":{"id":`.
4. In Railway, set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.

## Day to day

- **Add a funnel for a new post:** add it to the business file with the post or reel ID and the
  keyword. You'll find the ID in `/admin/comments` after anyone comments on the post, or with
  `npm run cli -- meta:posts our-business`. Commit, and Railway redeploys. Later, your content system
  will add funnels automatically.
- **Take over a conversation:** just reply from Instagram or Meta Business Suite. The AI pauses in
  that thread for 12 hours. Pause or resume any thread from `/admin/leads`.
- **Running next to ManyChat is safe.** Meta allows one private reply per comment, so whichever tool
  answers first wins and the other logs a harmless failure.

## Costs

- **Meta:** $0 per message.
- **Railway (server and database):** about $5 a month.
- **Claude:** with `claude-opus-5-5`, about 1–3 cents per AI reply. Dry runs and the test page also
  use the AI. To lower the cost, set `ai.effort: low` in the business file or choose a cheaper
  `CLAUDE_MODEL`.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Meta says the redirect URL is blocked | The redirect URI from the Setup page isn't in Facebook Login → Settings → Valid OAuth Redirect URIs. |
| "Meta shared no Pages" after login | You didn't tick the Page in the Meta dialog, or you aren't an admin of it. Connect again. |
| Nothing arrives at all | Check, in order: is the app Live? Is the Page subscribed (Connect page)? Did "Register webhooks" succeed? Is "Allow access to messages" on in Instagram? |
| Comments from your own account do nothing | By design. Test from a second account. |
| `200/2018028` | The person has no role on the app. Add them as a Tester, or get Advanced Access. |
| `100/2534025` on a private reply | The comment is older than 7 days, was deleted, or another tool already replied. |
| `190` | The Page token stopped working (password change, role removed). Press Connect again. |
| `368` | Meta flagged the messages as spam. Sending pauses for 24 hours automatically. Fix keywords and copy. |
| A funnel didn't fire | `/admin/comments` explains why, for every comment. |
