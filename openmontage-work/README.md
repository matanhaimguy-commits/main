# OpenMontage work (saved from a cloud session)

`OpenMontage/` itself is a fresh clone of https://github.com/calesthio/OpenMontage
and is git-ignored. This folder keeps what cannot be re-downloaded.

## Restore on a new machine
1. `git clone https://github.com/calesthio/OpenMontage.git OpenMontage && cd OpenMontage && make setup`
2. Voice (only if huggingface.co is blocked): download
   `https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-lessac-medium.tar.gz`,
   extract, and save the two files in `OpenMontage/` as `en_US-lessac-medium.onnx` and
   `en_US-lessac-medium.onnx.json`. Run OpenMontage with `.venv` activated so `piper` is found.
3. `npx hyperframes browser ensure` (headless browser for rendering).
4. Only behind a proxy that blocks remotion.media: copy `setup-fixes/remotion-composer/*`
   (including `.local/`) into `OpenMontage/remotion-composer/`.
5. Copy `projects/why-the-sky-is-blue` into `OpenMontage/projects/`.

## Status of "Why Is the Sky Blue?" (animated-explainer pipeline)
research done -> proposal done -> **script awaiting user approval** -> storyboard next.
