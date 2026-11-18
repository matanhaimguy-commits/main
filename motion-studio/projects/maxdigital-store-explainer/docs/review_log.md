# Review log

## Round 1 (styleframes, 20 beats, phone size)
Hook 7, readability 8, motion 8, continuity 8, pacing 7, composition 7, brand 9, sound n/a, message sound-off 8.
Fixed: stacked "new sale" chips overlapped; empty first beat of the chores scene; third badge text overflowed; the opening
word too small.

## Round 2 (full render v0, contact sheet every 2.5 s)
Hook 8, readability 8, motion 8, continuity 8, pacing 8, composition 8, brand 9, sound 8 (measured, not heard), sound-off 8.
Fixed: the task pile overlapped the logo reveal (now pulled in before the wipe); step 1 sat empty for 1.2 s (the chart card
now draws on "שלב ראשון"); step 2 panels appeared late (outlines now draw on "והחלק").

## Round 3 (v1)
Checks: seekcheck PASS (24 revisits, every 0.1 s); audio_qa: -14.9 LUFS mix / -15.0 LUFS on the muxed file, true peak
-1.3 dB after AAC, no dropouts, low-mid warning on 4 seconds of the male voice (EQ applied, logged); segment seam at
29.5 s checked frame by frame, no jump.
Known: step 2 opens on the step tag alone for about 1 s (a planned rest under "שלב שני"); the last ~2 s are the end card
over the music tail. Nobody has listened yet; a native Hebrew speaker must check the voice.

## v2 (owner notes: trust, energy, real images, SFX, camera)
Checks: seekcheck PASS; audio_qa -14.0 LUFS (muxed -14.1), true peak -1.3 dB after AAC, no dropouts, low-mid warning
on 5 seconds (male voice; EQ applied); voice energy 65.2 (v1 take 27-ish), 3.35 words a second; render seam at 23.2 s
checked frame by frame. 60 sound events in 46 s (v1: 45 in 58 s). Contact sheet every 2 s: every 2 s frame changes.
Known: the brand card holds 1.7 s (planned rest under the logo); nobody has listened; Hebrew pronunciation not verified
by a native speaker.

## v3 (Brandify Eagle voice with emotion tags)
Checks: seekcheck PASS; audio_qa -14.1 LUFS, true peak -1.4 dB after AAC, no dropouts; low-mid warning on 8 half-seconds
(the Eagle is a deep baritone; extra EQ cut at 180 and 280 Hz applied, down from 12); seam at 29.6 s clean; 59.3 s.
Voice: energy 63.4, pitch spread 21 semitones, speech pace 2.68 words a second, speed 1.07. Nobody has listened yet.

## v4 ("we also teach you")
Checks: seekcheck PASS; audio_qa -14.0 LUFS mix, -14.1 muxed, true peak -1.3 dB after AAC, no dropouts; the Eagle
low-mid warning as in v3; seam at 31 s clean; 62 s, 1860 frames. Teaching card overlap with the headline fixed before
render. Nobody has listened yet.

## v5 (music only)
audio_qa: -14.0 LUFS, true peak -1.5 dBTP, no dropouts, low-mid warning on 9 half-seconds (12 in v4). Same picture as v4.
Joins: 120 ms at 18.79 s (under the brand flash and impact), 30 ms bar repeat on a downbeat. Nobody has listened yet.
