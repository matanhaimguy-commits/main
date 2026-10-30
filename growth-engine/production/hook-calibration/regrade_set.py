"""Builds the re-grade folder: the 6 best stacks plus 2 anchors (B1, B6 from calibration round 3). Words only."""
import json, pathlib, random, sys
OURS = "Owners of one-person or small service businesses (consultants, coaches, small agencies), late 30s to mid 40s, who get clients by referral and LinkedIn, with lumpy months and no predictable way to get the next client."
ST = [
 ("W9-11 R3c","Offer not selling? Fix its first line before the price.","Cutting your price because nobody buys? Fix your offer's first line.",OURS),
 ("W9-10 R4a","Still no replies? It's the first line, not the volume.","Doubled your cold emails? The first line is why nobody answers.",OURS),
 ("W1-02 R3c","Your next post's first line? A buyer already wrote it.","A buyer already wrote it. Here's where to find your own.",OURS),
 ("W9-04 R3a","Months of posting, few leads? Use buyers' exact words instead.","Few leads after months of posting? Use your buyers' exact words.",OURS),
 ("W9-02 best","Referrals aren't your problem. The timing is.","Some months you sign three clients. Some months, literally nothing.",OURS),
 ("EN06 page best","Likes, no bookings? Don't fix the post. Fix the page.","Your post asks about slow months. Your page never answers it.",OURS),
 ("ANCHOR B1","Foam in the toilet? That's your kidneys crying for help","I'm your struggling kidneys, and that foam you keep seeing in the toilet? That's me crying for help.","Adults who see foam in the toilet and worry about their kidneys."),
 ("ANCHOR B6","She's not gaining weight. She's swollen.","She's not gaining weight. She's swollen.","Women who think they are gaining weight when the swelling is fluid."),
]
folder = pathlib.Path(sys.argv[1]); folder.mkdir(parents=True, exist_ok=True)
order = ST[:]; random.Random(41).shuffle(order)
lines = ['# Stacks to grade (words only: the visual was not made for any of them, write "n/a" for visual)\n']; key = {}
for i,(n,t,s,b) in enumerate(order,1):
    l = f"S{i:02d}"; key[l] = {"id":n,"text":t,"spoken":s}
    lines.append(f'## {l}\n- TARGET BUYER: {b}\n- VISUAL: frame not made yet\n- TEXT: "{t}"\n- SPOKEN: "{s}"\n')
(folder/"stacks.md").write_text("\n".join(lines)); pathlib.Path(sys.argv[2]).write_text(json.dumps(key, indent=1))
