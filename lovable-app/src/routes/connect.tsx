import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { toast } from "sonner";
import { CopyField } from "@/components/app/copy-field";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { businessSlugsFn } from "@/lib/api/businesses.functions";
import { assignPageFn, getOverview, registerWebhooksFn, removePageFn, subscribePageFn } from "@/lib/api/setup.functions";
import { errorText, timeAgo } from "@/lib/format";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/connect")({
  head: () => ({ meta: [{ title: "Connect · Social Agent" }, { name: "robots", content: "noindex" }] }),
  validateSearch: (s: Record<string, unknown>): { msg?: string; err?: string } => ({
    ...(typeof s["msg"] === "string" ? { msg: s["msg"] } : {}),
    ...(typeof s["err"] === "string" ? { err: s["err"] } : {}),
  }),
  beforeLoad: requireLogin,
  component: ConnectPage,
});

function ConnectPage() {
  const { msg, err } = Route.useSearch();
  const qc = useQueryClient();
  const overview = useQuery({ queryKey: ["overview"], queryFn: () => getOverview() });
  const slugs = useQuery({ queryKey: ["business-slugs"], queryFn: () => businessSlugsFn() });
  const [busy, setBusy] = useState<string | null>(null);

  const run = async (key: string, fn: () => Promise<{ ok: boolean; message: string }>) => {
    setBusy(key);
    try {
      const res = await fn();
      if (res.ok) toast.success(res.message);
      else toast.error(res.message, { duration: 12_000 });
      await qc.invalidateQueries();
    } catch (e) {
      toast.error(errorText(e));
    } finally {
      setBusy(null);
    }
  };

  const o = overview.data;
  const keysMissing = o && !(o.metaApp.id && o.metaApp.hasSecret);

  return (
    <Shell title="Connect Facebook & Instagram" description="Link your Pages, choose which business each one serves, and register the webhooks.">
      {msg && <div className="mb-4 rounded-xl border border-emerald-200 bg-emerald-50 p-4 text-sm text-emerald-900">{msg}</div>}
      {err && <div className="mb-4 rounded-xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-900">{err}</div>}
      {overview.isLoading && <LoadingBlock />}
      {overview.error && <ErrorBlock error={overview.error} />}
      {o && (
        <div className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>1. Connect your Pages</CardTitle>
              <CardDescription>
                Log in with the Facebook account that manages the Page. Meta asks which Pages and Instagram accounts to share: tick the ones this system should
                answer for. The Instagram account must be a professional account linked to the Page.
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-3">
              {keysMissing ? (
                <p className="text-sm text-rose-700">
                  Add the Meta App ID and App Secret in <Link to="/settings" className="underline">Settings</Link> first.
                </p>
              ) : (
                <Button asChild>
                  <a href="/api/connect/start">Connect Facebook &amp; Instagram</a>
                </Button>
              )}
              <p className="text-xs text-muted-foreground">If Meta says the address is blocked, add this to Facebook Login → Settings → Valid OAuth Redirect URIs:</p>
              <CopyField label="Redirect URI" value={o.urls.callback} />
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>2. Choose which business each Page belongs to</CardTitle>
              <CardDescription>Saving also subscribes the Page to this app's webhooks.</CardDescription>
            </CardHeader>
            <CardContent>
              {o.connections.length === 0 ? (
                <p className="text-sm text-muted-foreground">No Pages connected yet.</p>
              ) : (
                <div className="divide-y">
                  {o.connections.map((p) => (
                    <div key={p.pageId} className="flex flex-wrap items-center gap-3 py-3">
                      <div className="min-w-48 flex-1">
                        <div className="font-medium">{p.pageName}</div>
                        <div className="text-xs text-muted-foreground">
                          {p.instagramId ? `Instagram @${p.instagramUsername ?? p.instagramId}` : "No Instagram account linked to this Page"}
                        </div>
                      </div>
                      <select
                        className="h-9 rounded-md border bg-background px-2 text-sm"
                        value={p.business ?? ""}
                        disabled={busy !== null}
                        onChange={(e) => run(`assign:${p.pageId}`, () => assignPageFn({ data: { pageId: p.pageId, business: e.target.value || null } }))}
                      >
                        <option value="">— not used —</option>
                        {(slugs.data ?? []).map((b) => (
                          <option key={b.slug} value={b.slug}>
                            {b.name}
                          </option>
                        ))}
                      </select>
                      {p.subscribedAt ? <Pill tone="green">Subscribed {timeAgo(p.subscribedAt)}</Pill> : <Pill tone="amber">Not subscribed</Pill>}
                      <Button size="sm" variant="outline" disabled={busy !== null} onClick={() => run(`sub:${p.pageId}`, () => subscribePageFn({ data: { pageId: p.pageId } }))}>
                        Subscribe{p.subscribedAt ? " again" : ""}
                      </Button>
                      <Button
                        size="sm"
                        variant="ghost"
                        disabled={busy !== null}
                        onClick={() => {
                          if (confirm(`Remove ${p.pageName}? The bot stops answering for it.`)) run(`rm:${p.pageId}`, () => removePageFn({ data: { pageId: p.pageId } }));
                        }}
                      >
                        Remove
                      </Button>
                    </div>
                  ))}
                </div>
              )}
              {(slugs.data ?? []).length === 0 && (
                <p className="mt-3 text-sm text-muted-foreground">
                  No businesses yet. <Link to="/businesses" className="underline">Create one</Link> first.
                </p>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>3. App webhooks</CardTitle>
              <CardDescription>
                Tells Meta where to send comments and messages, for Facebook and Instagram. The same as filling in App Dashboard → Webhooks by hand; you only
                need it once.
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-3">
              <Button disabled={busy !== null || !!keysMissing || o.preview} onClick={() => run("webhooks", () => registerWebhooksFn())}>
                {busy === "webhooks" ? "Registering…" : "Register webhooks"}
              </Button>
              {o.preview && <p className="text-sm text-amber-800">Open the published address to do this (Meta cannot reach the preview).</p>}
              {o.webhookVerifiedAt && <p className="text-sm text-emerald-700">Meta verified the webhook {timeAgo(o.webhookVerifiedAt)}.</p>}
              {o.appWebhooks?.some((r) => !r.ok) && (
                <p className="text-sm text-rose-700">
                  Last attempt: {o.appWebhooks.filter((r) => !r.ok).map((r) => `${r.object}: ${r.error}`).join(" · ")}
                </p>
              )}
              <div className="rounded-lg border p-3">
                <div className="mb-1 text-xs font-medium">By hand (App Dashboard → Webhooks):</div>
                <CopyField label="Callback URL" value={o.urls.webhook} />
                <CopyField label="Verify token" value={o.verifyToken} />
                <p className="mt-2 text-xs text-muted-foreground">
                  Page object: feed, messages, messaging_postbacks, message_deliveries, message_reads, message_echoes. Instagram object: comments, messages,
                  messaging_postbacks, messaging_seen.
                </p>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </Shell>
  );
}
