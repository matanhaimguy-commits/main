---
type: content-log
updated: 2026-10-18
tags: [client, straightscale, content, hub, qa]
---

# StraightScale content log

Every post for [[StraightScale]] known from the repo: what it is, when it runs, where it stands on the hub
([[Social Agent hub]]) and what its checks found. Add a row whenever a post is made, approved, published, vetoed or
scored, and say so in the day's log ([[Log 2026-10-18]] for today). Owner questions that block posts are in
[[StraightScale decisions]]. How posts are made and reviewed: [[Growth Engine]], [[Production layer]],
[[Motion Studio]]. Back to [[00 Index]].

**How current this is.** The repo's last commit is 16 Oct 2026. "Draft" below means a draft on the hub's Content page
as of 16 Oct. Whether Matan approved it, or the hub published it, after that is not recorded in the repo. Check the
hub's Content page, or `growth-engine/tools/hub.py items`, before trusting a status.

Times are Tirana time. Hub item numbers are the hub's content rows.

Source: git log of /home/user/main (last commit 16 Oct 2026), clients/straightscale/plans/2026-W42.md, clients/straightscale/reviews/2026-10-W3-director-friday.md

## Posts

| Date | Format | Title (Albanian) | Card · hub item | Ask | Status |
|---|---|---|---|---|---|
| Thu 15 Oct, 20:09 | Carousel, 7 slides | 7 gjëra që po të kushtojnë klientë çdo javë | SS-2026-10-W2-01 · item 1 | comment ANALIZA | **Published**: https://www.instagram.com/p/DehkW3EDa0B/ (moved from Mon 19 on Matan's request). Its corner shows a model-drawn logo; leave it or re-post is open (LIVE-CAROUSEL-LOGO) |
| Fri 16 Oct, 19:30 | Single image | Nëse nesër telefoni nuk bie fare, nga vjen klienti i radhës? | SS-2026-10-W2-02 · item 3 | comment where clients come from | Draft; published or not is unknown |
| Sat 17 Oct, 19:30 | Reel 13.6 s, voiced quote | Kjo javë e vështirë është për tani, jo përgjithmonë. | SS-2026-10-W2-03 · item 7 | send to an owner | Draft; v4 review pending; published or not is unknown |
| Sun 18 Oct, 18:00 | Single image | Sa mesazhe mbetën pa përgjigje këtë javë? | SS-2026-10-W2-04 · item 4 | comment the number | Draft; v4 edit made; v4 review by a fresh visual-reviewer on 18 Oct: PASS (files not committed yet). Which version the hub draft shows is unknown |
| Mon 19 Oct, 19:30 | Carousel, 7 slides | 5 numra që duhet t'i dish çdo muaj | SS-2026-10-W3-01 · item 5 | save | Draft; Director verdict FIX (caption), fix is in `item.json` |
| Tue 20 Oct, 19:30 | Single image | Një video virale është fat. Klientët çdo muaj janë sistem. | SS-2026-10-W3-02 · item 6 | comment ANALIZA | Draft; Director verdict FIX (caption), fix is in `item.json`; v4 edit made; v4 review on 18 Oct: PASS (files not committed yet). Which version the hub draft shows is unknown |
| Wed 21 Oct, 19:30 | Reel 60 s, narrated story, v2 "The 22:47 race" | Ajo nuk pyeti vetëm ty për çmimin. | old SS-2026-10-W3-03 · item 2 | comment ANALIZA | **Vetoed** by the Organic Director on 16 Oct; replaced by a new card (row below). See "The vetoed Wed 21 reel" |
| Wed 21 Oct, 19:30 | Motion reel 30 s (replacement) | draft text hook: Të shkruajnë, por nuk blejnë? | SS-2026-10-W3-03 (rewritten) | send | Card planned, 20 credits; needs a G-DIRECTOR pass by Mon 19, 22:00, or the slot stays empty |
| Thu 22 Oct, 19:30 | Carousel, 8 slides | Patchwork Marketing: 4 suppliers and the job nobody owns | SS-2026-10-W3-04 | comment ANALIZA | Card planned, Director APPROVE, not made as of 16 Oct |
| Fri 23 Oct, 19:30 | Voiced motion reel 30 s | Freelancer vs agency vs system, ranked | SS-2026-10-W3-05 | comment ANALIZA | Card planned, Director FIX applied (40 to 30 s), not made |
| Sat 24 Oct, 19:30 | Carousel | 3 things we never do for a client | SS-2026-10-W3-06 | follow | Card planned, Director FIX applied (copy line), not made |
| Sun 25 Oct, 18:00 | Quote reel | vault C4: a "nobody calls back in time" problem | SS-2026-10-W3-07 | send | Card planned, Director APPROVE, not made; waits for the narrator listen |
| Wed 28 Oct, 19:30 | Claymation story reel 30 s (`pov_day`) | angle: Të shkruajnë, por nuk blejnë | SS-2026-10-W4-03 (draft card in the Director memo, not yet filed) | send | Planned; needs 7 owner checkpoints. Falls back to Sun 1 Nov 18:00 if the look is not approved by Thu 22 |

Not posted and not in the hub any more: the first version of the Wed 21 reel (24 s kinetic type, no voice), rejected
by Matan on 15 Oct as boring, too much text and no voice. Its files stay in `content/2026-w43-3-reel/v1/`.

Source: clients/straightscale/plans/2026-W42.json, clients/straightscale/plans/2026-W42.md, clients/straightscale/plans/2026-W43.md, clients/straightscale/content/*/item.json, clients/straightscale/cards/2026-10-W2/, clients/straightscale/cards/2026-10-W3/, clients/straightscale/reviews/2026-10-W3-director-friday.md sections 1 and 4, clients/straightscale/content/2026-w43-3-reel/qa.md

## The vetoed Wed 21 reel

- What it was: hub item 2, "Ajo nuk pyeti vetëm ty për çmimin.", the 60 s v2 remake made 15 Oct with MiniMax H3
  footage, an ElevenLabs voice, music and effects (project `motion-studio/projects/straightscale-2026-w43-3-reel-v2`).
  It was made after Matan rejected v1, for the same slot and the same ask.
- Why the Director vetoed it (16 Oct): it promises an answer time ("brenda 1 minute", a stopwatch); it uses a count
  ("three businesses") and facts that are not in the brain; it says what the analysis covers (D3); it shows photoreal
  AI customers and owners face-on and the strategist outside his staged set (D1 interim); the voice is English on an
  Albanian account; the payoff sells one piece (an AI assistant), not the system; it was delivered at 24 fps with no
  run ledger.
- A fresh final review the same day also failed it (16 defects, 5 major) and said a retake is needed under the D1
  interim rule.
- The Director's action: Matan rejects hub item 2; the daily run pushes the replacement as a new draft. The reel is
  not for organic; any paid reuse needs the same truth fixes.
- Matan's own answer to the veto is **not recorded in the repo**. The brief for this brain note said he wanted to post
  it; no file confirms that. Ask him, and record the answer in [[StraightScale decisions]].

Source: clients/straightscale/reviews/2026-10-W3-director-friday.md section 2, clients/straightscale/content/2026-w43-3-reel/item.json, clients/straightscale/content/2026-w43-3-reel/qa/FINAL.v2.review.json, clients/straightscale/cards/2026-10-W3/SS-2026-10-W3-03.yaml (notes)

## QA history, one line per post

- **w43-1 carousel (live, 15 Oct):** read letter by letter, two edit fixes (slides 6 and 7); re-fitted from 3:4 to
  4:5 on 15 Oct for auto-publish; made before the production gates; native Albanian read never ticked; cost not
  measured.
- **w42-5 image (Fri 16):** v2 real-logo fix FAIL (3 minors); v3 code edits FAIL (1 minor: highlight box ends 4 px
  short of the last letter); native read open; 1 credit.
- **w42-6 reel (Sat 17):** v1 FAIL (loudness, captions in the Reels button zone), v2 FAIL (super over his head, loudness
  range from the end-card music fade), v3 FAIL (pseudo-text on the cover, compressor lifted the music in pauses); v4 remixed without the
  compressor and the cover softened, review pending; AI label on; native listen open; 26.75 Higgsfield and 708
  ElevenLabs credits.
- **w42-7 image (Sun 18):** v2 real-logo fix FAIL (3 minors); v3 FAIL (3 minors: a wall sign reading as a blue cross,
  off-palette crimson, text-like marks); v4 removed the wall sign by code, v4 review 18 Oct PASS (v4 files not committed yet);
  native read open; 1 credit.
- **w43-1b carousel (Mon 19):** every slide PASS after the real-logo fix, but the set FAIL (major: the logo sits at a
  different height on each slide, up to 50 px apart); caption fixed per the Director; native read open; 7 credits.
- **w43-2 image (Tue 20):** v2 real-logo fix FAIL (3 minors); v3 FAIL (1 minor: the cedilla of "çdo" touches the
  box); v4 moved the lower line down 5 px by code, v4 review 18 Oct PASS (v4 files not committed yet); caption fixed per
  the Director; native read open; 1 credit.
- **w43-3 reel v2 (Wed 21, vetoed):** final review 16 Oct FAIL, retake needed; Director veto 16 Oct; native read and
  phone listen never done; spend not measured (about 10 H3 clips plus stills).

Source: clients/straightscale/content/*/qa.md, clients/straightscale/content/*/qa/*.review.json, clients/straightscale/content/2026-w42-7-image/qa/v4_edit.md, clients/straightscale/content/2026-w43-2-image/qa/v4_edit.md, clients/straightscale/content/2026-w42-7-image/qa/IMG-W42-7.v4.review.json, clients/straightscale/content/2026-w43-2-image/qa/IMG-W43-2.v4.review.json, clients/straightscale/ledger.csv

## Results

None logged. `results-log.md` and `analytics/posts.csv` have headers only, and `analytics/learnings.md` holds two
production lessons (make 4:5 from the start; every reel has a voice), not performance lessons. Reading results
automatically waits on Insights access (D6).

Source: clients/straightscale/results-log.md, clients/straightscale/analytics/posts.csv, clients/straightscale/analytics/learnings.md

## Director memos

- **Fri 16 Oct 2026, W3 batch review** (`clients/straightscale/reviews/2026-10-W3-director-friday.md`): vetoed the
  Wed 21 reel and rewrote its card; fixed 4 more cards; caption fixes for items 5 and 6; chose the first story reel
  (`pov_day` claymation, W4 Wed 28 Oct); budget check (37 of 1,300 credits logged for October, understated); listed
  the blocks and who clears them.
