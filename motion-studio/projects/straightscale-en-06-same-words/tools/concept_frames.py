"""Run from the repo root: python3 motion-studio/projects/straightscale-en-06-same-words/tools/concept_frames.py. Shot Spec + prompt v6 for the EN 06 concept frames, from one source so they never drift (STANDARDS 6 reels zone)."""
import yaml
POST="SSEN-2026-11-W4-01"; RUN=f"clients/straightscale-en/runs/{POST}/"
REF=("no sheet yet: this concept frame is the first image of the prop (hook-lab-organic: concept frames come at step 2); "
     "the prop sheet is cut from the approved frame at step 7")
LANE=("Premium studio claymation scene - everything sculpted from matte plasticine with refined intentional craftsmanship: "
 "subtle tool marks, controlled texture, soft rounded geometry, slight subsurface warmth, macro lens feel with shallow depth "
 "of field, soft diffused studio lighting with a gentle rim glow, the scene filling the entire frame with the camera inside "
 "the miniature clay world. Vertical 9:16 frame.")
PHYS=("Everything in frame is real professionally sculpted matte plasticine, photographed - refined sculpting marks, real cast "
 "shadows, soft studio lighting, the clay scene filling the entire frame.")
ZONE=("Layout (STANDARDS 6; heights measured down from the top edge of the frame): the top 30% of the frame is plain and "
 "empty (the text hook is set at 14% to 30% in the edit); every key element sits between 30% and 55% of the frame height "
 "(captions start at 55%) and inside 6% to 94% of the width, and inside 6% to 79% of the width wherever it lies lower than "
 "50% of the height; lower than 55% there is only the plain continuation of the surface, nothing else.")
NEG=["no logo, wordmark or real app name or app icon anywhere","no digits or numbers anywhere",
 "no words other than the quoted ones","nothing in the top 30% of the frame (measured down from the top edge) except the plain surface",
 "no people, no hands, no faces","no workbench, table edge or room around the clay world","no glossy CGI look, no glass reflections"]
def tx(s, surf, x, y):
    return {"string":s,"surface":surf,"position":f"x {x[0]}% to {x[1]}%, y {y[0]}% to {y[1]}%","case":"upper","must_be_exact":True,"occlusion":"nothing covers any letter"}
def frame(f):
    spec={"shot_id":f["id"],"post_id":POST,"format":"claymation","script_lines":["L1"],"line_text":f["line"],
     "story_purpose":f["purpose"],"must_read_in_1s":f["read"],"subjects":f["subjects"],"hands":"none visible","props":f["props"],
     "text_in_image":f["texts"],"action_physics":[f["physics"]],"static":True,
     "setting":{"ref":None,"details":f["setting"],"background_rule":f["bg"]},
     "camera":{"framing":f["framing"],"angle":f["angle"],"lens":"macro, shallow depth of field","aspect":"9:16","safe_zones":ZONE},
     "continuity":{"previous_shot":None,"carry_over":[]},"regions":f["regions"],
     "style":LANE+" Palette (every colour in this frame): "+f["palette"]+".","must_not":NEG,"hero":True,
     "notes":f"Concept frame for hook stacks {f['stacks']} (Hook Lab v4). The text hook is overlaid in code at 14% to 30%, not drawn by the model."}
    yaml.safe_dump(spec,open(RUN+"shots/"+f["id"]+".spec.yaml","w"),sort_keys=False,allow_unicode=True,width=110)
    tlines=" ".join(f'"{t["string"]}" on {t["surface"]}, at {t["position"]};' for t in f["texts"])
    p="\n\n".join([LANE+" Palette (every colour in this frame): "+f["palette"]+".",
     "References: none attached (text to image).",
     "Camera: "+f["angle"]+"; macro lens feel, shallow depth of field, vertical 9:16. "+f["framing"]+".",
     "Subject and props: "+f["describe"],
     "Hands: no hands visible.",
     "Action as contact points: "+f["physics"],
     "Text: heavy bold capital letters, exactly: "+tlines+" nothing covers any letter. No other text anywhere.",
     "Setting and background: "+f["setting"]+". "+f["bg"]+".",
     ZONE,"Continuity: first frame of the reel; nothing carried over.",
     "Negatives: "+"; ".join(NEG)+".",PHYS])
    open(RUN+"prompts/CF-"+f["key"]+".v6.txt","w").write(p+"\n")
SCREEN=("A macro close-up of one clay phone screen, seen square on: the screen's rounded top edge with a terracotta #C8553D clay "
 "rim runs straight across the frame at 30% of the frame height, and the screen continues past the left, right and bottom "
 "edges of the frame. The screen is matte clay, not glass, no reflections. From the top edge down to 30% of the frame height "
 "there is only plain cream #F3E9D8 clay. On the screen, edge to edge: a cream #F3E9D8 band from 30.5% to 37% of the frame "
 "height holding the words, with a thin deep ink #2B2A33 clay line along its bottom edge; under it a plain sage #8FA98B "
 "screen field that continues to the bottom edge of the frame.")
BG_SCREEN="no signs, frames, posters or other screens; the only writing is the quoted text"
BAND=lambda: tx("BOOK A CALL","the cream band at the top of the screen, deep ink #2B2A33 letters, centred",(14,86),(31.5,36))
SETTING="the clay phone screen fills the frame from 30% of the height down; from the top edge to 30% only plain cream clay; lower than 55% only the plain sage screen field"
frames=[
 {"key":"V1","id":"H-01-V1","stacks":"EN06-V1, EN06-V2","line":"The problem isn't your posts. It's what happens after someone clicks.",
  "purpose":"The page a post leads to: likes came in (the hearts) but the booking calendar stays empty.",
  "read":"A BOOK A CALL page with an empty calendar, hearts piled under it.",
  "subjects":[{"id":"PR-SCREEN","ref":REF,"state":"lit, the booking page","pose":"fills the frame from 30% of the height down, edge to edge","expression":"","instances":1}],
  "props":[{"id":"PR-SCREEN","story_critical":True,"ref":REF,"state":"lit, the booking page","content":"cream band with BOOK A CALL in deep ink; on the sage field a calendar of 2 rows by 4 columns of wide flat rounded cream clay tiles, each about twice as wide as tall, with sage gaps, x 8% to 78%, y 39% to 48%, every tile empty: no digits, no names, no marks","size_in_frame":"the full width, from 30% of the height to the bottom edge"},
           {"id":"PR-HEARTS","story_critical":True,"ref":REF,"state":"a low pile lying on the screen","content":"a low row, one heart high with a few resting on top and never taller than 5% of the frame height, of plump thumb-pressed clay hearts in heart red #D64545, each about 4.5% of the frame width, on the plain sage field under the calendar, x 8% to 60%, y 50% to 55%, touching only the screen and each other, not touching the calendar"}],
  "texts":[BAND()],
  "physics":"The screen faces the camera square on; the hearts lie flat against the screen surface in one low pile under the calendar, each resting on the screen or on the heart under it; nothing touches the band, the letters or the calendar tiles.",
  "setting":SETTING,"bg":BG_SCREEN,
  "framing":"One subject: the booking page, edge to edge, big",
  "angle":"straight on, square to the screen, camera inside the miniature clay world","palette":"warm cream #F3E9D8, terracotta #C8553D, sage #8FA98B, deep ink #2B2A33, heart red #D64545",
  "describe":SCREEN+" The calendar: 2 rows by 4 columns of wide flat rounded cream clay tiles, each about twice as wide as tall, with sage gaps, from 8% to 78% of the frame width and 39% to 48% of the frame height, every tile empty: no digits, no names, no marks. Under the calendar, a low row, one heart high with a few resting on top and never taller than 5% of the frame height, of plump thumb-pressed clay hearts in heart red #D64545, each about 4.5% of the frame width, from 8% to 60% of the frame width and 50% to 55% of the frame height, not touching the calendar. The sage field continues plain to the right of the calendar and the hearts, and everywhere lower than 55% of the frame height.",
  "regions":[{"name":"book-a-call","kind":"text","box":[0.14,0.315,0.86,0.36]},{"name":"calendar","kind":"prop","box":[0.08,0.39,0.78,0.48]},{"name":"hearts","kind":"prop","box":[0.08,0.50,0.60,0.55]}]},
 {"key":"V9","id":"H-01-V9","stacks":"EN06-V9","line":"Before you post more, click your own link. Read that page.",
  "purpose":"Check the page first: a magnifying glass on the booking page shows the calendar is empty.",
  "read":"A magnifying glass on a BOOK A CALL page shows the calendar is empty.",
  "subjects":[{"id":"PR-SCREEN","ref":REF,"state":"lit, the booking page","pose":"fills the frame from 30% of the height down, edge to edge","expression":"","instances":1}],
  "props":[{"id":"PR-SCREEN","story_critical":True,"ref":REF,"state":"lit, the booking page","content":"cream band with BOOK A CALL in deep ink; on the sage field a calendar of 3 rows by 4 columns of wide flat rounded cream clay tiles, each about 16% of the frame width by 4% of the frame height, with sage gaps, x 8% to 78%, y 39% to 54%, every tile empty: no digits, no names, no marks","size_in_frame":"the full width, from 30% of the height to the bottom edge"},
           {"id":"PR-GLASS","story_critical":True,"ref":REF,"state":"lying flat on the screen","content":"one magnifying glass: a round lens 24% of the frame width across (x 38% to 62%, y 40% to 53.5%) in a thick terracotta #C8553D clay rim; the lens face is a solid matte clay disc with no shine, carrying the same empty cream tiles modelled larger on it; one straight terracotta #C8553D clay handle, a round clay bar about 2.5% of the frame height thick, runs horizontally from the left point of the rim (x 38%, y 46.75%) to the viewer's left and ends at x 18%, y 46.75%, lying flat across the calendar with a soft contact shadow under it"}],
  "texts":[BAND()],
  "physics":"The screen faces the camera square on; the magnifying glass lies flat against the screen surface over the calendar, its rim and its horizontal handle touching the calendar tiles; nothing touches the band or the letters.",
  "setting":SETTING,"bg":BG_SCREEN,
  "framing":"One subject: the booking page, edge to edge, the magnifying glass on the calendar",
  "angle":"straight on, square to the screen, camera inside the miniature clay world","palette":"warm cream #F3E9D8, terracotta #C8553D, sage #8FA98B, deep ink #2B2A33",
  "describe":SCREEN+" The calendar: 3 rows by 4 columns of wide flat rounded cream clay tiles, each about 16% of the frame width by 4% of the frame height, with sage gaps, from 8% to 78% of the frame width and 39% to 54% of the frame height, every tile empty: no digits, no names, no marks. On the calendar lies one magnifying glass: a round lens 24% of the frame width across, from 38% to 62% of the frame width and 40% to 53.5% of the frame height, in a thick terracotta #C8553D clay rim; the lens face is a solid matte clay disc with no shine, carrying the same empty cream tiles modelled larger on it. One straight terracotta #C8553D clay handle, a round clay bar about 2.5% of the frame height thick, runs horizontally from the left point of the rim (38% of the width, 46.75% of the height) to the viewer's left and ends at 18% of the width at the same height, lying flat across the calendar with a soft contact shadow under it. The sage field continues plain to the right of the calendar and everywhere lower than 55% of the frame height.",
  "regions":[{"name":"book-a-call","kind":"text","box":[0.14,0.315,0.86,0.36]},{"name":"calendar","kind":"prop","box":[0.08,0.39,0.78,0.54]},{"name":"lens","kind":"prop","box":[0.38,0.40,0.62,0.535]},{"name":"handle","kind":"prop","box":[0.18,0.455,0.38,0.48]}]},
 {"key":"V8","id":"H-01-V8","stacks":"EN06-V8","line":"Your post says one thing. Your page says another. Nobody books.",
  "purpose":"The mismatch: the post speaks the buyer's words, the page it leads to speaks different words.",
  "read":"The post says TIRED OF SLOW MONTHS?, the page under it says WELCOME TO OUR WEBSITE.",
  "subjects":[{"id":"PR-POST","ref":REF,"state":"a flat clay card lying on the clay ground","pose":"x 6% to 94%, y 31% to 41.5%","expression":"","instances":1},
              {"id":"PR-PAGE","ref":REF,"state":"a flat clay card lying on the clay ground","pose":"x 6% to 79%, y 45.5% to 55%","expression":"","instances":1}],
  "props":[{"id":"PR-POST","story_critical":True,"ref":REF,"state":"lying flat","content":"one flat cream #F3E9D8 clay slab with rounded corners and a thick terracotta #C8553D clay rim, one layer, its two lines of deep ink letters on it","size_in_frame":"88% of the width, 10.5% of the height"},
           {"id":"PR-HEARTS","story_critical":True,"ref":REF,"state":"pressed onto the post card","content":"three small clay hearts in heart red #D64545 pressed onto the post card to the right of line 2, x 74% to 88%, y 36.5% to 40.5%, clear of every letter"},
           {"id":"PR-PAGE","story_critical":True,"ref":REF,"state":"lying flat","content":"one flat grey-blue #9AA3AD clay slab with rounded corners, one layer, its two lines of deep ink letters centred on it","size_in_frame":"73% of the width, 9.5% of the height"},
           {"id":"PR-ARROW","story_critical":False,"ref":None,"state":"lying flat between the cards","content":"one short thick terracotta #C8553D clay arrow pointing down, x 40% to 48%, y 42% to 45%, touching neither card"}],
  "texts":[tx("TIRED OF SLOW","the post card, line 1, deep ink #2B2A33 letters, centred",(12,88),(32,36)),
           tx("MONTHS?","the post card, line 2, deep ink #2B2A33 letters, centred",(32,68),(36.5,40.5)),
           tx("WELCOME TO","the page card, line 1, deep ink #2B2A33 letters, centred on the card",(14,71),(46.5,50.5)),
           tx("OUR WEBSITE","the page card, line 2, deep ink #2B2A33 letters, centred on the card",(12,73),(50.5,54.5))],
  "physics":"Both cards and the arrow lie flat on the sage clay ground; the three hearts are pressed into the post card's surface to the right of line 2; nothing else rests on the cards.",
  "setting":"a flat sage #8FA98B clay ground filling the whole frame; from the top edge to 30% and everywhere lower than 55% only plain ground","bg":"no signs, frames, posters or screens; the only writing is the quoted text",
  "framing":"Two cards stacked vertically, the post card centred and the page card left of 79% of the width, the arrow between them; the whole card area in sharp focus",
  "angle":"seen from straight above, the lens looking straight down at the clay ground, square to the frame","palette":"warm cream #F3E9D8, terracotta #C8553D, sage #8FA98B, deep ink #2B2A33, grey-blue #9AA3AD, heart red #D64545",
  "describe":"A flat sage #8FA98B clay ground fills the whole frame. On it lie two flat clay cards, one above the other. The upper card (the post): one flat cream #F3E9D8 clay slab with rounded corners and a thick terracotta #C8553D clay rim, one layer, from 6% to 94% of the frame width and 31% to 41.5% of the frame height. Three small clay hearts in heart red #D64545 are pressed onto the post card to the right of its second line, from 74% to 88% of the frame width and 36.5% to 40.5% of the frame height, clear of every letter. The lower card (the page): one flat grey-blue #9AA3AD clay slab with rounded corners, one layer, from 6% to 79% of the frame width and 45.5% to 55% of the frame height. Between them, one short thick terracotta #C8553D clay arrow pointing down, from 40% to 48% of the frame width and 42% to 45% of the frame height, touching neither card. From the top edge down to 30% and everywhere lower than 55% of the frame height the ground is plain and empty.",
  "regions":[{"name":"post","kind":"prop","box":[0.06,0.31,0.94,0.415]},{"name":"post-text","kind":"text","box":[0.12,0.32,0.88,0.405]},{"name":"hearts","kind":"prop","box":[0.74,0.365,0.88,0.405]},{"name":"arrow","kind":"prop","box":[0.40,0.42,0.48,0.45]},{"name":"page","kind":"prop","box":[0.06,0.455,0.79,0.55]},{"name":"page-text","kind":"text","box":[0.12,0.465,0.73,0.545]}]},
]
for f in frames: frame(f)
