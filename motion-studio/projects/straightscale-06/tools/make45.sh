#!/usr/bin/env bash
# Builds the 4:5 HyperFrames project (film-4x5/) from the 9:16 master page. Same code and timeline: the page picks
# its 4:5 layout table from the root size, so this is a native re-layout, not a crop. HyperFrames allows one root
# composition per project, hence the second folder.   bash tools/make45.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p film-4x5
rm -rf film-4x5/assets && cp -r film/assets film-4x5/assets && cp film/hyperframes.json film/package.json film-4x5/
printf '{\n  "id": "film-4x5",\n  "name": "film-4x5"\n}\n' > film-4x5/meta.json
sed -e 's/data-height="1920"/data-height="1350"/' \
    -e 's/content="width=1080, height=1920"/content="width=1080, height=1350"/' \
    -e 's/html, body { margin: 0; width: 1080px; height: 1920px;/html, body { margin: 0; width: 1080px; height: 1350px;/' \
    -e 's/ data-resolution="portrait"//' \
    film/index.html > film-4x5/index.html
grep -c 'data-height="1350"' film-4x5/index.html
