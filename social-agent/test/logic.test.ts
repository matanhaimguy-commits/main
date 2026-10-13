import { describe, expect, it } from 'vitest';
import { matchesKeyword, normalize, pickVariant } from '../src/logic/text.js';
import { decodePayload, encodePayload, selectCommentFunnel, selectMessageFunnel } from '../src/logic/funnels.js';
import { isAllowedRecipient, isReply, screenComment } from '../src/logic/comments.js';
import { auditBusiness, blocksLive, riskyMatches } from '../src/logic/audit.js';
import { toMetaMessage } from '../src/meta/messages.js';
import type { CommentEvent } from '../src/meta/webhook.js';
import { IG_ID, PAGE_ID, makeBusiness } from './fixtures.js';

describe('normalize / matchesKeyword', () => {
  it('ignores case, emoji, punctuation and niqqud', () => {
    expect(normalize('  GUIDE!!! 🔥🔥 ')).toBe('guide');
    expect(normalize('מַדְרִיךְ')).toBe('מדריך');
    expect(normalize('צ׳יפס')).toBe('ציפס');
  });

  it('exact needs the whole comment to be the keyword', () => {
    expect(matchesKeyword('Guide 🙏', 'guide', 'exact')).toBe(true);
    expect(matchesKeyword('send me the guide', 'guide', 'exact')).toBe(false);
  });

  it('word matches whole words only', () => {
    expect(matchesKeyword('Send me the GUIDE please', 'guide', 'word')).toBe(true);
    expect(matchesKeyword('these guidelines are great', 'guide', 'word')).toBe(false);
    expect(matchesKeyword('I want the free guide now', 'free guide', 'word')).toBe(true);
  });

  it('word matches Hebrew keywords with attached prefixes', () => {
    expect(matchesKeyword('אשמח למדריך', 'מדריך', 'word')).toBe(true);
    expect(matchesKeyword('והמדריך!', 'מדריך', 'word')).toBe(true);
    expect(matchesKeyword('מדריכה מעולה', 'מדריך', 'word')).toBe(false);
    expect(matchesKeyword('אבמדריך', 'מדריך', 'word')).toBe(false);
  });

  it('contains matches inside other words', () => {
    expect(matchesKeyword('these guidelines', 'guide', 'contains')).toBe(true);
  });

  it('pickVariant is deterministic', () => {
    expect(pickVariant(['a', 'b', 'c'], 'x')).toBe(pickVariant(['a', 'b', 'c'], 'x'));
    expect(pickVariant([], 'x')).toBeUndefined();
  });
});

describe('selectCommentFunnel', () => {
  const pinned = { id: 'pinned', posts: ['P1'], keywords: ['guide'], opener: { text: 'a', button: 'b' }, deliver: { text: 'c', link: 'https://x.io', button: 'd' } };
  const catchAll = { ...pinned, id: 'catch-all', posts: [], all_posts: true, all_posts_acknowledged: true, keywords: ['guide', 'price'] };

  it('a pinned funnel beats a catch-all, and the catch-all stays silent on that post', () => {
    const b = makeBusiness({ funnels: [catchAll, pinned] });
    const hit = selectCommentFunnel(b.funnels, { platform: 'instagram', postId: 'P1', text: 'guide' });
    expect(hit.kind === 'matched' && hit.funnel.id).toBe('pinned');
    const miss = selectCommentFunnel(b.funnels, { platform: 'instagram', postId: 'P1', text: 'price?' });
    expect(miss).toMatchObject({ kind: 'skipped', reason: 'keyword_not_matched' });
  });

  it('a catch-all handles posts without a pinned funnel', () => {
    const b = makeBusiness({ funnels: [catchAll, pinned] });
    const hit = selectCommentFunnel(b.funnels, { platform: 'facebook', postId: 'OTHER', text: 'price' });
    expect(hit.kind === 'matched' && hit.funnel.id).toBe('catch-all');
  });

  it('a paused funnel stops, it does not fall through', () => {
    const b = makeBusiness({
      funnels: [{ ...pinned, status: 'paused' }, { ...pinned, id: 'second' }],
    });
    const d = selectCommentFunnel(b.funnels, { platform: 'instagram', postId: 'P1', text: 'guide' });
    expect(d).toMatchObject({ kind: 'skipped', reason: 'funnel_paused' });
    expect(d.kind === 'skipped' && d.funnel?.id).toBe('pinned');
  });

  it('reports posts with no funnel', () => {
    const b = makeBusiness({ funnels: [pinned] });
    expect(selectCommentFunnel(b.funnels, { platform: 'instagram', postId: 'P2', text: 'guide' })).toMatchObject({
      kind: 'skipped',
      reason: 'no_funnel_for_post',
    });
  });

  it('respects platforms', () => {
    const b = makeBusiness({ funnels: [{ ...pinned, platforms: ['facebook'] }] });
    expect(selectCommentFunnel(b.funnels, { platform: 'instagram', postId: 'P1', text: 'guide' }).kind).toBe('skipped');
  });

  it('story and DM keyword funnels are account-wide', () => {
    const b = makeBusiness({ funnels: [{ ...pinned, posts: [], trigger: 'story_reply', match: 'exact' }] });
    const d = selectMessageFunnel(b.funnels, { platform: 'instagram', trigger: 'story_reply', text: 'Guide!' });
    expect(d.kind).toBe('matched');
  });
});

describe('screenComment', () => {
  const b = makeBusiness();
  const base: CommentEvent = {
    type: 'comment',
    platform: 'facebook',
    accountId: PAGE_ID,
    commentId: 'C1',
    postId: `${PAGE_ID}_42`,
    parentId: `${PAGE_ID}_42`,
    authorId: '999',
    text: 'guide',
    createdAt: new Date(),
    verb: 'add',
  };

  it('a Facebook top-level comment has parent_id == post_id and is NOT a reply', () => {
    expect(isReply(base)).toBe(false);
    expect(screenComment(base, b)).toBeUndefined();
  });

  it('a Facebook reply has a different parent', () => {
    expect(screenComment({ ...base, parentId: 'OTHER_COMMENT' }, b)).toBe('is_reply');
  });

  it('an Instagram comment with parent_id is a reply', () => {
    expect(isReply({ platform: 'instagram', parentId: 'X', postId: 'M' })).toBe(true);
    expect(isReply({ platform: 'instagram', postId: 'M' })).toBe(false);
  });

  it('skips our own comments (no DM loop) on both platforms', () => {
    expect(screenComment({ ...base, authorId: PAGE_ID }, b)).toBe('own_comment');
    expect(screenComment({ ...base, platform: 'instagram', parentId: undefined, authorId: IG_ID }, b)).toBe('own_comment');
  });

  it('skips edits, empty text and comments older than 7 days', () => {
    expect(screenComment({ ...base, verb: 'edited' }, b)).toBe('not_new');
    expect(screenComment({ ...base, text: '🔥🔥' }, b)).toBe('no_text');
    expect(screenComment({ ...base, createdAt: new Date(Date.now() - 8 * 86400_000) }, b)).toBe('outside_reply_window');
  });

  it('testers list limits who gets messages', () => {
    const t = makeBusiness({ testers: ['@MyTestAccount', '12345'] });
    expect(isAllowedRecipient(t, { username: 'mytestaccount' })).toBe(true);
    expect(isAllowedRecipient(t, { id: '12345' })).toBe(true);
    expect(isAllowedRecipient(t, { id: '999', username: 'stranger' })).toBe(false);
    expect(isAllowedRecipient(b, { id: '999' })).toBe(true);
  });
});

describe('payloads and messages', () => {
  it('round-trips funnel payloads', () => {
    const p = encodePayload({ funnelId: 'guide-reel', step: 'deliver' });
    expect(decodePayload(p)).toEqual({ funnelId: 'guide-reel', step: 'deliver' });
    expect(decodePayload('GET_STARTED')).toBeUndefined();
  });

  it('builds a button template', () => {
    const m = toMetaMessage({ text: 'hi', button: { title: 'Open', url: 'https://x.io' } }, 'instagram');
    expect(m).toEqual({
      attachment: {
        type: 'template',
        payload: { template_type: 'button', text: 'hi', buttons: [{ type: 'web_url', url: 'https://x.io', title: 'Open' }] },
      },
    });
    expect(toMetaMessage({ text: 'x'.repeat(1500) }, 'instagram')).toMatchObject({ text: expect.stringMatching(/…$/) });
  });
});

describe('audit', () => {
  const env = { hasToken: true };

  it('passes the fixture', () => {
    const issues = auditBusiness(makeBusiness(), env);
    expect(issues.filter((i) => i.level === 'error')).toEqual([]);
  });

  it('refuses short contains keywords and shows what they would catch', () => {
    expect(riskyMatches('guide', 'contains')).toContain('guidelines');
    const b = makeBusiness({
      funnels: [{ id: 'x', posts: ['P'], keywords: ['hi'], match: 'contains', opener: { text: 'a', button: 'b' }, deliver: { text: 'c', link: 'guide_pdf', button: 'd' } }],
    });
    const issues = auditBusiness(b, env);
    expect(blocksLive(issues)).toBe(true);
    expect(issues.some((i) => i.message.includes('too short'))).toBe(true);
  });

  it('refuses unpinned comment funnels and unacknowledged all_posts', () => {
    const f = { id: 'x', keywords: ['guide'], opener: { text: 'a', button: 'b' }, deliver: { text: 'c', link: 'guide_pdf', button: 'd' } };
    expect(blocksLive(auditBusiness(makeBusiness({ funnels: [f] }), env))).toBe(true);
    expect(blocksLive(auditBusiness(makeBusiness({ funnels: [{ ...f, all_posts: true }] }), env))).toBe(true);
    expect(blocksLive(auditBusiness(makeBusiness({ funnels: [{ ...f, all_posts: true, all_posts_acknowledged: true }] }), env))).toBe(false);
  });

  it('refuses link shorteners, placeholders and unknown link ids', () => {
    const f = { id: 'x', posts: ['P'], keywords: ['guide'], opener: { text: 'see bit.ly/abc', button: 'b' }, deliver: { text: 'c', link: 'nope', button: 'd' } };
    const issues = auditBusiness(makeBusiness({ funnels: [f], name: 'TODO business name' }), env);
    expect(issues.some((i) => i.message.includes('bit.ly'))).toBe(true);
    expect(issues.some((i) => i.message.includes('placeholder'))).toBe(true);
    expect(issues.some((i) => i.message.includes('"nope"'))).toBe(true);
  });

  it('flags a missing token as an error only for live businesses', () => {
    expect(blocksLive(auditBusiness(makeBusiness(), { hasToken: false }))).toBe(true);
    expect(blocksLive(auditBusiness(makeBusiness({ live: false }), { hasToken: false }))).toBe(false);
    expect(blocksLive(auditBusiness(makeBusiness({ meta: {} }), { hasToken: false }))).toBe(true);
  });
});
