import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { ErrorBlock, LoadingBlock, Pill, Shell, Step } from "@/components/app/shell";
import { CopyField } from "@/components/app/copy-field";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { statsFn } from "@/lib/api/inbox.functions";
import { getOverview } from "@/lib/api/setup.functions";
import { timeAgo } from "@/lib/format";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/")({
  head: () => ({ meta: [{ title: "Overview · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: OverviewPage,
});

const STAT_LABELS: [key: string, label: string][] = [
  ["comments", "Comments"],
  ["funnel_comments", "Matched a funnel"],
  ["dms_sent", "Messages sent"],
  ["taps", "Button taps"],
  ["ai_replies", "AI replies"],
  ["new_contacts", "New people"],
  ["hot", "Hot / booked leads"],
  ["failed", "Failed sends"],
];

function OverviewPage() {
  const overview = useQuery({ queryKey: ["overview"], queryFn: () => getOverview() });
  const stats = useQuery({ queryKey: ["stats"], queryFn: () => statsFn({ data: {} }) });
  const o = overview.data;

  return (
    <Shell title="Overview" description="What is set up, what is left, and how the last 7 days went.">
      {overview.isLoading && <LoadingBlock />}
      {overview.error && <ErrorBlock error={overview.error} />}
      {o && (
        <div className="space-y-6">
          {o.preview && (
            <div className="rounded-xl border border-amber-200 bg-amber-50 p-4 text-sm text-amber-900">
              You are on Lovable's preview address. Meta must talk to the <b>published</b> app, so do the setup from there:{" "}
              {o.base.includes("preview") ? "publish the project in Lovable, then open its .lovable.app address." : <a className="underline" href={o.base}>{o.base}</a>}
            </div>
          )}

          {stats.data && (
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              {STAT_LABELS.map(([key, label]) => (
                <Card key={key}>
                  <CardContent className="p-4">
                    <div className="text-2xl font-semibold tabular-nums">{(stats.data as Record<string, number>)[key] ?? 0}</div>
                    <div className="text-xs text-muted-foreground">{label}</div>
                  </CardContent>
                </Card>
              ))}
            </div>
          )}
          {stats.data && stats.data.dry_runs > 0 && (
            <p className="text-sm text-muted-foreground">
              {stats.data.dry_runs} message(s) were recorded as dry runs (not sent) this week. See <Link to="/activity" className="underline">Activity</Link>.
            </p>
          )}

          <Card>
            <CardHeader>
              <CardTitle>Setup</CardTitle>
              <CardDescription>Work down the list. Every step links to where it is done.</CardDescription>
            </CardHeader>
            <CardContent className="divide-y">
              <Step state={o.metaApp.id && o.metaApp.hasSecret ? "done" : "todo"} title="1. Meta app keys">
                {o.metaApp.id && o.metaApp.hasSecret ? (
                  <>App ID {o.metaApp.id}.</>
                ) : (
                  <>
                    Create the app at developers.facebook.com (see the guide), then paste its App ID and App Secret in{" "}
                    <Link to="/settings" className="underline">Settings</Link>.
                  </>
                )}
              </Step>
              <Step state="info" title="2. Paste these into your Meta app">
                <div className="mt-2 rounded-lg border bg-background p-3">
                  <CopyField label="App settings → Basic → Privacy Policy URL" value={o.urls.privacy} />
                  <CopyField label="App settings → Basic → User data deletion URL" value={o.urls.dataDeletion} />
                  <CopyField label="Facebook Login → Settings → Valid OAuth Redirect URIs" value={o.urls.callback} />
                  <CopyField label="Webhooks → Callback URL" value={o.urls.webhook} />
                  <CopyField label="Webhooks → Verify token" value={o.verifyToken ?? "(add the App Secret first)"} />
                </div>
              </Step>
              <Step state={o.connections.length ? "done" : "todo"} title="3. Connect Facebook & Instagram">
                {o.connections.length ? (
                  <>
                    {o.connections.length} Page(s): {o.connections.map((c) => c.pageName + (c.instagramUsername ? ` (@${c.instagramUsername})` : "")).join(", ")}.
                  </>
                ) : (
                  <>
                    On <Link to="/connect" className="underline">Connect</Link>, press "Connect Facebook &amp; Instagram" and pick your Page.
                  </>
                )}
              </Step>
              <Step state={o.webhookVerifiedAt ? "done" : "todo"} title="4. Meta webhooks registered">
                {o.webhookVerifiedAt ? (
                  <>Meta verified the webhook {timeAgo(o.webhookVerifiedAt)}.</>
                ) : (
                  <>
                    On <Link to="/connect" className="underline">Connect</Link>, press "Register webhooks".
                  </>
                )}
              </Step>
              <Step state={o.businesses.some((b) => b.pageId) ? "done" : "todo"} title="5. Each Page answers for a business">
                {o.businesses.length === 0 ? (
                  <>
                    Create your business on <Link to="/businesses" className="underline">Businesses</Link>.
                  </>
                ) : o.businesses.some((b) => b.pageId) ? (
                  <>{o.businesses.filter((b) => b.pageId).map((b) => b.name).join(", ")}.</>
                ) : (
                  <>
                    On <Link to="/connect" className="underline">Connect</Link>, choose the business for your Page.
                  </>
                )}
              </Step>
              <Step state="info" title="6. Two switches only you can flip">
                In the Meta App Dashboard, switch the app from <b>Development</b> to <b>Live</b>. In the Instagram app: Settings → Messages and story replies →
                Message controls → Connected tools → turn on <b>Allow access to messages</b>.
              </Step>
              <Step state={o.lastEventAt ? "done" : "todo"} title="7. Events arriving from Meta">
                {o.lastEventAt ? <>Last one {timeAgo(o.lastEventAt)}.</> : <>None yet. Comment on a post or send a DM from a second account.</>}
              </Step>
              <Step
                state={o.tick.lastAt && Date.now() - new Date(o.tick.lastAt).getTime() < 5 * 60_000 ? "done" : o.tick.target ? "warn" : "todo"}
                title="8. Background worker"
              >
                {o.tick.lastAt ? (
                  <>Last run {timeAgo(o.tick.lastAt)} (it runs every minute for follow-ups and anything left over).</>
                ) : o.tick.target ? (
                  <>Starting. It should run within a minute.</>
                ) : (
                  <>Starts the first time you open this dashboard from the published address.</>
                )}
              </Step>
              <Step state={o.ai ? "done" : "todo"} title="9. AI (Claude) key">
                {o.ai ? (
                  <>
                    Set. <Link to="/test" className="underline">Chat with the bot</Link> to hear how it answers.
                  </>
                ) : (
                  <>
                    Add your Claude API key in <Link to="/settings" className="underline">Settings</Link>. Funnels work without it; AI replies do not.
                  </>
                )}
              </Step>
              <Step state={o.liveSending ? "done" : "warn"} title="10. Real sending">
                {o.liveSending ? (
                  <>On. Each business also needs "Live" switched on and no blocking problems.</>
                ) : (
                  <>
                    Off: everything is a dry run (recorded, not sent). Switch it on in <Link to="/settings" className="underline">Settings</Link> once tests look right.
                  </>
                )}
              </Step>
              <Step state={o.alerts ? "done" : "info"} title="Alerts (optional)">
                {o.alerts ? "Configured." : "Add a Telegram bot in Settings to hear about hot leads and problems."}
              </Step>
            </CardContent>
          </Card>

          {o.invalidBusinesses.length > 0 && (
            <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-800">
              {o.invalidBusinesses.map((b) => (
                <div key={b.slug}>
                  <b>{b.slug}</b> has a problem and is not running: {b.problems.slice(0, 3).join("; ")}{" "}
                  <Link to="/businesses/$slug" params={{ slug: b.slug }} className="underline">
                    Fix it
                  </Link>
                </div>
              ))}
            </div>
          )}

          <div className="grid gap-4 md:grid-cols-2">
            {o.businesses.map((b) => {
              const errors = b.issues.filter((i) => i.level === "error");
              return (
                <Card key={b.slug}>
                  <CardHeader className="pb-3">
                    <div className="flex items-start justify-between gap-2">
                      <CardTitle className="text-base">{b.name}</CardTitle>
                      {b.live ? <Pill tone="green">Live</Pill> : <Pill tone="amber">Dry run</Pill>}
                    </div>
                    {!b.live && <CardDescription>{b.reason}</CardDescription>}
                  </CardHeader>
                  <CardContent className="space-y-1 text-sm">
                    <div>Facebook: {b.pageName ?? b.pageId ?? <span className="text-rose-700">not connected</span>}</div>
                    <div>Instagram: {b.instagramUsername ? `@${b.instagramUsername}` : (b.instagramId ?? <span className="text-rose-700">not linked</span>)}</div>
                    <div>
                      {b.funnels} funnel(s) · {b.testers.length ? `testers only: ${b.testers.join(", ")}` : "answers everyone"}
                    </div>
                    {errors.length > 0 && (
                      <div className="pt-1 text-rose-700">
                        {errors.length} problem(s) block real sending: {errors[0]!.message}
                        {errors.length > 1 ? " …" : ""}
                      </div>
                    )}
                    <div className="flex gap-2 pt-3">
                      <Button asChild size="sm" variant="outline">
                        <Link to="/businesses/$slug" params={{ slug: b.slug }}>
                          Edit
                        </Link>
                      </Button>
                      <Button asChild size="sm" variant="outline">
                        <Link to="/test" search={{ b: b.slug }}>
                          Test
                        </Link>
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      )}
    </Shell>
  );
}
