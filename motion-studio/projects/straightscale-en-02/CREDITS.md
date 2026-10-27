# Credits and licences: StraightScale · EN reel 02 "Your buyers already wrote your hooks"

Every third-party element in the delivered film, with its licence. Ship this with the delivery.

## Brand material
- StraightScale white wordmark (`assets/brand/wordmark-white.png`): the client's own file, identical to
  `clients/straightscale/brand/wordmark-white.png`. Shown at native proportions, never redrawn.

## Fonts
- Playfair Display, Montserrat: SIL Open Font License 1.1 (`assets/fonts/*/LICENSE.txt`), self-hosted.

## Quotes shown on screen
- Four short buyer sentences, verbatim, from public reviews, a Reddit comment and a newsletter, collected in the
  StraightScale research run (Oct 2026). No names, handles or company names are shown; each slip shows only the kind of
  source and the month (PROJECT.md, "Facts and quotes on screen").

## Music and sound
- Original score written for this film (`audio/score.py`), played with sampled instruments:
  - VSCO 2 Community Edition (Versilian Studios): pizzicato strings, strings, timpani, tambourine. CC0 1.0.
  - VCSL (Versilian Community Sample Library): marimba, vibraphone, harp, glockenspiel. CC0 1.0.
  - No Salamander piano and no MuldjordKit drums, so no CC BY credit line is required.
- Sampler and procedural foley code: Lemo-Opuscar `core/audio/sampler.py`, `sfx.py` (MIT), used as a library.

## Voice
- Kokoro-82M (kokoro-onnx v1.0, voice `af_heart`), generated offline (`audio/tts_kokoro.py`). Apache-2.0, commercial use
  allowed. Word timings: pocketsphinx forced alignment; Whisper base.en check, mean word match 0.923 (the misses are
  numerals written as digits and soundalikes: where/were, write/right).
- The house standard is ElevenLabs; the account's payment failed on 26 Oct 2026. A voice swap only needs a new
  `audio/vo.wav` and `words.json`; the film re-times itself.

## Images, footage, generated media
- None. Everything on screen is drawn in code or is the client's logo file. No AI images or video.

## Data shown on screen (source and date for every number)
- "567 buyer sentences collected": `06-VOC_MASTER.csv` of the research run, 567 quotes from 414 authors (Oct 2026).
  "Before our first video": the English page had posted no video when the research was done.
- "$15,000" is inside a buyer's quote (1-star review, Sep 2026), not a claim of ours.
- "Struggling with inconsistent lead generation?" is written by us as the example of a polished line, labelled
  POLISHED and struck out.
