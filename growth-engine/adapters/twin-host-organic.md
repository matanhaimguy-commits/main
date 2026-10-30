# Twin host, organic adapter

For `reel_twin_stage` (the founder's HeyGen twin hosts a designed stage edit), and for the twin as the presenter in
`reel_whiteboard` and `reel_strategist_prop` (FORMATS.md 2.18, `presenter_identities`). Pass this file, the Post Card,
`growth-engine/production/STANDARDS.md` and `adapters/ugc-talking-head-organic.md` (the pipeline shape it follows).
Where they disagree, this file and STANDARDS.md win for twin cards.

## 1. Who is on screen (truth rules first)
- **Only a card marked `twin_host: true`, only for a brain with a `host` block** (looks, voices; today
  `clients/straightscale-en`). `organic.py card-check` refuses a twin card without the flag, a flag without the block,
  and any card that casts the owner's twin without the flag (`card_people.py`). The router never offers
  `reel_twin_stage` otherwise, and a slot is re-routed to the twin only where it ranks first with the flag on
  (`organic.py route` prints that line); take it only with a written reason in the card's `notes`.
- **The twin speaks as Matan, the founder, in his cloned voice** (D-T1, D-T2). The AI label is whatever the brain's
  `visual.ai_label` says (off on @straightscale_, D-T3); the hub notes say "AI label: off" or "AI label: on".
- **STANDARDS 7, the twin rule, stays:** the twin never claims a result, number or client that is not in the proof
  bank; no invented anecdote (a story is framed "POV: ...", never as fact); no price, guarantee, urgency or "we answer
  within an hour"; never plays a client or customer; not "I tried this and got X" unless that result is a proof-bank
  entry with permission `yes`. Screens and graphics show states, never counts or a platform's name (STANDARDS 6).
- The edit never covers the face's meaning: no graphic over the eyes or mouth, and the twin stays on screen 50% or less.

## 2. The pipeline, steps 0 to 15
Steps follow `AI-VIDEO-PIPELINE.md`. Anything not changed here is as in the UGC adapter.

| Step | What (twin changes in bold) | Gate |
|---|---|---|
| 0 | Brief from the brain and the `host` block: looks, voices, `speaks_as`. Confirm the card has `twin_host: true` | G-BRIEF |
| 1 | THE PICTURE: the one set, UI or prop the whole edit hangs on; the hook's frame 1 is a real concept frame | G-IDEA |
| 2 | Hook Lab; passes only the twin hook rule (2 anchors, packet-v2; `hook-lab-organic.md`) | G-HOOK |
| 3 | Script Lab O30 or O60 (`script-lab-organic.md`), spoken by the founder, in his words. **Release the script, then pin its exact text: G-SCRIPT PASS with `--data '{"script_sha256": "<sha256 of the text>"}'`** | G-SCRIPT 85+, G-HUMAN-SPINE (delegated) |
| 4 | **Voice first: `pipeline.py budget <slug> <post> --planned USD --balance USD --heygen CREDITS`, then `create_speech` with a voice id from `host.voices` and exactly the pinned text** (no `engine`, `settings`, `forceRegenerate`). Register the result with `pipeline.py media ... VO@v<n> --id <audio URL or asset id>`, then G-AUDIO PASS on it | G-BUDGET, G-AUDIO-MASTER, G-HUMAN-VOICE (once per voice, Matan only), G-AUDIO |
| 5 | Word timings from the voice with `xai/stt-v1` on Atlas; slices and the beat clock | G-TIMELINE |
| 6 | **Beat sheet**: a visual change every 2 to 3 s in layers A to E (set, B-roll and UI, words, twin, hero words and captions); one hero move per beat; mark which beats show the twin | G-PLAN, G-SPEC |
| 7 | **Set bible**: the signature set (one GPT Image 2 still, quality medium on Atlas, about $0.06) and the UI scenes; the twin's look is already HeyGen's, there is no portrait to generate | G-PROMPT-IMG, G-VIS-SHEET, G-HUMAN-LOOK (once, delegable) |
| 8 | Storyboard of the hook beats; hook board | G-VIS-BOARD, G-CONTINUITY, G-HUMAN-HOOKBOARD |
| 9 | **Re-price the whole piece** (Atlas USD for the set and B-roll, HeyGen credits for the voice and the twin clip); close step 9. The gate refuses every video call before it | G-BUDGET |
| 10 | **A-roll: `create_video_from_avatar`, audio-driven only.** `pipeline.py asset <slug> <post> AROLL --type video_clip --shots <S..> --tool mcp__HeyGen__create_video_from_avatar`, `pipeline.py prompt ... AROLL --file <one-line note> --media <the voice id>:audio`; a look id from `host.looks`; `aspectRatio` `9:16`; `fit` `cover` for the landscape look; the voice's `audioUrl` or `audioAssetId` and nothing else (no script text, voice, motion prompt, captions, background, background removal, webm, 4k). Run `pipeline.py check-call --explain <tool> <input.json>` first. B-roll: H3 keyframe clips on Atlas, within the balance | G-PROMPT-VID |
| 11 | Per-take QA of the A-roll: frames 1 per second, lip drift against the voice, word check, face crops (landscape look: the crop must keep the face centred), hands | G-TAKE, G-ASSETS |
| 12 | **Edit with the twin kit** (section 4) | G-MOTION-TEXT before render, G-MOTION-FRAMES |
| 13 | Final QA: sound-off watch, transcript, loudness -14 LUFS, safe zones, pacing (a change every 2 to 3 s, nothing held over 3 s), truth check against the proof bank | G-FINAL, G-DIRECTOR |
| 14 | Hub draft: caption, keyword, "AI label: off" or "on" per the brain, HeyGen credits and Atlas USD in the notes. Never post | G-HUMAN-FINAL (Matan only) |
| 15 | Learn: 72 h and 7 d results into the scorecard; log the measured HeyGen credits per second so the estimates stop being guesses | analyst |

## 3. The HeyGen route (the only one)
Only `mcp__HeyGen__create_speech` and `mcp__HeyGen__create_video_from_avatar` open, service `heygen_twin`
(STANDARDS 10, `standards.json` `models.heygen`). The order is fixed, as in `.claude/agents/video-producer.md`:
budget with `--heygen`, voice (G-SCRIPT with `script_sha256`), register and G-AUDIO PASS, then the audio-driven clip,
then `organic.py ledger-add ... --heygen <credits charged>`. Every other HeyGen tool, the heygen CLI, direct HTTP calls
to HeyGen and the media-use audio scripts are denied. A session never adds a voice or look: the brain's `host` block is
the allowlist and changes only with Matan.

## 4. The edit: the twin kit
The edit is the twin kit in `motion-studio/twin-kit` (branch `claude/twin-edit-kit`, may not be merged yet: read its
`README.md` for the composer command and the six moves; if the folder is missing, ask the main session, do not hand-build
an edit). The kit cuts the twin out, lays the layers back to front, places the sound effects on every move, ducks the
music under the voice and loudness-normalises. Rules it enforces and this adapter relies on: one hero move per beat,
readable in under 1 s, a sound on every move, a visual change every 2 to 3 s, the twin on screen 50% or less.

## 5. The traps
- **A landscape look in 9:16 needs a cover fit.** The landscape twin (1280x720) is 16:9; set `fit: cover` on the call,
  then check the crop keeps the face and hands inside 9:16. `contain` leaves bars and fails the safe zones. The portrait
  photo look is native 9:16 and needs no fit; the pilot compares both and a fresh reviewer picks.
- **Contain vs cover at the edit.** Compose the twin cutout at its cover-fitted size; never scale a `contain` clip up to
  fill the frame (soft face, wrong crop).
- **Render time.** HeyGen renders take minutes; poll `get_video`, never recreate to poll, and ask before retrying an
  error (check an unknown outcome first, because a retry is a second charge).
- **The cutout is slow.** Background removal (`hyperframes remove-background`) costs about 25 minutes of CPU per twin
  minute. Cut out only the beats where the twin is on screen with a layer behind or around it, never the whole reel,
  and reuse a cutout for repeated camera angles.
- **No unplanned credits.** No 4k, no HeyGen-side background removal, no second voice take without a new G-BUDGET; the
  gate refuses them anyway.
- **Words over the face.** Words that orbit or sit behind the head must clear the eyes and mouth in every frame; check
  the contact sheet at beats, not only at the cut points.

## 6. Close and copy
One organic CTA that fits the card's job (`script-lab-organic.md`): follow, save, send, comment, keyword (only one live
in the brain) or dm. No link, price, discount, guarantee or urgency. HeyGen credits are unmeasured until the pilot reel
(`organic.json` `heygen_credits_status`); budget what the pilot recorded once it exists.
