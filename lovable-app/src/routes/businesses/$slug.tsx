import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createFileRoute, Link, useRouter } from "@tanstack/react-router";
import { Plus } from "lucide-react";
import { useEffect, useState } from "react";
import { toast } from "sonner";
import { AreaField, Field, LinesField, NumberField, RowsEditor, SelectField, setIn, SwitchField, TextField, CommaField } from "@/components/app/fields";
import { FunnelEditor } from "@/components/app/funnel-editor";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";
import { starterFunnel } from "@/agent/config/starter";
import type { Issue } from "@/agent/logic/audit";
import { deleteBusinessFn, getBusinessFn, saveBusinessFn } from "@/lib/api/businesses.functions";
import { errorText } from "@/lib/format";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/businesses/$slug")({
  head: () => ({ meta: [{ title: "Business · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: BusinessPage,
});

type AnyObj = Record<string, any>;

function BusinessPage() {
  const { slug } = Route.useParams();
  const qc = useQueryClient();
  const router = useRouter();
  const detail = useQuery({ queryKey: ["business", slug], queryFn: () => getBusinessFn({ data: { slug } }) });
  const [cfg, setCfg] = useState<AnyObj | null>(null);
  const [yaml, setYaml] = useState("");
  const [dirty, setDirty] = useState(false);
  const [saving, setSaving] = useState(false);
  const [problems, setProblems] = useState<string[]>([]);
  const [issues, setIssues] = useState<Issue[] | null>(null);
  const [tab, setTab] = useState("business");

  useEffect(() => {
    if (!detail.data || dirty) return;
    setCfg(detail.data.config);
    setYaml(detail.data.yaml);
    setProblems(detail.data.problems);
    setIssues(null);
    if (!detail.data.config) setTab("yaml");
  }, [detail.data, dirty]);

  const set = (path: (string | number)[], value: unknown) => {
    setCfg((c) => (c ? setIn(c, path, value) : c));
    setDirty(true);
  };

  const save = async (fromYaml: boolean) => {
    setSaving(true);
    try {
      const res = await saveBusinessFn({ data: fromYaml ? { slug, yaml } : { slug, config: cfg ?? {} } });
      setProblems(res.problems);
      if (!res.ok) {
        toast.error("Not saved. Fix the problems listed at the top.");
        return;
      }
      setIssues(res.issues);
      setDirty(false);
      toast.success(res.issues.some((i) => i.level === "error") ? "Saved. Some problems still block real sending." : "Saved.");
      await qc.invalidateQueries();
    } catch (err) {
      toast.error(errorText(err));
    } finally {
      setSaving(false);
    }
  };

  const remove = async () => {
    if (!confirm(`Delete ${slug}? Its funnels stop immediately. Conversations stay in the database.`)) return;
    await deleteBusinessFn({ data: { slug } });
    await qc.invalidateQueries();
    await router.navigate({ to: "/businesses" });
  };

  const d = detail.data;
  const shownIssues = issues ?? d?.issues ?? [];
  const errors = shownIssues.filter((i) => i.level === "error");
  const warnings = shownIssues.filter((i) => i.level === "warn");

  return (
    <Shell
      title={cfg?.["name"] ?? slug}
      description={
        d?.connected ? (
          <>
            Answers for {d.connected.pageName}
            {d.connected.instagramUsername ? ` and @${d.connected.instagramUsername}` : ""}.
          </>
        ) : (
          <>
            No Page yet: choose this business on <Link to="/connect" className="underline">Connect</Link>.
          </>
        )
      }
      actions={
        <>
          {d?.live && (d.live.live ? <Pill tone="green">Live</Pill> : <Pill tone="amber">Dry run · {d.live.reason}</Pill>)}
          <Button variant="outline" asChild>
            <Link to="/test" search={{ b: slug }}>
              Test
            </Link>
          </Button>
          <Button onClick={() => save(tab === "yaml")} disabled={saving || (tab !== "yaml" && !cfg)}>
            {saving ? "Saving…" : dirty || tab === "yaml" ? "Save" : "Saved"}
          </Button>
        </>
      }
    >
      {detail.isLoading && <LoadingBlock />}
      {detail.error && <ErrorBlock error={detail.error} />}
      {d === null && <ErrorBlock error="This business does not exist." />}
      {d && (
        <div className="space-y-4">
          {problems.length > 0 && (
            <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-900">
              <div className="mb-1 font-medium">These must be fixed before saving:</div>
              <ul className="list-disc space-y-0.5 pl-5">
                {problems.map((p) => (
                  <li key={p}>{p}</li>
                ))}
              </ul>
            </div>
          )}
          {(errors.length > 0 || warnings.length > 0) && (
            <div className="rounded-xl border bg-background p-4 text-sm">
              {errors.length > 0 && (
                <>
                  <div className="mb-1 font-medium text-rose-800">Blocks real sending ({errors.length})</div>
                  <ul className="mb-3 list-disc space-y-0.5 pl-5 text-rose-800">
                    {errors.map((i, n) => (
                      <li key={n}>
                        {i.where && <span className="font-mono text-xs">[{i.where}] </span>}
                        {i.message}
                      </li>
                    ))}
                  </ul>
                </>
              )}
              {warnings.length > 0 && (
                <>
                  <div className="mb-1 font-medium text-amber-800">Worth a look ({warnings.length})</div>
                  <ul className="list-disc space-y-0.5 pl-5 text-amber-900">
                    {warnings.map((i, n) => (
                      <li key={n}>
                        {i.where && <span className="font-mono text-xs">[{i.where}] </span>}
                        {i.message}
                      </li>
                    ))}
                  </ul>
                </>
              )}
            </div>
          )}

          <Tabs value={tab} onValueChange={setTab}>
            <TabsList className="flex h-auto flex-wrap justify-start">
              <TabsTrigger value="business" disabled={!cfg}>
                Business
              </TabsTrigger>
              <TabsTrigger value="links" disabled={!cfg}>
                Links
              </TabsTrigger>
              <TabsTrigger value="funnels" disabled={!cfg}>
                Funnels {cfg ? `(${(cfg["funnels"] ?? []).length})` : ""}
              </TabsTrigger>
              <TabsTrigger value="ai" disabled={!cfg}>
                AI &amp; rules
              </TabsTrigger>
              <TabsTrigger value="yaml">Advanced (YAML)</TabsTrigger>
            </TabsList>

            {cfg && (
              <>
                <TabsContent value="business" className="space-y-4">
                  <Card>
                    <CardHeader>
                      <CardTitle>Who you are</CardTitle>
                      <CardDescription>The AI only says what is written here. Be specific: services, prices, who it is for.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <TextField label="Business name" value={cfg["name"]} onChange={(v) => set(["name"], v ?? "")} />
                      <AreaField label="About" rows={3} value={cfg["profile"]?.["about"]} onChange={(v) => set(["profile", "about"], v ?? "")} />
                      <AreaField
                        label="Offers and prices"
                        hint="Each service, what is included and the price (or 'price on a call')."
                        rows={5}
                        value={cfg["profile"]?.["offers"]}
                        onChange={(v) => set(["profile", "offers"], v ?? "")}
                      />
                      <AreaField label="Ideal customer" rows={2} optional value={cfg["profile"]?.["audience"]} onChange={(v) => set(["profile", "audience"], v)} />
                      <TextField
                        label="Goal of every conversation"
                        hint="The one next step, e.g. book a free 20-minute call."
                        value={cfg["profile"]?.["goal"]}
                        onChange={(v) => set(["profile", "goal"], v ?? "")}
                      />
                      <LinesField
                        label="Questions the AI asks to qualify a lead"
                        value={cfg["profile"]?.["qualifying_questions"]}
                        onChange={(v) => set(["profile", "qualifying_questions"], v)}
                      />
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <CardTitle>Questions people ask</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <RowsEditor
                        items={(cfg["profile"]?.["faq"] ?? []) as AnyObj[]}
                        onChange={(v) => set(["profile", "faq"], v)}
                        make={() => ({ q: "", a: "" })}
                        addLabel="Add a question"
                        render={(item, update) => (
                          <div className="grid gap-2">
                            <Input placeholder="Question" value={item["q"] ?? ""} onChange={(e) => update({ ...item, q: e.target.value })} />
                            <Textarea rows={2} placeholder="Answer" value={item["a"] ?? ""} onChange={(e) => update({ ...item, a: e.target.value })} />
                          </div>
                        )}
                      />
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <CardTitle>Voice and limits</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <AreaField
                        label="Voice"
                        hint="How it sounds. Language, tone, emoji."
                        rows={2}
                        optional
                        value={cfg["profile"]?.["voice"]}
                        onChange={(v) => set(["profile", "voice"], v)}
                      />
                      <AreaField label="Policies" hint="Refunds, delivery, guarantees…" rows={2} optional value={cfg["profile"]?.["policies"]} onChange={(v) => set(["profile", "policies"], v)} />
                      <LinesField label="Never" hint="Things the AI must never say or do. One per line." value={cfg["profile"]?.["never"]} onChange={(v) => set(["profile", "never"], v)} />
                      <AreaField label="Anything else" rows={2} optional value={cfg["profile"]?.["extra"]} onChange={(v) => set(["profile", "extra"], v)} />
                    </CardContent>
                  </Card>
                </TabsContent>

                <TabsContent value="links">
                  <Card>
                    <CardHeader>
                      <CardTitle>Links</CardTitle>
                      <CardDescription>
                        Buttons the bot can send: booking page, price list, guide. The AI sends only these. Use the real address, never a link shortener.
                      </CardDescription>
                    </CardHeader>
                    <CardContent>
                      <RowsEditor
                        items={(cfg["links"] ?? []) as AnyObj[]}
                        onChange={(v) => set(["links"], v)}
                        make={() => ({ id: "", title: "", url: "https://", when: "" })}
                        addLabel="Add a link"
                        render={(item, update) => (
                          <div className="grid gap-2 sm:grid-cols-2">
                            <Field label="Id" hint="e.g. book_call">
                              <Input value={item["id"] ?? ""} onChange={(e) => update({ ...item, id: e.target.value.toLowerCase() })} />
                            </Field>
                            <Field label="Button text" hint={`${(item["title"] ?? "").length}/20`}>
                              <Input value={item["title"] ?? ""} onChange={(e) => update({ ...item, title: e.target.value })} />
                            </Field>
                            <Field label="Address" className="sm:col-span-2">
                              <Input value={item["url"] ?? ""} onChange={(e) => update({ ...item, url: e.target.value })} />
                            </Field>
                            <Field label="When to send it" hint="Tells the AI when this link fits." className="sm:col-span-2">
                              <Input value={item["when"] ?? ""} onChange={(e) => update({ ...item, when: e.target.value })} />
                            </Field>
                          </div>
                        )}
                      />
                    </CardContent>
                  </Card>
                </TabsContent>

                <TabsContent value="funnels" className="space-y-3">
                  <p className="text-sm text-muted-foreground">
                    Someone comments a keyword on a pinned post → they get a private DM with a button → tapping it delivers your link and opens the chat for
                    the AI. One comment triggers one funnel, at most once.
                  </p>
                  {((cfg["funnels"] ?? []) as AnyObj[]).map((f, i) => (
                    <FunnelEditor
                      key={i}
                      slug={slug}
                      funnel={f}
                      links={(cfg["links"] ?? []) as AnyObj[]}
                      defaultOpen={!f["id"]}
                      onChange={(next) => set(["funnels", i], next)}
                      onRemove={() => set(["funnels"], (cfg["funnels"] as AnyObj[]).filter((_, j) => j !== i))}
                    />
                  ))}
                  <Button variant="outline" onClick={() => set(["funnels"], [...(cfg["funnels"] ?? []), starterFunnel(`funnel-${(cfg["funnels"] ?? []).length + 1}`)])}>
                    <Plus /> Add a funnel
                  </Button>
                </TabsContent>

                <TabsContent value="ai" className="space-y-4">
                  <Card>
                    <CardHeader>
                      <CardTitle>Switches</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      <SwitchField label="Business enabled" checked={cfg["enabled"] !== false} onChange={(v) => set(["enabled"], v)} />
                      <SwitchField
                        label="Live"
                        hint="Real messages go out only when this is on, real sending is on in Settings, and nothing blocks it above."
                        checked={!!cfg["live"]}
                        onChange={(v) => set(["live"], v)}
                      />
                      <CommaField
                        label="Testers only"
                        hint="While this has names, only these Instagram usernames (or user IDs) get messages. Empty = everyone."
                        value={cfg["testers"]}
                        onChange={(v) => set(["testers"], v)}
                        placeholder="@my_test_account"
                      />
                      <TextField label="Time zone" value={cfg["timezone"]} onChange={(v) => set(["timezone"], v ?? "UTC")} />
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <CardTitle>AI</CardTitle>
                      <CardDescription>What the AI may do on its own.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      <SwitchField label="AI on" checked={cfg["ai"]?.["enabled"] !== false} onChange={(v) => set(["ai", "enabled"], v)} />
                      <SwitchField label="Answer DMs" checked={cfg["ai"]?.["dm_replies"] !== false} onChange={(v) => set(["ai", "dm_replies"], v)} />
                      <SwitchField
                        label="Answer questions in comments publicly"
                        hint="For comments no funnel owns."
                        checked={!!cfg["ai"]?.["comment_replies"]}
                        onChange={(v) => set(["ai", "comment_replies"], v)}
                      />
                      <SwitchField
                        label="DM people who show buying intent in comments"
                        hint="A private reply to comments like 'how much?' that no funnel owns."
                        checked={!!cfg["ai"]?.["comment_dms"]}
                        onChange={(v) => set(["ai", "comment_dms"], v)}
                      />
                      <SwitchField label="Hide spam comments" checked={!!cfg["ai"]?.["hide_spam"]} onChange={(v) => set(["ai", "hide_spam"], v)} />
                      <SwitchField
                        label="One follow-up for quiet warm leads"
                        hint="Inside Meta's 24-hour window only."
                        checked={cfg["ai"]?.["followup"]?.["enabled"] !== false}
                        onChange={(v) => set(["ai", "followup", "enabled"], v)}
                      />
                      <div className="grid gap-4 pt-2 sm:grid-cols-3">
                        <SelectField
                          label="Thinking effort"
                          value={cfg["ai"]?.["effort"] ?? "medium"}
                          options={["low", "medium", "high"].map((v) => ({ value: v, label: v }))}
                          onChange={(v) => set(["ai", "effort"], v)}
                        />
                        <NumberField
                          label="Wait before answering (s)"
                          hint="So a burst of messages gets one answer."
                          min={0}
                          max={120}
                          value={cfg["ai"]?.["reply_delay_seconds"]}
                          onChange={(v) => set(["ai", "reply_delay_seconds"], v)}
                        />
                        <NumberField
                          label="Follow up after (hours)"
                          min={1}
                          max={22}
                          value={cfg["ai"]?.["followup"]?.["after_hours"]}
                          onChange={(v) => set(["ai", "followup", "after_hours"], v)}
                        />
                        <NumberField
                          label="Pause after a person replies (hours)"
                          min={0}
                          value={cfg["ai"]?.["pause_hours_after_human"]}
                          onChange={(v) => set(["ai", "pause_hours_after_human"], v)}
                        />
                        <NumberField
                          label="Max AI replies per person per day"
                          min={1}
                          value={cfg["ai"]?.["max_replies_per_contact_per_day"]}
                          onChange={(v) => set(["ai", "max_replies_per_contact_per_day"], v)}
                        />
                        <NumberField
                          label="Max public replies per day"
                          min={0}
                          value={cfg["ai"]?.["max_public_replies_per_day"]}
                          onChange={(v) => set(["ai", "max_public_replies_per_day"], v)}
                        />
                      </div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <CardTitle>More</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      <SwitchField
                        label="Also react to replies inside comment threads"
                        checked={!!cfg["comments"]?.["include_replies"]}
                        onChange={(v) => set(["comments", "include_replies"], v)}
                      />
                      <SwitchField
                        label="Track link clicks"
                        hint="Links go through this app first so clicks are counted."
                        checked={!!cfg["track_clicks"]}
                        onChange={(v) => set(["track_clicks"], v)}
                      />
                    </CardContent>
                  </Card>
                  <div className="flex justify-end">
                    <Button variant="ghost" className="text-destructive" onClick={remove}>
                      Delete this business
                    </Button>
                  </div>
                </TabsContent>
              </>
            )}

            <TabsContent value="yaml">
              <Card>
                <CardHeader>
                  <CardTitle>Advanced: the whole business as YAML</CardTitle>
                  <CardDescription>
                    Everything on the other tabs, as text. Saving here replaces the business{dirty ? " (unsaved form changes are discarded)" : ""}.
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-3">
                  <Textarea className="min-h-[480px] font-mono text-xs" value={yaml} onChange={(e) => setYaml(e.target.value)} spellCheck={false} />
                  <Button onClick={() => save(true)} disabled={saving}>
                    Save YAML
                  </Button>
                </CardContent>
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      )}
    </Shell>
  );
}
