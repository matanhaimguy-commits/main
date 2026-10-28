# Reference bank tag vocabulary

Cards use these slugs so `tools/refbank.py` can search, pick and stop repeats. Add a new slug here first if
nothing fits (keep it short, lowercase, hyphenated) and say why in the commit.

## category (exactly one)
| slug | what it is |
|---|---|
| cgi-fooh | fake out-of-home / impossible CGI in real footage (giant product, landmark moves, object in a city) |
| brand-ad | a brand's own ad or a commercial-craft piece |
| product-motion | product shown in motion: 3D packshot, product in a world, product video recreation |
| logo-reveal | a logo built, animated or revealed (incl. "which brand next" series) |
| ui-saas | interface, app, SaaS or software motion (cards, cursor, screens, flows) |
| brand-identity | identity system shown as a case study or brand board reveal |
| kinetic-type | type is the picture: words move, build, stack, morph |
| lyric-mograph | motion-graphics edit cut to a song's lyrics (fan edits, trends) |
| explainer-3d | 3D explainer: medical, science, engineering, "how it works" |
| explainer-2d | 2D explainer: illustrated, stick figure, metaphor worlds, narrated facts |
| data-infographic | numbers, charts, diagrams, frameworks, infographics in motion |
| satisfying-sim | physics or simulation that is pleasing to watch (cloth, softbody, liquid, cutting) |
| beat-sync | motion hits locked to music beats (marbles, polyrhythms, music-driven loops) |
| asmr-care | slow, tactile "care/cleaning/fixing" animation with foley as the hook |
| story-comedy | character animation with a joke, POV or relatable situation |
| spectacle-world | awe: scale, impossible worlds, rave visuals, liminal spaces |
| vfx-edit | live action plus VFX/compositing (powers, transformations, effect showcases) |
| talking-explainer | one expert talks to camera (or as a voice over graphics) and the words carry the film: a claim, a rule, a list, a framework |
| conversation-scene | two voices: a role-played sales call, a hot seat, a street interview, a question asked off camera and answered |
| story-reel | one person tells a short story with a turn (rise, fall, the lesson), first person or in an interview |

## hook (one or two: what stops the thumb in the first 2 s)
impossible-object · scale-shock · pattern-interrupt · question · bold-claim · relatable-pov · transformation-promise ·
wait-for-it · guess-challenge · mid-action-start · contrast-split · direct-address · sound-hook · number-ladder ·
brand-name-drop · series-hook · price-or-value-question · familiar-ip · beautiful-first-frame · text-headline ·
stop-doing · if-i-had-to

## devices (list every one the film leans on; the first is the signature device)
Camera and space: one-take-camera · rack-focus · screen-in-frame · zoom-through-scale · pull-back-reveal · orbit · dolly-follow · pov-camera ·
top-down-plan · x-ray-cutaway · exploded-view · map-zoom
Transitions: match-cut · morph · shape-wipe · mask-reveal · whip-pan · glitch-cut · object-carries-camera ·
cut-on-beat · reverse-play · seamless-loop
Structure: escalation-ladder · before-after · versus-compare · countdown · list-of-n · timeline-progression ·
assembly-build · deconstruction · chain-reaction · transformation-sequence · series-episode
Type: word-stack · word-by-word · typing-caret · type-morph · 3d-type · type-on-path · lyric-sync-type ·
highlight-pill · scribble-annotation · big-number
Graphics: chart-grow · counter-ticker · node-diagram · icon-system · focus-brackets · progress-ring · ui-card-stack ·
cursor-demo · split-screen · grid-mosaic · halftone-collage · paper-cutout · pixel-art · stick-figure
Simulation and material: cloth-sim · softbody · liquid-sim · rigid-body-drop · particles · marble-run ·
beat-sync-hits · cutting-slicing · inflate-deflate · giant-product · product-in-world · fooh-composite ·
glass-refraction · clay-plasticine · lego-bricks · minecraft-voxel
Character: character-host · lip-sync · reaction-shot · pose-to-pose-comedy · creature-reveal · literal-metaphor · thought-bubble
Sound: asmr-foley · whoosh-transitions · bass-drop · silence-before-hit · voiceover-explainer · trending-audio
Talk: roleplay-dialogue · street-interview · qa-cold-open · quadrant-matrix · rise-fall-turn · prop-analogy · step-plan ·
mentor-quote

## energy (one)
calm · medium · high · frantic

## palette (one or two)
dark · light · saturated · pastel · mono · neon · natural · brand-colour

## sound (one or more)
music-beat · voiceover · asmr-foley · trending-audio · sfx-heavy · silence-moments · diegetic-audio · dialogue

## engine (our build route; one or more, first is preferred)
hyperframes · canvas · lemo:<style> (e.g. lemo:watercolor) · cab (Claude Animation Base) · collage ·
gen-image (paid) · gen-video (paid) · gen-3d (paid) · footage (client footage) · blender (not in our stack yet)

## fit (business types this grammar suits; several)
saas · agency · local-service · ecommerce · restaurant · health · finance · education · real-estate · b2b ·
personal-brand · events · coaching · any
