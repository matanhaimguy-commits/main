# Hook Lab v5: EN 04 to EN 06 in their new formats (28 Oct 2026, producer session)

Bar (Matan): A or A+ on visual, text and spoken from both of 2 fresh blind graders (sonnet, persona card only), after
`organic.py hooks` PASS. At most 3 rounds per idea, then the next fitting idea from the bank. No Atlas spend.

## Result: no stack passed. G-HOOK FAIL recorded on every run (W2-01, W3-01, W4-01, W9-01, W9-03)
| Slot | Ideas tried (rounds) | Best stack | Best grades (grader 1 / grader 2, T and S) |
|---|---|---|---|
| W2-01 (EN 04, `reel_story_narrated`) | price idea (3 of 3, 2 from before) -> bank W9-03 (3) -> bank W9-02 (3) | W9-02 R2c: "Referrals aren't your problem. The timing is." / "Some months you sign three clients. Some months, literally nothing." | A, A / A-, A- |
| W3-01 (EN 05, `reel_animation_short`) | boosted post (3) -> bank W9-01 (3) | W9-01 R2b: "Your biggest client left, and now next month is empty?" / "You lose one big client. Next month, literally nothing. Here's why." | B+, A / B+, A- |
| W4-01 (EN 06, `reel_animation_short`) | the page (3) | EN06-C round 1: "Likes, no bookings? Don't fix the post. Fix the page." / "Your post asks about slow months. Your page never answers it." | A-, A / A-, A |
No visual was graded: the two reused frames failed G-VIS (below) and every new frame waits for the Atlas top-up.
The bank has no TOF reach idea left (W9-04, W9-05, W9-07 are MOF trust, W9-06 is BOF convert), so W4-01 got no
replacement and W2-01 and W3-01 stopped after their replacements.

## What the rounds show (for the main session)
1. **The two-grader A bar is the binding limit.** 36 stack reads; text reached A from one grader once (W9-02) and
   spoken reached A five times, never from both on both channels. Every best stack ends at A- with one named nit.
2. **Graders vary a lot.** EN 06's "Your page never answers it" got A from both graders in round 1, and the same idea
   ("website" swapped in) got B- from both in round 2.
3. **Words-only grading hurts picture-led hooks.** EN 06 ("Your website just says welcome") reads as cryptic without
   its frame (the post card "TIRED OF SLOW MONTHS?" over "WELCOME TO OUR WEBSITE"). The quickest gain is the frame:
   CF-V8@v2 for EN 06, then grade the best two stacks with it.
4. Recurring fixes: say the same words on screen and in the voice; name the cost (clients, not "results");
   no bare "a guess", "the others", "the timing"; a payoff cue beats a mirror.

## Frames
| Frame | Run | State | Cost to make |
|---|---|---|---|
| CF-V1@v1 (EN 04 phone, "We can get it done cheaper.") | W2-01 | downloaded; G-VIS FAIL (hero: 5 major, hands and layout off spec); idea dropped | spent earlier |
| CF-V7@v1 (EN 04 phone and red pen) | W2-01 | downloaded; not reviewed (idea dropped) | spent earlier |
| CF-V3@v1 (EN 05 pile of posts, empty calendar) | W3-01 | downloaded; not reused (text hook covers the calendar, empty lower half, no talking post) | spent earlier |
| CF-V8@v1 (EN 06 post card over page card) | W4-01 | downloaded; G-VIS FAIL (hero: 1 major, page card in the caption zone) | spent earlier |
| CF-V8@v2 (EN 06, layout moved up) | W4-01 | prompt `prompts/CF-V8.v2.1.txt` registered; G-PROMPT-IMG not run | $0.04739 |
| CF-V9@v1 (EN 05 blindfolded talking post) | W3-01 | G-SPEC and G-PROMPT-IMG PASS (earlier); waiting; its idea is now dropped | $0.04739 |
| CF-B1@v1 (W9-03 three sticky notes) | W9-03 | spec PASS spec-check, prompt registered; reviews not run (idea dropped) | $0.04739 |
| CF-W1@v1 (W9-01 "BIG CLIENT" block tower) | W9-01 | spec-check PASS; G-SPEC FAIL (fresh reviewer: P4 the lean contradicts the support, P8 the block crosses x 79%, P11 camera height and "half slid out"; fix in `qa/H-01.spec.review.json`); prompt registered, not reviewed; idea dropped | $0.04739 |
Prices: `standards.json` (gpt-image-2 text-to-image, 1152x2048, medium). No Atlas generation in this session.

## Files
Stacks: `docs/hooks-v5*.json` in the EN 04, 05 and 06 projects (every one PASSES `organic.py hooks`). Grades:
`clients/straightscale-en/runs/<run>/qa/hooks-v5/` and `docs/hooks-v5-W9-02-grades.md` here. Grader packets
(persona card, instructions) were built per round in the session scratchpad; the persona card text is in
`clients/straightscale-en/runs/SSEN-2026-11-W2-01/qa/hooks-v5/persona.md`.
