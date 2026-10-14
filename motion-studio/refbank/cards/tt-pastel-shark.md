---
id: tt-pastel-shark
title: "An animator's 2018 character meets her 2025 character and is stunned that the new one can move"
url: https://www.tiktok.com/@pastel.shark/video/7495122783018503430
platform: tiktok
creator: pastel.shark
plays: 19100000
likes: 2500000
shares: 13400
saves: 206674
followers: 143800
posted: 2025-04-19
captured: 2026-10-14
duration_s: 9
category: story-comedy
hook: [contrast-split, text-headline]
devices: [versus-compare, pose-to-pose-comedy, lip-sync, before-after, reaction-shot]
energy: calm
palette: [pastel]
palette_hex: ["#8b9c7b", "#241c19", "#605352", "#e5a07d", "#b3785d"]
sound: [trending-audio, dialogue, music-beat]
voiceover: false
text_on_screen: headline
engine: [canvas, cab, gen-image]
difficulty: 3
fit: [agency, saas, personal-brand, ecommerce, local-service]
wow: 3
relevance: 4
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 2.25
  change_rhythm_cv: 0.4
  quiet_share_2fps: 0.588
  hook_change_0_2s: 0.05
---

## The film in one line
Two versions of the same cartoon woman stand side by side under the labels "2025" and "2018": the smooth 2025
version crosses her arms and talks down to her past self, the 2018 version gasps in delight that her future self
is "fully articulated", then shows how little she can move herself and snaps back to her one stock pose.

## Why it stops the scroll (first 2 s)
- 0.0 s: sage green backdrop, two women framed from the thighs up, white rounded bold labels "2025" (left) and
  "2018" (right) above their heads. Left: dark hair with magenta streaks, black top, jeans, arms down. Right:
  long ombre hair, strapless floral dress, hand on hip, frozen smile.
- 0.5 s: 2025 has already folded her arms and is talking.
- 1.0 s: 2025 closes her eyes in a smug grin.
- 2.0 s: 2025 side-eyes 2018, who has not moved at all.
- Mechanism: the year labels are a two-word headline that sets up the comparison instantly, and the contrast is
  visible before any joke lands: one figure moves with acting, the other is a still drawing. Anyone who has seen
  the "fully articulated" trend audio recognises the setup.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | both figures, year labels | 2025 crosses her arms | trend audio dialogue starts (2025 speaks) |
| 0.5-2.0 | same | 2025 talks, grins with eyes shut, then side-glance; 2018 frozen | 2025 line, dismissive tone |
| 2.5-3.5 | 2018 hands jump to her cheeks, mouth an "o" | pose snap, no in-betweens | 2018 gasps |
| 4.0-5.5 | 2018 grinning, hands clasped under chin | held pose, small mouth changes | 2018 marvels that 2025 is fully articulated |
| 6.0-6.5 | 2018 arms down, flat mouth, blank stare | snap to a deadpan pose | beat of contrast, her own limits |
| 7.0-8.0 | 2018 back to hand on hip, stock smile | stiff arm wave per AI description (between sampled frames) | upbeat electronic dance music |
| 8.5 | 2018 eyes closed, 2025 still unimpressed | blink | music to the end |

## Signature device
Same subject, two eras, two animation techniques in one frame. The "new" version is animated with full acting:
in-betweened arm cross, eye closes, head tilts, glances, continuous lip-sync. The "old" version is animated the
way the old style could: three or four held drawings that snap with no in-betweens (stock pose, hands to cheeks,
hands clasped, arms down) and a mouth that barely changes. Both stand on one flat colour field, framed identically
(thigh-up, equal size, 30% and 70% of the width) with big plain year labels above. The gap between the two
motion qualities is the joke, so the only animation work that matters is making the difference obvious.

## Pacing read
Almost nothing changes globally: 3 big changes in 9 s, one every 2.25 s, with 59% of the 2 fps samples quiet and
a longest still stretch of 3 s. That stillness is the point; the old character is literally stuck. The beats are
the old character's pose snaps at about 2.5, 6.0 and 7.0 s, each a small hit against the static frame. The new
character fills the rests with low-amplitude acting. It ends on a held blink with music still running, which
makes the loop feel natural.

## Look
- Palette by role: muted sage green field (#8b9c7b) as the only background, dark hair and clothing (#241c19,
  #605352), warm skin tones (#e5a07d, #b3785d), magenta hair streak as the 2025 accent, white labels.
- Type: rounded geometric bold sans, white, cap height about 7% of the frame height, static.
- Texture: clean digital cel style, soft shading on the 2025 figure, flatter rendering on the 2018 figure.
- Camera: locked, no zoom. The frames sampled here are a wide crop with both figures cut at the thigh.

## Why it works
- Instant comparison: the labels and the side-by-side layout say "then vs now" in a glance.
- Relatable creator pride ("look how far I came") wrapped in self-deprecating comedy, so people root for both.
- The trend audio gives a known script, so viewers wait for the punchline they expect.
- Comment trigger: artists post their own old vs new art; saves (207 K) are mostly other animators bookmarking
  the trend. 19.1 M plays on 143.8 K followers is about 133x.

## Steal this (grammar) / Leave this (content)
- Steal: old and new version of the same thing side by side, each animated in the style of its era; plain year
  labels as the headline; the old one reacts to the new one's abilities; locked camera, flat colour field; the
  old one's limited motion is the punchline.
- Leave: their characters, the trend audio and its dialogue, the "fully articulated" line, their art style.

## Build it in our studio
- Engine: `canvas` with layered sprite puppets; `cab` if we want painterly characters (slow); `gen-image`
  (paid, approval) for the pose sheets.
- Scene plan: 1) pick the subject that exists in two eras (logo, website, product, mascot) and get the real old
  and new assets from the client; 2) the old one gets 3-4 held poses that cut with no tweening; 3) the new one
  gets springy, continuous motion (`spring()` on rotation and scale, eased glances, idle breathing); 4) year
  labels static above each; 5) a short dialogue voiceover or captions and a music sting when the old one tries
  to move.
- Hard part: lip-sync and acting on the new character. Use captions instead of dialogue, or a mouth chart
  driven by phoneme timings from `hyperframes transcribe`.
- Difficulty 3 with characters; 2 when the "characters" are a client's old and new logo or interface.

## Business translations
- Agency or studio rebrand reveal: the client's real old logo stands stiff next to the new animated identity and
  can only blink while the new one shows off its motion system.
- SaaS product update: the real 2019 dashboard screenshot sits frozen next to the new release, which scrolls,
  filters and animates; labels "v1" and "v3".
- Barbershop or salon: the shop's real first storefront photo, cut out and stiff, beside today's storefront that
  waves people in.
