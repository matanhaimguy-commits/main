# Hook Lab v4: EN 06 (28 Oct 2026): fix the best stack, grade on a real frame

Brief (main session, phase 2): start from the best earlier stack (text "Likes, no bookings? Don't post more.", spoken
"The problem isn't your posts. It's what happens after someone clicks."), fix the graders' two notes (BOOK A CALL
page and calendar too small on a phone; "Don't post more" can read as "stop posting"), write 10 stacks from Hook
Library formats in buyer words, code-check, keep 4, make one real 9:16 concept frame each through the pipeline, then
2 fresh blind graders per round, at most 3 rounds. Run: `clients/straightscale-en/runs/SSEN-2026-11-W4-01/`.

## Status: BLOCKED at the real frame (network), no grade yet
- The one frame that cleared every gate (CF-V8@v1) was generated on Atlas (prediction `d4fe8943474746edb8773d75aef49cd0`,
  about $0.047), but the file cannot be downloaded: the environment's network policy refuses
  `atlas-media.oss-us-west-1.aliyuncs.com` (proxy 403 on CONNECT; the CLI's own DNS also fails). The real-frame rule
  forbids a visual grade without the image, so no stack was sent to the graders and G-HOOK is not recorded.
- To unblock: add `atlas-media.oss-us-west-1.aliyuncs.com` to the environment's allowed domains (Network access in the
  cloud environment settings), then `atlas generate get d4fe8943474746edb8773d75aef49cd0 -o <run>/assets/CF-V8.v1.png`
  (no new spend; the asset's media id is already registered).
- No other generation was made after the block, on purpose (spend without a file to grade is waste).

## The 10 stacks (`docs/hooks-v4.json`; all 10 PASS `organic.py hooks straightscale-en`)
| id | format | text | spoken |
|---|---|---|---|
| EN06-V1 (the fixed earlier stack) | HF-05 | Likes, no bookings? Don't post more. Fix the page. | The problem isn't your posts. It's what happens after someone clicks. |
| EN06-V2 | HF-05 | Likes, no bookings? Don't fix your posts. Fix the page. | Your posts work. The page they click to loses the clients. |
| EN06-V3 | HF-04 | "Post more." No. Fix the page they click to. | Likes but no bookings? Look at your page after the click. |
| EN06-V4 | HF-12 | Likes, no bookings? Your posts aren't the problem. | You think your posts don't work. Check the page they click. |
| EN06-V5 | HF-19 | Likes, no bookings? Is it your posts or page? | Is it your posts or your page? Here's how to tell. |
| EN06-V6 | HF-04 | You don't need more likes. You need bookings. | More posts won't fix it. Your page is the problem. |
| EN06-V7 | HF-26 | Likes, no bookings? Stop rewriting your posts. | If your posts get likes, stop rewriting them. Check the page. |
| EN06-V8 | HF-03 | Likes, no bookings? Your post and your page don't match. | Your post says one thing. Your page says another. Nobody books. |
| EN06-V9 | HF-21 | Likes, no bookings? Check the page first. | Before you post more, click your own link. Read that page. |
| EN06-V10 | HF-16 | Where do your likes go after the click? | Your post gets likes. Then they click. Then nothing. |

Fix 2 ("stop posting"): V1 adds "Fix the page." so "Don't post more" has one reading (do this instead). Kept 4: V1,
V2, V8, V9 (V5 and V10 open on a question, which 0 of 12 library winners do; V3, V4, V6, V7 overlap V1/V2). V1 and V2
share one frame (same picture, different words).

## Fix 1 (frame too small): what the reviews found
The earlier frame idea (a whole phone plus a laptop) cannot be big on a phone because STANDARDS 6 leaves only a band
for key content: top 14% clear, text hook at 14% to 30%, key props 15% to 55% (captions start at 55%), bottom 35%
clear, right 21% of the lower half clear. So every frame is now a macro close-up: the booking page (or the two cards)
fills the full width between 30% and 55% of the height. Six review rounds of fresh prompt-reviewers (spec mode and
prompt mode) on 4 then 3 frames; every fail was recorded with `pipeline.py record` (some superseded reports could not
be recorded because the prompt changed first). Specs and prompts are built from one source:
`tools/concept_frames.py` (run from the repo root); the text hook overlay for the graders: `tools/overlay_hook.py`.

| Frame | Stacks | Picture | Gate state |
|---|---|---|---|
| CF-V8@v1 (H-01-V8) | V8 | top-down: cream post card "TIRED OF SLOW / MONTHS?" with hearts, arrow down, grey-blue page card "WELCOME TO / OUR WEBSITE" | G-SPEC PASS, G-PROMPT-IMG PASS, G-BUDGET PASS, generated, file blocked |
| CF-V1@v1 (H-01-V1) | V1, V2 | macro booking page: BOOK A CALL band, empty 2x4 calendar of tiles, a low row of hearts | v6 in review |
| CF-V9@v1 (H-01-V9) | V9 | same page, a magnifying glass on the empty calendar | v6 in review |

Prompt loop limit (2) was passed on CF-V1, CF-V8 and CF-V9; this session (acting for the director role) chose
"rewrite and simplify" each time, never escalation (replace, don't escalate). The CF-V2 asset is dropped (V2 uses
CF-V1's frame); its spec was deleted.

## Look choice for the main session
No claymation lane is fixed for the series; the frames use the claymation skill's lane 4 "Premium studio plasticine"
block verbatim, palette cream / terracotta / sage / deep ink / heart red. Note the skill's own advice (Nano Banana 2
for clay) does not apply: Atlas gpt-image-2 is the only allowed image model.

## Spend
Atlas: 1 image, about $0.047 (of the $1.00 cap). G-BUDGET planned $0.30.

## What the main session should record
Nothing yet: no G-HOOK, no G-SCRIPT, no G-HUMAN-SPINE. When the frame is downloadable: G-VIS on each frame (visual-reviewer,
after `vqa_crops.py`), overlay the text hook, then 2 fresh blind graders per round (persona card AV-01, the frame file,
the text, the spoken line).
