// Finds the preinstalled Chrome headless shell, newest version first. The version folder changes between
// containers (1194 on 12 Oct, 1243 on 5 Nov), so never hard-code it.
//   import { headlessShell } from './browser_path.mjs';  headlessShell() -> path or undefined
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = '/opt/pw-browsers';
const BINARIES = ['chrome-headless-shell-linux64/chrome-headless-shell', 'chrome-linux/headless_shell'];

export function headlessShell(root = ROOT) {
  if (!existsSync(root)) return undefined;
  const dirs = readdirSync(root).filter((d) => d.startsWith('chromium_headless_shell-'))
    .sort((a, b) => Number(b.split('-').pop()) - Number(a.split('-').pop()));
  for (const d of dirs) for (const b of BINARIES) if (existsSync(join(root, d, b))) return join(root, d, b);
  return undefined;
}
