import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link, useRouter } from "@tanstack/react-router";
import { useState, type FormEvent } from "react";
import { toast } from "sonner";
import { ErrorBlock, LoadingBlock, Pill, Shell } from "@/components/app/shell";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createBusinessFn, listBusinessesFn } from "@/lib/api/businesses.functions";
import { errorText } from "@/lib/format";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/businesses/")({
  head: () => ({ meta: [{ title: "Businesses · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: BusinessesPage,
});

const toSlug = (name: string) =>
  name
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 40);

function BusinessesPage() {
  const list = useQuery({ queryKey: ["businesses"], queryFn: () => listBusinessesFn() });
  const [open, setOpen] = useState(false);

  return (
    <Shell
      title="Businesses"
      description="Each business has its own details, links and comment-to-DM funnels. The AI answers with what is written here."
      actions={<Button onClick={() => setOpen(true)}>New business</Button>}
    >
      {list.isLoading && <LoadingBlock />}
      {list.error && <ErrorBlock error={list.error} />}
      {list.data && (
        <div className="space-y-3">
          {list.data.invalid.map((b) => (
            <Card key={b.slug} className="border-rose-200">
              <CardContent className="flex flex-wrap items-center justify-between gap-3 p-4">
                <div>
                  <div className="font-medium">{b.slug}</div>
                  <div className="text-sm text-rose-700">Not running: {b.problems.slice(0, 2).join("; ")}</div>
                </div>
                <Button asChild size="sm">
                  <Link to="/businesses/$slug" params={{ slug: b.slug }}>
                    Fix
                  </Link>
                </Button>
              </CardContent>
            </Card>
          ))}
          {list.data.businesses.length === 0 && list.data.invalid.length === 0 && (
            <Card>
              <CardContent className="p-10 text-center">
                <p className="text-sm text-muted-foreground">No businesses yet. Start with your own.</p>
                <Button className="mt-4" onClick={() => setOpen(true)}>
                  Create the first business
                </Button>
              </CardContent>
            </Card>
          )}
          {list.data.businesses.map((b) => (
            <Link key={b.slug} to="/businesses/$slug" params={{ slug: b.slug }} className="block">
              <Card className="transition-colors hover:bg-accent/40">
                <CardContent className="flex flex-wrap items-center justify-between gap-3 p-4">
                  <div>
                    <div className="font-medium">{b.name}</div>
                    <div className="text-xs text-muted-foreground">
                      {b.slug} · {b.activeFunnels}/{b.funnels} funnels active · {b.connected ? "Page connected" : "no Page yet"}
                    </div>
                  </div>
                  <div className="flex flex-wrap items-center gap-2">
                    {b.errors > 0 && <Pill tone="red">{b.errors} to fix</Pill>}
                    {b.warnings > 0 && <Pill tone="amber">{b.warnings} warnings</Pill>}
                    {!b.enabled ? <Pill tone="gray">Disabled</Pill> : b.live ? <Pill tone="green">Live</Pill> : <Pill tone="amber">Dry run</Pill>}
                  </div>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      )}
      <NewBusinessDialog open={open} onOpenChange={setOpen} />
    </Shell>
  );
}

function NewBusinessDialog({ open, onOpenChange }: { open: boolean; onOpenChange: (v: boolean) => void }) {
  const router = useRouter();
  const [name, setName] = useState("");
  const [slug, setSlug] = useState("");
  const [slugTouched, setSlugTouched] = useState(false);
  const [busy, setBusy] = useState(false);
  const effectiveSlug = slugTouched ? slug : toSlug(name);

  const submit = async (e: FormEvent) => {
    e.preventDefault();
    setBusy(true);
    try {
      const res = await createBusinessFn({ data: { slug: effectiveSlug, name: name.trim() } });
      if (!res.ok) return void toast.error(res.problems.join(" "));
      onOpenChange(false);
      await router.navigate({ to: "/businesses/$slug", params: { slug: effectiveSlug } });
    } catch (err) {
      toast.error(errorText(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <form onSubmit={submit} className="space-y-4">
          <DialogHeader>
            <DialogTitle>New business</DialogTitle>
            <DialogDescription>You fill in the details on the next screen. Nothing goes live until you switch it on.</DialogDescription>
          </DialogHeader>
          <div className="space-y-1.5">
            <Label htmlFor="bname">Business name</Label>
            <Input id="bname" value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Matan Studio" required autoFocus />
          </div>
          <div className="space-y-1.5">
            <Label htmlFor="bslug">Short id</Label>
            <Input
              id="bslug"
              value={effectiveSlug}
              onChange={(e) => {
                setSlugTouched(true);
                setSlug(e.target.value.toLowerCase());
              }}
              pattern="[a-z0-9][a-z0-9_\-]*"
              required
            />
            <p className="text-xs text-muted-foreground">Lowercase letters, digits and dashes. It cannot change later.</p>
          </div>
          <DialogFooter>
            <Button type="submit" disabled={busy || !effectiveSlug}>
              Create
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
