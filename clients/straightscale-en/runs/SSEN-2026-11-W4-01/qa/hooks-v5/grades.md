# EN 06 Hook Lab v5: 2 fresh blind graders (sonnet) per round, text and spoken only
CF-V8@v1 failed G-VIS (hero, 1 major: the page card sits in the caption zone below 55%), so no visual was shown or graded.

## Round 1 (`docs/hooks-v5.json`)
| Stack | Grader 1 V/T/S | Grader 2 V/T/S |
|---|---|---|
| A "Likes, no bookings? Your post and your page don't match." / "Your post says one thing. Your page says another. Nobody books." | n/a, B, B+ | n/a, B, B |
| B "Likes but no bookings? Read where your post sends them." / "Your post talks about slow months. Your page just says welcome." | n/a, C+, A- | n/a, B-, A- |
| C "Likes, no bookings? Don't fix the post. Fix the page." / "Your post asks about slow months. Your page never answers it." | n/a, A-, A | n/a, A-, A |
Both rank C first. Shared notes: "page" is undefined (website or profile?), "bookings" sounds like a salon, not a
consultant. Result: FAIL (text A-). Round 2 swaps in "clients" and "website".

## Round 2 (`docs/hooks-v5-r2.json`)
| Stack | Grader 3 V/T/S | Grader 4 V/T/S |
|---|---|---|
| A "Likes, no clients? Don't fix the post. Fix your website." / "Your post asks about slow months. Your website never answers it." | n/a, B, B- | n/a, B, B- |
| B "Likes, no clients? Don't fix the post. Fix the website." / "Your post talks about slow months. Your website just says welcome." | n/a, B+, A- | n/a, B, B+ |
| C "Posts get likes, not clients? Fix the website first." / (A's spoken) | n/a, B, B- | n/a, B+, B- |
Both rank B first. The round 1 spoken line scored A from both graders there and B- from both here: the read varies
a lot between fresh graders. Notes: a post doesn't "ask"; "fix the website" says nothing about what is wrong;
"just says welcome" is the concrete, picturable line; text and voice should say the same thing. Result: FAIL.
Round 3 (last) puts "your website just says welcome" on screen.
