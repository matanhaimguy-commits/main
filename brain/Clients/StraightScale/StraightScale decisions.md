---
type: decisions
updated: 2026-10-18
tags: [client, straightscale, decisions, owner-questions]
---

# StraightScale decisions

Every question waiting for Matan (the owner and approver) for [[StraightScale]], with its status. "Open" means no
answer is recorded in the repo. "Decided" means a file records the answer. Until a question is decided, its interim
rule holds. When Matan answers, change the status here, update `clients/straightscale/brain.json` (and
`brain.md`), record queue answers with `growth-engine/tools/pipeline.py approve`, and note it in the day's log
([[Log 2026-10-18]] for today). Back to [[00 Index]]. Related: [[Growth Engine]], [[Production layer]],
[[StraightScale content log]].

Status checked against the repo on 18 Oct 2026. The last commit is from 16 Oct, so an answer given in chat or in the
hub after that is not reflected here.

## D1 to D9: brand and strategy decisions

| ID | Question | Recommended | Interim rule until decided | Status |
|---|---|---|---|---|
| D1 | Label the AI characters (strategist, owners) as AI, and add real human content (team, office, Matan's voice) every week? | Yes to both (OS 13.1) | AI people only from behind or as clearly staged scenes; no AI person presented as a real client. Instagram's AI label goes on for photoreal AI scenes and AI voices (STANDARDS 7). | open |
| D2 | Register: informal "ti" (all posts so far) or formal "ju" (brand doc 14)? | Pick one for the account and keep it | "ti" | open (interim "ti") |
| D3 | What exactly does the ANALIZA analysis include, and what does the person keep even if they don't buy? | Write it down; it unlocks B8 offer-explainer posts | No post or caption says what the analysis covers | open |
| D4 | Free "no obligation" analysis (brand kit) or an application with a EUR 50 deposit (OS 8.5)? | Decide before the DM flow changes | None recorded; the brand kit and every post so far say free, no obligation | open |
| D5 | Film the first 3 clients from day one, with permission, for proof and The Build series? | Yes (OS 13.6) | No B6 proof posts; The Build series waits | open |
| D6 | Insights access for the Learn loop: add `instagram_manage_insights` to the Meta login configuration and reconnect? | Yes (OS 13.10) | `analytics/posts.csv` cannot fill automatically; reading results depends on Matan | open |
| D7 | Owner ramble: a 15 to 20 minute voice note (what annoys you in the industry, what clients always ask, what everyone gets wrong)? | Yes; fills the contrarian vault, voice samples and story bank | None; meanwhile the vault holds 5 positions from strategy docs and there are no voice samples | open |
| D8 | Package scope for clients: carousels and stories have no unit in any package (OS 13.4) | Define before selling organic content to clients | None recorded | open |
| D9 | Drama model routing: allow the drama skill's other models (Kling 3.0, Seedance, Veo and others) for organic drama? | No recommendation recorded | Every drama shot uses H3 (silent shots in keyframe mode); other models stay off | open (queue 16 Oct, G-EXCEPTION) |

Source: clients/straightscale/brain.json (decisions_open), clients/straightscale/brain-gaps.md (Decisions for the owner), growth-engine/production/queue/2026-10-16.md (G-EXCEPTION D9), clients/straightscale/reviews/2026-10-W3-director-friday.md sections 2 and 8

## The approval queue of 16 Oct 2026

The latest queue file holds 6 pending decisions, all on the run `SS-LIB-STYLE`. Matan answers in chat ("approve
R1", "reject, because ..."); Claude records the answer with `pipeline.py approve`. The Director's target dates come
from the Friday memo.

| Queue item | Gate | Question | What it unblocks | Target date | Status |
|---|---|---|---|---|---|
| R1 | G-HUMAN-TEST | Stylized model side-by-side (Nano Banana 2 vs GPT Image 2.5): one character sheet and one 3-panel storyboard, about 10 credits | The first animation story reel (claymation, crochet, 3D, 2D) | yes by Mon 19 Oct | open |
| R2 | G-HUMAN-TEST | H3 duration re-test: one 5 s and one 14 s talking slice, about 80 Higgsfield credits | The first talking-head or story reel. The Director notes the W4 claymation pilot has no lip-sync, so Matan may skip R2 for that piece and save about 80 credits; the plan keeps it | yes by Mon 19 Oct | open |
| D9 | G-EXCEPTION | Drama model routing (see the table above) | Other drama models | none given | open |
| VOICE-(narrator voice id; full item name in the queue file) | G-HUMAN-VOICE | Listen to a 15 s pilot of the narrator voice (Strategist, male 45) and say yes or no; the Albanian pace band is measured on this audition | The Wed 21, Fri 23 and Sun 25 reels and the W4 pilot | Sun 18 Oct | open |
| CAROUSEL-BUDGET | G-HUMAN-FINAL | A carousel now costs about 13 credits (3 concept frames each); 3 a week is about 39, over the brand kit's 30 a week. Raise the weekly line to about 40, or make fewer carousels? | Retakes on the Thu 22 and Sat 24 carousels; a second cover round needs Matan's yes | Wed 21 Oct | open |
| LIVE-CAROUSEL-LOGO | G-HUMAN-FINAL | The carousel live since 15 Oct shows a model-drawn logo in its corner and cannot be edited after posting. Leave it, or archive it and re-post a fixed version? | Nothing else waits on it | none given | open |

Source: growth-engine/production/queue/2026-10-16.md, clients/straightscale/runs/SS-LIB-STYLE/ledger.json (queue), clients/straightscale/reviews/2026-10-W3-director-friday.md sections 4, 7 and 8

## Other owner actions the Director asked for (16 Oct)

| Action | Why | By | Status |
|---|---|---|---|
| Reject hub item 2 (the Wed 21 reel "Ajo nuk pyeti vetëm ty për çmimin.") on the Content page | The Director vetoed it on truth, originality and language; the daily run pushes a replacement draft | Sun 18 Oct | not recorded in the repo (see [[StraightScale content log]]) |
| Approve hub items 5 and 6 after their caption fixes | Fixes for a client-work claim and a D3 line | Sun 18 Oct | the caption fixes are in `content/2026-w43-1b-carousel/item.json` and `content/2026-w43-2-image/item.json`; hub approval not recorded |
| G-HUMAN-HOOKBOARD on each motion reel's hook styleframe | Wed 21 and Fri 23 reels | the day before each slot | open |
| G-HUMAN-LOOK for the story series (`SS-LIB-POV`: owner character, showroom set, red-case phone prop) | The W4 `pov_day` pilot | Thu 22 Oct | open |
| Give the Albanian name of the Only Choice System and its five steps, if a script names them | Otherwise scripts name only Patchwork Marketing | before the pilot script | open |

Source: clients/straightscale/reviews/2026-10-W3-director-friday.md sections 2, 3, 4 and 8

## Other open questions found in the client files

- What the HARTA resource is (people comment HARTA, but no resource or funnel exists). Open.
- A direct booking link (calendar or WhatsApp) in place of straightscale.com. Open.
- Any documented results, with permission, for the proof bank. Open; none exist.
- How many new clients a month StraightScale can take on. Open.
- Organic video counts per package: the Organic OS and the older project docs disagree (tracked as DP-11 in
  `brain.json` price notes). Open.
- The content map (Oct to Nov) is waiting for the Director review and then Matan. Open.

Source: clients/straightscale/plans/2026-W43.md, clients/straightscale/brand-kit.md (One path, Free resources), clients/straightscale/brain.json (business_model), clients/straightscale/content-map.json (approved_by)

## Decided

| Date | Decision | Who | Source |
|---|---|---|---|
| 15 Oct 2026 | Post every day ("make an upload every day"); times 19:30 Tirana, Sundays 18:00 | Matan | plans/2026-W42.md, growth-engine/DAILY.md |
| 15 Oct 2026 | The 7-slide carousel goes out Thu 15 instead of Mon 19 | Matan | plans/2026-W42.json |
| 15 Oct 2026 | The text-only kinetic-type reel (w43-3 v1) is rejected as boring, too much text and no voice; from now on every reel has a voice | Matan | plans/2026-W43.md, analytics/learnings.md |
| 15 Oct 2026 | The look is approved: G-HUMAN-LOOK PASS for the style reference `STYLE-TOP@v1`, given by asking to publish the carousel it comes from | Matan | runs/SS-LIB-STYLE/ledger.json |
| 16 Oct 2026 | Veto of the Wed 21 reel; its slot becomes a 30 s motion reel (trust, B2, send, 20 credits) | Organic Director | reviews/2026-10-W3-director-friday.md section 2 |
| 16 Oct 2026 | First story reel: a `pov_day` claymation short (30 s, 70 to 100 credits) in W4, Wed 28 Oct 19:30, after 7 owner checkpoints | Organic Director | reviews/2026-10-W3-director-friday.md section 4 |

All paths above are under `clients/straightscale/` unless they start with `growth-engine/`.
