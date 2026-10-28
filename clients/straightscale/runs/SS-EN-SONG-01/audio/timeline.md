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

## What is NOT measured yet (G-TIMELINE open)
- **Word timestamps.** Atlas CLI 0.1.38 returns only `text` for `xai/stt-v1` (`generate audio` and `generate get` alike,
  diarize on or off): no word or segment times reach the session. Atlas gap.
- **BPM, vocal stem, slices, voice-in time.** The masters live on `atlas-media.oss-us-west-1.aliyuncs.com`, which this
  environment's network policy refuses (403 on CONNECT), so the files can't be loaded for faster-whisper, librosa or a
  stem split. Known from step 4 (faster-whisper small.en, 27 Oct): O60 voice at 0.8 s, "lumpy months" by 1.5 s; O30
  voice at 0.0 s, by 1.1 s.

To close step 5: allow `atlas-media.oss-us-west-1.aliyuncs.com` in the environment's network settings (or a session
that can reach it), then faster-whisper word timestamps aligned to the lyrics, librosa BPM (prompt: 96), the vocal stem,
the line table with times and the slices (5 to 15 s, one per lip-sync sequence). Nothing in steps 6 and 7 needs the
times: Shot Specs carry line ids, and the look bible stills are timeless. Storyboards (step 8) and clips need them.

## Line table (line ids for the Shot Specs; times to come)
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

Planning pace for step 6 (an estimate from the lengths, not a measurement): O60 about 3.3 s a line, O30 about 2.9 s.
