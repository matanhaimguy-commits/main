import { IG_ID, PAGE_ID } from './fixtures';

// Webhook payloads as Meta sends them.

const nowSec = () => Math.floor(Date.now() / 1000);

export function fbComment(o: { id: string; post?: string; parent?: string; from?: string; text: string; verb?: string }) {
  const post = o.post ?? `${PAGE_ID}_POST_A`;
  return {
    object: 'page',
    entry: [
      {
        id: PAGE_ID,
        time: nowSec(),
        changes: [
          {
            field: 'feed',
            value: {
              item: 'comment',
              verb: o.verb ?? 'add',
              comment_id: o.id,
              post_id: post,
              parent_id: o.parent ?? post,
              from: { id: o.from ?? 'FB_USER_1', name: 'Dana Levi' },
              message: o.text,
              created_time: nowSec(),
            },
          },
        ],
      },
    ],
  };
}

export function igComment(o: { id: string; media?: string; from?: string; username?: string; text: string; parent?: string }) {
  return {
    object: 'instagram',
    entry: [
      {
        id: IG_ID,
        time: nowSec(),
        changes: [
          {
            field: 'comments',
            value: {
              id: o.id,
              text: o.text,
              from: { id: o.from ?? 'IG_USER_1', username: o.username ?? 'dana' },
              media: { id: o.media ?? 'MEDIA_A', media_product_type: 'REELS' },
              ...(o.parent ? { parent_id: o.parent } : {}),
            },
          },
        ],
      },
    ],
  };
}

export function igMessaging(items: Record<string, unknown>[]) {
  return { object: 'instagram', entry: [{ id: IG_ID, time: Date.now(), messaging: items }] };
}

export const igText = (from: string, mid: string, text: string, extra: Record<string, unknown> = {}) => ({
  sender: { id: from },
  recipient: { id: IG_ID },
  timestamp: Date.now(),
  message: { mid, text, ...extra },
});

export const igPostback = (from: string, mid: string, payload: string, title = 'Send it to me') => ({
  sender: { id: from },
  recipient: { id: IG_ID },
  timestamp: Date.now(),
  postback: { mid, payload, title },
});

export const igEcho = (to: string, mid: string, text: string, appId?: string) => ({
  sender: { id: IG_ID },
  recipient: { id: to },
  timestamp: Date.now(),
  message: { mid, text, is_echo: true, ...(appId ? { app_id: appId } : {}) },
});
