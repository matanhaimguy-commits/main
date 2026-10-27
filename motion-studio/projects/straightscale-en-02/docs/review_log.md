# Review log: StraightScale · EN reel 02 "Your buyers already wrote your hooks"

## Round 1 · 27 Oct 2026 · first full build
Sheet: `out/sheet1.png`
| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 7 | the buyer's sentence is on screen from frame 0 and the highlighter follows the voice; the slip sits high and the lower half is empty for 4.5 s |
| Readability at phone size | 7 | quotes 60-72 px Playfair; the stamp text was 34 px |
| Motion quality | 8 | slips slide on springs; highlights sweep word by word |
| Continuity | 8 | the hook slip shrinks, the three sources fan in behind it, then come forward one by one |
| Variety and pacing | 8 | |
| Composition | 6 | empty lower half in the hook; the stamp ran off the slip and off the frame; at 32.5 s the polish cards and the 567 card overlapped |
| Brand accuracy | 9 | ivory, charcoal, gold highlighter, red only for the strike |
| Sound | n/a | |
| Message with the sound off | 8 | the quote, the source tags and the captions carry it |
Fixes: hook slip centred and 1.08x with a gold quote mark above it; stamp "BUYER'S WORDS" inside the slip at 52 px; the 567 count starts on "We collected" and the polish cards leave before it; the wall dims to 12% under the CTA.

## Round 2 · 27 Oct 2026 · after fixes
Sheets: `out/sheet2.png`, `out/sheet3.png`
| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 8 | quote mark, slip, highlighter sweeping as the words are spoken |
| Readability at phone size | 8 | every resting text 44 px or more |
| Motion quality | 8 | |
| Continuity | 8 | |
| Variety and pacing | 8 | |
| Composition | 8 | |
| Brand accuracy | 9 | |
| Sound | n/a | |
| Message with the sound off | 8 | |
Also fixed: a long caption row ("1. Your competitors' worst reviews:") now shrinks to fit 800 px; slips parked off frame are no longer drawn.

## Round 3 · 27 Oct 2026 · final render v1 (60 fps, mixed)
Sheets: `out/contact.png`, `out/phone.png`, `out/strip.png`, `out/spectrum.png`
| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 8 | |
| Readability at phone size | 8 | `out/phone.png` |
| Motion quality | 8 | 4-subframe motion blur; seams at 14 s and 28 s match their neighbouring frames |
| Continuity | 8 | |
| Variety and pacing | 8 | pacing.py: 35% still, longest quiet run 1.75 s, rhythm CV 0.72, spread 22.6x |
| Composition | 8 | |
| Brand accuracy | 9 | |
| Sound | 8 | -14.1 LUFS, true peak -1.5 dBTP; music 13.7 dB under the voice; a stop before the reveal, the resolve when 567 lands, a cadence on the logo. Nobody has listened yet |
| Message with the sound off | 8 | |

Automatic checks:
- `tools/seekcheck.mjs`: PASS.
- `tools/safezone.mjs`: no flags while any text is at rest; the remaining flags are slips mid-slide (entering from or leaving past the frame edge) and the small preview fan (texture-size, marked fine).
- `tools/pacing.py`: PASS on all five checks.
- `tools/audio_qa.py`: loudness, true peak, dropouts and voice-to-music gap PASS. WARN low-mid energy at 0.0, 3.5, 8.0, 10.0, 15.5, 17.5, 24.0, 24.5, 25.5, 36.0 s: the voice stem alone trips it at most of these times; the music stem's own flags sit at chord changes, 13.7 dB under the voice.

Known and told to the owner:
- Voice is Kokoro (offline), not ElevenLabs (payment failed). Whisper heard every word; the misses are digits and soundalikes.
- Nobody has listened to the mix.
- The CTA resource ("the exact searches we use") and its hub funnel for WORDS don't exist yet: build both before posting.
