# Hook Lab v4: EN 04 (28 Oct 2026, phase 2 session): stopped, the visual could not be graded

Bar (Matan): `organic.py hooks straightscale-en` PASS, and A or A+ on visual, text and spoken from both of 2 fresh
blind graders; the visual only from a real frame image. At most 3 rounds. Stacks: `hooks-v4.json`. Run:
`clients/straightscale-en/runs/SSEN-2026-11-W2-01/`.

## Result: no master. The bar cannot be reached in this session
- **Blocker:** Atlas stores every output on `atlas-media.oss-us-west-1.aliyuncs.com`, and this environment's network
  policy refuses that host (proxy 403). CF-V1 and CF-V7 were generated (ids `855b65dfda4242ac998d6c5996ffbefa`,
  `f8d86803cc644ebbaf51d3661ea36e31`) but could not be downloaded, so no grader saw a frame. The Higgsfield sandbox
  route is off by the gate hook (owner rule). Fix: allow that host in the environment's Network access settings, then
  download with `atlas generate get <id>`.
- So rounds 1 and 2 graded **text and spoken only**; round 3 (the last) is kept for the real frame.
- **Best stack: `EN04-V10b`** (HF-04, `Q-RN-0033`, code check PASS): text "They went with someone cheaper? It wasn't
  your price." · spoken "You sounded like the others, so price was all they saw." · frame `CF-V10` (the phone, one
  message "We can get it done cheaper.", one hand). Round 2: grader C T A- / S A-, grader D T A- / S A-. Visual: not
  graded.
- **The fix both round 2 graders point at (untested):** `EN04-V10e`, spoken "You sounded like the others, so price
  became the only difference." (clears the half-second clash between "wasn't your price" and "price was all they
  saw"; code check PASS).
- **Ceiling the graders name in both rounds (4 of 4):** losing on price is next to AV-01's core pain (lumpy months),
  not on it, so the text tops out at A-. Earlier rounds (v1 to v3) hit the same A- ceiling. That reads as the idea, not
  the wording: per "Replace, don't escalate", the next round should either tie the price loss to the lumpy month, or
  take the next idea in the bank.

## Round 3 (when the frame host is open)
Download CF-V10 (generate it: G-SPEC, G-PROMPT-IMG and G-BUDGET already PASS), lay the text hook with
`tools/text_hook_overlay.py`, run G-VIS, then 2 fresh blind graders on `EN04-V10e` (and `V10b`) with the frame image.

## Every stack and its code check (`hooks-v4.json`)
| id | format | text | spoken | code |
|---|---|---|---|---|
| V1 | HF-04 | Lost a client to someone cheaper? It wasn't your price. | They just couldn't tell you apart from the others. | PASS |
| V2 | HF-04 | Lost a client to someone cheaper? It wasn't your price. | Drop your price, and the next one still goes cheaper. | PASS |
| V3 | HF-04 | "Drop your price." No. Stop sounding like everyone else. | They can get it done cheaper because you sound the same. | PASS |
| V4 | HF-23 | When you sound like everyone, price is all that's left. | That's why you hear: we can get it cheaper elsewhere. | PASS |
| V5 | HF-19 | Too expensive, or the same as everyone? Find out. | They went cheaper? Here's an easy way to find out if it's you. | FAIL (dropped) |
| V6 | HF-24 | One sentence decides if they go cheaper | I can tell who loses to cheaper from your first sentence. | PASS |
| V7 | HF-21 | Never answer "cheaper" with a lower price | They can get it done cheaper? Don't touch your price. | PASS |
| V8 | HF-03 | Cheaper coach vs the coach they can't compare | You both got the same question. Only you dropped your price. | PASS |
| V9 | HF-28 | Why clients pick someone cheaper (not your price) | Why do clients go cheaper? They can't tell you apart. | PASS |
| V10 | HF-04 | Lost a client to someone cheaper? It wasn't your price. | You sounded like everyone else, so price was all they saw. | PASS |
| V10b-e | HF-04 | round 2 rewrites of V10, see the json | | PASS |

Kept 4 for frames: V1, V10, V7 (phone and message), V3 (three identical sheets). Pre-grade checklist: each frame one
subject in the 15 to 55% band; each spoken line adds the cause or the failed fix to the text; "quote", "deal" and
"lead" kept out after the v3 notes.

## Concept frames (pipeline)
Shot Specs `H-01-V1/V10/V7/V3`, assets `CF-*@v1` (still, hero, hook). Prompt review: 4 to 5 rounds of fresh
prompt-reviewers each (6-word bubble, hands, safe zone, ambiguity); final G-SPEC and G-PROMPT-IMG PASS for all four.
G-BUDGET PASS ($0.40 planned). Generated: CF-V1, CF-V7 (2 x $0.047). Not generated: CF-V10, CF-V3.

## Grades (graders saw only the persona card, the text and the spoken line)
- Round 1: A: V7 T B- S B-, V10 T B+ S A-, V3 T C S C+, V1 T B+ S A-. B: V1 T A- S B+, V3 T B- S B-, V10 T A- S A,
  V7 T B S B-. Both: V7 and V3 out ("a rule, no reason", "who says 'Drop your price'?"); "lost a client" reads as
  churn; not their core pain.
- Round 2 (V10 spoken on three texts): C: "deal" T B+ (sales-team word), "They went with" T A-, "client" T B (churn);
  S A- ("sounded like the others" close to "fix your messaging"). D: same order, "They went with" T A- S A-; fix
  "so price became the only difference".
