# Hook grader calibration (29 Oct 2026, session on `claude/hook-calibration`)

**Result: NOT calibrated after 3 rounds. The old grader packet is kept. The six best stacks were not re-graded.**
No paid generation. No owner checkpoint (G-HOOK, G-HUMAN-HOOKBOARD) was recorded. The bar was not changed.

## The question
Four hook sessions found no stack at A or A+ on text and spoken from both fresh graders. Does the measuring stick match
the `readymerce-hook-lab` skill (v1.1) that Matan named?

**Calibrated means:** at least 5 of 6 known-strong stacks get A or A+ on text and spoken from both graders, and at
least 5 of 6 known-weak stacks get B+ or lower. Graders: 2 fresh sonnet agents per round, given only the packet and 12
shuffled stacks (words only; no frames, since no reference came with one). Files in `hook-calibration/`: the set
builder `build_set.py`, `key-round*.json` (the source of every stack; graders never saw them) and `packet-v2/`.

## Round 1: the current packet (persona card + instructions, unchanged from v5)
Set: 6 strong from refbank outlier cards (10x to 90x their channel median), 6 weak (3 of our weakest graded stacks, 3
built from the skill's named flop patterns). Grades are Text / Spoken.

| Stack | Source | Grader 1 | Grader 2 | Meets? |
|---|---|---|---|---|
| A1 "Entrepreneur vs businessman" quiz | strong, refbank 90x | C / C+ | B- / B | no |
| A2 "Talk about money first" | strong, refbank 15.8x | B- / B- | B- / B | no |
| A3 "3 marketing books" | strong, refbank 15.4x | C / C | C / C+ | no |
| A4 "$3,000 in 30 days" | strong, refbank 17.7x | B / B | B / B- | no |
| A5 "One sentence tells who makes it" | strong, refbank 11.6x | B / B+ | B / B+ | no |
| A6 "Fined, conned, tire shop" | strong, refbank 13.0x | B- / C+ | C / B- | no |
| W1 "A buyer wrote this line" | weak, ours (C / B-) | B- / C+ | B- / C+ | yes |
| W2 "One big client left" | weak, ours (B- / B-) | A / A- | A- / A- | **no** |
| W3 "Likes but no bookings" | weak, ours (C+ / B-) | B / B+ | B / B+ | yes |
| W4 "CONSULTANTS OVER 40" | weak, skill pattern | A- / B+ | A- / B+ | **no** |
| W5 "SHOCKING client hack" | weak, skill pattern | D / D | C- / D | yes |
| W6 "Struggling with your business?" | weak, skill pattern | C / D+ | C / C- | yes |

Strong 0 of 6. Weak 4 of 6. Not calibrated.

## Why (old packet against the skill)
| # | Old packet | Skill | Effect seen |
|---|---|---|---|
| 1 | A persona card ("you stop only if something is clearly about you") grades topic fit to one life. | Gate 1 is that the *ad's target buyer* thinks "that's me". Craft is graded by the rubric. | Strong stacks aimed at managers, employees or creatives got "not me" and C or B. W2 and W4 got A or A- by mirroring the persona's own words ("lumpy", "pipeline"). |
| 2 | No rubric at all: no 11 principles, no 9 gates, no anti-patterns, no per-channel rules. | The grade is a prediction from the rubric. | The grader made up its own standard. It did not punish an age-label hook ("CONSULTANTS OVER 40" got A-), which the skill bans. |
| 3 | "Be strict", and for anything below A "name the exact weakness and the smallest fix". | "Grade honestly, never inflate". A is "a minor tradeoff that doesn't hurt performance". "Give reasons only when asked." | Every stack is pushed to find a fix, so a nit becomes a grade drop. |
| 4 | "Clarity matters most." | Clarity is principle 2 of 11. | Minor. Matan said "clarity above all", so it stays in spirit. |
| 5 | Grade scale A+ to F with shorter meanings. | Full table. | Same scale. Not a cause. |

## Round 2: packet-v2 (rubric from the skill, target buyer on every stack, no persona, no "fix" field)
Packet changes only. `packet-v2/rubric.md` is the skill's grade table, 9 gates, 11 principles (text and spoken
columns), anti-patterns, per-channel rules and hook types, copied word for word. `instructions.md` asks for gates
failed, a text grade, a spoken grade and one line of reasoning. Each stack carries a TARGET BUYER line. Same set as
round 1, new fresh graders.

| Stack | Grader 3 | Grader 4 | Meets? |
|---|---|---|---|
| A1 | C / C | C / C | no |
| A2 | C / C | C / B- | no |
| A3 | C / C | C / C | no |
| A4 | B / B- | B- / B | no |
| A5 | B+ / B+ | B / B+ | no |
| A6 | B- / C | B- / C | no |
| W1 | B+ / A- | B / B+ | **no** (spoken A-) |
| W2 | A- / A- | A- / B+ | **no** |
| W3 | B+ / A- | B / B+ | **no** (spoken A-) |
| W4 | D / C | D / C | yes |
| W5 | F / F | F / F | yes |
| W6 | D / D | D / D | yes |

Strong 0 of 6. Weak 3 of 6. Not calibrated. The label, hype and generic stacks now fall to D or F (the packet change
worked there). But the refbank hooks are talking-head openers for other audiences ("Are you a businessman...", "Age 18
I started..."). The skill's own gates mark them down: no problem named in the first 6 words, no twist, a story setup.
So this strong set did not match the skill's rubric, whatever packet is used. Our own "weak" stacks (W1 to W3) were
only weak by the very packet under test, so they are not independent.

## Round 3: same packet-v2, new set
Strong set replaced with the skill's own winner hooks (Section 6 table, running 30+ days; spoken lines verbatim). The
skill quotes no text hooks for them, so the text lines were written by us to the skill's text rules (4 to 10 words,
claim or hidden cause). Weak set replaced with the skill's named flop patterns (a category label, "doctors won't tell
you", "sewer water" and "slime", an age label, bait words, "a burnt-out mom"), because our own weak stacks had been
graded by the packet under test. Packet unchanged from round 2.

| Stack | Source | Grader 5 | Grader 6 | Meets? |
|---|---|---|---|---|
| B1 kidneys "foam in the toilet" | strong, skill winner | B / B+ | A- / A- | no |
| B2 "box dye ... Cute." | strong, skill winner | A- / B+ | A- / B+ | no |
| B3 "worse eye bags than women" | strong, skill winner | B+ / B | A- / B+ | no |
| B4 "eGFR dropped again" | strong, skill winner | A- / B | A- / B+ | no |
| B5 "She'd hidden her legs for 15 years" | strong, skill winner | B+ / B+ | B+ / B+ | no |
| B6 "not gaining weight, swollen" | strong, skill winner | A- / A- | A- / A- | no |
| W1 "PARASITE CLEANSE" | weak, skill pattern | D / D | D / D | yes |
| W2 "sewer water" | weak, skill pattern | D / D | D / D | yes |
| W3 "WOMEN OVER 50" | weak, skill pattern | D / D | D / D | yes |
| W4 "CONSULTANTS OVER 40" | weak, skill pattern | D / B- | D / C | yes |
| W5 "SHOCKING client hack" | weak, skill pattern | F / F | F / F | yes |
| W6 "Struggling with your business?" | weak, skill pattern | D / D | C / D | yes |

Strong 0 of 6 (the top grade given anywhere was A-, never A). Weak 6 of 6. Not calibrated.

## Verdict
**Not calibrated in 3 rounds.** Per the brief: the old packet stays, and the six best stacks were not re-graded.

What the three rounds show, for the main session to weigh (this session changed nothing else):
1. The old persona packet is not the skill. It has no rubric, grades topic fit, and let a banned age-label hook reach
   A-. packet-v2 follows the skill's rubric word for word and separates strong from weak well: every weak stack built
   from the skill's flop patterns scored D or F in round 3, and the skill's winners scored A- to B+.
2. Even with the skill's rubric, sonnet graders gave the skill's own proven winners A- at best, never A, across 24
   text and spoken reads in round 3. The reasons were small and named: a spoken line of only 7 words, no number, "us"
   unnamed without the visual, a stock phrase. That is the skill's own A- meaning ("one weakness that could be
   fixed"). So the A and A+ bar, as these graders apply it, may not be reachable by words alone. This session was told
   never to change the bar, so it did not.
3. Open choices for the main session (not taken here): use packet-v2 as the measuring stick and re-grade the six best
   stacks with it (expect A- to B+ ceilings); or run one more calibration round with a stronger "A means a minor
   tradeoff that does not hurt performance" instruction, which the skill already says and graders still did not follow.
4. Caveats: the round 3 strong set comes from the skill's winners (health ads) with text we wrote, and the skill does
   not print a grade for any example. Words only; the visual channel was never tested.

## Not done
The re-grade of W9-11 R3c, W9-10 R4a, W1-02 R3c, W9-04 R3a, W9-02's best and the EN 06 page idea's best. The brief
says not to run it when calibration fails.

## Re-grade with packet-v2 (done at the main session's request, after the verdict above)
Main session (29 Oct, after reading this file) asked for the re-grade anyway: Matan decides how the bar maps onto these
graders. Packet-v2 unchanged. Words only (no frames), no new writing, no edits to the stacks. 2 fresh sonnet graders
(7 and 8), 8 shuffled stacks: the six best plus anchors B1 and B6 from round 3. `hook-calibration/regrade_set.py`
builds the set. No G-HOOK or other checkpoint recorded. Grades are Text / Spoken, gates failed in brackets.

| Stack (text / spoken) | Grader 7 | Grader 8 | At A on both channels, both graders? |
|---|---|---|---|
| W9-11 R3c "Offer not selling? Fix its first line before the price." / "Cutting your price because nobody buys? Fix your offer's first line." | B / A- [] | B / B+ [] | FAIL |
| W9-10 R4a "Still no replies? It's the first line, not the volume." / "Doubled your cold emails? The first line is why nobody answers." | B / A- [] | A- / A- [] | FAIL (closest) |
| W1-02 R3c "Your next post's first line? A buyer already wrote it." / "A buyer already wrote it. Here's where to find your own." | B- / C [1,3,4] | C / C [1,3,4] | FAIL |
| W9-04 R3a "Months of posting, few leads? Use buyers' exact words instead." / "Few leads after months of posting? Use your buyers' exact words." | B- / B- [6] | B+ / B+ [] | FAIL |
| W9-02 best "Referrals aren't your problem. The timing is." / "Some months you sign three clients. Some months, literally nothing." | B+ / A- [] | B+ / A- [] | FAIL |
| EN 06 page best "Likes, no bookings? Don't fix the post. Fix the page." / "Your post asks about slow months. Your page never answers it." | B+ / B+ [] | B+ / B- [2] | FAIL |
| Anchor B1 (skill winner, kidneys) | D / C [8,9] | D / C [1,8,9] | FAIL |
| Anchor B6 (skill winner, "not gaining weight, swollen") | B+ / B [] | B / B [1,4] | FAIL |

What the anchors say:
- The same two anchors scored A- / A- (B1) and A- / A- (B6) in round 3. In this run B1 fell to D / C (both graders) and B6
  to B+ / B and B / B. The spread on one unchanged stack is two to four grades. Single reads of one grader are not a
  stable measure, and a pass needs both graders at A on both channels.
- Packet-v2 gives no stack an A on either channel anywhere in this run. Spoken reached A- in five reads (W9-11 once, W9-10
  twice, W9-02 twice; none for the anchors); text reached A- once (W9-10, grader 8).
- Ranking (grader 7 | grader 8): W9-10 first | W9-02 first; W9-02 and W9-10 are the top two for both graders; W1-02 R3c is
  last of our six for both (gates 1, 3 and 4: "it" is never named).
- By the skill's own definition, the six best stacks sit at B to A- on spoken and B- to B+ on text. Nothing here meets
  "A or A+ on text and spoken from both graders". Whether the bar should map to A- on these graders is Matan's call.
