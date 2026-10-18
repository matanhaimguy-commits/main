---
type: client
updated: 2026-10-18
tags: [client, straightscale, brain, instagram, albanian]
---

# StraightScale

StraightScale is our own agency and the first (and so far only) client of the [[Growth Engine]]. This note is the
client brain in plain words: who they sell to, what they may and may not say, how they look, where they post and
what is still unknown. Open questions for Matan are in [[StraightScale decisions]]. Every post made so far, with its
status and QA history, is in [[StraightScale content log]]. Rules that hold for every client are in [[Standing rules]].
A new client starts from [[Client brain template]]. Back to [[00 Index]].

The machine-readable version is `clients/straightscale/brain.json`. If this note and brain.json disagree, brain.json
wins and this note gets fixed. Check it with `python3 growth-engine/tools/organic.py brain-check straightscale`.
Next 90-day refresh is due 15 Jan 2027.

Source: clients/straightscale/brain.md, clients/straightscale/brain.json (client, updated, refresh_due)

## Where the files live

All under `clients/straightscale/`.

| What | File |
|---|---|
| Brain (data, then human summary) | `brain.json`, `brain.md` |
| What is missing from the brain | `brain-gaps.md` |
| Brand kit (offer, voice, never-list, colours) | `brand-kit.md` |
| Carousel and image look | `style-bible.md` |
| Real logo files | `brand/` (`wordmark-white.png`, `logo-full.png`, `symbol.png`, `README.md`, `brand.json`) |
| Content map (Oct to Nov 2026) | `content-map.json`, `content-map.md` |
| Post Cards | `cards/2026-10-W2/`, `cards/2026-10-W3/` |
| Finished posts, one folder each | `content/<key>/` (`item.json`, `caption.txt`, `alt-text.txt`, `qa.md`, `qa/`, `hosted.json`) |
| Director reviews | `reviews/` |
| Research and buyer words | `research/2026-10-14/`, `research/demand-map.csv`, `competitors.md` |
| Week plans | `plans/2026-W42.*`, `plans/2026-W43.*` |
| Spend | `ledger.csv`, production runs in `runs/` |
| Results and lessons | `results-log.md`, `analytics/posts.csv`, `analytics/learnings.md` |

Source: ls of clients/straightscale/

## What they sell

- The **StraightScale Client Engine**, in three parts. Foundation: diagnosis, research, offer, brand strategy,
  12-month plan. Build: brand identity, Google profile, conversion website, CRM and tracking, instant-answer and
  follow-up automations, rebooking, reviews and referrals, AI chatbot, AI sales trainer. Grow: filmed video content,
  social media, ad creatives, Meta ads, a monthly scoreboard (spend, leads, booked clients, cost per booked client,
  revenue per euro).
- Packages Silver, Gold, Diamond. Prices are given only on a call or at the analysis. Internal price notes sit in
  `brain.json` (`business_model.price_notes`) and never go into content.
- Unknown: margin, and how many new clients a month StraightScale can take on.

Source: clients/straightscale/brand-kit.md (Offer), clients/straightscale/brain.json (business_model)

## The rule of three ones

- **One offer:** the free 45-minute business analysis, at our office in Tirana or at the client's business, no
  obligation.
- **One path:** the viewer comments **ANALIZA**, the hub's DM bot answers in the DMs with the booking button (hub
  funnel `analiza`, live). The booking link today is straightscale.com; a direct calendar or WhatsApp link is still
  pending from the owner.
- **One metric:** booked analyses from content (keyword comments, then DMs, then leads, then hot or booked).
- What the analysis actually covers, and what the person keeps if they don't buy, is **not written down** (decision
  D3). Until it is, no post says what happens in the analysis.

Source: clients/straightscale/brand-kit.md (The rule of three ones), clients/straightscale/brain.json (offer, decisions_open D3)

## Avatar AV-01 and buyer words

**The owner who pays for enquiries and loses them.** Owner of an established Albanian business with 5+ staff and
EUR 300+ per customer, where the sale needs a conversation: clinics, developers, kitchens and furniture, windows and
renovation, solar, private schools, car importers. The brand kit also lists salons, gyms, consultants, law and
accounting firms. Age 35 to 60 per the brand kit.

- Situation: busy, works in the business every day, gets clients from referrals and Instagram but not predictably,
  pays several suppliers for marketing that does not connect.
- Fears: the phone goes quiet; ad money disappears; clients don't come back; messages go unanswered while they work.
- Has tried: more ads, boosting posts, a freelancer or a social media agency.
- Believes (wrongly): "I need more followers or more ads"; "they compare me on price because my price is too high".
- Wants: clients every month, not by luck; a system that works while they work.

Buyer words in Albanian (written by us from the brand kit's worries; **none verified yet** with real buyers):

| Phrase | Meaning |
|---|---|
| na shkruajnë po nuk blejnë | they write to us but don't buy |
| telefoni nuk bie | the phone goes quiet |
| mesazhet mbeten pa përgjigje kur jam në punë | messages go unanswered while I work |
| klientët nuk kthehen | clients don't come back |
| paratë e reklamave zhduken | the ads money disappears |

The demand map has 10 phrases; 20 to 40 are needed. Real words should come from hub comments and DMs, sales calls
and competitor comments.

Source: clients/straightscale/brain.json (avatars), clients/straightscale/brand-kit.md (Avatar), clients/straightscale/research/demand-map.csv, clients/straightscale/brain-gaps.md

## Mechanism and beliefs

- Problem name: **Patchwork Marketing** (several suppliers, pieces that don't work together).
- Solution name: **the Only Choice System**, five steps: Find, Own, Attract, Convert, Close. These are also the five
  content pillars. Its Albanian name is not given; a script may name it only once the owner supplies it.
- Big idea: "You don't need more marketing. You need marketing that works together."
- Contrast: "Agencies sell you pieces. We build the whole system, starting with your buyers."
- Belief ladder B1 to B8: all "unknown" until comments, DMs and calls show otherwise. B6 ("it works for a business
  like mine") is not held because there is no public proof; B6 posts only through The Build series once a client
  agrees to be filmed (D5).
- Contrarian vault: C1 marketing that works together; C2 agencies sell pieces; C3 ads aren't failing, enquiries die
  after the click; C4 a "nobody calls back in time" problem; C5 a viral video is luck, clients every month are a
  system.

Source: clients/straightscale/brain.json (mechanism, belief_ladder, contrarian_vault), clients/straightscale/reviews/2026-10-W3-director-friday.md section 4

## Voice and language

- Albanian (`sq`) only. One language per account; an English voice on this account is a fail.
- Register: informal **"ti"**. This is the interim answer to D2 (brand doc 14 says "ju"); keep "ti" until Matan
  decides.
- Direct, calm, practical. A strategist talking to an owner. Short sentences. Teach, don't hype.
- At most one emoji per post.
- Every Albanian string (image text, slides, captions, voice) is flagged in the hub notes for a native Albanian read.
- No real voice samples of the owner exist yet (D7, the owner ramble).

Source: clients/straightscale/brain.json (voice), clients/straightscale/brand-kit.md (Avatar, Voice), clients/straightscale/reviews/2026-10-W3-director-friday.md section 2 (gate 5)

## Facts we may use in content

- Free analysis, 45 minutes, at our office in Tirana or at the client's business, no obligation ("falas", "45
  minuta", "në zyrën tonë në Tiranë ose te biznesi yt", "pa detyrim").
- The parts of the Client Engine listed above, and the five numbers of the monthly scoreboard.
- City: Tirana. Market: Albania, also Kosovo and North Macedonia.
- Nothing else. There is **no public proof**: no results, client names, reviews or testimonials until the owner adds
  them with permission. One internal ad result exists (proof bank IP-01) and is internal only, never in content.

Source: clients/straightscale/brand-kit.md (Offer, Proof bank), clients/straightscale/brain.json (proof_bank, market)

## Never

- No prices or discounts.
- No invented numbers, results, client names or reviews. No count unless it is in brain.json.
- No guarantees, deadlines or promised results.
- Never "we answer within 1 hour" or any answer-time promise.
- Never "we chase the client's leads". We build them a system.
- No hype words. No em dashes.
- No real local business mocked by name without permission.
- No line on what the analysis covers until D3 is written.
- No AI person presented as a real client; AI people only from behind or as clearly staged scenes (D1 interim).

Source: clients/straightscale/brain.json (constraints, voice.banned, decisions_open D1 and D3), clients/straightscale/brand-kit.md (Never), clients/straightscale/reviews/2026-10-W3-director-friday.md section 2

## Visual identity

- Colours: mark red #BE0F18 (only in the real logo and the phone case), crimson #B31217 (highlight boxes and the
  swipe arrow), gold #DD9A10 (only the small slide counter), ivory #F8F6EF, marble #EDE4D6, charcoal #1F1F1F. No gold
  text on ivory; no red text on charcoal.
- Type: Playfair Display (headlines) and Montserrat (body, labels, figures).
- World: "Tirana after dark", warm tungsten light, the Tirana clock tower. Recurring object: a smartphone in a deep
  red case that changes state with the story. The paid-ad winner set is the strategist at a whiteboard with one prop.
- **Logo: real files only, never drawn by a model.** Prompts leave the bottom-left corner calm and empty; after the
  review the real file is pasted with `python3 growth-engine/tools/brand_overlay.py <in> <out> --client straightscale`.
  Files: `clients/straightscale/brand/`.
- **Style reference: `STYLE-TOP@v1`** in `clients/straightscale/runs/SS-LIB-STYLE/` (the top of the 15 Oct carousel
  cover). It passed its visual review on 15 Oct and Matan approved the look the same day. The old full cover failed
  its review (a model-drawn logo) and is no longer a reference.
- Images and carousels: 1080x1350 (4:5). Instagram's publishing API refuses 3:4.
- Faces are AI characters, never shown as real clients. AI label: decision D1. No real footage exists yet, so no
  behind-the-scenes formats.

Source: clients/straightscale/brand-kit.md (Visual identity), clients/straightscale/style-bible.md, clients/straightscale/brand/README.md, clients/straightscale/runs/SS-LIB-STYLE/ledger.json, growth-engine/DAILY.md (single image / carousel), clients/straightscale/analytics/learnings.md

## Accounts and cadence

- Instagram: @straightscale_. Facebook cross-posting is not built.
- Approver: Matan, on the hub's Content page. Nothing posts without his approval. Auto-publish is on for
  StraightScale, so approved items go out at their time.
- Since 15 Oct 2026 (owner's request): **one post a day**, **19:30 Tirana time, Sundays 18:00**. The daily run keeps
  the hub 4 days ahead with drafts.
- Target mix per week: 3 reels, 3 carousels, 1 image; account stage "new" (reach 50%, trust 35%, convert 15%; at most
  1 hard offer a month). Daily stories are in the package.
- Every reel has a voice (the text-only reel was rejected on 15 Oct).

Source: lovable-app/docs/APP_REVIEW_RECORDING.md, clients/straightscale/brain.json (package, constraints.approver), growth-engine/DAILY.md (intro, section 2), clients/straightscale/plans/2026-W42.md, clients/straightscale/content-map.md, clients/straightscale/analytics/learnings.md

## Budget

- Monthly cap: **1,300 Higgsfield credits**. ElevenLabs credits are outside the cap.
- Brand kit weekly line: carousels up to 30 Higgsfield credits a week; voiceover only on flagship reels; no paid
  music. Whether to raise the carousel line is an open question (CAROUSEL-BUDGET in [[StraightScale decisions]]).
- October so far (Director memo, 16 Oct): 37 of 1,300 Higgsfield credits logged. This understates the month: two
  pieces were never measured (the 15 Oct carousel and the vetoed reel).

Source: clients/straightscale/brain.json (package.monthly_credit_cap), clients/straightscale/brand-kit.md (Budget per week), clients/straightscale/reviews/2026-10-W3-director-friday.md section 7, clients/straightscale/ledger.csv

## Keyword funnels

| Keyword | What it gives | Live | Hub funnel |
|---|---|---|---|
| ANALIZA | the free 45-minute analysis (booking button in the DM; link mode) | yes | `analiza` |
| PATCHWORK | the Patchwork Test, 10 questions (planned) | no, not built | none |
| HARTA | unknown; people already comment it, no resource exists | no | none |

Only ANALIZA may be used in a post. PATCHWORK and HARTA may not appear until a resource and a live funnel exist.
Two competitors also use the keyword ANALIZA (research 14 Oct), so posts lead with the self-check and only then offer
the analysis.

Source: clients/straightscale/brain.json (lead_magnets), clients/straightscale/brand-kit.md (Free resources behind keywords), clients/straightscale/content-map.md (Keywords), clients/straightscale/plans/2026-W43.md, clients/straightscale/content/2026-w43-1-carousel/qa.md

## Content strategy now

- Theme for Oct to Nov 2026: Patchwork Marketing, then the Only Choice System. Pillars: Find, Own, Attract, Convert,
  Close.
- Series in the lab (10 episodes each before judging): Patchwork Autopsy (carousel teardown), One Step (carousel per
  system step), Ad Library Spy (voiced motion reel), The Build (waits for a filmed client, D5).
- The content map is still marked "pending: Director review, then Matan".
- Research 14 Oct: locally, posts about the owner beat business tips (a numbered self-check carousel and an owner-fear
  question image were the local outliers); "growth is a system, not a viral video" is already a competitor's line.
- First story reel: a `pov_day` claymation short planned for W4, Wed 28 Oct (see [[StraightScale content log]]).

Source: clients/straightscale/content-map.md, clients/straightscale/content-map.json (approved_by), clients/straightscale/plans/2026-W43.md, clients/straightscale/research/2026-10-14/report.md, clients/straightscale/reviews/2026-10-W3-director-friday.md section 4

## Still unknown

Capacity; margin; awareness and sophistication stage; real buyer words; the owner's voice samples; what ANALIZA,
PATCHWORK and HARTA deliver; the AI label rule; baseline numbers (followers, reach, views, where clients come from);
approval turnaround; which beliefs the audience holds. No post results are logged yet (`results-log.md` and
`analytics/posts.csv` are empty), partly because Insights access (D6) is not set up.

Source: clients/straightscale/brain-gaps.md, clients/straightscale/results-log.md, clients/straightscale/analytics/posts.csv

## Keeping this note true

When brain.json, brand-kit.md or a decision changes, update this note and [[StraightScale decisions]] in the same
session, and say what changed in that day's log (for today, [[Log 2026-10-18]]). Client facts change only in
`clients/straightscale/brain.json`; after each change run
`python3 growth-engine/tools/brain_note.py straightscale --title StraightScale` to refresh the generated profile
below, then `python3 growth-engine/tools/organic.py brain-check straightscale`. The daily run can check the note
with `--check` (exit 1 means out of date).

Source: growth-engine/tools/brain_note.py (docstring)

## Profile (generated)

<!-- generated:start -->
Generated from `clients/straightscale/brain.json` by `growth-engine/tools/brain_note.py`. Do not edit between the markers:
change brain.json and run the tool again. Keys that look like secrets are never written here.

- **Client:** straightscale
- **Updated:** 2026-10-15
- **Refresh due:** 2027-01-15
- **Sources:**
  - brand-kit.md (hub profile)
  - growth-engine/ORGANIC-OS.md v1 section 12 (owner-supplied, from project docs 20-UMP-UMS-FINAL, 19-CORE-OFFER, 14-BRAND, HOOK-LIBRARY-B2B-AL)
  - research/2026-10-14
- **Demand map file:** research/demand-map.csv

### Business model

- **Sells:** The StraightScale Client Engine: Foundation (diagnosis, research, offer, brand strategy, 12-month plan), Build (brand identity, Google profile, conversion website, CRM and tracking, instant-answer and follow-up automations, rebooking, reviews and referrals, AI chatbot, AI sales trainer), Grow (filmed video content, social media, ad creatives, Meta ads, monthly scoreboard). Packages Silver, Gold, Diamond.
- **Price notes:** Internal only, never in content: a Diamond package is EUR 3,490 (OS v1 7.7); organic video Gold 8 / Diamond 16 a month (project docs still say Silver 4 / Gold 8 / Diamond 12, DP-11 open).
- **Margin:** unknown
- **Capacity:** unknown: how many new clients a month StraightScale can onboard
- **Sales process:** Comment ANALIZA -> DM (hub funnel analiza) -> free 45-minute analysis at the office in Tirana or at the client's business, no obligation -> proposal. OS v1 8.5 proposes an application with a EUR 50 deposit: not decided (see decisions).

### Offer

- **Main offer:** Free 45-minute business analysis, at our office in Tirana or at the client's business, no obligation
- **Next step:** Comment ANALIZA on a post; the DM bot sends the booking step
- **Keyword:** ANALIZA
- **Delivers:** unknown: what the analysis covers and what the person keeps even if they don't buy is not written down (OS 13.5). Known: 45 minutes, office in Tirana or at the business, no obligation.

### Avatars

- **AV-01**: The owner who pays for enquiries and loses them
  - **Role:** Owner of an established Albanian business with 5+ staff and EUR 300+ per customer where the sale needs a conversation: clinics, developers, kitchens and furniture, windows and renovation, solar, private schools, car importers (OS 12; the brand kit also lists salons, gyms, consultants, law and accounting firms)
  - **Situation:** Busy, works in the business every day; gets clients from referrals and Instagram but not predictably; pays several suppliers for marketing that does not connect.
  - **Keeps up:** The phone goes quiet; enquiries come in and nobody answers in time.
  - **Words:**
    - na shkruajnë po nuk blejnë
    - telefoni nuk bie
    - mesazhet mbeten pa përgjigje kur jam në punë
    - klientët nuk kthehen
    - paratë e reklamave zhduken
  - **Tried:**
    - more ads
    - boosting posts
    - a freelancer or a social media agency (pieces, not a system)
  - **False beliefs:**
    - I need more followers or more ads
    - they compare me on price because my price is too high
  - **Desires:**
    - clients every month, not by luck
    - a system that works while they work
  - **Fears:**
    - the phone goes quiet
    - money spent on ads disappears
    - clients don't come back
  - **Identity:** a serious business owner who built something real and wants it to grow predictably
  - **Note:** Words are from the brand kit's documented worries, written in Albanian by us: confirm with real buyer words (demand map gap).

### Awareness

- **Stage:** unknown: 07-AWARENESS-SOPHISTICATION.md is not in this repo
- **Sophistication:** unknown
- **Notes:** 14 Oct research: locally, posts about the owner beat business tips; two competitors use the keyword ANALIZA.

### Mechanism

- **UMP:** Patchwork Marketing: paying several suppliers for pieces that do not work together
- **UMS:** The Only Choice System
- **Steps:**
  - Find
  - Own
  - Attract
  - Convert
  - Close
- **Big idea:** You don't need more marketing. You need marketing that works together.
- **Contrast line:** Agencies sell you pieces. We build the whole system, starting with your buyers.

### Belief ladder

- **B1**: Your ads aren't failing. Your enquiries are dying after the click.
  - **State:** unknown
- **B2**: It isn't your fault: the real cause is Patchwork Marketing, pieces that don't work together.
  - **State:** unknown
- **B3**: It can be solved: a few numbers show exactly where the leak is.
  - **State:** unknown
- **B4**: The Only Choice System (Find, Own, Attract, Convert, Close) is how it gets solved.
  - **State:** unknown
- **B5**: A system beats hiring a marketer or another agency for pieces.
  - **State:** unknown
- **B6**: It works for a business like mine (needs proof: The Build until then).
  - **State:** not_held
- **B7**: I trust and like the StraightScale people.
  - **State:** unknown
- **B8**: The free analysis is easy, safe and worth doing now.
  - **State:** unknown

### Contrarian vault

- **C1**: You don't need more marketing. You need marketing that works together.
  - **Source:** OS 12 big idea
- **C2**: Agencies sell you pieces. We build the whole system, starting with your buyers.
  - **Source:** OS 12 contrast line
- **C3**: Your ads aren't failing. Your enquiries are dying after the click.
  - **Source:** OS 6.1 B1
- **C4**: You don't have a marketing problem. You have a 'nobody calls back in time' problem.
  - **Source:** OS 12 belief path
- **C5**: A viral video is luck. Clients every month are a system.
  - **Source:** brand kit ('we build them a system') + research/2026-10-14

### Proof bank

- **IP-01**: Best paid ad format so far: a StraightScale strategist at a whiteboard with one real prop; all 4 paid winners used it, about ILS 19 per lead.
  - **Type:** internal ad result
  - **Source:** HOOK-LIBRARY-B2B-AL (OS 7.7)
  - **Permission:** internal_only
  - **Date:** 2026-10

### Lead magnets

- **ANALIZA**: free 45-minute analysis
  - **Delivers:** unknown: contents not written down (OS 13.5). Known: 45 minutes, office in Tirana or at the business, no obligation.
  - **Live:** yes
  - **Funnel ID:** analiza
- **PATCHWORK**: Patchwork Test: 10 questions that show where the business leaks enquiries (OS 12)
  - **Delivers:** unknown: not built yet
  - **Live:** no
  - **Funnel ID:** not set
- **HARTA**: unknown: people comment it, no resource exists
  - **Delivers:** unknown
  - **Live:** no
  - **Funnel ID:** not set

### Voice

- **Adjectives:**
  - direct
  - calm
  - practical
- **Samples:** none
- **Banned:**
  - hype words
  - em dashes
  - prices or discounts
  - guarantees
  - we answer within 1 hour
  - we chase your leads
  - invented numbers, clients or reviews
- **Language:** sq
- **Register:** ti (current posts; brand doc 14 says ju: decision D2)
- **Emoji:** at most one

### Visual

- **Fonts:**
  - Playfair Display (display)
  - Montserrat (body, labels)
- **Logo files:**
  - motion-studio/projects/straightscale-03/assets/brand/logo-full.png
  - motion-studio/projects/straightscale-03/assets/brand/wordmark-white.png
  - motion-studio/projects/straightscale-03/assets/brand/symbol.png
- **Face:** ai_character
- **AI label:** unknown: decision D1 (OS 13.1)
- **Real footage:** no
- **Set:** Tirana after dark; the strategist at a whiteboard (paid winner)
- **Recurring object:** a smartphone in a deep red case that changes state with the story
- **Style bible:** style-bible.md

#### Colors

- **Mark red:** #BE0F18
- **Accent:** #B31217
- **Gold:** #DD9A10
- **Ivory:** #F8F6EF
- **Marble:** #EDE4D6
- **Charcoal:** #1F1F1F

### Market

- **Language:** sq
- **Country:** Albania (also Kosovo, North Macedonia)
- **City:** Tirana
- **Timezone:** Europe/Tirane
- **Events:** none

### Constraints

- **Cannot say:**
  - prices or discounts
  - invented numbers, results, client names, reviews
  - deadlines, guarantees or promised results
  - we answer within 1 hour
  - we chase the client's leads (we build them a system)
  - hype words
  - em dashes
- **Will not show:**
  - real local businesses mocked by name without permission
- **Approver:** Matan (hub Content page)
- **Turnaround hours:** not set

### Baseline

- **Followers:** not set
- **Reach 30d:** not set
- **Median views:** not set
- **Saves:** not set
- **Sends:** not set
- **DMs:** not set
- **Client sources:** unknown
- **As of:** not set

### Package

- **Posts per week:** 7
- **Videos per month:** 12
- **Carousels per month:** 12
- **Stories:** yes
- **Platforms:**
  - instagram
  - facebook (cross-post, not built)
- **Monthly credit cap:** 1300
- **Account stage:** new

### Decisions open

- **D1**: Label the AI characters (strategist, owners) as AI, and add real human content (team, office, Matan's voice) every week?
  - **Recommendation:** Yes to both (OS 13.1).
  - **Interim:** AI people are only shown from behind or as clearly staged scenes; no AI person is presented as a real client.
- **D2**: Register: informal 'ti' (all posts so far) or formal 'ju' (brand doc 14)?
  - **Recommendation:** Pick one for the account and keep it.
  - **Interim:** ti, to stay consistent with what is already posted.
- **D3**: What exactly does the ANALIZA analysis include, and what does the person keep even if they don't buy?
  - **Recommendation:** Write it down; it unlocks B8 posts (offer explainer).
  - **Interim:** No B8 'what happens in the analysis' posts until written.
- **D4**: Free analysis 'no obligation' (brand kit) vs an application with a EUR 50 deposit (OS 8.5)?
  - **Recommendation:** Decide before the DM flow changes.
- **D5**: Film the first 3 clients from day one (with permission) for proof and The Build series?
  - **Recommendation:** Yes (OS 13.6).
- **D6**: Insights access for the Learn loop: add the instagram_manage_insights permission to the Meta login configuration and reconnect?
  - **Recommendation:** Yes (OS 13.10); without it posts.csv can't be filled automatically.
- **D7**: Owner ramble: a 15-20 minute voice note (what annoys you in the industry, what clients always ask, what everyone gets wrong)?
  - **Recommendation:** Fills the contrarian vault, voice samples and story bank.
- **D8**: Package scope for clients: carousels and stories have no unit in any package (OS 13.4).
  - **Recommendation:** Define before selling organic content to clients.

Source: clients/straightscale/brain.json
<!-- generated:end -->

## Notes from the owner

Matan writes here. Claude reads this section and never edits, moves or deletes it; the tool above never touches it.
