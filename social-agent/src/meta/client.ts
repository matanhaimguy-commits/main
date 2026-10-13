import type { Platform } from '../config/schema.js';

export type ErrorCategory =
  | 'token' // token expired / revoked / password changed: everything for this Page will fail
  | 'permission' // missing permission, feature not approved, or app not Live
  | 'already_replied' // the one private reply for this comment was already used (by us or another tool)
  | 'comment_ineligible' // too old, deleted, or the person's settings block private replies
  | 'outside_window' // DM outside the 24h window
  | 'user_unavailable' // person blocked the Page, deleted the account, or isn't receiving messages from you
  | 'thread_owner' // another app (e.g. ManyChat) controls this conversation
  | 'spam_block' // Meta temporarily blocked sending as spam: stop and back off
  | 'rate_limit'
  | 'invalid_request'
  | 'unknown';

export class MetaApiError extends Error {
  constructor(
    message: string,
    readonly status: number,
    readonly code?: number,
    readonly subcode?: number,
    readonly type?: string,
    readonly fbtraceId?: string,
  ) {
    super(message);
    this.name = 'MetaApiError';
  }

  get category(): ErrorCategory {
    return categorize(this.code, this.subcode, this.message);
  }
}

/** The request may or may not have reached Meta (timeout, connection reset). Never retry. */
export class MetaNetworkError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'MetaNetworkError';
  }
}

export function categorize(code?: number, subcode?: number, message = ''): ErrorCategory {
  const m = message.toLowerCase();
  if (code === 190 || code === 102 || code === 463 || code === 467) return 'token';
  if (code === 368) return 'spam_block';
  if (code === 10900 || subcode === 2534023 || /already replied|already has a reply/.test(m)) return 'already_replied';
  if (subcode === 2534025 || subcode === 1893049 || code === 10903) return 'comment_ineligible';
  if (subcode === 2018278 || subcode === 2534022) return 'outside_window';
  if (subcode === 2018108 || code === 551 || subcode === 1545041) return 'user_unavailable';
  if (code === 2018300 || subcode === 2534037) return 'thread_owner';
  if (code === 4 || code === 17 || code === 32 || code === 613 || (code !== undefined && code >= 80000 && code < 80100)) {
    return 'rate_limit';
  }
  if (/outside of allowed window|outside the allowed window|messaging window/.test(m)) return 'outside_window';
  if (code === 10 || code === 3 || code === 230 || (code !== undefined && code >= 200 && code < 300)) return 'permission';
  if (code === 100) return 'invalid_request';
  return 'unknown';
}

export interface SendResponse {
  recipient_id?: string;
  message_id?: string;
}

export interface MetaApi {
  /** POST /{page-id}/messages. recipient is {id} for a DM or {comment_id} for a private reply. */
  sendMessage(input: {
    pageId: string;
    recipient: { id: string } | { comment_id: string };
    message: Record<string, unknown>;
    messagingType?: 'RESPONSE' | 'MESSAGE_TAG' | 'UPDATE';
    tag?: string;
  }): Promise<SendResponse>;
  /** Public reply under a comment. */
  replyToComment(platform: Platform, commentId: string, text: string): Promise<{ id?: string }>;
  hideComment(platform: Platform, commentId: string, hide: boolean): Promise<unknown>;
  /** Instagram User Profile API / Messenger user profile. Only works after the person messaged you. */
  getUserProfile(userId: string, fields: string[]): Promise<Record<string, unknown>>;
  get<T = any>(path: string, params?: Record<string, string>): Promise<T>;
  post<T = any>(path: string, body?: Record<string, unknown>): Promise<T>;
}

export interface MetaClientOptions {
  accessToken: string;
  version: string;
  fetchImpl?: typeof fetch;
  timeoutMs?: number;
  baseUrl?: string;
}

export function createMetaClient(opts: MetaClientOptions): MetaApi {
  const doFetch = opts.fetchImpl ?? fetch;
  const base = `${opts.baseUrl ?? 'https://graph.facebook.com'}/${opts.version}`;
  const timeoutMs = opts.timeoutMs ?? 20_000;

  async function request<T>(method: 'GET' | 'POST', path: string, params?: Record<string, unknown>): Promise<T> {
    const url = new URL(`${base}/${path.replace(/^\//, '')}`);
    let body: string | undefined;
    if (method === 'GET') {
      for (const [k, v] of Object.entries(params ?? {})) url.searchParams.set(k, String(v));
    } else {
      body = JSON.stringify(params ?? {});
    }
    let res: Response;
    try {
      res = await doFetch(url, {
        method,
        headers: {
          ...(opts.accessToken ? { Authorization: `Bearer ${opts.accessToken}` } : {}),
          ...(body ? { 'Content-Type': 'application/json' } : {}),
        },
        body,
        signal: AbortSignal.timeout(timeoutMs),
      });
    } catch (err) {
      throw new MetaNetworkError(`${method} ${path}: ${(err as Error).message}`);
    }
    const text = await res.text();
    let json: any;
    try {
      json = text ? JSON.parse(text) : {};
    } catch {
      if (!res.ok) throw new MetaApiError(`HTTP ${res.status}: ${text.slice(0, 200)}`, res.status);
      throw new MetaNetworkError(`${method} ${path}: unparseable response`);
    }
    if (!res.ok || json?.error) {
      const e = json?.error ?? {};
      throw new MetaApiError(
        e.error_user_msg || e.message || `HTTP ${res.status}`,
        res.status,
        e.code,
        e.error_subcode,
        e.type,
        e.fbtrace_id,
      );
    }
    return json as T;
  }

  return {
    get: (path, params) => request('GET', path, params),
    post: (path, body) => request('POST', path, body),

    sendMessage({ pageId, recipient, message, messagingType, tag }) {
      const body: Record<string, unknown> = { recipient, message };
      // Private replies (recipient.comment_id) take no messaging_type.
      if ('id' in recipient) body.messaging_type = messagingType ?? 'RESPONSE';
      if (tag) body.tag = tag;
      return request<SendResponse>('POST', `${pageId}/messages`, body);
    },

    replyToComment(platform, commentId, text) {
      // Facebook: POST /{comment-id}/comments. Instagram: POST /{ig-comment-id}/replies.
      const edge = platform === 'instagram' ? 'replies' : 'comments';
      return request('POST', `${commentId}/${edge}`, { message: text });
    },

    hideComment(platform, commentId, hide) {
      return request('POST', commentId, platform === 'instagram' ? { hide } : { is_hidden: hide });
    },

    getUserProfile(userId, fields) {
      return request('GET', userId, { fields: fields.join(',') });
    },
  };
}
