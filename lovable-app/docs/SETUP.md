# Setup: from zero to working

Everything happens in the browser. The app is already built and hosted on Lovable; you only
connect it to Meta and describe your business. Keep the app's **Overview** page open while you
work: it shows what is done, what is left, and the exact values to paste into Meta.

Until you switch real sending on, nothing is ever sent. The system records what it *would*
send (Activity page), so you can watch it work safely first.

## Before you start

- **Instagram professional account linked to a Facebook Page.** Business or creator account; you
  must be an admin of the Page.
  - Check in the Instagram app: Settings → Account type and tools.
  - Link it from Meta Business Suite → Settings → Instagram accounts.
- **Instagram setting:** in the Instagram app, open Settings → Messages and story replies → Message
  controls → Connected tools, and turn on **Allow access to messages**. Without it, Instagram DMs
  never reach the app.
- **A second Instagram/Facebook account** for testing. Comments from the business account itself are
  ignored on purpose, so you can't test with it.
- **A Claude API key** (console.anthropic.com → API keys) for the AI replies.

## Part 1: Open the app (2 minutes)

1. Open the published address (it ends in `.lovable.app`). Use the published address, not
   Lovable's editor preview: Meta can only talk to the published one.
2. Choose a dashboard password. You'll use it to log in from now on.
3. Go to **Settings** and paste your **Claude API key**, then Save.

## Part 2: Create the Meta app (about 20 minutes)

1. Go to **developers.facebook.com → My Apps → Create App**.
   - If asked for a use case, pick **Other**, then app type **Business**.
   - Connect your Business portfolio if asked.
2. In the app, add these products (**Add product** in the left menu): **Facebook Login for
   Business**, **Messenger**, **Instagram** (the "API setup with Facebook login" option) and
   **Webhooks**.
3. Open **App settings → Basic** and fill in:
   - **Privacy Policy URL** and **User data deletion URL**: copy both from the app's Overview page.
   - App icon, category and contact email. Then **Save**.
4. On the same screen, copy the **App ID** and **App Secret** (click Show) into the app's
   **Settings** page and Save.
5. Open **Facebook Login for Business → Settings → Valid OAuth Redirect URIs** and paste the
   redirect URI from the Overview page (it ends in `/api/connect/callback`). Save.
   - If your app shows a **Configurations** tab instead of permissions, create one (login variation
     General, token type User access token, the permissions listed under "Meta's review" below) and
     paste its ID into Settings → "Facebook Login configuration ID".
6. **App roles → Roles:** add your second (test) Facebook account as a **Tester** and accept the
   invite from that account.
7. Switch the app from **Development** to **Live** with the toggle at the top of the dashboard.

## Part 3: Connect your Facebook Page and Instagram (2 minutes)

1. In the app, open **Connect** and press **Connect Facebook & Instagram**.
2. Log in with the Facebook account that manages the Page. When Meta asks, tick your **Page** and its
   **Instagram account**, and allow everything it asks for.
3. Back on Connect, choose **which business** the Page belongs to. Saving also subscribes the Page.
4. Press **Register webhooks**. If it shows an error, paste the callback URL and verify token shown
   there into App Dashboard → **Webhooks** by hand.
5. The Overview page should now be green down to "Events arriving from Meta".

## Part 4: Describe the business and see it work

1. **Businesses → your business.** Fill in who you are, offers and prices, the goal of every
   conversation, and the questions the AI should ask. Add your links (booking page, price list).
   Everything marked TODO must be replaced: it blocks real sending.
2. **Funnels tab → Add a funnel.** Pick the post or reel ("Pick from recent posts"), the keywords,
   the first message, and what gets delivered after the tap.
3. **Test the bot.** Chat with it like a customer, and simulate a comment to see which funnel fires
   and exactly what the person receives. Nothing is sent.
4. **Comment or DM from your second account.** The Activity page shows every comment, what the bot
   decided, and what it would have sent (marked "dry run").
5. **Switch on real sending** when it looks right:
   - Settings → Real sending: on.
   - Business → AI & rules → Live: on, and put `@your_second_account` in **Testers only**. With
     testers set, only that account gets real messages.
6. Test the full flow from the second account: the comment gets a DM (look in Message Requests),
   tapping the button delivers the link, replying gets an AI answer, and replying yourself from the
   Instagram app makes the AI step back.
7. When it's all right, empty **Testers only** so it answers everyone.

## Meta's review (for strangers)

Meta only delivers messages from **people with a role on your app** (admins, developers, testers)
until your app has **Advanced Access**. Anyone else gets error `200/2018028`. Instagram comment
events also need Advanced Access.

- Test with your tester account first. If strangers' messages don't arrive, go to **App Review →
  Permissions and features** and request Advanced Access for:
  - `pages_messaging`, `pages_manage_metadata`, `pages_read_engagement`, `pages_manage_engagement`
  - `instagram_basic`, `instagram_manage_messages`, `instagram_manage_comments`
  - `business_management`
- Complete **Business Verification**.
- Meta asks for a short screen recording: your tester account commenting, receiving the DM, tapping,
  and getting an answer.

## Alerts (optional, recommended)

Get a Telegram message for hot leads, handoffs and problems:

1. In Telegram, talk to **@BotFather** → `/newbot` and copy the token.
2. Send your new bot any message, then get your chat ID from **@userinfobot**.
3. Paste both in Settings → Alerts.

## Day to day

- **New post with a keyword:** Businesses → Funnels → Add a funnel → Pick from recent posts.
- **Take over a conversation:** just reply from Instagram or Meta Business Suite. The AI pauses in that
  thread (12 hours by default). Pause or resume it from the conversation in the Inbox.
- **Running next to ManyChat is safe.** Meta allows one private reply per comment, so whichever tool
  answers first wins and the other logs a harmless failure.

## Costs

- **Meta:** $0 per message.
- **Lovable:** hosting and the database are part of your Lovable plan. The app runs a small job once a
  minute. Code changes are pushed through GitHub and use no Lovable credits.
- **Claude:** with `claude-opus-5-5`, about 1–3 cents per AI reply. Test chats also use the AI. To
  lower the cost, set Thinking effort to "low" on the business, or choose a cheaper model in Settings.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Meta says the redirect URL is blocked | The redirect URI from Overview isn't in Facebook Login → Settings → Valid OAuth Redirect URIs. |
| "Meta shared no Pages" after login | You didn't tick the Page in the Meta dialog, or you aren't an admin of it. Connect again. |
| Nothing arrives at all | In order: is the Meta app Live? Is the Page subscribed (Connect)? Did "Register webhooks" succeed? Is "Allow access to messages" on in Instagram? |
| Comments from your own account do nothing | By design. Test from a second account. |
| `200/2018028` | The person has no role on the app. Add them as a Tester, or get Advanced Access. |
| `100/2534025` on a private reply | The comment is older than 7 days, was deleted, or another tool already replied. |
| `190` | The Page token stopped working (password change, role removed). Press Connect again. |
| `368` | Meta flagged the messages as spam. Sending pauses for 24 hours automatically. Fix keywords and copy. |
| A funnel didn't fire | The Activity page explains why, for every comment. |
| Background worker not running | Open the dashboard once from the published address; it registers itself. |
