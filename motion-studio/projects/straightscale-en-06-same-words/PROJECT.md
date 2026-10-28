# StraightScale EN · EN 06 "The page that changed the subject" (part five: Funnel)

Workflow: `readymerce-hook-lab` with `growth-engine/adapters/hook-lab-organic.md`, `readymerce-script-lab` with
`growth-engine/adapters/script-lab-organic.md`, story format from `growth-engine/production/STORY-FORMATS.md`; the
motion-reel skill for the build later. Docs: `docs/hook-stacks.md`, `docs/script-lab.md`, `docs/script.md`.

## Series (shared by EN 04, 05, 06; set by the session that made them, 28 Oct 2026)
- Account @straightscale_ (English, global). Avatar AV-01 "the lumpy-pipeline owner": founder-led coaches, consultants
  and agency owners whose months are lumpy (persona card: `../straightscale-en-03-song/docs/script-lab.md` section 2).
- Picture: Patchwork Marketing in its DIY form (every fix sewn on alone), the song's cloth world: the method is one cloth
  (the buyers' words) and every piece is cut from it, in order.
- Order of the method (vault note "StraightScale EN offer"): Research, Offer, Organic, Funnel, Paid ads. Part one is the
  song "Maya's quilt" (EN 03), part two is EN 02 (Research: where to find your buyers' words). This series continues:
  EN 04 = part three, Offer · EN 05 = part four, Organic · EN 06 = part five, Funnel. Paid ads (sung in the song) would be
  part six; the order is an owner question (summary).
- Each reel teaches one step the song only promised, so a follower gets the next piece; each ends on a follow CTA for
  the next part (reach job; no live keyword on the EN page).
- Facts only from the repo and the vault: the offer sheet, the buyer quotes already cited with ids in EN 01, EN 02 and
  the song's docs. No invented numbers, results, clients or quotes; no proof numbers (evidence files not collected).
  Names are composites in a stylized world. Never the not-sold angles (reply speed, lead follow-up, sales scripts).
- Copy rules: no em dashes, no hype words, "you/your", text hook 4 to 10 words, the name Patchwork Marketing never in the
  hook, no offer in the hook, StraightScale named at most on the end card.
- Spend: none. No image, video or audio generation in this stage.

## Brief
- Step this reel teaches: Funnel: the page the posts lead to says the offer in the same buyer words the post used, then takes the conversion (offer sheet step 4: "a landing page that attracts the buyer, shows the offer and takes the conversions").
- Story template: `hidden_villain` (STORY-FORMATS 3.3, ST3 via DEV-F2 villain mocking the fixes, Hook Lab HL-T2 / HL-T1)
- Format: `reel_animation` (tier A, O60 + O30 each written on its own, animation style `claymation`; tier A needs `wildcard` or `angle_proven`: owner question)
- Reference: `tt-zackdfilms92` (explainer-3d; signature device character-host, plus x-ray-cutaway, voiceover-explainer): a host character shown the real cause through a cutaway. `refbank.py check --client straightscale --devices character-host,x-ray-cutaway,voiceover-explainer --category explainer-3d`: ok, no
  repeats against the last films (28 Oct). The song (EN 03) is not in the refbank ledger; checked by hand: no shared
  device or category with its claymation song cut. Log with `refbank.py log` only after delivery.
- Platform: 9:16 1080x1920 master, voiced, captions (sound-off read must carry it).
- CTA: follow for the next part (reach job).

## Status
Stage: script & VO (hooks and spines written; recommended spine A taken to a release candidate at both tiers)
Current version: none (no picture, no audio)
Next step: GATE 4, Matan picks the spine (A, B or C) and answers the hook question; then the concept frame
(G-HUMAN-HOOKBOARD), the voice (Voice 1 the page, Voice 2 the narrator) and the build through the motion-reel skill
Blockers / open questions: G-HOOK not passed after 5 blind rounds (master stack best: text A- and A-, spoken A- and A-,
visual A- in round 4, B and B+ in round 5); tier A needs `wildcard` or `angle_proven`; every cold reader asked "do my
clients even reach a page?" (GATE 4 question in `docs/script-lab.md` 9)

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 28 Oct | Hooks v1 rejected (Matan: unclear, not the buyers' words, written English, not proven formats). Hooks v2 built only from proven sources (Hook Library HA ads 30+ days or HF outliers 3x+) and verbatim buyer phrases; all pass `organic.py hooks`. Master = the ad-proven stack. The script release candidate is ON HOLD: it was written on the v1 hook and must be rewritten on the v2 master once Matan approves it, with the new "said, not written" rule | v1 kept; more AI grading rounds | an AI grade is opinion; proof is a post or ad that already won with this buyer | Matan (rejection), Claude (v2) |
| 28 Oct | GATE 4 decided: spine A "The page that changed the subject" (the page is the villain); the hooks it was asked with (v1) were later rejected, see the row above; the scripts wait for the v2 hooks. Still open: the month's wildcard slot for tier A, and whether part five is Funnel or Paid ads (the song sings Paid ads) | B, C, more hook rounds | the writer's recommendation | Matan |
| 28 Oct | GATE 4: which spine (A "The page that changed the subject", B "Maya follows one visitor", C "Three ways I change the subject"), the hook stack below A, `wildcard` for tier A, the "do they reach a page?" doubt | see `docs/script-lab.md` 8 and 9 | the owner's gate | Matan (pending) |
| 28 Oct | Recommended spine A taken through WRITE: O60 180 words, about 72 s, gate 88; O30 86 words, about 34 s, gate 87; draft plus 3 rewrites, no critical fail. Labelled release candidate, provisional until Matan picks | write B or C first; stop at the spines | the owner needs something to judge; scripts are cheap | Claude |
| 28 Oct | Master hook stack: text "More posts won't fix a page that changes the subject.", spoken "More posts? Fine. I'm the page they land on. I change the subject.", H-01 the visitor whose blue bubble matches nothing on the grey page. G-HOOK not passed after the 5-round cap; the joined master was not graded blind | more rounds (the brief's cap is 5) | best text and spoken from round 5, best visual from round 4; spoken line 1 changed by the Script Lab seam fix (listen readers couldn't tell who "I" was) | Claude, owner to decide |
| 28 Oct | Second person ("you", "your page") for the villain, not Maya in third person | "her page" stacks | every "her" stack graded down for "not me" (rounds 1 and 2) | Claude |
| 28 Oct | The bad page's jargon print never says SCALE | SYNERGY, SOLUTIONS, SCALE | a sound-off reader linked SCALE to @straightscale_ | Claude |
| 28 Oct | Blind graders and cold readers were fresh headless Claude instances (`claude -p`, no tools, empty folder) | the Agent tool | the Agent tool was not available in this session | Claude |
| 28 Oct | Template, format and reference as in the brief | the other STORY-FORMATS templates; refbank pick list | each reel of the series uses a different template and format from the song and from each other; refs pass `check` | Claude |

## Approvals
| Date | What (brief, concept, script, VO, styleframes, cut vN) | By | Notes |
|---|---|---|---|

## Log
- 28 Oct · folder made from `templates/project`; brief, template, format and reference set · ok
- 28 Oct · Hook Lab: 10 stacks graded; G-HOOK 5 rounds, two fresh blind graders each (10 graders): not passed, best
  master recorded (`docs/hook-stacks.md`) · open
- 28 Oct · Script Lab: brief card, persona, structure pick, ladder, 3 spines, recommendation, GATE 4 question
  (`docs/script-lab.md`); spine A written at O60 and O30, 4 gated loops with 16 fresh cold readers, RC O60 88, O30 87
  (`docs/script.md`) · waiting on Matan
- 28 Oct · hooks v1 rejected by Matan; hooks v2 from proven formats in docs/hook-stacks.md and docs/hooks.json (all PASS) · script on hold
