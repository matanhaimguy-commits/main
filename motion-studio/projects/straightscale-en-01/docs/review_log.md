# Review log: StraightScale · EN reel 01 "The step after the reply"

Every round is logged. Never ship with a known blemish without writing it here and telling the client.

## Round 1 · 26 Oct 2026 · first full build (styleframes = every beat)
Sheet: `out/sheet1.png` (48 frames, every 0.9 s)

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 6 | the text is there by frame 0, but the stage and figures are too small to stop a thumb |
| Readability at phone size | 5 | figures 77 px tall, ledger and plank numbers tiny; the 59-owner grid reads as dashes (4.8-8.2) |
| Motion quality | 7 | walks, falls and springs work; the counter starts at 0 before anyone arrives (0-0.5) |
| Continuity | 7 | the path survives every beat |
| Variety and pacing | 7 | something changes every 0.5-1.5 s |
| Composition | 4 | lower half empty; the reply counter collides with PROSPECT MORE (9.3); bubble 3 and the CTA list overlap the LinkedIn pill (33.6, 38.1); two captions overlap at each hand-off (25.5) |
| Brand accuracy | 8 | real wordmark, brand palette and fonts |
| Sound | n/a | not built yet |
| Message clear with the sound off | 7 | captions carry it |

Three worst problems and the fix for each:
1. Stage too small and frame half empty: path moved to y 1340, figures 1.6x, text in three zones (captions 380-500, information 600-1020, stage 1340).
2. Collisions: one centred column at most 800 px wide (inside the right UI zone); the reply count sits beside the pill; bubbles sized to their text.
3. Caption overlap: hard cuts inside a line, and a line's last chunk never outlives the next line's first.

## Round 2 · 26 Oct 2026 · rebuilt layout
Sheets: `out/sheet2.png`, `out/sheet3.png`, `out/sheet4.png`, `out/strip_fast.png`, `out/zoom.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | "3 clients in March." + a March … 3 scoreboard counting 1-2-3 on "three clients", flips to April … 0 as the path breaks (0-2.9) |
| Readability at phone size | 8 | all text 44 px or more (safezone.mjs), checked at 360 px wide (`out/phone.png`) |
| Motion quality | 8 | one push only (1.06, 14.4-17); numerals fly onto the planks (17.3-18.6); the count climbs, then falls to 0 as replies drop |
| Continuity | 8 | the path, the channel pill and the figures carry every beat; the small reply count grows into the big one |
| Variety and pacing | 8 | pacing.py: rhythm CV 0.81, spread 16x, longest quiet run 1.58 s, nothing frozen |
| Composition | 8 | the middle zone is filled in every beat (scoreboard, grid, tags, count, numerals, ledger, bubbles, CTA, close) |
| Brand accuracy | 9 | palette roles held: red only for the leak, gold for people and key numbers |
| Sound | n/a | |
| Message clear with the sound off | 8 | captions plus the path: replies arrive, fall in the gap, three planks close it, people cross |

Fixes made this round: the middle-zone gaps in lines 4-6 and the close (big reply count, big numerals, close moved
to the middle); the grid became 12 x 5 with clear rows; the counter stays inside the safe zone through the push.

## Round 3 · 26 Oct 2026 · final render v1 (60 fps, mixed and mastered)
Sheets: `out/contact.png`, `out/phone.png`, `out/strip.png`, `out/fix_check.png`, `out/fix_check2.png`, `out/spectrum.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | as round 2 |
| Readability at phone size | 8 | `out/phone.png` |
| Motion quality | 8 | 4-subframe motion blur; seams at 14.5 and 29 s invisible (frame differences at the seam match their neighbours) |
| Continuity | 8 | |
| Variety and pacing | 8 | |
| Composition | 8 | after the fixes below |
| Brand accuracy | 9 | |
| Sound | 8 | -14.0 LUFS, true peak -1.4 dBTP after AAC; music 15.6 dB under the voice while it speaks; accents placed from the film's events; a real cadence on the logo. Nobody has listened yet |
| Message clear with the sound off | 8 | |

Found on the rendered file and fixed (full re-render):
1. 11.2-11.6 s: the reply count grew into the middle while PROSPECT MORE was still fading; the tags now clear by 11.26 s and the count rises before it slides left.
2. A faint ring around the centre of every frame from the vignette's linear ramp: replaced by a smoothstep falloff.

Automatic checks (final source):
- `tools/seekcheck.mjs`: PASS (24 revisits, every 0.1 s).
- `tools/safezone.mjs`: one flag by design: "April" during the 0.16 s squash-flip at 1.8 s (the word is mid-flip, its height passes under 44 px).
- `tools/pacing.py` (draft 15 fps): PASS on rests, frozen stretches, rhythm variety and spread.
- `tools/audio_qa.py`: loudness and true peak PASS; voice-to-music gap PASS; dropouts none. WARN low-mid energy at 0.0, 3.0, 8.0, 16.5, 20.0, 28.5, 30.5, 33.5, 37.5, 40.5 s: the voice stem alone trips it at the same times (the female voice's fundamental sits at 180-250 Hz); in the music stem the flags are the two deliberate low drones (April 2-4 s, the leak 15-17 s), 15 dB under the voice.

Known and told to the client:
- The voice is Kokoro (offline), not ElevenLabs: the ElevenLabs account's payment failed. Whisper heard every word (mean 0.956), but a human should listen once.
- Nobody has listened to the mix; it was measured only.
