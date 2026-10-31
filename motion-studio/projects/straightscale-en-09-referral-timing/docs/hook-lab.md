# EN W1-03 twin pilot: Hook Lab under the twin hook rule (step 2, G-HOOK)

Producer session, 31 Oct 2026. Packet-v2 with the 2 anchors (ANCHOR-B1 kidneys, ANCHOR-B6 swollen), built by
`growth-engine/tools/hook_packet.py`, shuffled under neutral labels; keys in `hooks-twin-r*.key.json`. 2 fresh Sonnet
graders per round, 2 at a time. Verdicts by `hook_rule.py`/`hook_record.py` (`hooks-twin-r*.records.json`). Every
stack passed `organic.py hooks` first. No frame exists, so visual is "n/a" everywhere and no stack can pass yet.

## Round 1 (`hooks-twin-r1.json`), words only
| Stack | Text / spoken | Grader 1 T/S, checks failed | Grader 2 T/S, checks failed |
|---|---|---|---|
| W902-T1 | "Referrals aren't your problem. The timing is." / "Some months you sign three clients. Some months, literally nothing." | B, B+, none | B, B+, 4 |
| W902-T2 | "Referrals aren't your problem. Waiting for them is." / (T1's spoken) | A-, B+, none | B+, B+, 4 |
| W902-T3 | "Can you pick the month your next referral comes?" / "No. So some months you sign three clients, some months nothing." | B, C, 2 3 | B-, B-, 3 4 |
| W910-R3c (cross-check) | "Still no replies? It's the first line, not the volume." / "You doubled your cold emails. The first line is the problem." | B+, A-, none | B+, B+, none |
| ANCHOR-B1 | (kidneys) | C, C, 7 9 | C, C, 1 2 9 |
| ANCHOR-B6 | (swollen) | B-, C, 1 3 4 | C, C, 1 2 3 6 |
Result: every stack beats both anchors on text and spoken. Grader 2 failed check 4 (sound-off: the text alone names
the problem) on W9-02's texts: "waiting" and "timing" imply the empty months but don't say them. Fix: the text names the
problem.

## Round 2 (`hooks-twin-r2.json`), words only
| Stack | Text / spoken | Grader 3 T/S, checks failed | Grader 4 T/S, checks failed |
|---|---|---|---|
| **W902-R2a (master)** | "Empty months? It's not referrals. It's waiting for them." / "Some months you sign three clients. Some months, literally nothing." | B+, A-, none | B+, B+, none |
| W902-R2b (variant) | "Some months full, some empty? Referrals aren't the problem." / "You sign three clients, then you wait. And nothing comes." | B, B+, none | A-, B+, none |
| W902-R2c (variant) | R2a's text / R2b's spoken | B+, B+, none | B+, B+, none |
| W910-R3c (cross-check) | unchanged | B+, A-, 4 | B, A-, 4 |
| ANCHOR-B1 | (kidneys) | C, C, 3 8 9 | C, C, 8 9 |
| ANCHOR-B6 | (swollen) | B-, B-, 4 6 | B, B, 4 |
Result: all three W9-02 stacks clear the rule on text and spoken from both graders (at least both anchors, no check
failed). W9-10's stack failed check 4 from both, so W9-02 stays the slot's idea. Round 2 of 3 used.

## Verdict
G-HOOK not recorded: `hook_rule.py` returns "no visual grade" for every stack, and a PASS needs all three channels.
Step 2 is blocked on the visual channel only. Master stack W902-R2a; trial variants W902-R2b and W902-R2c.

Note for the main session: both graders grade the anchors low (C to B, each failing 2 to 4 checks), because the packet
shows them as words only, out of their health niche. Beating them on text and spoken is an easy bar until the anchors
are graded with their frames.

## What the visual channel needs (not generated: no generation in this session)
Three concept frames, then one more blind run (round 3) with the frames in the packet:
1. **ANCHOR-B1 frame** (kidneys, foam): one `openai/gpt-image-2/text-to-image` still at 1152x2048, medium, $0.04739.
2. **ANCHOR-B6 frame** (swollen ankles, not weight): same route and size, $0.04739.
   The anchor frames are calibration only, never published; B6 shows an AI woman's legs or ankles (body part only, no
   face) so STANDARDS 7 is not touched. They should be made once and reused in every later twin grading run.
3. **Our frame 1** (W902-R2a): the twin stage, the wall calendar set above with referral cards on random weeks and one
   month blank, the text hook in the top third. The set: `openai/gpt-image-2/edit` at 1152x2048 with the series look
   references, medium, $0.058694. The twin in the lower third is laid on by code from a still of a HeyGen look at $0
   (needs a look still, which only HeyGen gives: no call made here).
Total $0.153; with the 25% retake buffer $0.19. G-BUDGET first, then G-PROMPT-IMG and G-VIS per frame (one Shot Spec
each). Atlas balance at the plan was $1.98.
