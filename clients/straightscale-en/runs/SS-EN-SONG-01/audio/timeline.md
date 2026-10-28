# SS-EN-SONG-01 · step 5 audio timeline (28 Oct 2026, EN 03 production session)

Masters (G-HUMAN-SONG PASS, Matan, 28 Oct 17:12 UTC), Atlas `suno/chirp-v6` output index 1 (take 2) of each prediction,
URLs registered on the assets (`pipeline.py media ... --id`):
- SONG-O60@v1: prediction `8f0741beaf4346989948dbc2cecbd25d`, take 2, 59.6 s
- SONG-O30@v1: prediction `298342acc20f468497b7dd16efe3ef1a`, take 2, 32.4 s

## What was measured here: lyric match on Atlas `xai/stt-v1`
Raw output: `stt/SONG-O60.xai-stt.json`, `stt/SONG-O30.xai-stt.json` (language en; O30 with diarize). Word match to the
FINAL lyrics (`docs/lyrics.md`), difflib on words:

| Master | Lyric words | Heard | Match | Differences (lyric -> heard) |
|---|---|---|---|---|
| O60 | 183 | 183 | 0.951 | "patched on alone" -> "on her lawn"; "her posts" -> "her post"; "ads went last" -> "ads won't last"; "that cloth" -> "the cloth"; "no scrap sewn" -> "no scraps sewn"; "filled her March" -> "filled in March" |
| O30 | 105 | 106 | 0.910 | "patched on alone. That's" -> "on a loan. As"; "then ads last" -> "then as last"; "posts" -> "post" (x2); "worked" -> "works" |

Every scripted line is heard in order, the spoken question and the CTA included; both over the 0.88 floor and in line
with the step 4 faster-whisper check (0.956 / 0.896). Caption the sung words, and set these in bold so a misheard
word can't change the meaning: **ALONE**, **ADS LAST** (O30) / **ADS WENT LAST** (O60), **THAT CLOTH**, **POSTS**.

## Step 5 measured (28 Oct 2026, EN 03 production session 2): G-TIMELINE
Masters downloaded to `masters/` (kept out of git, see `.gitignore`), then `growth-engine/tools/song_timeline.py`:
- **Word timings** (`words.json`): forced alignment of the line table's words to each master with pocketsphinx (its
  bundled en-us model). faster-whisper could not run here: its model host (huggingface.co) is refused by this
  environment's network policy, so the words are placed, not recognised; the lyric match itself stays the STT one above
  (0.951 / 0.910) and the step 4 faster-whisper check (0.956 / 0.896). Every lyric word aligned in order, both masters.
- **Beat grid** (`timeline.json`): librosa beat_track (same method as `motion-studio/beats.py`).
- **Vocal stem**: not made (Demucs weights sit on blocked hosts); not needed before step 10.
- **Slices**: planned as times (whole lines, 5 to 15 s, cuts on a beat inside the gap between lines); the files are
  cut at step 10 only for a shot that needs an audio reference, each with its own G-AUDIO.

| Master | BPM (measured) | Length | Voice in | Lines | Slices |
|---|---|---|---|---|---|
| O60 | 97.0 | 59.57 s | 0.92 s | 18 | 6 |
| O30 | 85.2 | 32.37 s | 0.36 s | 11 | 3 |

BPM note: the prompt asked 96; O60 measures 97, O30 85 (librosa can halve or misread a soft folk groove; cut on the
`beats` list in `timeline.json`, not on a computed grid).

### Line times (seconds)

O60:
| Line | Start | End | Length |
|---|---|---|---|
| O60-L01 | 0.92 | 3.59 | 2.67 |
| O60-L02 | 3.59 | 6.09 | 2.5 |
| O60-L03 | 6.09 | 8.55 | 2.46 |
| O60-L04 | 8.55 | 10.8 | 2.25 |
| O60-L05 | 10.8 | 13.55 | 2.75 |
| O60-L06 | 13.55 | 16.33 | 2.78 |
| O60-L07 | 17.26 | 20.79 | 3.53 |
| O60-L08 | 21.5 | 23.47 | 1.97 |
| O60-L09 | 23.87 | 29.18 | 5.31 |
| O60-L10 | 29.18 | 32.12 | 2.94 |
| O60-L11 | 32.12 | 34.53 | 2.41 |
| O60-L12 | 34.74 | 37.25 | 2.51 |
| O60-L13 | 37.25 | 39.75 | 2.5 |
| O60-L14 | 39.75 | 42.08 | 2.33 |
| O60-L15 | 42.08 | 44.74 | 2.66 |
| O60-L16 | 45.02 | 49.52 | 4.5 |
| O60-L17 | 49.52 | 54.01 | 4.49 |
| O60-L18 | 55.14 | 58.66 | 3.52 |

| Slice | Start | End | Length | Lines |
|---|---|---|---|---|
| O60-S01 | 0.0 | 8.55 | 8.55 | O60-L01 to O60-L03 |
| O60-S02 | 8.55 | 21.34 | 12.79 | O60-L04 to O60-L07 |
| O60-S03 | 21.34 | 32.12 | 10.78 | O60-L08 to O60-L10 |
| O60-S04 | 32.12 | 42.08 | 9.96 | O60-L11 to O60-L14 |
| O60-S05 | 42.08 | 54.37 | 12.29 | O60-L15 to O60-L17 |
| O60-S06 | 54.37 | 59.57 | 5.2 | O60-L18 to O60-L18 |

O30:
| Line | Start | End | Length |
|---|---|---|---|
| O30-L01 | 0.36 | 3.22 | 2.86 |
| O30-L02 | 3.22 | 6.94 | 3.72 |
| O30-L03 | 6.94 | 9.32 | 2.38 |
| O30-L04 | 10.48 | 13.67 | 3.19 |
| O30-L05 | 13.67 | 16.68 | 3.01 |
| O30-L06 | 16.68 | 19.43 | 2.75 |
| O30-L07 | 19.43 | 20.74 | 1.31 |
| O30-L08 | 20.74 | 22.24 | 1.5 |
| O30-L09 | 22.24 | 25.12 | 2.88 |
| O30-L10 | 25.12 | 27.87 | 2.75 |
| O30-L11 | 29.02 | 32.37 | 3.35 |

| Slice | Start | End | Length | Lines |
|---|---|---|---|---|
| O30-S01 | 0.0 | 9.69 | 9.69 | O30-L01 to O30-L03 |
| O30-S02 | 9.69 | 19.43 | 9.74 | O30-L04 to O30-L06 |
| O30-S03 | 19.43 | 32.37 | 12.94 | O30-L07 to O30-L11 |

## Line table (line ids for the Shot Specs; times above)
O60 (song order, FINAL lyrics):
| Id | Section | Words |
|---|---|---|
| O60-L01 | Verse 1 | Lumpy months? It was never where your clients came from, |
| O60-L02 | Verse 1 | take Maya, a consultant: referrals filled her March, |
| O60-L03 | Verse 1 | then April went quiet, she'd been too busy in March |
| O60-L04 | Verse 1 | to look for April's clients while the work was coming in. |
| O60-L05 | Verse 1 | So she tried some fixes: cold email, LinkedIn, |
| O60-L06 | Verse 1 | a coach and then some ads, and each held a month, then came loose. |
| O60-L07 | Spoken | A friend who'd had lumpy months too asked her: "Are your fixes connected?" |
| O60-L08 | Pre-chorus | They weren't: just scraps, each one patched on alone, |
| O60-L09 | Chorus | that's patchwork marketing: no scrap is sewn to the next. |
| O60-L10 | Chorus | Steady months don't need one more scrap sewn on, |
| O60-L11 | Chorus | just one cloth to cut every piece from. |
| O60-L12 | Verse 2 | That cloth is the words her buyers use for their problem: |
| O60-L13 | Verse 2 | her offer came from those words, her posts came from that offer, |
| O60-L14 | Verse 2 | and ads went last, only on the posts that worked, |
| O60-L15 | Verse 2 | so those posts kept finding buyers while she was busy. |
| O60-L16 | Outro | Next April wasn't as full as March, but nothing came loose. |
| O60-L17 | Outro | No more patchwork marketing, no scrap sewn on alone. |
| O60-L18 | Spoken | Follow for part two: where to find your buyers' words. |

O30:
| Id | Section | Words |
|---|---|---|
| O30-L01 | Verse | Lumpy months? It was never where your clients came from, |
| O30-L02 | Verse | posts, emails, a coach, some ads: each held a month, then came loose, |
| O30-L03 | Verse | 'cause each was a scrap, patched on alone. |
| O30-L04 | Chorus | That's patchwork marketing: no scrap is sewn to the next. |
| O30-L05 | Chorus | Not one more scrap: one cloth to cut every piece from, |
| O30-L06 | Chorus | and that cloth is the words your buyers use for their problem. |
| O30-L07 | Chorus | Make the offer from their words, |
| O30-L08 | Chorus | then make the posts from the offer, |
| O30-L09 | Chorus | then ads last, only on the posts that worked, |
| O30-L10 | Chorus | so those posts keep finding buyers while you're busy. |
| O30-L11 | Spoken | Follow for part two: where to find your buyers' words. |

