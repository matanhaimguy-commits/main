import type { MetaApi } from './client.js';

// Webhook fields this app needs. Page: Facebook comments (feed) and Messenger events.
export const PAGE_FIELDS = ['feed', 'messages', 'messaging_postbacks', 'message_deliveries', 'message_reads', 'message_echoes'];
// Instagram (set on the app; every connected Instagram account receives them).
export const INSTAGRAM_FIELDS = ['comments', 'messages', 'messaging_postbacks', 'messaging_seen'];

// Permissions requested by the "Connect Facebook & Instagram" button.
export const LOGIN_SCOPES = [
  'pages_show_list',
  'pages_manage_metadata',
  'pages_messaging',
  'pages_read_engagement',
  'pages_manage_engagement',
  'instagram_basic',
  'instagram_manage_messages',
  'instagram_manage_comments',
  'business_management',
];

/** Installs this app on the Page so its events reach the webhook. Needs the Page token. */
export function subscribePage(pageApi: MetaApi, pageId: string) {
  return pageApi.post(`${pageId}/subscribed_apps`, { subscribed_fields: PAGE_FIELDS.join(',') });
}

/**
 * Registers the app-level webhooks (callback URL + fields) for Page and Instagram objects,
 * the same thing as filling in App Dashboard → Webhooks. Meta calls GET /webhook to verify
 * while this runs, so the server must already be reachable at callbackUrl.
 */
export async function subscribeApp(
  appApi: MetaApi,
  appId: string,
  callbackUrl: string,
  verifyToken: string,
): Promise<{ object: string; ok: boolean; error?: string }[]> {
  const results = [];
  for (const [object, fields] of [
    ['page', PAGE_FIELDS],
    ['instagram', INSTAGRAM_FIELDS],
  ] as const) {
    try {
      await appApi.post(`${appId}/subscriptions`, {
        object,
        callback_url: callbackUrl,
        fields: fields.join(','),
        verify_token: verifyToken,
        include_values: true,
      });
      results.push({ object, ok: true });
    } catch (err) {
      results.push({ object, ok: false, error: (err as Error).message });
    }
  }
  return results;
}
