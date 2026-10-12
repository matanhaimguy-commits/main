import { Config } from "@remotion/cli/config";
import fs from "fs";
import os from "os";
import path from "path";

// Local setup: this machine cannot reach remotion.media to download
// Remotion's own Chrome Headless Shell, so reuse a headless shell that is
// already installed (HyperFrames' cache, or the preinstalled Playwright one).
// Set REMOTION_BROWSER_EXECUTABLE to override.
const candidates = [
  process.env.REMOTION_BROWSER_EXECUTABLE,
  ...(() => {
    const root = path.join(os.homedir(), ".cache/hyperframes/chrome/chrome-headless-shell");
    try {
      return fs
        .readdirSync(root)
        .sort()
        .reverse()
        .map((v) => path.join(root, v, "chrome-headless-shell-linux64/chrome-headless-shell"));
    } catch {
      return [];
    }
  })(),
  "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
].filter((p): p is string => Boolean(p));

const browser = candidates.find((p) => fs.existsSync(p));
if (browser) {
  // Remotion forces "--no-proxy-server"; when an HTTPS proxy is required,
  // launch through a wrapper that routes Chrome via the proxy instead.
  const wrapper = [process.cwd(), __dirname]
    .map((d) => path.join(d, ".local/chrome-via-proxy.sh"))
    .find((p) => fs.existsSync(p));
  if ((process.env.HTTPS_PROXY || process.env.https_proxy) && wrapper) {
    process.env.REAL_CHROME = browser;
    Config.setBrowserExecutable(wrapper);
  } else {
    Config.setBrowserExecutable(browser);
  }
}
