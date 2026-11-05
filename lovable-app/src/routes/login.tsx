import { useQueryClient } from "@tanstack/react-query";
import { createFileRoute, redirect, useRouter } from "@tanstack/react-router";
import { useState, type FormEvent } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createPasswordFn, getSession, loginFn } from "@/lib/api/session.functions";
import { errorText } from "@/lib/format";

export const Route = createFileRoute("/login")({
  head: () => ({ meta: [{ title: "Log in · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: async () => {
    const session = await getSession();
    if (session.loggedIn) throw redirect({ to: "/" });
    return { session };
  },
  component: LoginPage,
});

function LoginPage() {
  const { session } = Route.useRouteContext();
  const router = useRouter();
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const firstRun = session.db.ok && !session.hasPassword;

  const queryClient = useQueryClient();
  const submit = async (e: FormEvent) => {
    e.preventDefault();
    setError(null);
    if (firstRun && password !== confirm) return setError("The two passwords are different.");
    setBusy(true);
    try {
      const res = firstRun ? await createPasswordFn({ data: { password } }) : await loginFn({ data: { password } });
      if (!res.ok) return setError(res.error ?? "Could not log in.");
      // Owner and reviewer see different things: drop anything cached from another login.
      queryClient.clear();
      await router.navigate({ to: "/" });
    } catch (err) {
      setError(errorText(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-muted/30 px-4">
      <Card className="w-full max-w-sm">
        <CardHeader>
          <CardTitle className="text-xl">Social Agent</CardTitle>
          <CardDescription>
            {!session.db.ok
              ? "The database is not ready yet."
              : firstRun
                ? "Welcome. Choose a password for this dashboard. You will use it to log in from now on."
                : "Log in to manage your Instagram and Facebook automations."}
          </CardDescription>
        </CardHeader>
        <CardContent>
          {!session.db.ok ? (
            <p className="rounded-md bg-amber-50 p-3 text-sm text-amber-900">{session.db.problem}</p>
          ) : (
            <form onSubmit={submit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="password">{firstRun ? "New password" : "Password"}</Label>
                <Input id="password" type="password" autoComplete={firstRun ? "new-password" : "current-password"} value={password} onChange={(e) => setPassword(e.target.value)} autoFocus required />
              </div>
              {firstRun && (
                <div className="space-y-2">
                  <Label htmlFor="confirm">Repeat the password</Label>
                  <Input id="confirm" type="password" autoComplete="new-password" value={confirm} onChange={(e) => setConfirm(e.target.value)} required />
                  <p className="text-xs text-muted-foreground">At least 8 characters.</p>
                </div>
              )}
              {error && <p className="text-sm text-destructive">{error}</p>}
              <Button type="submit" className="w-full" disabled={busy}>
                {busy ? "One moment…" : firstRun ? "Create password" : "Log in"}
              </Button>
            </form>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
