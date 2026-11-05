// Loads the film's classic scripts into a sandbox with a fake window, so their pure parts can be tested in node.
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

export function load(files, extra = {}) {
  const window = { ...extra };
  const ctx = vm.createContext({ window, Math, JSON, Object, Array, Number, Error });
  for (const f of files) vm.runInContext(readFileSync(new URL('../' + f, import.meta.url), 'utf8'), ctx, { filename: f });
  return window.SS;
}
