# Hook Lab v7: W1-02, W1-03 and the EN 06 extra round (28 Oct 2026, producer session)

Decisions applied: main session, delegated by Matan, plan 28 Oct (nearest posts first; one extra round for W9-10 R3c;
the hook-frame gate decision on offsets). Bar (Matan): A or A+ on visual, text and spoken from both fresh blind
graders. Graders: fresh sonnet agents, packet only (persona.md, instructions.md, stacks.md, frames with the text hook
laid on at y 14% to 30% and a 360 px phone copy). A round stops at the first grader who puts no stack at A on every
channel. Branch: `claude/hooks-v6-en04-06` with `origin/claude/dreamy-babbage-qxf3cx` merged in.

## Result: no stack passed. G-HOOK FAIL recorded on W1-02, W1-03 and W4-01
| Slot | Ideas (rounds) | Best stack | Grades V, T, S (grader / grader) |
|---|---|---|---|
| W1-02 (Wed 4 Nov, `reel_whiteboard`) | EN 02's idea (3 of 3), then bank W9-04 (3 of 3) | EN 02 idea R3c: "Your next post's first line? A buyer already wrote it." / "A buyer already wrote it. Here's where to find your own." with CF-W102 | B+, B+, A- (one grader) |
| | | W9-04 R3a: "Months of posting, few leads? Use buyers' exact words instead." / "Few leads after months of posting? Use your buyers' exact words." (words only) | n/a, B+, A- / n/a, B+, B+ |
| W1-03 (Fri 6 Nov, `reel_talking_object`) | own idea out of rounds (v4: 3 of 3), bank W9-11 (3 of 3) | W9-11 R3c: "Offer not selling? Fix its first line before the price." / "Cutting your price because nobody buys? Fix your offer's first line." with CF-W911 | A-, A-, A- / B, B+, B+ |
| W4-01 (EN 06) | W9-10 extra round (1) | W9-10 R4a: "Still no replies? It's the first line, not the volume." / "Doubled your cold emails? The first line is why nobody answers." with CF-W910@v2 | A-, B+, A- / A-, B+, A |

Both W1-02 and W1-03 go back to the main session for a new idea (no escalation to Matan): the bank has no TOF reach
idea left for W1-03, and its only MOF trust idea left for W1-02 is W9-07 (`reel_motion`, list); W9-05 repeats EN 02.

## What these rounds taught us
1. **The frame cut both ways.** W9-10's text was A from both graders words only (v6) and B+ from both with the
   picture: the frame shows paper planes, so "replies to what?" became the question. Name the channel on screen
   ("No replies to your cold emails? It's the first line."). W9-11's frame (struck WE DELIVER RESULTS) lifted the
   visual to A- from one grader.
2. **Say one line on both channels.** Every grader of the last two rounds asked for the spoken line on screen word for
   word when it was the clearer one ("Cutting your price because nobody buys? Fix your offer's first line."). The
   11-word spoken limit and the 10-word text limit make that possible only for lines of 10 words or fewer.
3. **Name the object.** "First line" alone was read as "of what?" every time; "your offer's first line", "your next
   post's first line" fixed it. "Hook" is marketer jargon for this buyer; "copy" reads as plagiarism.
4. **No empty teases.** "Here's where.", "Here's what you need instead" graded B- to C. A payoff cue with an object
   ("Here's where to find your own") graded A-.
5. **EN 02's released hook can't be reused as is.** Its quote (Q-E-0009) has no recovered raw row, so the words check
   refuses it and the board can't show it. The board used the recovered row Q-RN-0011 ("feeling completely
   invisible"); graders read it as "half me" and asked for the link to getting clients.

## Frames (4 made, $0.18956 of the $0.20 budget)
| Frame | Run | G-VIS | Edit-fixable offset | Cost |
|---|---|---|---|---|
| CF-W102@v1 (whiteboard, "feeling completely invisible") | W1-02 | Reviewer: one defect, position only, marked edit_fixable; the ledger shows FAIL (the hero rule counts it; only the owner can override a reviewer gate) | up 4 points (about 82 px), scale to about 95%, extend the plain board | $0.04739 |
| CF-W910@v1 (bin of paper planes, HOPE THIS FINDS YOU WELL) | W4-01 | FAIL: everything about 1.5x size, bin in the caption zone | none (size) | $0.04739 |
| CF-W910@v2 | W4-01 | FAIL: 1 critical, 1 major, 1 minor (the flying plane in the text-hook zone and too big) | bin base 1.5 points low only | $0.04739 |
| CF-W911@v1 (OFFER card in a bin, WE DELIVER RESULTS struck) | W1-03 | FAIL: size (card 47% wide against 32%, bin into the caption zone), 1 minor (inner frame line) | none (size); no second try (budget) | $0.04739 |

Every frame went through Shot Spec, spec-check, a fresh G-SPEC review (W102 2 reviews, W910 3, W911 3), a fresh
G-PROMPT-IMG review, the gated generation command with a fresh G-BUDGET, and a fresh G-VIS review. The image model's
size and centring problem remains: three of four frames came out bigger or lower than the spec. Live balance: $2.168
at the start, $1.979 at the end (the $1.50 floor never reached).

## Other changes
- W1-02 card: `funnel_stage: MOF` and the router's reason and score (reel_whiteboard 6.17, L19 fit 4.17 for the
  mechanism beat) added; `organic.py card-check` OK.
- `research/buyer-phrases-en.md`: `Q-R-0146` added word for word from its raw row (reddit id p9x5zk5).

## Files
Stacks: `docs/hooks-v7-*.json` in the EN 02, EN 06 and EN 08 (`straightscale-en-08-offer-not-dead`) projects; every
graded stack PASSES `organic.py hooks`. Grades: `clients/straightscale-en/runs/<run>/qa/hooks-v7/`. Specs, prompts,
reviews and frames under each run's `shots/`, `prompts/`, `qa/` and `assets/`. No owner checkpoint was recorded or
asked; nothing was published; the hub was not touched.
