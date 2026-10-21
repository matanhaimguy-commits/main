# Image review packet, same logic as growth-engine/tools/vqa_crops.py cmd_image (full, 3x3 tiles at 2x, a 2x crop per
# spec region with 3% pad, 200 px thumb, manifest.json with must_open). For the Higgsfield sandbox, which has no PyYAML:
# usage: python3 vqa_image.py <src.png> <out_dir> <regions.json> <png|jpg>
import json, sys
from pathlib import Path
from PIL import Image
src, out, spec_p, ext, hero = sys.argv[1], Path(sys.argv[2]), sys.argv[3], sys.argv[4], True
specs = [json.loads(Path(spec_p).read_text())]
out.mkdir(parents=True, exist_ok=True)
im = Image.open(src).convert("RGB"); w, h = im.size
files, must = [], []
def up2(i): return i.resize((i.width * 2, i.height * 2), Image.LANCZOS)
def save(img, name, required=True):
    if ext != "png": name = name.rsplit(".", 1)[0] + "." + ext
    p = out / name
    img.save(p, quality=88) if ext == "jpg" else img.save(p)
    files.append(name)
    if required: must.append(name)
    return p
save(im, "full.png")
for r in range(3):
    for c in range(3):
        box = (c * w // 3, r * h // 3, (c + 1) * w // 3, (r + 1) * h // 3)
        save(up2(im.crop(box)), f"tile_r{r + 1}c{c + 1}.png")
for s in specs:
    for rg in s.get("regions") or []:
        x0, y0, x1, y1 = rg["box"]; pad = 0.03
        box = (int(max(0, x0 - pad) * w), int(max(0, y0 - pad) * h), int(min(1, x1 + pad) * w), int(min(1, y1 + pad) * h))
        save(up2(im.crop(box)), f"region_{s.get('shot_id', 'shot')}_{rg['name']}.png")
thumb = im.copy(); thumb.thumbnail((200, 200 * h // w)); save(thumb, "thumb_200.png", required=hero)
man = {"kind": "image", "source": src, "size": [w, h], "hero": hero, "files": files, "must_open": must, "panels": 0, "ocr": None, "ocr_note": None}
(out / "manifest.json").write_text(json.dumps(man, indent=2, ensure_ascii=False))
