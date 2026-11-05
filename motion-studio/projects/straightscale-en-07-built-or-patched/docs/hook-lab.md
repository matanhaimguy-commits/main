# Hook Lab: SSEN-2026-11-W1-03 "Built or patched?" (EN 07)

Card: `clients/straightscale-en/cards/2026-11-W1/SSEN-2026-11-W1-03.yaml` (reach, B2, reel_motion, 30 s).
Rules: `growth-engine/adapters/hook-lab-organic.md` (proven formats, buyer words, real frames, replace rule).
Director's change applied: the test must be one the viewer can answer ("Did your last fix use anything the one
before it learned?"); round 1 put it on screen (EN07-05), round 2 shortened it ("Does each fix start from zero?").

**Verdict: REPLACE.** After 3 rounds no stack got A or A+ on visual, text and spoken from both blind graders.
G-HOOK recorded FAIL in the run ledger (28 Oct 2026). Script Lab was not run (replace rule). Spend: $0.

## Method
- 10 stacks written from Hook Library formats with buyer phrase ids (`hooks-r1-all.json`); all 10 pass
  `organic.py hooks` after one fix (EN07-04 had no contrast word).
- Pre-grade checklist before every round: frame 1 viewed at phone size, spoken line not repeating the text, one
  reading only, a concrete payoff. Platform names kept off screen (STANDARDS 6), which removed EN07-06 and EN07-08.
- Frame 1 per finalist rendered in code with the repo engine (`node ../../stills.mjs --page frames/hookframe.html?s=ID`),
  1080x1920, EN 02's look: ivory paper, charcoal, gold, red only for strikes, Montserrat 800. Device: scraps of
  cloth sewn on a charcoal cloth (the card's key visual). Files in `docs/hook-frames/r{1,2,3}-frame1-*.jpg` (copies of the PNGs the graders saw in `out/`, which is gitignored).
- Each round: 2 new general-purpose agents, each given only `persona-card.md`, the frame files, the text and the
  spoken line, letters shuffled between graders. Grades are readers' opinions, not proof (adapter rule 5).

## Grades (visual / text / spoken)
| Round | Stack | Format | Text | Spoken | Grader 1 | Grader 2 |
|---|---|---|---|---|---|---|
| 1 | EN07-01 | HF-19 90x | It works one month, then stops? | Is your marketing built, or patched? Here's an easy test. | B / B+ / A- | A- / A / A |
| 1 | EN07-02 | HF-04 11.3x | "Try a new channel." No. Stop patching. | Your channel's fine. Every fix you tried got patched on alone. | A- / B+ / B- | B+ / B+ / B- |
| 1 | EN07-03 | HF-05 10.9x | Tried everything? Each fix stood alone. | You shouldn't add one more fix. Build on the last one. | A- / B+ / B | A- / A- / B |
| 1 | EN07-05 | HF-24 11.6x | Did your last fix use what the one before learned? | I can tell if your marketing will hold from one question. | C+ / B- / A- | B- / B- / B+ |
| 2 | EN07-01 | HF-19 | Clients one month, nothing the next? | Is your marketing built, or patched? One question tells you. | C / A / A- | C+ / A / A- |
| 2 | EN07-02 | HF-04 | "Try a new channel." That's not the problem. | Your channel's fine. Each fix just started from zero. | A- / A- / B+ | A- / B+ / B |
| 2 | EN07-03 | HF-06 6.7x | Tried everything? Each fix started from zero. | Your fixes each worked a while. Here's why none stuck. | A- / B+ / A | A- / B+ / A |
| 2 | EN07-05 | HF-24 | Does each fix start from zero? | One question shows if your marketing will hold. | B- / B- / B | B- / C / B- |
| 3 | EN07-R3A | HF-06 | Clients one month, nothing the next? | Your fixes each worked a while. Here's why none stuck. | B+ / A / A- | A- / A / A- |
| 3 | EN07-R3B | HF-19 | Referrals, cold email, posting. None of it stuck. | Is your marketing built, or patched? Here's how to tell. | B+ / B / B | B+ / B+ / B |
| 3 | EN07-R3C | HF-04 | "Try a new channel." That's not your problem. | It's not the channel. Every fix you tried started from scratch. | A- / B+ / A- | A- / A / B+ |

## What the graders kept saying (input for the next idea, not for more polishing)
1. "Built or patched" reads as an agency's framework or a quiz; the buyer never calls her tactics "fixes".
   The card's own spoken hook (HF-19) lost every round on that.
2. The buyer's words win the text channel: "Clients one month, nothing the next?" (Q-R-0058) got A from all four
   graders who saw it.
3. A still of cloth scraps shows the tactics, not the swing between months; graders asked for the failure itself
   (peeling, falling, a bare outline), which a still shows weakly. The motion version may read better, but a
   still is what the bar grades.
4. "None of it stuck" is pushed back on: her channels work, on and off.
5. The answerable test (director round 1) worked as a spoken promise, not as on-screen text: as text it was
   read twice (B-, C).

## Suggested next idea in the bank (the main session's call)
Keep Q-R-0058 as the text hook and the three labelled tactics as the frame, but drop the built/patched label and
the word "fix"; a format whose payoff is the swing itself (e.g. HF-06's "every month feels like starting from
zero again") on a frame that shows a full month next to an empty one.
