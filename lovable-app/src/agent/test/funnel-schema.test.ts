// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { ConfigError, parseBusiness } from '../config/load';
import { FunnelSchema } from '../config/schema';
import { auditBusiness } from '../logic/audit';
import { makeBusiness } from './fixtures';

const funnel = (over: Record<string, unknown> = {}) => ({
  id: 'guide-reel',
  keywords: ['guide'],
  opener: { text: 'Want the guide?', button: 'Send it' },
  deliver: { text: 'Here it is', link: 'https://acme.studio/guide.pdf', button: 'Open' },
  after: 'One question: what do you sell?',
  ...over,
});

describe('funnel after_delay_minutes', () => {
  it('defaults to 0, so funnels written before the setting do not change', () => {
    expect(FunnelSchema.parse(funnel()).after_delay_minutes).toBe(0);
    expect(makeBusiness().funnels[0]!.after_delay_minutes).toBe(0);
  });

  it('accepts whole minutes from 0 to 60', () => {
    for (const n of [0, 1, 15, 60]) expect(FunnelSchema.parse(funnel({ after_delay_minutes: n })).after_delay_minutes).toBe(n);
  });

  it.each([
    ['above 60', 61],
    ['negative', -1],
    ['not whole', 12.5],
    ['text', '10'],
    ['null', null],
  ])('refuses a delay that is %s', (_name, value) => {
    expect(FunnelSchema.safeParse(funnel({ after_delay_minutes: value })).success).toBe(false);
  });

  it('names the setting when a business config is refused', () => {
    const raw = { ...makeBusiness(), funnels: [funnel({ after_delay_minutes: 90 })] };
    expect(() => parseBusiness(raw, 'acme')).toThrow(ConfigError);
    try {
      parseBusiness(raw, 'acme');
    } catch (err) {
      expect((err as ConfigError).problems.join(' ')).toMatch(/funnels\.0\.after_delay_minutes.*60/);
    }
  });

  it('the audit warns about a delay with nothing to delay', () => {
    const base = { ai: { reply_delay_seconds: 0 } };
    const without = makeBusiness({ ...base, funnels: [funnel({ after: undefined, after_delay_minutes: 15 })] });
    const issues = auditBusiness(without, { hasToken: true }).filter((i) => i.message.includes('after_delay_minutes'));
    expect(issues).toHaveLength(1);
    expect(issues[0]!.level).toBe('warn');
    const withText = makeBusiness({ ...base, funnels: [funnel({ after_delay_minutes: 15 })] });
    expect(auditBusiness(withText, { hasToken: true }).some((i) => i.message.includes('after_delay_minutes'))).toBe(false);
  });
});
