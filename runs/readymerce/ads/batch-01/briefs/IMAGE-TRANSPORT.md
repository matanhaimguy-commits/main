# IMAGE-TRANSPORT — how renders get from Higgsfield to this repo (verified 2026-09-25T00:58Z)

The render CDN (d8j0ntlcm91z4.cloudfront.net) is blocked from this container, but the Higgsfield sandbox (`mcp__Higgs__sandbox_exec`) has internet and ImageMagick/Pillow. Verified round trip: sandbox `curl` → `convert -resize` → `base64 -w 76` on stdout → local `base64 -d` heredoc → md5 identical → the JPEG opens and is viewable with the Read tool.

Per image (one sandbox call, then one local Bash call):
1. sandbox: `cd /home/user && curl -sS -f -o in.png '<rawUrl>' && identify -format '%wx%h' in.png && echo && convert in.png -resize 800x800 -quality 74 out.jpg && md5sum out.jpg && wc -c < out.jpg && echo BEGIN && base64 -w 76 out.jpg && echo END` (≈60–90 KB base64 for an 800 px JPEG; keep every base64 line intact).
2. local: `base64 -d > images/<id>.jpg <<'EOF' … EOF` then `md5sum` must match, then `python3 -c "from PIL import Image; print(Image.open('images/<id>.jpg').size)"`.
3. Record in the ledger: the full-resolution rawUrl and job_id (the operator downloads full size from the Higgsfield workspace), the actual pixel dimensions of the render (from `identify`), and the local proof copy path.
4. QA = open the local JPEG with the Read tool and check: every manifest string present and spelled right, no invented text, product fidelity (V1 only), the ratio (from `identify`, not the filename), phone-size readability. Mark qa.status pass/fail with notes. Never mark pass without looking.
