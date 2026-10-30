# Your job: a blind clarity read of hook stacks (you never saw how they were made)
Each stack is the first 1 to 3 seconds of a different Instagram Reel:
- VISUAL: frame 1, as an image file with the on-screen text already laid on it (open the full image AND the
  360 px wide "_phone" copy: that is the real size on a phone). If a stack says "frame not made yet", do not grade
  the visual: write "n/a".
- TEXT: the words on screen from frame 1 (also visible in the image).
- SPOKEN: the first spoken line, heard from 0.0 s when the sound is on.
Read persona.md first and answer as that person.

Per stack, answer:
1. That's me / half / not me (2 seconds, sound off).
2. In one sentence: what do you think this reel is about?
3. What do you expect the rest of the reel to show or tell you?
4. Would you keep watching past 2 seconds? yes / maybe / no, and why in one line.
5. Any word or phrase that was unclear, could be read two ways, or sounds like something nobody says out loud.
6. A grade per channel (VISUAL, TEXT, SPOKEN) on this scale: A+ (every principle firing), A (strong, only a minor
   tradeoff), A- (strong, one fixable weakness: name it), B+ (would perform, 1 to 2 clear gaps), B, B-, C, D, F.
   The bar is "clear, concise, and makes me want to watch the whole reel". Clarity matters most. Be strict: never
   inflate. For anything below A, name the exact weakness and the smallest fix.
Then rank the stacks best to worst.

Return your answer as JSON:
{"stacks":[{"id":"...","me":"...","about":"...","expect":"...","keep_watching":"...","unclear":"...",
 "visual":"A-","text":"A","spoken":"A","weakness":"...","fix":"..."}],"ranking":["..."]}
Write nothing else. Do not read any file outside the folder you were given.
