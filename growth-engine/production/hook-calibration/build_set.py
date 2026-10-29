"""Builds the blind calibration set: key.json (provenance, never given to graders) and a stacks.md per round folder."""
import json, random, sys, pathlib

STACKS = [
 # id, kind, source, text, spoken
 ("A1","strong","refbank yt-alexberman-orange (90x channel median). Text = the video's real title. Spoken verbatim from card.",
  "The difference between entrepreneur and businessman",
  "Are you a businessman or are you an entrepreneur? Here's an easy way to find out."),
 ("A2","strong","refbank yt-thefutur-money-first (15.8x). Text = real title. Spoken verbatim from card.",
  "Talk about money first!",
  "Just talk about money first. Talk about money because money is the disqualifier."),
 ("A3","strong","refbank yt-thefutur-three-books (15.4x). Text = real title. Spoken verbatim from card.",
  "3 marketing books to grow your business",
  "What are three marketing books every creative should read?"),
 ("A4","strong","refbank yt-patrickdang-thirty-days (17.7x). Spoken verbatim; text written by us from the card's one-line summary (the card has no seen text).",
  "Make $3,000 in 30 days with a full-time job",
  "If I needed to make $3,000 with Claude AI in the next 30 days, here's exactly what I would do, even if I had a full-time job."),
 ("A5","strong","refbank yt-codie-five-levels (11.6x). Spoken verbatim; text written by us from the card (the card has no seen text).",
  "One sentence shows who will make it",
  "I can now tell if an employee's going to make it from one sentence, and it's what they say when something breaks."),
 ("A6","strong","refbank yt-noahkagan-tire-shop (13.0x, 8.4M plays). Spoken verbatim; text from the card's title.",
  "Fined, conned, back at the tire shop",
  "Age 18 I started my own business selling nuts door-to-door."),
 ("W1","weak","Our own weakest graded: W1-02 v7 R1a (graders: n/a, B-, B- / n/a, C, B-).",
  "A buyer wrote this line, not a marketer.",
  "A buyer already wrote that line. That's why you stopped."),
 ("W2","weak","Our own weakest graded: W9-01 v5 A (both graders: B- text, B- spoken).",
  "One big client left. Half your month went with them.",
  "One client leaves, and your month goes with them. Here's why."),
 ("W3","weak","Our own weakest graded: W4-01 v5 B (graders: C+, A- / B-, A-). Text C+/B-.",
  "Likes but no bookings? Read where your post sends them.",
  "Your post talks about slow months. Your page just says welcome."),
 ("W4","weak","Built from the skill's anti-patterns (age/category label as text, 'doctors won't tell you', conspiracy). Skill says these died in 2 to 3 days. Written by us for this buyer.",
  "CONSULTANTS OVER 40",
  "Gurus won't tell you why your pipeline is dry, but I will."),
 ("W5","weak","Built from the skill's anti-patterns (bait words, 'hack', throat-clearing, generic). Written by us for this buyer.",
  "SHOCKING client hack. Wait for it!",
  "So basically, I want to talk about something that's a total game changer for getting clients."),
 ("W6","weak","Built from the skill's loser example ('a burnt-out mom' lost; generic person, generic fear, a list). Written by us for this buyer.",
  "Struggling with your business?",
  "A burnt-out business owner who is tired, stressed, behind on everything and out of ideas."),
]

BUYER = {
 "A1":"Ambitious small-business owners and aspiring founders on Instagram or YouTube Shorts.",
 "A2":"People who sell services (consultants, agencies, coaches) and lose deals on price.",
 "A3":"Creatives and small-business owners who want to learn marketing.",
 "A4":"Employees with a full-time job who want a side income using AI.",
 "A5":"Managers and business owners who have employees.",
 "A6":"Aspiring entrepreneurs who like founder stories.",
}
OURS = "Owners of one-person or small service businesses (consultants, coaches, small agencies), late 30s to mid 40s, who get clients by referral and LinkedIn, with lumpy months and no predictable way to get the next client."

def write(folder, seed=11, buyer=False):
    folder = pathlib.Path(folder); folder.mkdir(parents=True, exist_ok=True)
    order = STACKS[:]; random.Random(seed).shuffle(order)
    lines = ["# Stacks to grade (words only: the visual was not made for any of them, write \"n/a\" for visual)\n"]
    key = {}
    for i,(sid,kind,src,t,s) in enumerate(order,1):
        label = f"S{i:02d}"
        key[label] = {"id":sid,"kind":kind,"source":src,"text":t,"spoken":s}
        lines.append(f"## {label}\n" + (f"- TARGET BUYER: {BUYER.get(sid, OURS)}\n" if buyer else "") + f"- VISUAL: frame not made yet\n- TEXT: \"{t}\"\n- SPOKEN: \"{s}\"\n")
    (folder/"stacks.md").write_text("\n".join(lines))
    return key

if __name__ == "__main__":
    key = write(sys.argv[1], buyer=len(sys.argv)>3)
    pathlib.Path(sys.argv[2]).write_text(json.dumps(key, indent=1))
