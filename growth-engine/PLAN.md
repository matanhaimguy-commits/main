# Growth Engine: plan

Written 14 Oct 2026. Owner: StraightScale. Status: phase 1 in progress (see the end).

## What it is

One system that grows every client's Instagram and Facebook from research to booked clients:

```
 onboard ─► research ─► plan ─► produce ─► approve ─► publish ─► engage ─► measure
   ▲                                                                           │
   └───────────────────────── winners become templates ◄──────────────────────┘
```

- **Research:** what is winning in the client's niche this week (competitors, formats, hooks), plus how the
  client's own posts did.
- **Plan:** the week's posts, each with one job (reach, trust, leads) and one call to action.
- **Produce:** reels (motion-reel → HyperFrames / motion-studio), carousels (carousel-machine → GPT Image 2),
  single images, captions, first comments.
- **Publish:** on a schedule, from the hub.
- **Engage:** the DM bot we already run answers comments and DMs, sends the keyword's link, and books calls.
- **Measure:** reach, saves, shares, keyword comments, DMs, leads and bookings per post feed the next week.

## Two halves and the bridge

| | **Hub** (Social Agent, the Lovable app) | **Studio** (this repo, in Claude Code sessions) |
|---|---|---|
| Runs | Always on (Cloudflare Worker + Lovable Cloud database, cron every minute) | When started: one session per client per week, or on demand |
| Holds | Clients, connected Pages, funnels, DMs, leads, the content calendar, media files, post results | Brand kits, research runs, plans, project sources (HyperFrames, prompts), renders |
| Does | DM bot, comment funnels, onboarding page, approval, scheduled publishing, insights | Research, strategy, writing, design, video, QA |
| Why there | Must answer in seconds, day and night; cheap to run | Needs Chromium, ffmpeg, Whisper, the skills and Claude: heavy, runs in bursts |

**The bridge is the hub's Content API** (`/api/content/*`, one secret token): the studio reads each client's
brief and results from it, uploads finished media, creates calendar items and upserts the keyword funnels.
Nothing is copied by hand between the two.

## One client, one week

| Step | What | Tool | Output |
|---|---|---|---|
| 0. Once per client | Brand kit: avatar, voice samples, offer, proof bank, visual identity, style bible, competitor list | Hub profile + `hyperframes capture <site>` + carousel-machine Step 0 | `clients/<slug>/brand-kit.md`, `style-bible.md`, `competitors.md` |
| 1. Research (Mon) | Last 7 days of 6-10 competitors, ranked by likes and breakout; hook, format, transcript, why it worked | ig-competitor-research, scrape through the Apify connector | `clients/<slug>/research/<date>/` report.html, pattern.txt, ideas.json |
| 2. Learn | Last week's own posts: reach, saves, sends, keyword comments, DMs, leads, bookings | Hub `/api/content/insights` | `clients/<slug>/results-log.md` |
| 3. Plan | 5 posts by default: 2 reels, 2 carousels, 1 single image. Each: goal, format (from winners), hook, belief to move, CTA (rotate keyword / save / send / book) | growth-engine skill | `clients/<slug>/plans/<week>.md` + `plan.json` |
| 4. Produce | Reels from the client's format templates; carousels with the locked style bible; captions, first comment, alt text | motion-reel (HyperFrames) · carousel-machine (Higgsfield GPT Image 2) | `clients/<slug>/content/<date>-<topic>/` |
| 5. QA | Automatic checks (seekcheck, pacing, audio, read time, slide text letter by letter), facts check, native-language flag | motion-reel stage 10 · carousel-machine step 9 | QA notes per item |
| 6. Ship | Media → hub storage; items → calendar as drafts; keyword funnels upserted | `growth-engine/tools/hub.py` | Drafts on the hub's Content page |
| 7. Approve | We (or the client) approve and set times | Hub Content page | Status approved / scheduled |
| 8. Publish | At the set time | Hub publisher (Instagram Content Publishing API) | Live post, permalink stored |
| 9. Engage | Keyword comment → public reply + DM with the link; AI conversation; lead saved; booking | Hub DM bot (live today) | Leads in the Inbox |

## What makes it scale to 50 clients

1. **Templates, not one-offs.** The full 13-stage motion-reel workflow is for flagship pieces. Daily posts reuse a
   small library of proven formats per client: HyperFrames compositions with variables (hook, points, CTA,
   brand tokens, logo), and a locked carousel style bible with anchor images. Each new post is fill-in, render, QA.
   Winners (2x the client's baseline) are saved as new templates.
2. **One batch per client per week.** A scheduled task starts a fresh cloud session every Monday per client:
   research → plan → produce the whole week → ship drafts. The hub publishes day by day.
3. **Cheap where it can be.** DMs run on Claude Haiku 5.5 (well under a cent per reply). Research is the
   only Apify cost (a few cents per run). Reels render on CPU for free. Carousels cost Higgsfield credits
   (about 10-13 per carousel). Voiceover and AI music only on flagship pieces.
4. **Measure leads, not likes.** Every post carries its own keyword, so the hub can count the comments, DMs,
   taps, leads and bookings each post produced.

## Onboarding a new client

1. We create the client in the hub and send them their **onboarding link** (`/join/<code>`).
2. On that page the client fills a short brief (business, offer, audience, FAQ, website, brand colours,
   competitors) and presses **Connect Facebook & Instagram** (Facebook Login for Business).
3. Their Page and Instagram are connected and assigned to their business automatically.
4. We review the brief, run step 0 (brand kit) in the studio, set up the first funnel, test with a tester
   account, then switch the business to live.

**Meta requirements for clients' accounts** (our own account works today under Standard Access):

| Permission | Needed for | Status |
|---|---|---|
| instagram_manage_messages, pages_messaging | DMs and taps from the public, AI conversations | App Review in progress |
| instagram_manage_comments, pages_read_engagement | Comment funnels | Working (Standard) |
| instagram_content_publish, pages_manage_posts | Scheduled publishing | To add to the Login configuration + App Review |
| instagram_manage_insights, read_insights | Post results | To add + App Review |
| Business Verification + "on behalf of other businesses" | Managing clients' accounts | After our own account is approved |
| ads_management, ads_read | Boosting winners (phase 4) | Later |

## Safety rules (always)

- Nothing is posted until the business has **Auto-publish** on and the item is approved. Default: off.
- No invented facts, numbers, reviews, clients or results (both skills' first rule).
- Non-English copy is flagged for a native read before it is approved.
- A keyword CTA only when the resource behind it exists and its funnel is live.
- Secrets live in the hub's Settings or the cloud environment's secrets, never in chat or in git.

## Phases

| Phase | Scope | Status |
|---|---|---|
| 1 | This plan · hub Content API, storage, Content page (approve, schedule, download) · studio skill, client folders, hub CLI · StraightScale pilot week | In progress |
| 2 | Publisher (after instagram_content_publish) · insights pull · onboarding link and brief form | Next |
| 3 | Weekly scheduled session per client · template library per client · automatic results log | After 2 |
| 4 | Ads: boost the week's winner, retarget keyword commenters | Later |
