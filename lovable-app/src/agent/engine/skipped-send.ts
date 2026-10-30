import { claimSend, completeSend, type SendClaim } from '../db/repo';
import type { Deps } from './deps';

/**
 * Writes down a message that was deliberately not sent, in the send ledger, so the Activity page
 * shows it (status "skipped") with the reason. It also uses up the message's key, so that message
 * can never be sent afterwards by anything else.
 */
export async function recordSkippedSend(deps: Deps, claim: SendClaim, reason: string): Promise<void> {
  const sendId = await claimSend(deps.sql, claim);
  if (sendId === undefined) return; // the ledger already has this key: it was attempted or skipped before
  await completeSend(deps.sql, sendId, { status: 'skipped', errorMessage: `not sent: ${reason}` });
}
