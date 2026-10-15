---
id: tt-why-cgi
title: "A giant pink bra in a mall atrium becomes a trampoline: the softest landing"
url: https://www.tiktok.com/@why.cgi/video/7493502946521402642
platform: tiktok
creator: why.cgi
plays: 98200000
likes: 4500000
shares: 1800000
saves: 223377
followers: 41000
posted: 2025-04-15
captured: 2026-10-14
duration_s: 7
category: cgi-fooh
hook: [impossible-object, scale-shock]
devices: [giant-product, fooh-composite, pov-camera, softbody]
energy: high
palette: [pastel, light]
palette_hex: ["#605f58", "#7b7974", "#c8b3bb", "#9f9b96", "#d567a3"]
sound: [diegetic-audio]
voiceover: false
text_on_screen: none
engine: [gen-video, footage, canvas]
difficulty: 4
fit: [ecommerce, events, agency]
wow: 5
relevance: 4
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.494
---

## The film in one line
A spectator films from a mall balcony as a woman drops from a pink diving platform three floors up into a
giant pink bra lying in the atrium and bounces back up two storeys, again and again, like it is a trampoline.

## Why it stops the scroll (first 2 s)
- 0.0 s: over the shoulder of a girl in a green cap at a glass rail. Below, a pink bra about 15 m across lies on
  the atrium floor with a hot pink puffy "SKIMS" block behind it; a tiny figure stands on a pink platform on the
  third floor.
- 0.5 s: the camera drifts past her shoulder.
- 1.0-2.0 s: clean wide, balconies lined with onlookers, the figure still waiting on the platform.
- Mechanism: an impossible object at believable scale in a real public space, filmed like a bystander's phone
  clip, plus a visible "someone is about to jump" setup. No text or voice; the caption says "The softest landing".

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | stranger's shoulder, giant bra, SKIMS block | handheld push past the shoulder | mall ambience |
| 1.0-2.0 | wide atrium, crowds on three levels, figure on platform | slight sway | crowd murmur |
| 2.5 | she has dropped into the right cup | first contact | laughing and screaming (AI segment) |
| 3.0-3.5 | rebound to third-floor height, flipping | big vertical arc | screams |
| 4.0-4.5 | falls past the SKIMS block into the left cup | landing | laughter |
| 5.0-5.5 | second rebound to the second-floor rail | arc | laughter |
| 6.0-6.5 | lands in the right cup arms out, pops up again | third bounce | clip ends mid-bounce |

## Signature device
Product benefit turned into physics on a giant product in a real crowded space. The product (soft fabric) is
scaled to about 15 m and laid flat like a double trampoline in a multi-storey atrium; a human body is the scale
bar. She drops about three storeys and the cups throw her back up about two, on a bounce cycle of roughly 1.5 s,
alternating left and right cup. A branded pink diving platform sets up the jump before anything moves. Camera: a
bystander's phone, 9:16, one floor up, handheld drift, no zoom, no cuts, a stranger's shoulder in frame for the
first second, balconies full of composited spectators as social proof.

## Pacing read
12.86 cuts per 10 s and a big change every 0.5 s (CV 0.0, no quiet frames) are the low-resolution handheld wobble
and a moving figure; in reality it is one take with no cuts. The real rhythm is 2.5 s of setup where only the
camera breathes, then a regular 1.5 s bounce cycle. The 0.494 hook change is the camera leaving the shoulder. It
ends mid-bounce, so the loop restarts on a calm wide and viewers rewatch the first drop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 7.0 s sampled (0.0 per 10 s); 9 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette: mall greys (#605f58, #7b7974, #9f9b96) as ground, baby pink product (#c8b3bb) as hero, hot brand pink
  (#d567a3) on the logo block and platform; warm downlights and a gold ceiling ring.
- Type: none as graphics; the only brand word is the puffy 3D lettering built into the set.
- Material and light: satin vinyl product, soft overhead light matched to the plate, soft contact shadows.

## Why it works
- Open loop at 0 to 2 s (a person waiting above a giant soft object), payoff at 2.5 s, then repetition with
  height, so there is no dead time after the reveal.
- "Is this real?" ambiguity from bystander framing drives comments and shares (1.8 M shares).
- Everyone wants to try the jump; the mid-bounce ending hides the loop.

## Steal this (grammar) / Leave this (content)
- Steal: one product claim dramatised as one stunt on a giant version of the product; human for scale; a visible
  setup before the action; bystander phone camera with a foreground shoulder; crowds as proof; end mid-action.
- Leave: SKIMS, the bra shape and pink livery, the mall, the person, the caption line.

## Build it in our studio
- Engine: `gen-video` (paid, approval) for photoreal, with client footage of their venue as the plate; or a
  stylised `canvas` version.
- Photoreal plan: 1) handheld plate of the client's venue from a balcony, 3 s of stillness; 2) `gen-image` still of
  the giant product in that plate, approved first; 3) image-to-video: figure drops from a platform, bounces twice;
  4) diegetic ambience, a scream, soft bounce thuds.
- Canvas plan: illustrated atrium in fake-3D, product rim as a mesh whose surface dips on landing with a
  closed-form `spring()`, figure as a silhouette on parabolic arcs, seeded handheld noise.
- Hard part: contact. The surface must dip and rebound in sync with the body; drive dip depth from landing
  speed and let the spring settle over 0.4 s.
- Difficulty 4: photoreal needs paid generation and retries for believable physics.

## Business translations
- Mattress or bedding e-commerce: a giant pillow on a station concourse; a commuter falls back from the mezzanine
  and bounces up to the rail.
- Running shoe shop: a giant midsole on a town square used as a trampoline to show cushioning, filmed by a
  passer-by.
- Furniture retailer: a giant sofa cushion in their own car park; a staff member drops onto it from a scissor lift.
