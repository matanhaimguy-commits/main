# EDL · The 22:47 race (S60) · master time, 24 fps, 1080x1920

The ElevenLabs voice master (`vo_master.wav`, 60.0 s) is the timeline. Beats start at 0.00 (L1-L5), 18.94 (L6-L9),
31.51 (L10-L13) and 45.54 (L14-L16, strategist on camera). Speech ends at 58.26.

## Picture (build/compose.py)

| # | Master | Source | Move / look | Voice over it |
|---|---|---|---|---|
| 1 | 0.00-4.05 | k1 Elira on the sofa, from 0.00 | push 1.00 to 1.07 | L1 "She just sent..." |
| 2 | 4.05-5.30 | k2 owner 1 asleep, phone buzzing, from 0.45 | push 1.04 to 1.10 | L2 "One owner is asleep." |
| 3 | 5.30-6.45 | k3 owner 2 at dinner, from 0.90 | push 1.04 to 1.10 | "One is at dinner." |
| 4 | 6.45-11.55 | k4 owner 3 asleep, phone lights up, from 0.30 | slowed 1.047x, push 1.00 to 1.22 toward the phone | L3 |
| 5 | 11.55-13.40 | k5 Elira relieved, from 0.40 | push 1.02 to 1.08 | L4 "She books with him..." |
| 6 | 13.40-15.25 | k6 owner 1 next morning, from 0.20 | push 1.02 to 1.08 | "The other two answer in the morning." |
| 7 | 15.25-18.90 | k1 from 1.20 | blurred and darkened under the race graphic | L5 |
| 8 | 18.90-21.25 | k7 laser owner at work, gloves, from 0.60 | push 1.00 to 1.07 | L6 |
| 9 | 21.25-22.45 | k2 from 2.60 | push 1.06 to 1.12 | "or asleep" |
| 10 | 22.45-25.95 | k8 owner filming a post, from 0.30 | push 1.00 to 1.08 | L7 |
| 11 | 25.95-31.40 | k4 from 0.00 | slowed 1.06x, push 1.00 to 1.60 into the phone | L8, L9 |
| 12 | 31.40-40.05 | k4 from 0.00 | slowed 1.7x, heavy blur, under the phone chat | L10, L11 |
| 13 | 40.05-45.54 | k10 owner 3 reads the alert, smiles | slowed 1.063x; covered by the brand beat 42.6-45.6 | L12, L13 |
| 14 | 45.54-60.00 | t1b strategist on a night street (lip-synced) | push 1.00 to 1.04, clip audio muted, last frame held 0.08 s | L14-L16 |

## Overlay (overlay/overlay.js, rendered with overlay/render.mjs)

| Master | Element |
|---|---|
| 0.00-3.75 | Super "Ajo nuk pyeti vetëm ty për çmimin." (She didn't ask only you about the price.) |
| 0.30 / 0.90 / 1.50 | Three "Sa kushton?" bubbles fly from her phone to a tooth, scissors and laser chip |
| 4.05-11.5 | Clock chip "22:47" |
| 8.15-11.6 | Reply bubble "Përshëndetje! Ja çmimi dhe oraret e lira 👇" (Hi! Here's the price and the free slots) |
| 9.2-11.5 | Super "Përgjigje brenda 1 minute" (Reply within 1 minute) |
| 12.0-13.4 | Chip "✓ Rezervuar" (Booked) |
| 13.45-15.2 | Clock chip "07:10" |
| 15.25-18.95 | Race: 07:10, 08:30, 22:47 ✓ Rezervuar; super "Fiton përgjigja e parë e mirë." (The first good answer wins.) |
| 24.05-25.95 | Auto-reply bubble "Faleminderit për mesazhin! Do t'ju përgjigjemi së shpejti." struck out |
| 29.15-31.45 | Super "Asistent AI në Instagram" |
| 31.4-40.05 | Phone chat labelled SHEMBULL (example): Elira gets the price and two slots, books Thursday 18:00; Arbër goes quiet for an hour, gets another client's review, a "−20%" sticker is struck out |
| 40.35-42.55 | Alert banner "🔔 Klient i ri · rezervoi" (New client · booked) |
| 42.6-45.6 | Brand beat: wordmark, red rule |
| 46.8-49.65 | Super "Komento ANALIZA"; comment box types ANALIZA; stopwatch 0:00 to 0:05 |
| 49.65-52.9 | DM banner with our real opener (live funnel `analiza`, sent 2026-10-14) |
| 51.35-54.6 | Super "Analizë falas · 45 min / pa detyrim" (lower third) |
| 55.0-58.3 | Super "Bëhu përgjigja e parë." (Be the first answer.) |
| 58.35-60.0 | End card: symbol, "Komento ANALIZA 👇", "Analizë falas · 45 min / pa detyrim" |

## Sound (build/mix.py)

- Voice: ElevenLabs master, unprocessed.
- Music: `music1` (ElevenLabs), bed at -27 LUFS, sidechain-ducked under the voice (threshold 0.02, ratio 8), fades in 0.3 s, out from 58.6 s.
- Effects (ElevenLabs): swoosh 0.30, 0.90, 1.50, 37.20, 47.40 · buzz 4.55, 5.85, 19.30 · ping 8.20, 12.00, 32.05, 34.60, 40.40, 49.65.
- Master: two-pass loudnorm, measured after AAC: -14.06 LUFS, true peak -1.50 dBTP, LRA 2.8.
