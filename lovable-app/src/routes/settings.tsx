import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { useState, type FormEvent } from "react";
import { toast } from "sonner";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { CopyField } from "@/components/app/copy-field";
import { changePasswordFn, createReviewerPasswordFn, removeReviewerPasswordFn } from "@/lib/api/session.functions";
import { getSettings, saveSettingsFn } from "@/lib/api/setup.functions";
import { errorText, timeAgo } from "@/lib/format";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/settings")({
  head: () => ({ meta: [{ title: "Settings · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: SettingsPage,
});

const GROUPS: { title: string; description: string; keys: string[] }[] = [
  {
    title: "Meta app",
    description: "From developers.facebook.com → your app → App settings → Basic.",
    keys: ["META_APP_ID", "META_APP_SECRET", "META_LOGIN_CONFIG_ID"],
  },
  {
    title: "AI",
    description: "Your Claude API key from console.anthropic.com → API keys. The model can stay as it is.",
    keys: ["ANTHROPIC_API_KEY", "CLAUDE_MODEL"],
  },
  {
    title: "Alerts",
    description: "Optional. Telegram: talk to @BotFather → /newbot for the token; message your bot, then find the chat ID with @userinfobot.",
    keys: ["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID", "ALERT_WEBHOOK_URL"],
  },
  {
    title: "Public pages",
    description: "Shown on the privacy and data-deletion pages Meta requires. The public address is filled in automatically.",
    keys: ["OPERATOR_NAME", "OPERATOR_EMAIL", "PUBLIC_URL"],
  },
];

function SettingsPage() {
  const qc = useQueryClient();
  const settings = useQuery({ queryKey: ["settings"], queryFn: () => getSettings() });
  const [draft, setDraft] = useState<Record<string, string>>({});
  const [saving, setSaving] = useState(false);

  const save = async (values: Record<string, string>, liveSending?: boolean) => {
    setSaving(true);
    try {
      await saveSettingsFn({ data: { values, ...(liveSending !== undefined ? { liveSending } : {}) } });
      toast.success("Saved.");
      setDraft({});
      await qc.invalidateQueries();
    } catch (e) {
      toast.error(errorText(e));
    } finally {
      setSaving(false);
    }
  };

  const s = settings.data;
  return (
    <Shell title="Settings" description="Keys and switches. Secret values are stored encrypted and never shown again.">
      {settings.isLoading && <LoadingBlock />}
      {settings.error && <ErrorBlock error={settings.error} />}
      {s && (
        <div className="space-y-6">
          <Card className={s.liveSending ? "border-emerald-300" : "border-amber-300"}>
            <CardHeader>
              <div className="flex items-center justify-between gap-4">
                <div>
                  <CardTitle>Real sending</CardTitle>
                  <CardDescription className="mt-1.5">
                    While off, everything is a dry run: the system decides and records what it would send, and sends nothing. Each business also has its own
                    "Live" switch.
                  </CardDescription>
                </div>
                <Switch
                  checked={s.liveSending}
                  disabled={saving || s.liveSendingSource === "secret"}
                  onCheckedChange={(v) => {
                    if (v && !confirm("Switch on real sending? Live businesses will message real people (or only their testers, if set).")) return;
                    save({}, v);
                  }}
                />
              </div>
              {s.liveSendingSource === "secret" && <p className="text-xs text-muted-foreground">Set by the LIVE_SENDING secret in Lovable Cloud.</p>}
            </CardHeader>
          </Card>

          {GROUPS.map((g) => (
            <Card key={g.title}>
              <CardHeader>
                <CardTitle>{g.title}</CardTitle>
                <CardDescription>{g.description}</CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                {g.keys.map((key) => {
                  const f = s.fields.find((x) => x.key === key);
                  if (!f) return null;
                  const fromSecret = f.source === "secret";
                  return (
                    <div key={key} className="space-y-1.5">
                      <div className="flex items-center gap-2">
                        <Label htmlFor={key}>{f.label}</Label>
                        {f.set ? <Pill tone="green">{f.secret ? "saved" : "set"}</Pill> : <Pill tone="gray">empty</Pill>}
                        {fromSecret && <Pill tone="blue">from Lovable Cloud secret</Pill>}
                      </div>
                      <Input
                        id={key}
                        type={f.secret ? "password" : "text"}
                        autoComplete="off"
                        disabled={fromSecret}
                        placeholder={f.secret ? (f.set ? "•••••••• (type to replace)" : "paste here") : ""}
                        value={draft[key] ?? (f.secret ? "" : (f.value ?? ""))}
                        onChange={(e) => setDraft((d) => ({ ...d, [key]: e.target.value }))}
                      />
                    </div>
                  );
                })}
                <div className="flex gap-2">
                  <Button
                    disabled={saving || !g.keys.some((k) => draft[k] !== undefined)}
                    onClick={() => save(Object.fromEntries(g.keys.filter((k) => draft[k] !== undefined).map((k) => [k, draft[k]!])))}
                  >
                    Save
                  </Button>
                  {g.keys.some((k) => s.fields.find((f) => f.key === k)?.secret && s.fields.find((f) => f.key === k)?.set && s.fields.find((f) => f.key === k)?.source === "dashboard") && (
                    <Button
                      variant="ghost"
                      disabled={saving}
                      onClick={() => {
                        const secretKeys = g.keys.filter((k) => s.fields.find((f) => f.key === k)?.secret);
                        if (confirm("Clear the saved secret value(s) in this section?")) save(Object.fromEntries(secretKeys.map((k) => [k, ""])));
                      }}
                    >
                      Clear secrets
                    </Button>
                  )}
                </div>
              </CardContent>
            </Card>
          ))}

          <PasswordCard fromSecret={s.password.fromSecret} />
          <ReviewerCard exists={s.reviewer.exists} createdAt={s.reviewer.createdAt} />
        </div>
      )}
    </Shell>
  );
}

function PasswordCard({ fromSecret }: { fromSecret: boolean }) {
  const [current, setCurrent] = useState("");
  const [next, setNext] = useState("");
  const [busy, setBusy] = useState(false);
  const submit = async (e: FormEvent) => {
    e.preventDefault();
    setBusy(true);
    try {
      const res = await changePasswordFn({ data: { current, next } });
      if (res.ok) {
        toast.success("Password changed.");
        setCurrent("");
        setNext("");
      } else toast.error(res.error ?? "Could not change the password.");
    } catch (err) {
      toast.error(errorText(err));
    } finally {
      setBusy(false);
    }
  };
  return (
    <Card>
      <CardHeader>
        <CardTitle>Dashboard password</CardTitle>
        <CardDescription>{fromSecret ? "Set by the ADMIN_PASSWORD secret in Lovable Cloud." : "Changing it signs out every other browser."}</CardDescription>
      </CardHeader>
      {!fromSecret && (
        <CardContent>
          <form onSubmit={submit} className="grid gap-3 sm:grid-cols-[1fr_1fr_auto] sm:items-end">
            <div className="space-y-1.5">
              <Label htmlFor="cur">Current password</Label>
              <Input id="cur" type="password" autoComplete="current-password" value={current} onChange={(e) => setCurrent(e.target.value)} required />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="new">New password</Label>
              <Input id="new" type="password" autoComplete="new-password" value={next} onChange={(e) => setNext(e.target.value)} required minLength={8} />
            </div>
            <Button type="submit" disabled={busy}>
              Change
            </Button>
          </form>
        </CardContent>
      )}
    </Card>
  );
}

function ReviewerCard({ exists, createdAt }: { exists: boolean; createdAt: string | null }) {
  const qc = useQueryClient();
  const [password, setPassword] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const run = async (fn: () => Promise<void>) => {
    setBusy(true);
    try {
      await fn();
      await qc.invalidateQueries({ queryKey: ["settings"] });
    } catch (err) {
      toast.error(errorText(err));
    } finally {
      setBusy(false);
    }
  };
  const create = () =>
    run(async () => {
      if (exists && !window.confirm("Make a new reviewer password? The old one stops working.")) return;
      setPassword((await createReviewerPasswordFn()).password);
    });
  const remove = () =>
    run(async () => {
      await removeReviewerPasswordFn();
      setPassword(null);
      toast.success("Reviewer access is off.");
    });
  return (
    <Card>
      <CardHeader>
        <CardTitle>Reviewer access (Meta App Review)</CardTitle>
        <CardDescription>
          A second password for Meta's reviewers. With it they can look around, connect a Facebook Page and test the bot, but they cannot change
          settings, keys, businesses or real sending.
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-3 text-sm">
        {password && (
          <div className="rounded-lg border border-emerald-300 bg-emerald-50 p-3">
            <CopyField label="Reviewer password (shown only now: copy it into Meta's form)" value={password} />
          </div>
        )}
        <p className="text-muted-foreground">{exists ? `On, created ${timeAgo(createdAt)}.` : "Off."}</p>
        <div className="flex flex-wrap gap-2">
          <Button onClick={create} disabled={busy}>
            {exists ? "Make a new password" : "Create reviewer password"}
          </Button>
          {exists && (
            <Button variant="outline" onClick={remove} disabled={busy}>
              Turn off
            </Button>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
