# StraightScale carousel style bible (locked)

From carousel-machine's StraightScale preset, aligned with the motion brand (same reds, ivory, charcoal).

- **World:** "Tirana after dark": cinematic night city scenes, warm tungsten light, the Tirana clock tower visible
  through the cover's window. Same light and colour grade on every slide.
- **Thread:** a smartphone in a deep red case (#BE0F18), recurring on every slide, changing state with the story
  (silent, unread messages piling up, ringing, a booked calendar).
- **Palette:** scene tone near-black (#1F1F1F), type ivory (#F8F6EF), accent crimson #B31217 as solid highlight
  rectangles behind key words and the swipe arrow button, small gold (#DD9A10) only for the counter. #B31217 is the only
  saturated colour besides the gold counter and the phone case. (Source: brand-kit.md 45 and Organic OS 7.3; mark red
  #BE0F18 lives only in the real logo file and the phone case. This note is for people, not for the prompt.)
- **Type:** heavy bold geometric sans in ivory, left-aligned in the calm dark area; key words in solid crimson #B31217
  highlight rectangles. Spell ë and ç out letter by letter in every prompt.
- **Frame:** slide counter top right (gold), swipe arrow bottom right on slides 1 to N-1. The bottom-left corner (the
  lowest 9% of the height, the left 40% of the width) stays calm, dark and empty in the prompt: the model never draws the
  logo (brand kit: real files only). After the visual review passes, the real logo file is pasted there with
  `python3 growth-engine/tools/brand_overlay.py <in> <out> --client straightscale` (FL-13).
- **Format:** 1080x1350 (4:5, the tallest the Instagram publishing API accepts), GPT Image 2.5 via Higgsfield at aspect 4:5,
  2k, medium quality (1 credit each). The live 7-slide carousel of 15 Oct was made at 3:4 and re-fitted to 4:5.
- **Banned:** flat text-on-colour templates, stock-photo smiles, other brands' logos, invented UI with fake numbers.
