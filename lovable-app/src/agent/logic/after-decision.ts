import { windowOpen } from './messaging-window';

/** Why a queued last message was not sent. */
export type AfterSkip =
  | 'funnel_changed'
  | 'business_disabled'
  | 'opted_out'
  | 'not_a_tester'
  | 'queued_in_dry_run'
  | 'replied'
  | 'team_replied'
  | 'window_closed';

/** Plain-language reasons, written to the send ledger (Activity page) and the log. */
export const AFTER_SKIP_TEXT: Record<AfterSkip, string> = {
  funnel_changed: 'the funnel or its last message was removed while this was waiting',
  business_disabled: 'the business was switched off while this was waiting',
  opted_out: 'the person asked us to stop',
  not_a_tester: 'the business is in testers-only mode and this person is not on the list',
  queued_in_dry_run:
    'the earlier messages of this funnel were a dry run (nothing reached this person), so the question is not sent now that sending is live',
  replied: 'the person wrote back while this was waiting',
  team_replied: 'a team member wrote to this person while this was waiting',
  window_closed: 'the 24-hour messaging window is closed (the person last wrote more than 24 hours ago)',
};

export interface AfterFacts {
  now: Date;
  /** The funnel still exists and still has a last message. */
  funnelHasAfter: boolean;
  businessEnabled: boolean;
  allowedRecipient: boolean;
  optedOut: boolean;
  /** The business was in dry run when this was queued, and is live now. */
  queuedInDryRunButLiveNow: boolean;
  /** The person sent a message after this was queued. */
  personReplied: boolean;
  /** A team member wrote to the person after this was queued. */
  teamReplied: boolean;
  /** The person's last message (the 24h window counts from here). */
  lastInboundAt: Date | null;
}

export type AfterDecision = { send: true } | { send: false; reason: AfterSkip };

/** The checks that run when a queued last message comes due, most basic first. */
export function decideAfter(f: AfterFacts): AfterDecision {
  if (!f.funnelHasAfter) return { send: false, reason: 'funnel_changed' };
  if (!f.businessEnabled) return { send: false, reason: 'business_disabled' };
  if (f.optedOut) return { send: false, reason: 'opted_out' };
  if (!f.allowedRecipient) return { send: false, reason: 'not_a_tester' };
  if (f.queuedInDryRunButLiveNow) return { send: false, reason: 'queued_in_dry_run' };
  if (f.personReplied) return { send: false, reason: 'replied' };
  if (f.teamReplied) return { send: false, reason: 'team_replied' };
  if (!windowOpen(f.lastInboundAt, f.now)) return { send: false, reason: 'window_closed' };
  return { send: true };
}
