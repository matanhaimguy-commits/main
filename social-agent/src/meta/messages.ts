import type { Platform } from '../config/schema.js';

export type Button = { title: string; url: string } | { title: string; payload: string };

export interface OutboundMessage {
  text: string;
  button?: Button;
}

// Limits: Messenger text 2000 characters; Instagram text 1000 BYTES (Hebrew letters are 2
// bytes each, emoji 4); button-template text 640 characters.
const utf8 = new TextEncoder();

export function fitsLimit(text: string, platform: Platform, withButton: boolean): boolean {
  if (withButton) return [...text].length <= 640;
  if (platform === 'instagram') return utf8.encode(text).length <= 1000;
  return [...text].length <= 2000;
}

export function clampText(text: string, platform: Platform, withButton: boolean): string {
  const t = text.trim();
  if (fitsLimit(t, platform, withButton)) return t;
  const chars = [...t];
  // Shrink until it fits with the ellipsis appended.
  let lo = 0;
  let hi = chars.length;
  while (lo < hi) {
    const mid = Math.ceil((lo + hi) / 2);
    if (fitsLimit(chars.slice(0, mid).join('').trimEnd() + '…', platform, withButton)) lo = mid;
    else hi = mid - 1;
  }
  return chars.slice(0, lo).join('').trimEnd() + '…';
}

/**
 * A real button (button template) instead of quick-reply chips: messages from people who
 * don't follow you land in Message Requests, where buttons show and chips don't.
 */
export function toMetaMessage(m: OutboundMessage, platform: Platform): Record<string, unknown> {
  if (!m.button) return { text: clampText(m.text, platform, false) };
  const button =
    'url' in m.button
      ? { type: 'web_url', url: m.button.url, title: m.button.title }
      : { type: 'postback', payload: m.button.payload, title: m.button.title };
  return {
    attachment: {
      type: 'template',
      payload: {
        template_type: 'button',
        text: clampText(m.text, platform, true),
        buttons: [button],
      },
    },
  };
}

/** Plain text of an outbound message, for the transcript the AI reads. */
export function describeMessage(m: OutboundMessage): string {
  if (!m.button) return m.text;
  const target = 'url' in m.button ? ` -> ${m.button.url}` : '';
  return `${m.text}\n[button: ${m.button.title}${target}]`;
}
