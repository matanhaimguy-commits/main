# StraightScale EN · EN 05 "The post that knew" (part four: Organic)

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
- Step this reel teaches: Organic: posts cut from the offer, each one built on a buyer sentence, run as the free test lab that shows which message brings the right buyers (offer sheet step 3 and the mechanism "organic first, then paid").
- Story template: `object_speaks` (STORY-FORMATS 3.4, ST3 via DEV-F1 talking part, Hook Lab HL-T1)
- Format: `reel_animation_short` (tier B, O30, animation style `claymation`, the song's world)
- Reference: `ig-papertiger-animation` (brand-ad; signature device before-after, plus character-host, reaction-shot): a smug host character watches a before turn into an after. `refbank.py check --client straightscale --devices before-after,character-host,reaction-shot --category brand-ad`: ok, no
  repeats against the last films (28 Oct). The song (EN 03) is not in the refbank ledger; checked by hand: no shared
  device or category with its claymation song cut. Log with `refbank.py log` only after delivery.
- Platform: 9:16 1080x1920 master, voiced, captions (sound-off read must carry it).
- CTA: follow for the next part (reach job).

## Status
Stage: script & VO (hooks and spines written; recommended spine taken to a release candidate)
Current version: script loop 4, spine A, 86 words, about 34 s; 85/100, no critical fail ("Release candidate,
provisional until Matan picks the spine"). No picture, no audio.
Next step: GATE 4, Matan picks the spine (question in `docs/script-lab.md` section 9)
Blockers / open questions: G-HOOK not passed after 5 blind rounds (master V A-, T A to A-, S A to A-; re-grade on a real
concept frame before any storyboard) · text hook, "the next part" vs "part five", process-only payoff (GATE 4 riders) ·
L5 "around" to "built on" (not applied; needs its own gate)

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 28 Oct | Hooks v1 rejected (Matan: unclear, not the buyers' words, written English, not proven formats). Hooks v2 built only from proven sources (Hook Library HA ads 30+ days or HF outliers 3x+) and verbatim buyer phrases; all pass `organic.py hooks`. Master = the ad-proven stack. The script release candidate is ON HOLD: it was written on the v1 hook and must be rewritten on the v2 master once Matan approves it, with the new "said, not written" rule | v1 kept; more AI grading rounds | an AI grade is opinion; proof is a post or ad that already won with this buyer | Matan (rejection), Claude (v2) |
| 28 Oct | GATE 4: spine A "The post that got paid for" (ST3 on the talking post), B "Two posts" (ST6), or C "The push button" (ST8); riders: text hook, CTA wording, payoff picture | A, B, C (`docs/script-lab.md` 8 and 9) | Claude recommends A: the only spine with a graded opening, written to release candidate at 85 | Matan (pending) |
| 28 Oct | Spine A taken through WRITE: 4 loops (first draft + 3 rewrites), 85/100 at loop 4, no critical fail; labelled provisional | stop at loop 3 (critical fail) | the skill's 3 rewrite loops; loop 3 failed on "a free test" used before it was explained | Claude |
| 28 Oct | Master text hook swapped to "Quiet month? She paid to push a post. Nothing." (round 4, T A / A-); "...It wasn't the post." sent back to the Hook Lab | keep the graders' favourite text | Script Lab test 12: on spine A's body it read as a contradiction; one extra fresh sound-off read confirmed the swap (no script word changed) | Claude |
| 28 Oct | CTA "Follow for the next part: the page those buyers land on." with a "Part four" label on the end card, instead of "Follow for part five: ..." | the brief's "part five" | two cold readers stopped on "part five? what were one to four?"; the meaning (part five, Funnel) is unchanged; Matan may restore the number | Claude (Matan to confirm) |
| 28 Oct | Payoff shows a process (the buyers choose one post and walk toward the door), never a result; the CLIENTS pockets stay empty | a few clients in the pockets, as the song's owner-approved payoff | STORY-FORMATS 3 "the payoff shows a process"; no proof file; flagged because every sound-off reader asked "did she sign anyone?" | Claude (Matan to confirm) |
| 28 Oct | G-HOOK: not passed after 5 rounds of two fresh blind graders each; best stack recorded; taken to GATE 4 | more rounds | the cap in the brief (5 rounds); every grader's last A- is the visual at 1 s (a phone with a face reads cute first), which needs a real concept frame (no generation in this stage) | Claude, owner informed |
| 28 Oct | Persona card: the song's card plus two sentences ("you post content yourself... once or twice you put a little ad money behind a post"; "content has been a black box", Q-E-0183) | the song's card unchanged | the reel's moment (a paid push) must be in the persona's life, without naming the cause | Claude |
| 28 Oct | Template, format and reference as in the brief | the other STORY-FORMATS templates; refbank pick list | each reel of the series uses a different template and format from the song and from each other; refs pass `check` | Claude |

## Approvals
| Date | What (brief, concept, script, VO, styleframes, cut vN) | By | Notes |
|---|---|---|---|

## Log
- 28 Oct · folder made from `templates/project`; brief, template, format and reference set · ok
- 28 Oct · Hook Lab: 10 stacks graded, 3 kept; G-HOOK 5 rounds, 10 fresh blind graders (tool-less agents, persona
  card + H-01 spec in words only); not passed, best master recorded · `docs/hook-stacks.md`
- 28 Oct · Script Lab: brief card, persona, structure pick, ladder, 3 spines, recommendation, GATE 4 question; spine A
  through 4 loops with 9 fresh cold readers (listen-only and sound-off per loop, plus one hook-swap check); 85/100,
  release candidate, provisional · `docs/script-lab.md`, `docs/script.md`
- 28 Oct · no generation, no paid calls, nothing committed (the parent session commits)
- 28 Oct · hooks v1 rejected by Matan; hooks v2 from proven formats in docs/hook-stacks.md and docs/hooks.json (all PASS) · script on hold
