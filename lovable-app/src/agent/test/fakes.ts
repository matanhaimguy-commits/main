import type { CommentDecision, ReplyInput, ReplyResult, SalesAi } from '../ai/agent';
import { MetaApiError, MetaNetworkError, type MetaApi } from '../meta/client';
import { APP_ID } from './fixtures';

export interface Call {
  method: string;
  args: any[];
}

export class FakeMeta implements MetaApi {
  calls: Call[] = [];
  tokens: string[] = [];
  /** Queue of errors to throw on the next sendMessage calls. */
  failNext: Error[] = [];
  follows = new Map<string, boolean>();
  profiles = new Map<string, Record<string, unknown>>();
  private n = 0;

  async sendMessage(input: Parameters<MetaApi['sendMessage']>[0]) {
    this.calls.push({ method: 'sendMessage', args: [input] });
    const err = this.failNext.shift();
    if (err) throw err;
    this.n++;
    const recipient = 'comment_id' in input.recipient ? `PSID_FOR_${input.recipient.comment_id}` : input.recipient.id;
    return { recipient_id: recipient, message_id: `mid.${this.n}` };
  }
  async replyToComment(platform: string, commentId: string, text: string) {
    this.calls.push({ method: 'replyToComment', args: [platform, commentId, text] });
    return { id: `reply_${commentId}` };
  }
  async hideComment(platform: string, commentId: string, hide: boolean) {
    this.calls.push({ method: 'hideComment', args: [platform, commentId, hide] });
    return { success: true };
  }
  async getUserProfile(userId: string, fields: string[]) {
    this.calls.push({ method: 'getUserProfile', args: [userId, fields] });
    return { ...(this.profiles.get(userId) ?? {}), is_user_follow_business: this.follows.get(userId) ?? false };
  }
  /** Pages returned by me/accounts during the connect flow. */
  pages: { id: string; name: string; access_token?: string; instagram_business_account?: { id: string; username?: string } }[] = [];
  /** People Meta refuses to talk about (no Advanced Access and no role on the app). */
  refused = new Set<string>();
  async get(path: string, params?: Record<string, string>) {
    this.calls.push({ method: 'get', args: [path, params] });
    if (path.endsWith('/thread_owner') && this.refused.has(params?.recipient ?? '')) throw apiError(200, 2534048);
    if (path === 'oauth/access_token') return { access_token: params?.code ? 'SHORT_USER_TOKEN' : 'LONG_USER_TOKEN' } as any;
    if (path === 'me/accounts') return { data: this.pages } as any;
    return { data: [{ id: APP_ID }] } as any;
  }
  async post(path: string, body?: Record<string, unknown>) {
    this.calls.push({ method: 'post', args: [path, body] });
    return { success: true } as any;
  }
  sends() {
    return this.calls.filter((c) => c.method === 'sendMessage').map((c) => c.args[0]);
  }
}

export const apiError = (code: number, subcode?: number, message = 'error') => new MetaApiError(message, 400, code, subcode);
export const networkError = () => new MetaNetworkError('socket hang up');

export class FakeAi implements SalesAi {
  replies: ReplyInput[] = [];
  nextReply: Partial<ReplyResult> = { text: 'Happy to help! What are you looking for?' };
  nextDecision: CommentDecision = {
    intent: 'pricing',
    public_reply: 'Sent you a DM 🙌',
    send_dm: true,
    dm_text: 'Our ads management starts at 4,000 ILS a month. What do you sell?',
    hide: false,
    alert_owner: false,
    reason: 'asked about price',
  };
  async reply(input: ReplyInput): Promise<ReplyResult> {
    this.replies.push(input);
    return {
      text: null,
      lead: {},
      optOut: false,
      usage: { model: 'fake', inputTokens: 10, outputTokens: 5, cacheReadTokens: 0, stopReason: 'end_turn' },
      ...this.nextReply,
    };
  }
  async triageComment() {
    return { decision: this.nextDecision, usage: { model: 'fake', inputTokens: 1, outputTokens: 1, cacheReadTokens: 0, stopReason: 'end_turn' } };
  }
}
