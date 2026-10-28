# Hook Lab v4: EN 05 (28 Oct 2026): lumpy months first, real frames

Brief from the main session (phase 2): lead with the main pain (months that swing), not the boost; no hearts when the
point is leads; Matan's bar (`organic.py hooks` PASS and A or A+ on visual, text and spoken from both of 2 fresh blind
graders, visual graded only on a real frame); at most 3 rounds; Atlas at most $1.00.

## Status: BLOCKED at step 3 (concept frames), no grading round run
The first concept frame (CF-V3) was generated on Atlas (prediction `85b8bcfce1ce468f82b0e81d30cd4123`, gate ALLOW,
about $0.05), but the CLI could not download it: the output host `atlas-media.oss-us-west-1.aliyuncs.com` is refused
by this environment's network policy (proxy CONNECT 403). The Higgsfield sandbox route is switched off by the gate
(owner rule). Without a real frame there is no visual grade, so no stack can reach the bar here and no grader round
was started (it would spend a round on text and spoken only). The other three frames were not generated, to save the
budget until the download works. Fix: add `atlas-media.oss-us-west-1.aliyuncs.com` to the environment's allowed
domains, then fetch the finished image (`atlas generate get 85b8bcfce1ce468f82b0e81d30cd4123`) and run CF-V1, CF-V8,
CF-V9 (all gated and ready).

## The 10 stacks (`docs/hooks-v4.json`): code check 10 of 10 PASS
Round-1 failures fixed before the check passed (6 stacks: spoken over 11 words, no "you"); all lead with the swing.
| id | format | text | spoken |
|---|---|---|---|
| V1 | HF-06 6.7x | One month full, the next month nothing. Here's why. | Some months clients, other months nothing? Your posts know why. |
| V2 | HF-19 90x | Full month or empty month? Here's how to know. | Will next month be full, or nothing? Your posts already know. |
| V3 | HF-04 11.3x | "Post more." No. Post what clients ask about. | Some months nothing? You don't need more posts. You need one. |
| V4 | HF-21 15.8x | Empty months? Post what you sell, then watch who asks. | Just post what you sell. See which post gets clients asking. |
| V5 | HF-26 6.9x | Only one kind of post brings consistent clients | Want consistent clients? Stop posting your tips, memes and trends. |
| V6 | HF-24 11.6x | Only one post shows if next month fills up | One post tells me if your next month is empty. |
| V7 | HF-12 8.6x | "My posts get zero leads." Here's why. | Your posts get zero leads? You never asked who's buying. |
| V8 | HF-20 17.7x | One month full, one month empty. Post this instead. | If your months swing like this, here's what I'd post. |
| V9 | HF-05 10.9x | Some months nothing? Stop guessing what to post. | You shouldn't guess what to post. You should let clients pick. |
| V10 | HF-06 6.7x | Feast and famine months? It starts with your posts. | Every month starting from nothing? Your posts can tell you why. |
Buyer words: Q-R-0058 ("some months wed sign 3 clients other months literally nothing") in 8 of 10; Q-RN-0025,
Q-RN-0005, Q-RN-0004, Q-RN-0026 (ids in the json).

## Pre-grade checklist, kept 4
Kept: **V1** (hidden cause), **V3** (myth), **V8** (process, 17.7x format), **V9** (stop doing X; the talking post).
Dropped: V2 (spoken repeats the text's question), V4 (no swing in the spoken line, 10-word text), V5 (does not lead
with the swing; mocks), V6 (cryptic, near a claim), V7 (zero leads is the side pain; blames), V10 ("it starts with
your posts" vague). No frame shows hearts or counts: clients are clay people, empty months are bare calendar pages.

## Concept frames (run `clients/straightscale-en/runs/SSEN-2026-11-W3-01`)
Look: claymation lane 3 (stop-motion puppet: fabric and thread on clay), for the song's cloth world; STANDARDS 6
reels zone (text hook 14 to 27% down on plain wall, key content 28 to 56%). Text-to-image, 1152x2048, quality medium.
| asset | shot | picture | G-SPEC | G-PROMPT-IMG | frame |
|---|---|---|---|---|---|
| CF-V1 | H-01A | wall calendar: left month crowded with clay clients, right month bare | PASS (2nd review) | PASS | not made |
| CF-V3 | H-01B | tall pile of posts beside an empty month | PASS (2nd) | PASS | made, not downloadable |
| CF-V8 | H-01C | seesaw: full month down, empty month up | PASS (2nd) | PASS | not made |
| CF-V9 | H-01D | blindfolded talking post before an empty month | PASS (2nd) | PASS | not made |
First reviews (8 fresh reviewers) all failed on the safe zone, missing face regions and two-way negatives; fixed in v2.
G-BUDGET PASS ($0.60 planned). Spent: one image, about $0.05.

## G-HOOK, G-SCRIPT
Not recorded: no grading round, no master. `docs/hooks.json` (v2 master EN05-B) is unchanged; no Script Lab loop.
