# App Review screen recording: instagram_manage_messages

Meta asks for one screen recording per permission that shows how the app uses it. This is the shot list for
`instagram_manage_messages` (the same steps in Messenger cover `pages_messaging`). Aim for 2 to 3 minutes, one
continuous recording of your computer screen at 1080p, English on screen. No voice is needed if every step has a
caption; add the captions in Loom, Clipchamp or iMovie, or narrate them in English.

## Before you press record

- [ ] Two browser windows side by side: **A** = the dashboard (https://matan-social-agent.lovable.app), **B** = a
      private window on https://www.instagram.com logged in as the customer **@matanguy_**.
- [ ] @matanguy_ is an **Instagram Tester** on the Meta app (developers.facebook.com → the app → App roles → Roles)
      and accepted the invite (Instagram → Settings → Website permissions → Apps and websites → Tester invites).
      Until Advanced Access, Meta passes DMs only from people with a role, so the demo must use a tester.
- [ ] On @straightscale_: Settings → Messages and story replies → Message controls → Connected tools →
      **Allow access to messages** is on.
- [ ] Dashboard: Settings → real sending on; Businesses → StraightScale → **Live** on, **Testers only** empty.
- [ ] The AI is not paused in @matanguy_'s conversation (Inbox → the conversation → "AI in this conversation").
- [ ] Write as the customer **in English**: the assistant answers in the customer's language.
- [ ] Close other tabs and notifications; don't show passwords or the Settings keys page.

## Shot list (caption to put on screen in quotes)

1. **Window A, logged in, Overview page.**
   "Social Agent is an assistant for a business's Instagram and Facebook inbox. The business owner is logged in."
2. **Connect → "Connect Facebook & Instagram".** Go through the Facebook Login for Business dialog: choose the
   StraightScale Page and its Instagram account, show the permission list (including managing Instagram messages),
   continue. Back in the app the Page shows as connected and subscribed.
   "The business connects its Page and Instagram account and grants instagram_manage_messages."
3. **Businesses → StraightScale → AI & rules.** Scroll slowly past what it sells, the FAQ and the "never say" list.
   "The business tells the assistant what it offers and what it must never say. The assistant only uses these facts."
4. **Window B (the customer).** Open a DM to @straightscale_ and send:
   `Hi! I own a beauty salon in Tirana. Can you help me get more clients from Instagram?`
   "A customer sends a direct message to the business on Instagram."
5. **Stay on window B until the answer arrives** (about 10 to 40 seconds; keep it in one take).
   "The app receives the message through the Instagram messaging webhook and answers on behalf of the business."
6. **Window B:** reply once more so the back-and-forth is visible, e.g. `Yes, how does the free analysis work?`,
   and wait for the answer.
   "The assistant answers questions and offers a free analysis call. It never invents prices or results."
7. **Window A → Inbox → the @matanguy_ conversation.** Show the full transcript and the lead details.
   "Every conversation appears in the Inbox, so the team sees what the assistant said."
8. **Window A: press "Pause the AI here".** Then in window B send `Can I talk to a person?`; no automatic answer
   comes. (Or reply yourself from the StraightScale Instagram app: the AI steps back on its own.)
   "A person can take over at any time. The assistant stops answering in that conversation."
9. **Optional, compliance:** in window B send `STOP`.
   "Customers can opt out at any time; the app stops messaging them."
10. **Window A: press "Let the AI answer again"** to leave the conversation as you found it. End the recording.

## "How to test" text for the submission

> 1. Log in at https://matan-social-agent.lovable.app with the reviewer password provided in the notes
>    (read-only reviewer access).
> 2. Overview and Connect show the connected Facebook Page and Instagram account.
> 3. Send a direct message to the Instagram account @straightscale_ from an Instagram account that has a role on
>    the app. The app answers within a minute, on behalf of the business, using instagram_manage_messages.
> 4. The conversation appears in the Inbox. "Pause the AI here" stops automatic replies in that conversation; a
>    reply from the business's own Instagram app does the same.
> 5. Test the bot (left menu) lets you chat with the assistant without sending anything to Instagram.

Put the reviewer password in the submission's notes field, never in this file.

## Other permissions

- `pages_messaging`: the same shots in Messenger (window B on facebook.com as a tester, messaging the StraightScale
  Page).
- `instagram_manage_comments`, `pages_read_engagement`: comment a funnel keyword (e.g. `ANALIZA`) on a
  StraightScale post from the tester; show the private reply arriving in the tester's message requests and the
  comment in the dashboard's Activity page.
