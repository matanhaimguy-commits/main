/** The choices after tapping `label`: multi-select toggles it; single-select picks it (or clears it on a second tap). */
export function pick(choices: string[], label: string, multi: boolean): string[] {
  if (multi) return choices.includes(label) ? choices.filter((c) => c !== label) : [...choices, label];
  return choices.length === 1 && choices[0] === label ? [] : [label];
}

/** An answer needs a choice or a note. */
export const canSend = (choices: string[], note: string) => choices.length > 0 || note.trim().length > 0;
