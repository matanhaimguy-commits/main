# Credits and licences: StraightScale · EN reel 01 "The step after the reply"

Every third-party element in the delivered film, with its licence. Ship this with the delivery.

## Brand material
- StraightScale white wordmark (`assets/brand/wordmark-white.png`): the client's own file, identical to
  `clients/straightscale/brand/wordmark-white.png` in this repo. Shown at native proportions, never redrawn.

## Fonts
- Playfair Display, Montserrat: SIL Open Font License 1.1 (`assets/fonts/*/LICENSE.txt`), self-hosted.

## Music and sound
- Original score written for this film (`audio/score.py`), played with sampled instruments:
  - VSCO 2 Community Edition (Versilian Studios): upright piano, strings, pizzicato, timpani, tambourine. CC0 1.0.
  - VCSL (Versilian Community Sample Library): marimba, vibraphone, harp, glockenspiel. CC0 1.0.
  - No Salamander piano and no MuldjordKit drums were used, so no CC BY credit line is required.
- Sampler and procedural foley code: Lemo-Opuscar `core/audio/sampler.py`, `sfx.py` (MIT), used as a library.

## Voice
- Kokoro-82M (kokoro-onnx v1.0 model, voice `af_heart`), generated offline (`audio/tts_kokoro.py`). Model and voices:
  Apache-2.0, commercial use allowed. Word timings: pocketsphinx forced alignment (`audio/align_words.py`), checked
  with Whisper base.en (`audio/asr_check.py`, mean word match 0.956).
- Note: the house standard for client voice is ElevenLabs; the account's payment failed on 26 Oct 2026, so this
  version uses Kokoro. Swapping the voice later only needs a new `audio/vo.wav` and `words.json`; the film re-times
  itself from them.

## Images, footage, generated media
- None. Everything on screen is drawn in code or is the client's logo file. No AI images or video.

## Code and effects
- motion-studio canvas engine (`render.mjs`, `lib/motion.js`): our own.

## Data shown on screen (source and date for every number)
- "59 owners in our research describe this exact cycle": StraightScale research run, `06-VOC-REPORT.md` PP-02
  (feast and famine), 59 distinct authors (11 review, 48 organic), run of Oct 2026.
- "3 clients in March / 0 in April": a "you" scenario built from buyer words ("some months 3 clients, other months
  literally nothing", `11-BELIEFS.md` AV-01). Not a claim about anyone.
- The six-month table (replies 8,9,8,9,8,9; clients 3,1,0,3,0,2) and the message bubbles are labelled EXAMPLE on screen.
- The reply counter (up to 9) is an illustration of replies arriving, not a statistic.
- The five message names on the CTA card are the real titles in "The 5 leak-plug messages" resource
  (claude.ai/artifact/7hi7btY2uZA9J465Dy8xkz).
