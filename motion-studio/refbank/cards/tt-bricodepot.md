---
id: tt-bricodepot
title: "The new store catalogue is so heavy a tower crane lowers it into the car park and it cracks the tarmac"
url: https://www.tiktok.com/@bricodepot/video/7359483101438856480
platform: tiktok
creator: bricodepot
plays: 1700000
likes: 3902
shares: 379
saves: 555
followers: 468200
posted: 2024-04-19
captured: 2026-10-14
duration_s: 13
category: cgi-fooh
hook: [wait-for-it, brand-name-drop]
devices: [giant-product, rigid-body-drop, fooh-composite, pov-camera, reaction-shot]
energy: medium
palette: [brand-colour, natural]
palette_hex: ["#dce4eb", "#787b81", "#9cb0ca", "#4c4c4e", "#861f2c"]
sound: [diegetic-audio, sfx-heavy]
voiceover: false
text_on_screen: none
engine: [canvas, footage, gen-video]
difficulty: 3
fit: [ecommerce, local-service, b2b, real-estate]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 17.69
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.701
---

## The film in one line
Outside a Brico Depot store, onlookers film as a tower crane lowers a three-storey copy of the new 2024
catalogue out of the sky; it lands upright in the car park with a thud, cracking the tarmac around it.

## Why it stops the scroll (first 2 s)
- 0.0 s: low handheld shot of a red DIY store front with the big "BRICO DEPOT .fr" sign, empty car park, a man
  in a light shirt at the right edge, a woman filming on the left, the filmer's shadow on the tarmac.
- 0.5 s: the camera starts to tilt up; a yellow tower crane mast appears at the left edge.
- 1.0 s: more bystanders, phones up. Something is happening above.
- 1.5-2.0 s: the crane jib and a large flat object hanging from it enter at the top of frame.
- Mechanism: wait-for-it. Ordinary store, crowd filming upward, and the payoff is above the frame. The brand
  name is the biggest thing on screen from frame one.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.0 | store front and sign, car park, bystanders | handheld, slight tilt up | ambience, onlookers (not described in detail) |
| 1.5-2.0 | crane jib and a hanging slab enter top of frame | camera tilts up | ambience |
| 2.0-4.0 | slab descends toward the store roof; people raise phones | load lowers, camera follows | ambience |
| 5.0-6.0 | full tilt into blue sky with clouds; slab turns, its spine and page block show: it is a book | load rotates and swings | ambience |
| 7.0-8.0 | book nearly flat overhead, filling the top half; store sign at bottom | load drops close above roof | building tension |
| 8.5 | book stands upright on the tarmac, about three storeys tall, broken tarmac chunks around its base | landing (the drop happens between samples) | heavy thud (AI segment) |
| 9.0-10.0 | full cover readable: "L'OFFICIEL DU BRICOLAGE 2024", product photo grid, "Des prix dépôt, du stock, tous les jours." | handheld settle | ambience |
| 10.0-13.0 | hold on the standing catalogue with bystanders filming, filmer's shadow in foreground | small handheld drift | ambience, onlookers |

## Signature device
Product claim turned into physical weight. The caption claim is "more than 500 pages and 10,000 products, it's
HEAVY", and the film proves it physically: the printed catalogue, rebuilt as a rigid box about 10 m tall with a
real page block and spine, needs a tower crane to deliver and cracks the tarmac when it lands. The camera is a
bystander's phone that follows the load from store sign up into the sky (about 6 s of tilt, the object rotating
to reveal it is a book) and then snaps back down to ground level for the landing, which hides the hardest moment
(contact) inside a fast move. The cover art is the real catalogue cover, so the landed hero frame doubles as the
ad itself, held for the last 4.5 s.

## Pacing read
17.69 cuts per 10 s and a change every 0.5 s with CV 0.0 come from the continuous tilt and handheld motion, not
edits; the film reads as one take with a possible hidden cut at the landing (8.0 to 8.5 s). The structure is
8 s of rising tension (tilt up, slow descent, rotation reveal), an instant payoff, then a 4.5 s hold on the
landed catalogue, which is the only rest and is where the cover is readable. The hook change of 0.701 is the tilt
starting. It ends on the hold with no sting, so it does not loop cleanly.

## Look
- Palette by role: sky whites and blues (#dce4eb, #9cb0ca), tarmac greys (#787b81, #4c4c4e), brand red
  (#861f2c in shadow, bright red in sun) on the store and the catalogue spine.
- Type: no overlay. All text is in the world: the store sign and the catalogue cover (condensed bold caps on a red
  spine, a short white-on-red price claim).
- Texture and light: bright spring sun with hard shadows; the catalogue has a glossy cover and matte page edges.
- Camera: handheld phone at chest height, slow tilt up and fast tilt down.

## Why it works
- The setup (crane, crowd filming) gives a reason to wait.
- The rotation reveal at 5 to 6 s is a small surprise inside the wait: the slab is a book.
- The landing with cracked tarmac makes the claim ("heavy") felt, which is funnier than saying it.
- The landed frame is a full ad for the catalogue in front of the store, and the caption gives the call to
  action (pick up your copy in store).
- Note: about 3.9 K likes on 1.7 M plays suggests paid distribution; judge it as a brand template, not a viral.

## Steal this (grammar) / Leave this (content)
- Steal: take one claim about the product (heavy, soft, fast, big) and make it physical; deliver the giant
  product to the client's own storefront by crane; follow the load into the sky and snap back down for the
  impact; hold the landed product as the ad; bystanders filming as proof.
- Leave: Brico Depot, their catalogue cover and wording, the store, the crane footage.

## Build it in our studio
- Engine: `canvas` composited over client footage (tripod or steady handheld), `gen-video` (paid, approval) if the
  client wants full handheld realism.
- Scene plan: 1) film the client's storefront with a slow tilt up into the sky and a fast tilt down, ideally
  with staff filming on phones; 2) in canvas, build the product as a textured box in fake-3D (projection math)
  with the real cover on the front face, page block on the side; 3) animate the descent with a pendulum swing
  from `spring()` and a quarter turn to show the spine; 4) at the landing, a hard stop with 2 frames of camera
  shake, a cracked-tarmac decal and seeded dust particles; 5) diegetic ambience, crane whine, a big low thud.
- Hard part: matching the camera tilt. Use the plate's horizon and a few hand-placed track points, or film on a
  tripod head with a measured tilt and drive the canvas camera with the same angle curve.
- Difficulty 3: the object is rigid and flat-sided, so no simulation; tracking is the only real work.

## Business translations
- Furniture or homeware e-commerce launching a new collection: the lookbook arrives by crane at the warehouse
  and dents the loading bay.
- Local builders' merchant: the new price list lands in their own yard, upright, between the pallets.
- SaaS or B2B company launching a big annual report: the report, as a giant printed book, is lowered onto the
  office forecourt as staff film it.
