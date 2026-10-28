# StraightScale EN · EN 04 "The only choice" (part three: Offer)

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
- Step this reel teaches: Offer: build the offer from the buyers' words, with a mechanism of your own, so the buyer can't line you up against three others (offer sheet step 2: "why the client is the only choice and not one of many to compare").
- Story template: `two_days` (STORY-FORMATS 3.2, ST5 two futures, Hook Lab HL-T12)
- Format: `reel_story_narrated` (tier B, O60 single tier, POV camera, hands only, narrator; section 6.4)
- Reference: `tt-blick-thegobbler` (story-comedy; signature device versus-compare, plus pose-to-pose-comedy, seamless-loop): the same moment played twice side by side, the difference is one choice. `refbank.py check --client straightscale --devices versus-compare,pose-to-pose-comedy,seamless-loop --category story-comedy`: ok, no
  repeats against the last films (28 Oct). The song (EN 03) is not in the refbank ledger; checked by hand: no shared
  device or category with its claymation song cut. Log with `refbank.py log` only after delivery.
- Platform: 9:16 1080x1920 master, voiced, captions (sound-off read must carry it).
- CTA: follow for the next part (reach job).

## Status
Stage: script & VO (hooks and spines written; recommended spine B taken to a release candidate, 86/100, loop 4)
Current version: none (no picture, no audio)
Next step: GATE 4, Matan picks the spine (A, B or C; question in `docs/script-lab.md` section 9); then the master hook
stack's named fixes go to fresh blind graders on the concept frame
Blockers / open questions: G-HOOK not passed after 5 blind rounds (best: stack Q, V A-, T A-, S A to B+); the two
owners meet at about 31 s, not in frame 1 (every split frame lost the visual at phone size); the RC runs 74 s, tight
against O60's 75 s cap; the readable steps on her page need plain example words that are not StraightScale's method

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 28 Oct | Hooks v1 rejected (Matan: unclear, not the buyers' words, written English, not proven formats). Hooks v2 built only from proven sources (Hook Library HA ads 30+ days or HF outliers 3x+) and verbatim buyer phrases; all pass `organic.py hooks`. Master = the ad-proven stack. The script release candidate is ON HOLD: it was written on the v1 hook and must be rewritten on the v2 master once Matan approves it, with the new "said, not written" rule | v1 kept; more AI grading rounds | an AI grade is opinion; proof is a post or ad that already won with this buyer | Matan (rejection), Claude (v2) |
| 28 Oct | GATE 4: the spine (A "Same question" ST5, B "Decided before you quoted" ST3 on the two_days pair, C "Why you?" ST6); writer recommends B | A, B, C, B with A's split as a trial variant | pending | Matan (pending) |
| 28 Oct | Spine B taken through WRITE to a release candidate: 185 words, about 74 s, gate 86/100, no critical fail, loop 4 (rewrite 3 of 3); labelled provisional until the pick | stop at the spines | the brief asks for the recommended spine as an RC | Claude |
| 28 Oct | G-HOOK not passed after 5 rounds of 2 fresh blind graders each; master candidate Q recorded with its untested fixes, taken to GATE 4 | more rounds | the round cap in the brief; the visual held at A- for every grader | Claude, owner to be told |
| 28 Oct | The two owners meet at line 7 (about 31 s), not in frame 1 | STORY-FORMATS 3.2's split at 0 to 3 s (stack P) | the split frame lost the visual in all 5 rounds (bubbles halved at phone size) | Claude, owner to confirm at GATE 4 |
| 28 Oct | Picture: the series' cloth means only "what the offer is made of" (the same plain cloth vs a cloth printed with buyer phrases Q-R-0058, Q-R-0094, Q-R-0022); the fixes are real props | the song's patch for every fix | one meaning per object (Script Lab test 8) | Claude |
| 28 Oct | Template, format and reference as in the brief | the other STORY-FORMATS templates; refbank pick list | each reel of the series uses a different template and format from the song and from each other; refs pass `check` | Claude |

## Approvals
| Date | What (brief, concept, script, VO, styleframes, cut vN) | By | Notes |
|---|---|---|---|

## Log
- 28 Oct · folder made from `templates/project`; brief, template, format and reference set · ok
- 28 Oct · Hook Lab: 10 stacks graded, 3 kept; G-HOOK 5 rounds, 10 fresh blind graders (headless agents, persona card
  only): not passed, best stack Q V A-, T A-, S A to B+ · docs/hook-stacks.md
- 28 Oct · Script Lab: brief, persona, structure pick, ladder, 3 spines (A ST5, B ST3, C ST6), recommendation B; the GATE 4
  question · docs/script-lab.md
- 28 Oct · WRITE on spine B: 4 versions, 8 fresh cold readers (listen-only and sound-off per loop); loop 1 critical
  fail (two prospects or one), loop 2 78, loop 3 84, loop 4 86 with no critical fail: release candidate, provisional
  until Matan's pick · docs/script.md
- 28 Oct · hooks v1 rejected by Matan; hooks v2 from proven formats in docs/hook-stacks.md and docs/hooks.json (all PASS) · script on hold
