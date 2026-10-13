# Review log: StraightScale · Reel 03 "Qartësia"

Every round is logged. Never ship with a known blemish without writing it here and telling the client.

## Round 0 · 2026-10-13 · styleframes
Sheets: `out/sf_a.png`, `out/sf_b.png`, `out/sf_c.png`, `out/sf_d.png`; reference: `docs/refs/ref_contact.png`

| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 8 | "Vëmendja" focus pull + brackets + crimson "kushton." by 0.8 s |
| Readability at phone size | 7 | safezone: 5 lines over the right edge (stopwatch line, "më të zhurmshme.", typed line) |
| Motion quality | 8 | focus pulls, spring pops; final adds subframe blur |
| Continuity | 8 | rack focus between beats, brackets recur |
| Variety and pacing | 8 | a new prop every 1-3 s, as the reference |
| Composition | 7 | marble discs read as stains; "?" marks fought the line; noise words touched "1.800" |
| Brand accuracy | 9 | ivory/crimson, Playfair italic + Montserrat (the brand pair maps onto the reference's serif + grotesk), real logo |
| Sound | n/a | |
| Message with the sound off | 8 | costs, losses, noise, clarity, offer read from the type |

Fixes: lighter discs and more thin crimson rings (closer to the reference's out-of-focus arcs); figures 1.3x;
"?" marks at 28% behind the line; a clear band around "1.800"; hexagon edge accents drawn on purpose; five lines
resized; `tools/safezone.mjs` learned a fine-print class (texture-only lines, 26 px floor, flagged in the page).

## Round 1 · 2026-10-13 · draft 1 (15 fps, `out/draft_av.mp4`)
Sheets: `out/contact.png`, `out/strip.png` (2.3), `out/phone.png`

| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 8 | as round 0 |
| Readability at phone size | 9 | safezone ok; phone sheet readable |
| Motion quality | 7 | 1.6-2.7 the stopwatch hand swept through "Sepse çdo sekondë" |
| Continuity | 9 | |
| Variety and pacing | 8 | pacing.py: 9% still, CV 0.56, spread 5.1x, longest quiet run 2.25 s, no frozen stretch |
| Composition | 8 | pill cloud starts left in its row (as in the reference) |
| Brand accuracy | 9 | |
| Sound | 8 | audio_qa: -14.0 LUFS, -1.5 dBTP, no dropouts, music 14.4 dB under the voice; low-mid WARN is the voice (as reel 02) |
| Message with the sound off | 8 | |

Automatic checks: seekcheck PASS; pacing PASS (5/5); safezone ok; audio_qa PASS except the voice-driven low-mid WARN.
Fixes: hand sweep ends at -0.46 pi and ticks 0.03 pi per word, so it stays left of the type (`out/r1_fix.png`);
one fine-print line reworded.

## Round 2 · 2026-10-13 · fix check before the final
Sheets: `out/r1_fix.png` (1.7-2.9 every 0.2 s)
Hand clear of the text in every frame; the rack focus from beat 1 to beat 2 reads as in the reference.
Open, logged: the reference's soft-focus feel relies on blur; the final's 4-subframe motion blur adds to it, but
there is no depth-of-field camera, only per-element blur.
