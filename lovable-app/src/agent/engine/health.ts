import { getState, setState } from '../db/connections';
import { MetaApiError } from '../meta/client';
import type { Deps } from './deps';

/**
 * Silence is not success. A funnel can keep "sending" while nothing lands (a token problem,
 * a link behind a permission wall, Meta filtering). Instagram has no delivery receipts, so
 * landing is judged by reads, button taps and clicks; Facebook also has delivery receipts.
 */
export async function checkQuietFunnels(deps: Deps): Promise<string[]> {
  const rows = await deps.sql<
    { business: string; funnel_id: string; platform: string; sent: number; first_sent: Date; landed: number }[]
  >`
    WITH openers AS (
      SELECT business, funnel_id, platform, count(*)::int AS sent, min(sent_at) AS first_sent,
        count(delivered_at)::int + count(read_at)::int AS receipts
      FROM sends
      WHERE step = 'opener' AND status = 'sent' AND funnel_id IS NOT NULL
        AND sent_at > now() - interval '72 hours'
      GROUP BY 1, 2, 3
    ), taps AS (
      SELECT business, funnel_id, count(*)::int AS n FROM taps
      WHERE created_at > now() - interval '72 hours' GROUP BY 1, 2
    ), clicks AS (
      SELECT business, funnel_id, coalesce(sum(clicks), 0)::int AS n FROM links
      WHERE created_at > now() - interval '72 hours' GROUP BY 1, 2
    )
    SELECT o.business, o.funnel_id, o.platform, o.sent, o.first_sent,
      o.receipts + coalesce(t.n, 0) + coalesce(c.n, 0) AS landed
    FROM openers o
    LEFT JOIN taps t ON t.business = o.business AND t.funnel_id = o.funnel_id
    LEFT JOIN clicks c ON c.business = o.business AND c.funnel_id = o.funnel_id`;
  const quiet: string[] = [];
  for (const r of rows) {
    if (r.sent < 5 || r.landed > 0) continue;
    if (deps.now().getTime() - r.first_sent.getTime() < 2 * 3_600_000) continue;
    const name = deps.registry.bySlug(r.business)?.name ?? r.business;
    quiet.push(`${r.business}/${r.funnel_id}/${r.platform}`);
    await deps.alert({
      key: `quiet:${r.business}:${r.funnel_id}:${r.platform}`,
      text: `🔕 ${name}: funnel "${r.funnel_id}" sent ${r.sent} DMs on ${r.platform} in the last 72h and not one was read, tapped or clicked. Something is probably broken. Test it from an account with no connection to your app, and open the link while logged out.`,
      cooldownMinutes: 12 * 60,
    });
  }
  return quiet;
}

/** A crash between claiming a send and recording Meta's answer leaves it pending. Never retried. */
export async function checkStuckSends(deps: Deps): Promise<number> {
  const stuck = await deps.sql<{ business: string; id: number }[]>`
    UPDATE sends SET status = 'unknown',
      error_message = 'stuck in pending (process stopped mid-send); outcome unknown, not retried'
    WHERE status = 'pending' AND created_at < now() - interval '5 minutes'
    RETURNING business, id`;
  for (const s of stuck) {
    await deps.alert({
      key: `stuck:${s.business}`,
      text: `⚠️ ${s.business}: send #${s.id} never got an answer from Meta (process stopped mid-send). It was not retried.`,
      cooldownMinutes: 60,
    });
  }
  return stuck.length;
}

export async function checkFailedEvents(deps: Deps): Promise<number> {
  const [row] = await deps.sql<{ n: number }[]>`
    SELECT count(*)::int AS n FROM webhook_events WHERE status = 'error' AND received_at > now() - interval '24 hours'`;
  if (row!.n > 0) {
    await deps.alert({
      key: 'failed-events',
      text: `⚠️ ${row!.n} webhook event(s) failed processing 3 times in the last 24h. See webhook_events where status = 'error'.`,
      cooldownMinutes: 6 * 60,
    });
  }
  return row!.n;
}

/**
 * Meta unsubscribes an app from a Page after an hour of failed webhook deliveries, and then
 * simply stops sending. Check that our app is still installed on every live Page.
 */
export async function checkSubscriptions(deps: Deps): Promise<void> {
  const appId = deps.env.META_APP_ID;
  if (!appId) return;
  for (const b of deps.registry.businesses) {
    if (!b.enabled || !deps.isLive(b) || !b.meta.page_id) continue;
    const api = deps.metaFor(b);
    if (!api) continue;
    try {
      const res = await api.get<{ data: { id: string; subscribed_fields?: string[] }[] }>(`${b.meta.page_id}/subscribed_apps`);
      const ours = res.data.find((a) => a.id === appId);
      if (!ours) {
        await deps.alert({
          key: `unsubscribed:${b.slug}`,
          text: `🚨 ${b.name}: our app is no longer subscribed to the Page's webhooks, so nothing is arriving. Open the Connect page and press "Subscribe again" for this Page.`,
          cooldownMinutes: 6 * 60,
        });
      }
    } catch (err) {
      deps.log.warn('subscription check failed', { business: b.slug, err });
    }
  }
}

/** Meta's answer when the app lacks Advanced Access and the person has no role on the app. */
export const NO_ADVANCED_ACCESS = 2534048;

export type DmAccess = 'everyone' | 'roles_only' | 'unknown';

export interface DmAccessState {
  status: DmAccess;
  checkedAt: string;
  /** Since when the status has been what it is. */
  since: string;
  /** The account Meta was asked about. */
  probe: string | null;
  /** Someone Meta refused, asked about first next time: if they go through, access opened. */
  refusedId?: string;
}

/**
 * Until App Review grants Advanced Access to instagram_manage_messages, Meta passes Instagram
 * DMs, button taps and replies only from people with a role on the app. Comments and private
 * replies still reach everyone, so nothing looks broken while strangers' DMs go unanswered.
 * Every hour, ask Meta about real customers, keep the answer for the dashboard, and alert
 * the moment it changes.
 */
export async function checkDmAccess(deps: Deps): Promise<Record<string, DmAccessState>> {
  const prev = (await getState<Record<string, DmAccessState>>(deps.sql, 'dm_access'))?.value ?? {};
  const next: Record<string, DmAccessState> = {};
  const now = deps.now().toISOString();
  for (const b of deps.registry.businesses) {
    if (!b.enabled || !b.meta.page_id || !b.meta.instagram_id) continue;
    const api = deps.metaFor(b);
    if (!api) continue;
    const before = prev[b.slug];
    const people = await deps.sql<{ external_id: string; username: string | null }[]>`
      SELECT external_id, username FROM contacts
      WHERE business = ${b.slug} AND platform = 'instagram'
      ORDER BY (external_id = ${before?.refusedId ?? ''}) DESC, updated_at DESC
      LIMIT 3`;
    let status: DmAccess = 'unknown';
    let probe: string | null = null;
    let refusedId: string | undefined;
    for (const p of people) {
      try {
        await api.get(`${b.meta.page_id}/thread_owner`, { recipient: p.external_id, platform: 'instagram' });
        if (p.external_id === before?.refusedId) {
          status = 'everyone';
          probe = p.username ?? p.external_id;
          break;
        }
      } catch (err) {
        if (err instanceof MetaApiError && err.subcode === NO_ADVANCED_ACCESS) {
          status = 'roles_only';
          probe = p.username ?? p.external_id;
          refusedId = p.external_id;
          break;
        }
        deps.log.warn('dm access check failed', { business: b.slug, err });
      }
    }
    // Everyone asked about has a role: no new information, keep what we knew.
    if (status === 'unknown' && before && before.status !== 'unknown') {
      next[b.slug] = { ...before, checkedAt: now };
      continue;
    }
    next[b.slug] = { status, checkedAt: now, since: before?.status === status ? before.since : now, probe, refusedId };

    if (status === 'everyone' && before?.status === 'roles_only') {
      await deps.alert({
        key: `dm-access-open:${b.slug}`,
        text:
          `✅ ${b.name}: Meta now passes every Instagram DM to the app (Advanced Access is on), so the AI answers everyone who writes. ` +
          'If you set an Instant reply in Meta Business Suite as a stopgap, turn it off now, and switch funnel openers back to "tap" so commenters start a conversation.',
        cooldownMinutes: 7 * 24 * 60,
      });
    } else if (status === 'roles_only') {
      await deps.alert({
        key: `dm-access-roles:${b.slug}`,
        text:
          `⚠️ ${b.name}: Meta only passes Instagram DMs from people with a role on the app (no Advanced Access to instagram_manage_messages yet). ` +
          'Comment funnels in link mode still reach everyone; DMs from customers are not answered until App Review approves it.',
        cooldownMinutes: 24 * 60,
      });
    }
  }
  await setState(deps.sql, 'dm_access', next);
  return next;
}

export async function runHealthChecks(deps: Deps): Promise<void> {
  for (const check of [checkStuckSends, checkQuietFunnels, checkFailedEvents]) {
    try {
      await check(deps);
    } catch (err) {
      deps.log.error('health check failed', { check: check.name, err });
    }
  }
}
