# Atlas model tests (session F2, 28 Oct 2026)

Matan's decisions of 28 Oct (about 17:52 UTC, `FORMATS.md` 5). Every test asset carries G-HUMAN-TEST with his words.
Spend: $6.71 before, $2.41 after (about $4.30).

| Test | Assets | Spend | Result | Review |
|---|---|---|---|---|
| F9 download | the Chris audition mp3 | $0 | HTTP 200, plays (13.0 s): Atlas media downloads work | |
| Slice and face | SLICE-CHRIS (ElevenLabs v3 on Atlas, 8.2 s, 25/25 words), T-FACE (gpt-image-2 medium) | about $0.06 | | |
| F2 lip-sync | T-H3-768 | $0.24 | PARTIAL: synced 0 to 4.2 s, then H3 voices its own garbled words | `qa/take-review-T-H3-768.json`, `qa/drift-T-H3-768.json`, `qa/stt-T-H3-768.json` |
| F1 resolution | T-H3-768, T-H3-1440, T-H3-2K | $1.75 | phone size 6 / 7 / 7.5; recommend `1440p-sr` | `qa/f1-review.json`, `qa/f1-compare/` |
| F3 beds | T-BED-A, T-BED-B (`minimax/music-3.0`, instrumental) | $0.30 | no vocals (xai/stt-v1); A steady 10 to 50 s, B steady throughout | Matan's ears: Studio decision #3 |
| F6 sheets | T-SHEET-*, T-BOARD-* (4 styles x 2 models) | about $1.65 | Nano Banana 2 wins 3D and 2D; gpt-image-2 wins clay and crochet | `qa/f6-review-*.json`, `qa/f6/` |

The Studio run is #6. Decision #3 (`studio-decision.json`) asks for the resolution and the beds in one question. The hub
storage host was blocked, so only Atlas URLs were pushed.
