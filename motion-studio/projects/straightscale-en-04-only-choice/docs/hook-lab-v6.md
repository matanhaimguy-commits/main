# Hook Lab v6: the picture round for EN 04 and EN 06, new ideas for EN 05 (28 Oct 2026, producer session)

Decisions applied: main session, delegated by Matan, plan 28 Oct (one picture round for the two closest stacks; W9-01
retired; 4 new TOF reach ideas; replacements from them). Bar (Matan): A or A+ on visual, text and spoken from both
fresh graders. Graders: fresh sonnet agents, packet only (persona.md, instructions.md, stacks.md, frames with the text
hook laid on at y 14% to 30% and a 360 px phone copy). A round stops at the first grader who puts no stack at A on
every channel, since no second read can change it.

## Result: no stack passed. G-HOOK FAIL recorded on W2-01, W3-01 and W4-01
| Slot | Ideas this round (rounds) | Best stack | Grades (grader 1 / grader 2), V, T, S |
|---|---|---|---|
| W2-01 (EN 04, `reel_story_narrated`) | W9-02 picture round (1), then new W9-09 (3) | W9-02 v6a: "Referrals aren't your problem. The timing is." / "Some months you sign three clients. Some months, literally nothing." with CF-W902@v2 | B+, B+, A- / B+, B, A |
| W3-01 (EN 05, `reel_animation_short`) | new W9-08 (3) | W9-08 R1b: "Your posts work some months. Nobody knows which post." / "Some months your posts bring clients. You never know which post." (words only) | n/a, A-, A- / n/a, A-, A- |
| W4-01 (EN 06, `reel_animation_short`) | page idea picture round (1), then new W9-10 (3) | W9-10 R3c: "Still no replies? It's the first line, not the volume." / "You doubled your cold emails. The first line is the problem." (words only) | n/a, A, A / n/a, A, A- |

**Closest of the session: W9-10 R3c.** Text A from both graders, spoken A and A-. The one note on the voice: "blunt,
like an accusation, no payoff"; the fix offered: "You doubled your cold emails. The first line is why nobody
answers." Its visual was never graded (no frame budget left). The idea is out of rounds; whether to reopen it is the
main session's call.

## What the picture round showed
1. **The pictures did not lift the grades.** EN 06 with its frame: visual B+, text A-, spoken B at best (one grader).
   EN 04 with its frame: visual B+ from both. EN 05 with its frame: visual B-. The frames read (every word exact), but
   the graders saw small subjects, an empty lower half, and props that meant something else (hearts read as likes; a
   full October reads as a good month, with no cost shown for the empty one).
2. **gpt-image-2 centres the subject group.** All 5 frames landed 3 to 9 points lower than their boxes (the group
   centre near y 46% to 50%), so every frame failed G-VIS on position, even with a 20-band layout in the prompt and a
   spec box raised to 30% to 52%. Two ways out for the main session: accept a key band centred near 45% for concept
   frames, or composite the subject in code over a plain generated ground.
3. **Words only, the three new-idea stacks reached A- to A**, the same ceiling as v5. The recurring notes: say the
   text and the voice in the same words; give the voice a payoff cue, not a repeat; never overclaim the viewer's
   situation ("zero leads", "one post brought your last client" for a referral-fed owner); name the channel once.
4. **Spec reviews are the slow step.** H-01-W902 passed G-SPEC on the 3rd review, H-01-W908 on the 5th; each failure
   was a geometry or wording contradiction a reviewer could name.

## Frames (5 made, $0.237 of the $0.25 budget)
| Frame | Run | G-VIS | Cost |
|---|---|---|---|
| CF-V8@v2 (EN 06 post card over page card) | W4-01 | FAIL: 1 critical, 4 major (cards at y 33% to 68%, page card in the caption zone) | $0.04739 |
| CF-V8@v3 (EN 06, 20-band prompt) | W4-01 | FAIL: 1 major, 1 minor (page card y 52% to 64%; arrow touches both cards). Attempt limit reached | $0.04739 |
| CF-W902@v1 (EN 04 planner, 3 REFERRAL notes in October, November empty) | W2-01 | FAIL: 3 major (planner to y 60%) | $0.04739 |
| CF-W902@v2 (EN 04, tighter layout) | W2-01 | FAIL: 3 minor (everything about 3 points low, planner to y 58%) | $0.04739 |
| CF-W908@v1 (EN 05, six identical post cards, a tiny client on one) | W3-01 | FAIL: 3 major, 3 minor (grid 8 points low; oblique view; a chin shows) | $0.04739 |
Every prompt passed G-PROMPT-IMG (fresh reviewer) before its call; every call went through the gated `atlas`
command with a fresh G-BUDGET. Live balance: $2.405 at the start, $2.168 at the end (never under the $1.50 floor).
The EN 03 clips need about $3.11, more than the balance; the main session should know before it plans them.

## Replacements
- EN 06's page idea: replaced after its picture round (grader 1: no channel at A). Replacement W9-10: out of rounds.
- EN 04's W9-02: replaced after its picture round (visual B+ from both). Replacement W9-09: out of rounds.
- EN 05's W9-01 (retired before this round): replaced by W9-08, out of rounds.
- W9-11 was not run: its demand phrase `Q-R-0146` is in `research/demand-map.csv` but not in
  `research/buyer-phrases-en.md`, so `organic.py hooks` fails every stack on the words check until the row is added.

## The 4 new bank ideas (`clients/straightscale-en/cards/bank/`), idea gate (ORGANIC-OS 7.2)
| Card | Level 4 (narrow product) | Demand phrase | Trinity, shock, $5, key visual | Gate | Hook Lab |
|---|---|---|---|---|---|
| W9-08 (Organic, B2) | LinkedIn works some months because one post brought the client and nobody wrote down which: ask each new client which post made them reach out, then post it again on purpose | Q-R-0022 (direct) | clear, unique, depictable; 7; yes; a stack of identical post cards, a client steps out of one | PASS | 3 rounds, FAIL |
| W9-09 (Organic, B2) | Posting into an empty room: the first line names your topic; swap it for a sentence a buyer wrote | Q-RN-0025 (direct) | clear, unique, depictable; 6; yes; a clay megaphone shouting at empty chairs | PASS (overlap flag with EN 02, C4) | 3 rounds, FAIL |
| W9-10 (Research, B2) | Twice the outreach sends the same message twice: the first sentence is the problem, and it should be a buyer's sentence | Q-R-0027 (bridge) | clear, unique, depictable; 7; yes; paper planes all landing in one bin | PASS | 3 rounds, FAIL (closest) |
| W9-11 (Offer, B2) | Your offer isn't dead, it's in your words: rewrite its first sentence as the buyers' problem before changing price or product | Q-R-0146 (bridge) | clear, unique, depictable; 7; yes; an offer card over a bin, its first line crossed out | PASS (overlap flag with EN 04) | not run (phrase row missing) |
Format router on W9-08 for slot W3-01: `reel_animation_short` top (6.0, tied with `reel_talking_object`), so the slot
keeps its format.

## Files
Stacks: `docs/hooks-v6*.json` in the EN 04, 05 and 06 projects (every one PASSES `organic.py hooks`). Grades:
`clients/straightscale-en/runs/<run>/qa/hooks-v6/grades.md` (W2-01, W3-01, W4-01). Specs, prompts, reviews and frames
under each run's `shots/`, `prompts/`, `qa/` and `assets/`. No owner checkpoint was recorded or asked; nothing was
published and the hub was not touched.
