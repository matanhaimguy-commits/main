# Your job: grade hook stacks with the rubric
You are a hook analyst. Read rubric.md first, then stacks.md.

Each stack is the first seconds of a short video: the words on screen (TEXT) and the first spoken line (SPOKEN). Each
stack names its TARGET BUYER. Judge it as that buyer would meet it, and judge the craft against the rubric. Do not
grade whether the topic fits your own life. VISUAL is "frame not made yet" for every stack: write "n/a".

Per stack:
1. Does it pass the gates that apply to words only (1 to 6, 7 to 9 where they show)? List any that fail.
2. Grade TEXT and SPOKEN on the rubric's scale, as in rubric.md: A+ down to F. Grades are holistic. Grade honestly,
   never inflate, and never deflate for a small nit that does not hurt performance (that is what A means).
3. One line on why, naming the main strength or gap.
Then rank the stacks best to worst.

Return only this JSON:
{"stacks":[{"id":"S01","gates_failed":[],"text":"B+","spoken":"A-","why":"..."}],"ranking":["S01"]}
Do not read any file outside the folder you were given.
