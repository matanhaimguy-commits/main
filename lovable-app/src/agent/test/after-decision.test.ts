// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { AFTER_SKIP_TEXT, decideAfter, type AfterFacts, type AfterSkip } from '../logic/after-decision';

const NOW = new Date('2026-10-28T10:30:00Z');

/** Everything fine: the person tapped 30 minutes ago and has been quiet since. */
const facts = (over: Partial<AfterFacts> = {}): AfterFacts => ({
  now: NOW,
  funnelHasAfter: true,
  businessEnabled: true,
  allowedRecipient: true,
  optedOut: false,
  queuedInDryRunButLiveNow: false,
  personReplied: false,
  teamReplied: false,
  lastInboundAt: new Date('2026-10-28T10:00:00Z'),
  ...over,
});

describe('decideAfter', () => {
  it('sends when nothing stands in the way', () => {
    expect(decideAfter(facts())).toEqual({ send: true });
  });

  const cases: [AfterSkip, Partial<AfterFacts>][] = [
    ['funnel_changed', { funnelHasAfter: false }],
    ['business_disabled', { businessEnabled: false }],
    ['opted_out', { optedOut: true }],
    ['not_a_tester', { allowedRecipient: false }],
    ['queued_in_dry_run', { queuedInDryRunButLiveNow: true }],
    ['replied', { personReplied: true }],
    ['team_replied', { teamReplied: true }],
    ['window_closed', { lastInboundAt: new Date('2026-10-27T09:00:00Z') }],
    ['window_closed', { lastInboundAt: null }],
  ];
  it.each(cases)('skips with the reason %s', (reason, over) => {
    expect(decideAfter(facts(over))).toEqual({ send: false, reason });
  });

  it('has a plain-language sentence for every reason', () => {
    for (const [reason] of cases) expect(AFTER_SKIP_TEXT[reason].length).toBeGreaterThan(10);
  });

  it('reports the first reason when several apply', () => {
    expect(decideAfter(facts({ optedOut: true, personReplied: true, lastInboundAt: null }))).toEqual({ send: false, reason: 'opted_out' });
    expect(decideAfter(facts({ personReplied: true, lastInboundAt: null }))).toEqual({ send: false, reason: 'replied' });
  });
});
