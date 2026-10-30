"""Run the pinned HyperFrames CLI the way setup.sh says: no telemetry, no skills update, the preinstalled browser."""
import os
import subprocess

HF_VERSION = "0.8.150"
BROWSER = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"


def env():
    e = dict(os.environ, HYPERFRAMES_NO_TELEMETRY="1", DO_NOT_TRACK="1", HYPERFRAMES_SKIP_SKILLS="1")
    if os.path.exists(BROWSER):
        e.setdefault("HYPERFRAMES_BROWSER_PATH", BROWSER)
    return e


def cmd(*args):
    return ["npx", "-y", f"hyperframes@{HF_VERSION}", *[str(a) for a in args]]


def run(*args, cwd=None, log=None):
    """Run a hyperframes command; spinner output goes to `log` (a path) instead of the terminal."""
    out = open(log, "w") if log else subprocess.DEVNULL
    try:
        r = subprocess.run(cmd(*args), cwd=cwd, env=env(), stdout=out, stderr=subprocess.STDOUT)
    finally:
        if log:
            out.close()
    if r.returncode:
        raise RuntimeError(f"hyperframes {args[0]} failed (exit {r.returncode}); log: {log}")
    return r


def render(project, out, quality="looks", fps=None, log=None):
    args = ["render", project, "-o", out, "--quality", quality, "--video-frame-format", "png", "--quiet"]
    if fps:
        args += ["--fps", fps]
    return run(*args, log=log)


def remove_background(src, out, log=None):
    return run("remove-background", src, "-o", out, "--quality", "best", log=log)
