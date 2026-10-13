import { describe, expect, it } from 'vitest';
import { parseWebhook, sign, verifyHandshake, verifySignature } from '../src/meta/webhook.js';
import { categorize } from '../src/meta/client.js';
import { clampText, fitsLimit } from '../src/meta/messages.js';
import { APP_SECRET, IG_ID, PAGE_ID, VERIFY_TOKEN } from './fixtures.js';

describe('signature and handshake', () => {
  const body = JSON.stringify({ object: 'page', entry: [{ id: PAGE_ID, text: 'שלום \u{1F600}' }] });

  it('accepts a correctly signed body and rejects anything else', () => {
    expect(verifySignature(body, sign(body, APP_SECRET), APP_SECRET)).toBe(true);
    expect(verifySignature(body, sign(body, 'wrong'), APP_SECRET)).toBe(false);
    expect(verifySignature(body + ' ', sign(body, APP_SECRET), APP_SECRET)).toBe(false);
    expect(verifySignature(body, undefined, APP_SECRET)).toBe(false);
    expect(verifySignature(body, 'sha256=zz', APP_SECRET)).toBe(false);
  });

  it('echoes the challenge only for the right verify token', () => {
    expect(verifyHandshake({ 'hub.mode': 'subscribe', 'hub.verify_token': VERIFY_TOKEN, 'hub.challenge': '42' }, VERIFY_TOKEN)).toBe('42');
    expect(verifyHandshake({ 'hub.mode': 'subscribe', 'hub.verify_token': 'nope', 'hub.challenge': '42' }, VERIFY_TOKEN)).toBeUndefined();
    expect(verifyHandshake({ 'hub.verify_token': VERIFY_TOKEN, 'hub.challenge': '42' }, VERIFY_TOKEN)).toBeUndefined();
  });
});

describe('parseWebhook', () => {
  it('parses a Facebook feed comment', () => {
    const [ev] = parseWebhook({
      object: 'page',
      entry: [
        {
          id: PAGE_ID,
          time: 1_760_000_000,
          changes: [
            {
              field: 'feed',
              value: {
                item: 'comment',
                verb: 'add',
                comment_id: `${PAGE_ID}_42_7`,
                post_id: `${PAGE_ID}_42`,
                parent_id: `${PAGE_ID}_42`,
                from: { id: '555', name: 'Dana' },
                message: 'GUIDE',
                created_time: 1_760_000_000,
              },
            },
          ],
        },
      ],
    });
    expect(ev).toMatchObject({
      type: 'comment',
      platform: 'facebook',
      accountId: PAGE_ID,
      commentId: `${PAGE_ID}_42_7`,
      postId: `${PAGE_ID}_42`,
      parentId: `${PAGE_ID}_42`,
      authorId: '555',
      authorName: 'Dana',
      text: 'GUIDE',
      verb: 'add',
    });
    expect((ev as any).createdAt.getTime()).toBe(1_760_000_000_000);
  });

  it('ignores non-comment feed items (posts, reactions)', () => {
    const events = parseWebhook({
      object: 'page',
      entry: [{ id: PAGE_ID, changes: [{ field: 'feed', value: { item: 'reaction', verb: 'add', post_id: 'x' } }] }],
    });
    expect(events).toEqual([]);
  });

  it('parses an Instagram comment, with id or comment_id', () => {
    const value = { from: { id: '178000', username: 'dana' }, media: { id: 'MEDIA_A', media_product_type: 'REELS' }, text: 'מדריך' };
    for (const idKey of ['id', 'comment_id']) {
      const [ev] = parseWebhook({
        object: 'instagram',
        entry: [{ id: IG_ID, time: 1_760_000_000, changes: [{ field: 'comments', value: { ...value, [idKey]: 'IGC1' } }] }],
      });
      expect(ev).toMatchObject({
        type: 'comment',
        platform: 'instagram',
        accountId: IG_ID,
        commentId: 'IGC1',
        postId: 'MEDIA_A',
        authorId: '178000',
        authorName: 'dana',
        text: 'מדריך',
        mediaProductType: 'REELS',
      });
    }
  });

  it('parses messages, story replies, echoes, postbacks and receipts', () => {
    const events = parseWebhook({
      object: 'instagram',
      entry: [
        {
          id: IG_ID,
          time: 1_760_000_000_000,
          messaging: [
            { sender: { id: 'U1' }, recipient: { id: IG_ID }, timestamp: 1_760_000_000_000, message: { mid: 'm1', text: 'hi' } },
            {
              sender: { id: 'U1' },
              recipient: { id: IG_ID },
              timestamp: 1_760_000_001_000,
              message: { mid: 'm2', text: 'guide', reply_to: { story: { id: 'S1', url: 'https://cdn/x' } } },
            },
            { sender: { id: IG_ID }, recipient: { id: 'U1' }, timestamp: 1, message: { mid: 'm3', text: 'yo', is_echo: true, app_id: 123 } },
            { sender: { id: 'U1' }, recipient: { id: IG_ID }, timestamp: 2, postback: { title: 'Send it', payload: 'F|guide|deliver', mid: 'p1' } },
            { sender: { id: 'U1' }, recipient: { id: IG_ID }, timestamp: 3, read: { mid: 'm3' } },
          ],
          standby: [{ sender: { id: 'U2' }, recipient: { id: IG_ID }, timestamp: 4, message: { mid: 'm4', text: 'other app' } }],
        },
      ],
    });
    expect(events.map((e) => e.type)).toEqual(['message', 'message', 'message', 'postback', 'read', 'message']);
    expect(events[1]).toMatchObject({ storyReply: { id: 'S1' }, text: 'guide' });
    expect(events[2]).toMatchObject({ isEcho: true, appId: '123', senderId: IG_ID, recipientId: 'U1' });
    expect(events[3]).toMatchObject({ payload: 'F|guide|deliver', mid: 'p1' });
    expect(events[4]).toMatchObject({ mids: ['m3'] });
    expect(events[5]).toMatchObject({ standby: true, mid: 'm4' });
  });

  it('parses Facebook delivery and read watermarks', () => {
    const events = parseWebhook({
      object: 'page',
      entry: [
        {
          id: PAGE_ID,
          messaging: [
            { sender: { id: 'P1' }, recipient: { id: PAGE_ID }, timestamp: 5, delivery: { mids: ['m1'], watermark: 1_760_000_000_000 } },
            { sender: { id: 'P1' }, recipient: { id: PAGE_ID }, timestamp: 6, read: { watermark: 1_760_000_000_500 } },
          ],
        },
      ],
    });
    expect(events[0]).toMatchObject({ type: 'delivery', mids: ['m1'] });
    expect((events[1] as any).watermark.getTime()).toBe(1_760_000_000_500);
  });

  it('drops unknown objects', () => {
    expect(parseWebhook({ object: 'whatsapp_business_account', entry: [] })).toEqual([]);
    expect(parseWebhook({})).toEqual([]);
  });
});

describe('error categories', () => {
  it('maps documented codes', () => {
    expect(categorize(190)).toBe('token');
    expect(categorize(100, 2534025)).toBe('comment_ineligible');
    expect(categorize(10900)).toBe('already_replied');
    expect(categorize(10, 2018278)).toBe('outside_window');
    expect(categorize(10, 2018108)).toBe('user_unavailable');
    expect(categorize(200, 2018028)).toBe('permission');
    expect(categorize(613, 2534040)).toBe('rate_limit');
    expect(categorize(368, 1404169)).toBe('spam_block');
    expect(categorize(2018300)).toBe('thread_owner');
  });
});

describe('text limits', () => {
  it('counts Instagram text in bytes', () => {
    const hebrew = 'ש'.repeat(600); // 1200 bytes
    expect(fitsLimit(hebrew, 'instagram', false)).toBe(false);
    expect(fitsLimit(hebrew, 'facebook', false)).toBe(true);
    const clamped = clampText(hebrew, 'instagram', false);
    expect(new TextEncoder().encode(clamped).length).toBeLessThanOrEqual(1000);
    expect(clamped.endsWith('…')).toBe(true);
  });
});
