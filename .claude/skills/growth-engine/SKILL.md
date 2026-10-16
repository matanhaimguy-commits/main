---
name: growth-engine
description: The weekly content engine for a client (or for StraightScale itself). Researches what wins in the client's niche, plans the week, produces reels, carousels and single posts with a call to action each, checks them, sends them to the hub (the Social Agent app) as drafts with their keyword funnels, and learns from last week's results. Use for "make this week's content for <client>", "run the weekly cycle", "what should <client> post", "onboard <client> for content", or any request to produce Instagram/Facebook posts for a client. Video goes through motion-reel, carousels through carousel-machine, research through ig-competitor-research.
---

# Growth Engine: the studio side

Why and how it fits together: `growth-engine/PLAN.md`. Paths are relative to the repo root. One folder per
client: `clients/<slug>/` (slug = the business id in the hub).

```
clients/<slug>/
  brand-kit.md        who, offer, voice, proof bank, visual identity, the rule of three ones
  style-bible.md      locked carousel look (carousel-machine step 7), shared colours/type with motion brand.md
  competitors.md      ## Instagram list of @handles (never invented; unconfirmed ones marked)
  results-log.md      one line per published post (carousel-machine step 12 columns)
  research/<date>/    ig-competitor-research runs (dataset, report.html, pattern.txt, ideas.json)
  plans/<week>.md     the week's plan, + <week>.json (machine-readable, below)
  content/<key>/      one folder per post: media, caption.txt, item.json, funnel.json, qa.md
  templates/<name>/   winners saved as reusable skeletons (story map, hook pattern, prompts, composition)
```

## The Organic Growth OS (since 15 Oct 2026; it decides what to make, for whom, why)
`growth-engine/ORGANIC-OS.md` is the spec; where it and the steps below disagree, the OS wins. The chain:

| Layer | What | Files | Agent (`.claude/agents/`) | Check |
|---|---|---|---|---|
| 1 Brain | offer, avatars, demand map, mechanism, beliefs, vault, proof, voice, look, package | `brain.json`, `brain.md`, `research/demand-map.csv` | brain-builder | `organic.py brain-check <slug> --write` (blocking errors stop production) |
| 2 Research | 3-month outliers with the 4 checks, adjacent niches, format rules, idea bank | `research/<date>/outliers.csv`, `research/format-rules.md` | research-scout | `organic.py outliers <dataset.json>` |
| 3 Map | belief focus, pillars, series, mix by stage, calendar, live keywords | `content-map.json`, `content-map.md` | content-strategist, organic-director | director approval |
| 4 Cards | one Post Card per slot (job, belief, pillar, series, avatar, demand phrase, format, hypothesis, target) | `cards/<yyyy-mm>-W<n>/*.yaml` | content-strategist | `organic.py card-check`, `week-check`, `route` |
| 5 Make | idea gate, hooks and scripts (organic adapters), carousels, reels; one run per post | `content/<key>/`, `runs/<post_id>/` | idea-agent, hook-agent, script-agent, carousel-agent, video-producer, visual-planner, prompt/visual/take reviewers | `growth-engine/GATES.md`, `pipeline.py status`, the generation hook |
| 6 Ship | caption, keyword, stories, hub draft | hub `content_items` | distribution-agent, conversion-agent | Matan approves |
| 7 Learn | scorecard, flags, diagnosis, learnings, budget | `analytics/posts.csv`, `ledger.csv`, `analytics/learnings.md` | analyst, organic-director | `organic.py score`, `ledger` |

**Production layer (since 15 Oct 2026; how every image, carousel and video is made and checked):**
`growth-engine/production/`; read its `README.md` first. Every Higgsfield and ElevenLabs generation is gated by the
PreToolUse hook `.claude/hooks/generation_gate.py`: it blocks any call whose gates haven't passed. Every post is a run
(`growth-engine/tools/pipeline.py init`) through the 16 steps of `AI-VIDEO-PIPELINE.md`; every number comes from
`STANDARDS.md` (machine values in `standards.json`); every picture has a Shot Spec, a fresh prompt review and a fresh
visual or take review (`VISUAL-QA.md`, patterns in `failure-library.md`; agents visual-planner, prompt-reviewer,
visual-reviewer, take-reviewer). Review packets: `growth-engine/tools/vqa_crops.py`; the real logo goes on with
`growth-engine/tools/brand_overlay.py` (models never draw it). Story reels (POV day in the buyer's life, the problem as
a villain, two days, song, podcast, drama; claymation, crochet, 3D, 2D): `production/STORY-FORMATS.md`. Budget timing:
STANDARDS 10. Lengths: STANDARDS 8. AI label and AI people: STANDARDS 7 (D1 decides whether to extend it).

Adapters for the production skills: `growth-engine/adapters/` (hook-lab, script-lab, carousel-machine, motion-reel,
animation, drama, song, podcast, UGC and talking head). Format costs, the belief→job table and mixes:
`growth-engine/config/organic.json` (credit prices: STANDARDS 10 wins). Weekly mix for a 7-post account: 3 reels, 3
carousels, 1 image (images only for a strong question or a real review quote). New accounts: reach 50%, trust 35%,
convert 15%.

## Modes
- **weekly** (default): steps 1-7 for one client, the whole week in one session.
- **onboard**: step 0 for a new client, then a first weekly run.
- **daily**: keep the hub 4 days ahead with one post a day, by `growth-engine/DAILY.md` (StraightScale since 15 Oct
  2026; a scheduled cloud session runs it every morning).
- **single**: one piece on demand ("a reel about X for <client>"): steps 4-6 for that item.

Work in autopilot: decide, log the decision in the plan file, keep going. Stop only for paid generation
beyond the budget (the monthly credit cap in `brain.json`, checked by `pipeline.py budget`, and the weekly studio
budget in `brand-kit.md`), or when something is truly blocked. Never post anything yourself: the
hub publishes, and only what a person approved.

## Access check (start of every session)
- `python3 growth-engine/tools/hub.py ping`. Needs `HUB_TOKEN` (app Settings → Studio token, stored as a cloud
  environment secret) and network access to the hub host and its storage host. If it fails with
  `HUB_UNREACHABLE` / `STORAGE_UNREACHABLE`, keep producing into `clients/<slug>/content/` and tell the user
  which domain to allow; never paste the token anywhere.
- Research and images go through the connectors (Apify, Higgsfield), which work without network access.
- Video: `bash motion-studio/setup.sh` before building.

## Step 0 · Client kit (once per client)
1. `hub.py client <slug>` for the profile the DM bot already uses (about, offers, audience, goal, FAQ,
   never-list, voice, links, funnels, Instagram). That profile is the single source of truth for facts.
2. Capture the brand: `hyperframes capture <website>` or Firecrawl branding; the official logo file; fonts
   self-hosted. Write `brand-kit.md` following carousel-machine Step 0, and the motion `brand.md` from
   motion-reel stage 2. Same palette and type in both.
3. `style-bible.md`: carousel-machine Step 7, locked once.
4. `competitors.md`: 6-10 public accounts the client's audience watches, a mix of big and small, local and
   international. Find them with web search and the client's input; only handles you saw written on a page
   tied to the account. Mark unconfirmed ones `(unconfirmed)`.
5. The free resources behind keywords (guide, checklist, booking): list what really exists. A keyword CTA
   needs one.

## Step 1 · Research (weekly)
OS upgrade: base set = the last 3 months scored on views with the 4 outlier checks (`organic.py outliers`), plus the
weekly refresh; add the adjacent-niche accounts from `competitors.md`; likes-only breakout is a fallback for carousels.
ig-competitor-research, run directory `clients/<slug>/research/<YYYY-MM-DD>/`, creator line = the client's
one-line positioning, language = the client's posting language.
- **Scrape.** If this session has `APIFY_TOKEN` and can reach api.apify.com, run the skill's `scrape.py` as is.
  Otherwise use the Apify connector: `call-actor` `apify/instagram-scraper` with
  `{"directUrls": ["https://www.instagram.com/<handle>/", ...], "resultsType": "posts", "resultsLimit": 20,
  "addParentData": false}` and `callOptions.maxItems` = handles × 20, `waitSecs: 0`; wait with
  `get-actor-run`; then `get-dataset-items` with
  `fields=shortCode,url,type,ownerUsername,ownerFullName,inputUrl,timestamp,likesCount,commentsCount,videoViewCount,videoPlayCount,videoDuration,isPinned,productType`
  (paged, 100 at a time) and save them as `dataset.json`. Record the run id and cost in `scrape.json`.
- **Rank:** `rank_and_select.py "$RUN" --days 7 --per-creator 3 --top 12 --rank-by breakout`
  (breakout finds small accounts that popped; use likes when the list is mostly big accounts).
- **Detail the picks:** for each pick, `get-dataset-items` at its offset with
  `fields=caption,displayUrl,videoUrl,childPosts,images,musicInfo` and merge into its `post.json`.
  `prep_media.py` needs Instagram's CDN; when it is blocked, analyse from caption, type and numbers and say so.
- **Analyse and report:** phases 4-5 of the skill (one sub-agent per pick, pattern.txt, ideas.json,
  `build_report.py`). Ideas must be adapted to the client's angle and offer, never copied.

## Step 2 · Learn (weekly)
`hub.py results <slug> --days 14`. Append last week's published posts to `results-log.md` (date, format, hook,
keyword, likes, comments, keyword comments, DMs sent, taps, new leads, hot/booked). A post that beats the
client's baseline 2x is a template candidate; it becomes `templates/<name>/` at 3x with the 4 outlier checks, or
when it produced booked analyses (OS 3.1 and 9.5; carousel-machine step 12; for reels the HyperFrames composition
with its variables).

## Step 3 · Plan the week
Superseded by the OS: plan from the Content Map and write Post Cards (layer 4 above). Default mix for 7 posts: 3 reels,
3 carousels, 1 image; 5 posts: 2 reels, 2 carousels, 1 image (adjust from results: more of what wins). Each post:
one job (reach, trust, convert), one belief to move, one ask. Rotate the asks across the week (follow, save, send,
comment, keyword, dm, book; OS 6.2 and 7.3) so the account is not only asking for comments. A keyword only if it is
live in `brain.json` (StraightScale: ANALIZA). `book` only on convert posts, said as the keyword/DM path ("comment
ANALIZA; the booking button comes in the DM"): never a link, price, discount, guarantee or urgency.
Write `plans/<week>.md` (readable, with the reasoning and the research picks each post is based on) and
`plans/<week>.json`:

```json
{"client": "straightscale", "week": "2026-W42", "timezone": "Europe/Tirane",
 "posts": [{"key": "2026-w42-1-reel", "kind": "reel", "day": "2026-10-20", "time": "19:30",
            "goal": "leads", "pillar": "…", "hook": "…", "angle": "…", "format": "Kinetic Type Listicle",
            "based_on": ["research/2026-10-14 #3"], "cta": {"type": "keyword", "keyword": "ANALIZA",
            "resource": "free 45-minute analysis", "funnel_id": "analiza"}}]}
```
Best posting times: the client's audience's evenings unless results say otherwise.

## Step 4 · Produce
Every piece in `clients/<slug>/content/<key>/`.
- **Reel:** motion-reel in autopilot. Reuse the client's templates first (fill the variables, render); build a
  new composition only for a new format, and save it as a template when it works. Project folder
  `motion-studio/projects/<slug>-<key>/`; copy the final 9:16 MP4 (H.264, AAC, under 100 MB, 3-90 s) as
  `reel.mp4` and a cover frame as `cover.jpg` (delivery file rules: STANDARDS 3). Voiceover and AI music only within
  the budget, and only after a G-BUDGET PASS (`pipeline.py budget`, STANDARDS 10).
- **Carousel:** carousel-machine with the plan's brief, the brand kit and the locked style bible; model and settings per
  STANDARDS 1. The model never draws the logo: the prompt leaves the bottom-left corner calm and empty, and after the
  review `growth-engine/tools/brand_overlay.py <in> <out> --client <slug>` pastes the real file (FL-13). Slides as
  `slide-01.jpg`… (1080x1350 JPEG, 4:5, under 8 MB each: Instagram's publishing API refuses anything taller,
  so never 1080x1440), `alt-text.txt`.
  carousel-machine still says 3:4 and 1080x1440: inside this engine its export step makes 1080x1350 instead.
  Generate at 4:5 when the model offers it; a slide already made at 3:4 is scaled to 1013x1350 and centred on a
  blurred, darkened copy of itself (`convert in.png \( +clone -resize 1080x1350^ -gravity center -extent 1080x1350
  -blur 0x30 -brightness-contrast -20x0 \) +swap ... -composite`), so no text is cropped. The hub refuses images
  outside 4:5 to 1.91:1, and so does Instagram.
- **Single image:** one carousel-machine cover-style design, `image.jpg`.
- **Caption** (`caption.txt`): hook line, value, the one ask, 3-5 relevant hashtags, under 2,200 characters.
  Optional `first-comment.txt`.
- **Keyword funnel** (`funnel.json`) when the ask is a keyword: same shape as the hub's funnels
  (`trigger: comment`, `all_posts: true`, `all_posts_acknowledged: true`, unique keyword, opener in `link` mode
  until the app has Advanced Access for instagram_manage_messages, then `tap`). Reuse an existing funnel when
  the keyword already exists (`hub.py client <slug>` lists them).

## Step 5 · QA (never skip)
The production gates first: fresh reviewers per asset and per final cut (`VISUAL-QA.md`), and `pipeline.py status`
shows no open gates before the hub draft. Reels also get motion-reel stage 10 checks; carousels carousel-machine step 9
(every letter of every slide). All: facts only from the brand kit, `brain.json` and the hub profile; no invented
numbers, clients or results; no counts on screens, phones or in lines unless the number is in `brain.json`, and no
real platform logos or names on screen (STANDARDS 6); an anecdote in the brand's voice only as a clearly framed POV
("POV: ..."), never stated as fact; AI people only as STANDARDS 7 allows; the keyword's resource exists; one ask.
Write `qa.md`. Anything a person must check (native-language read of non-English copy, a claim, music licence) goes
into the item's `notes`, plus "AI label: on" when STANDARDS 7 applies.

## Step 6 · Ship to the hub
`content/<key>/item.json` with local paths; `hub.py push` uploads the media and creates the draft:
```json
{"business": "straightscale", "external_key": "2026-w42-1-reel", "kind": "reel", "title": "…",
 "caption": "<caption.txt>", "first_comment": "…", "alt_text": "…", "keyword": "ANALIZA", "funnel_id": "analiza",
 "media": [{"file": "reel.mp4", "type": "video"}], "cover_url": "cover.jpg",
 "scheduled_at": "2026-10-20T19:30:00+02:00", "notes": "Native Albanian read needed.",
 "source": {"plan": "plans/2026-W42.md", "research": "research/2026-10-14"}}
```
Then `hub.py funnel <slug> content/<key>/funnel.json` for new keywords. Re-running with the same
`external_key` updates the draft until it is published.

## Step 7 · Hand over
Commit and push the client folder (no secrets, no raw scraped media). Tell the user in a few lines: what was
researched (top pattern), the week's posts with days and asks, what needs a person (approvals on the Content
page, native read), the spend (Apify, Higgsfield credits, voice), and anything blocked.

## Rules
- Facts only from the client. Style from references, never content: never copy a competitor's words,
  visuals, characters or layout one to one.
- Non-English copy is always flagged for a native read.
- Never post, never switch a business to live, never change the DM bot's settings from the studio.
- Secrets: `HUB_TOKEN`, `APIFY_TOKEN` live in the cloud environment's secrets, never in chat or git.
