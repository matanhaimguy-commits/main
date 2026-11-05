# Credits and licences: StraightScale · Film 04 "One message, all the way"

## Reference (studied, not used)
- Instagram reel by satisfy3dverse (https://www.instagram.com/p/DdG2I51BjOj/, posted 10 Sep 2026, 109M plays), from
  the studio's reference bank card `refbank/cards/ig-satisfy3dverse.md`. Studied for grammar only (one hero object
  triggers every sound, follow-cam, set pieces changing, last frame = first frame). No footage, frames, audio, track,
  lettering or design from it is in this film; every element is drawn in code.

## Brand material
- StraightScale full logo `assets/brand/logo-full.png` (2067x761, transparent PNG): the owner's own file (copied from
  `projects/straightscale-03/assets/brand/`, originally the user's Google Drive, 5 Oct 2026). Used as the file, only
  scaled and composited onto an ivory plate in a niche on the wall, behind two marble doors that slide over it (a mask);
  never redrawn, traced or recoloured (v2).

## Fonts (self-hosted, `assets/fonts/`)
- Playfair Display 700, 700 italic, 900 italic: SIL Open Font License 1.1 (Copyright 2017 The Playfair Display
  Project Authors). Licence file: `assets/fonts/PlayfairDisplay/LICENSE.txt`.
- Montserrat 600, 700, 800: SIL Open Font License 1.1 (Copyright 2011 The Montserrat Project Authors). Licence file:
  `assets/fonts/Montserrat/LICENSE.txt`.

## Music and sound
- Original score, written for this film in `audio/score.py` (every contact of the ball is a note). Played with
  sampled instruments from:
  - VS Chamber Orchestra: Community Edition (Versilian Studios), CC0 1.0: violins, violas, cellos (section sustains),
    contrabass pizzicato, timpani.
  - Versilian Community Sample Library (Versilian Studios), CC0 1.0: marimba, xylophone, glockenspiel, vibraphone
    (soft mallets and bowed), tubular bells, concert harp, cajon, claps, hi-hat, small shaker.
  - CC0 needs no attribution; listed with thanks. No Salamander piano (CC BY 3.0) and no MuldjordKit drums
    (CC BY 4.0) are used, so no CC BY credit line is required.
- Instruments used (from the score's own list, `audio/instruments_used.txt`): cajon, cellos, claps,
  contrabass_pizz, glockenspiel, harp, hihat, marimba, shaker, timpani, tubular_bells, vibraphone, vibraphone_bowed,
  violas, violins, xylophone.
- Sound effects: synthesized in code (Lemo-Opuscar `core/audio/sfx.py`: click, clack, whoosh, thump; plus a band-passed
  noise roll for the tube and, in v2, a band-passed noise slide for the hatch doors), placed from the film's own event
  times (`audio/events.json`). The room tone under the planned silence (v2) is filtered noise generated in
  `audio/mix.py`.
- Sampler, foley and room code: Lemo-Opuscar `core/audio/sampler.py`, `sfx.py` (MIT), used as a library from `~/lemo`.

## Voice
- None (no voiceover in this film).

## Images, footage, generated media
- None. No AI images, video or audio; no paid generation (0 credits, 0 minutes; v1 and v2). Marble, plates, pegs, ball,
  tube, hatch, shaft and light are drawn procedurally in `index.html`.

## Code
- motion-studio canvas engine (`render.mjs`, `lib/motion.js`, `stills.mjs`, `tools/`): our own.

## Data shown on screen
- None. No numbers, results, client names, reviews, prices, discounts, guarantees or deadlines. Station names are the
  steps of a client's path; sub-labels ("instant answer", "follow-up", "rebooking") are Build items from
  `clients/straightscale/brand-kit.md`.
