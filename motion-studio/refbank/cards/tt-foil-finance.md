---
id: tt-foil-finance
title: "A step chart ticks month by month from 1960 to 2026 counting the times Switzerland accidentally invaded Liechtenstein"
url: https://www.tiktok.com/@foil.finance/video/7631673630346235149
platform: tiktok
creator: foil.finance
plays: 1500000
likes: 119400
shares: 8214
saves: 9302
followers: 2090
posted: 2026-04-24
captured: 2026-10-14
duration_s: 13
category: data-infographic
hook: [text-headline, bold-claim]
devices: [chart-grow, counter-ticker, timeline-progression, big-number]
energy: calm
palette: [dark, mono]
palette_hex: ["#171f24", "#242a2d", "#0e0f0d", "#1f1d14", "#a8acae"]
sound: [music-beat]
voiceover: false
text_on_screen: heavy
engine: [hyperframes, canvas]
difficulty: 1
fit: [finance, b2b, saas, education, real-estate, any]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 13.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.16
  hook_change_0_2s: 0.01
---

## The film in one line
Over a darkened photo of a border crossing with the Swiss and Liechtenstein flags and a boundary stone, a single
light-blue step line crawls from "Jan 1960" to "Apr 2026" while a big date counter ticks, stepping up from 0 to 5
as each accidental Swiss incursion happens, then flattens at 5 until the present day.

## Why it stops the scroll (first 2 s)
- 0.0 s: the whole film is already there: four lines of bold white text "number of times Switzerland has
  accidentally invaded Liechtenstein", a small grey "(1960-2026)", an empty chart with a dot at 0, and "Jan 1960"
  in large white type, all on a dark, blurred photo of two flags and a border stone.
- 0.5-2.0 s: only the date changes (Mar 1960, then Dec 1962) and the dot slides right along zero.
- Mechanism: the headline is an absurd, true-sounding claim ("accidentally invaded") that asks a question the
  chart promises to answer. The viewer stays to see the number. The transcript returns only "It's a good day";
  the AI description hears dramatic music ("Interstellar on Piano" per the post) and no narrator, so those words
  are most likely a mis-transcription of the music or a sample, not a voiceover. There is no spoken script; the
  on-screen title is the script.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-2.0 | title, empty chart, value 0, date Jan 1960 to Sep 1965 | dot slides along zero, date ticks | piano score |
| 2.5 | first step: line jumps to 1 (between Jun 1968 and Apr 1971); y-axis rescales to show 1 | vertical step, label "1" | music |
| 3.5 | second step to 2 (by Oct 1976); axis rescales to 2 | step, label | music builds |
| 4.0-5.0 | flat at 2 through Jul 1979 to Feb 1985 | dot slides, date ticks | music |
| 5.5 | step to 3 (by Nov 1987) | step, rescale | music |
| 6.5 | step to 4 (by May 1993) | step, rescale | music |
| 7.0-8.5 | flat at 4 from 1996 to 2004 | dot slides | music |
| 9.0 | step to 5 (by Mar 2007); axis now reads 0 to 6 | step | music |
| 9.5-13.0 | flat at 5 through 2010, 2015, 2021 to Apr 2026; ends on "Apr 2026" | dot reaches the right edge | music, ends |

## Signature device
A live step chart driven by a date clock. One line, one dot, one value label riding the dot, and a large date
readout under the chart that ticks in months at a constant rate (66 years in 13 s, about five years per second).
The y-axis auto-scales so the latest value always sits near the top of the plot, which makes each small step
read as a big jump. The chart sits in the upper middle of the frame (about 60% width), the title above it, the
date below it, all centred, over a full-bleed photo of the subject darkened to about 25% brightness so the white
type reads. The line is a steady light blue with a glowing endpoint; steps are instant vertical risers.

## Pacing read
The numbers say almost nothing moves: no cuts, no big changes, hook change 0.01, 16% quiet. That is correct and
it is the point. The picture is static and the only motion is a thin line and a date, so the film is all
anticipation: will it go up again? The steps arrive at uneven intervals (2.5, 3.5, 5.5, 6.5, 9.0 s), the
unevenness keeps the viewer guessing, and the last 4 s are flat, landing on today's date. No outro, no loop
device; the ending resolves the question.

## Look
- Palette by role: near-black blue-greys (#171f24, #242a2d, #0e0f0d) from the darkened photo, a warm dark olive
  (#1f1d14) from the grass, light grey axis labels (#a8acae), white type, light-blue line, with the red Swiss flag
  and the blue-red Liechtenstein flag as the only colour.
- Type: one bold geometric sans in white. Title about 55 px cap height on a 1080 frame, centred, lower case,
  four lines; subtitle about 25 px grey; date counter about 80 px bold; axis labels about 20 px grey; value label
  bold white beside the dot.
- Texture and light: a real photograph, blurred and darkened, no grain added.
- Camera: none. Fixed frame.

## Why it works
- Absurd but checkable fact in the title: people stay to see the count and comment the stories behind each step
  (the caption lists them with dates).
- Anticipation from a clock: viewers watch a timeline to see when the next jump comes.
- Ends on "now", which makes it feel current and invites "it'll be 6 soon" comments.
- Very cheap to make, which is why a 2 k follower account can break out to 1.5 M plays (about 700 times its
  follower count): the idea carries it.

## Steal this (grammar) / Leave this (content)
- Steal: a "number of times X has Y" title in plain lower case; one step line with a riding value label and a
  big date clock; auto-scaling y-axis; a darkened photo of the subject behind; constant time rate; end on
  today's date.
- Leave: the Swiss and Liechtenstein subject, their background photo, the data, the music.

## Build it in our studio
- Engine: HyperFrames (SVG line built from a data file, GSAP timeline mapping time to date; search the registry
  for a chart-grow or counter block first) or the canvas engine.
- Scene plan: 1) find a real, sourced, dated dataset with a surprising shape (put source and date in
  PROJECT.md); 2) map dates linearly to film time, 4 to 6 years per second for long spans; 3) draw the step line
  and dot, value label snapped to integer steps; 4) y-axis rescale on each new max with a short spring;
  5) background photo of the subject darkened to 25%; 6) a soft tick or piano note on each step.
- Hard part: the data and the title. The chart is trivial; the film only works if the fact is odd and true.
- Difficulty 1. Render about 3.5 minutes in HyperFrames for 13 s. No paid steps; music generated or licensed.

## Business translations
- Accounting firm: "number of times the tax filing deadline has been extended" over the years, from the
  official record, ending on this year.
- Real estate agent: "median asking price in [town]" as a stepped line from official land-registry data,
  date clock ticking, ending on this month.
- SaaS company: "number of integrations we support" stepping up release by release from the public changelog,
  ending on the launch of the newest one.
