import { useQuery, useQueryClient } from "@tanstack/react-query";
import { Link, useRouter } from "@tanstack/react-router";
import {
  Activity,
  BookOpen,
  Bot,
  Building2,
  Clapperboard,
  Gauge,
  Inbox,
  LogOut,
  PlugZap,
  Settings,
  type LucideIcon,
} from "lucide-react";
import type { ReactNode } from "react";
import { Toaster } from "@/components/ui/sonner";
import { getSession, logoutFn } from "@/lib/api/session.functions";
import { cn } from "@/lib/utils";

const NAV: { to: string; label: string; icon: LucideIcon }[] = [
  { to: "/", label: "Overview", icon: Gauge },
  { to: "/inbox", label: "Inbox", icon: Inbox },
  { to: "/businesses", label: "Businesses", icon: Building2 },
  { to: "/content", label: "Content", icon: Clapperboard },
  { to: "/activity", label: "Activity", icon: Activity },
  { to: "/test", label: "Test the bot", icon: Bot },
  { to: "/connect", label: "Connect", icon: PlugZap },
  { to: "/settings", label: "Settings", icon: Settings },
  { to: "/guide", label: "Meta app guide", icon: BookOpen },
];

export function Shell({ title, description, actions, children }: { title: string; description?: ReactNode; actions?: ReactNode; children: ReactNode }) {
  const router = useRouter();
  const queryClient = useQueryClient();
  const session = useQuery({ queryKey: ["session"], queryFn: () => getSession(), staleTime: 60_000 });
  const reviewer = session.data?.role === "reviewer";
  const nav = reviewer ? NAV.filter((item) => item.to !== "/settings") : NAV;
  const logout = async () => {
    await logoutFn();
    queryClient.clear();
    await router.navigate({ to: "/login" });
  };
  return (
    <div className="min-h-screen bg-muted/30">
      <aside className="fixed inset-y-0 left-0 hidden w-56 flex-col border-r bg-background md:flex">
        <div className="px-5 py-5">
          <div className="text-base font-semibold tracking-tight">Social Agent</div>
          <div className="text-xs text-muted-foreground">Instagram &amp; Facebook DMs</div>
        </div>
        <nav className="flex-1 space-y-0.5 px-3">
          {nav.map((item) => (
            <Link
              key={item.to}
              to={item.to}
              activeOptions={{ exact: item.to === "/" }}
              className="flex items-center gap-2.5 rounded-md px-2.5 py-2 text-sm text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
              activeProps={{ className: "bg-accent font-medium text-foreground" }}
            >
              <item.icon className="h-4 w-4" />
              {item.label}
            </Link>
          ))}
        </nav>
        <button
          onClick={logout}
          className="m-3 flex items-center gap-2.5 rounded-md px-2.5 py-2 text-sm text-muted-foreground hover:bg-accent hover:text-foreground"
        >
          <LogOut className="h-4 w-4" /> Log out
        </button>
      </aside>

      <div className="sticky top-0 z-10 flex gap-1 overflow-x-auto border-b bg-background px-3 py-2 md:hidden">
        {nav.map((item) => (
          <Link
            key={item.to}
            to={item.to}
            activeOptions={{ exact: item.to === "/" }}
            className="flex shrink-0 items-center gap-1.5 rounded-md px-2.5 py-1.5 text-xs text-muted-foreground"
            activeProps={{ className: "bg-accent font-medium text-foreground" }}
          >
            <item.icon className="h-3.5 w-3.5" />
            {item.label}
          </Link>
        ))}
      </div>

      <main className="md:pl-56">
        <div className="mx-auto max-w-6xl px-4 py-6 md:px-8 md:py-8">
          {reviewer && (
            <div className="mb-5 rounded-xl border border-sky-200 bg-sky-50 p-3 text-sm text-sky-900">
              Reviewer access: you can look at every page, connect a Facebook Page under Connect, and talk to the bot under Test the bot. Changing
              settings, businesses and sending is reserved for the owner.
            </div>
          )}
          <div className="mb-6 flex flex-wrap items-start justify-between gap-3">
            <div>
              <h1 className="text-2xl font-semibold tracking-tight">{title}</h1>
              {description && <p className="mt-1 text-sm text-muted-foreground">{description}</p>}
            </div>
            {actions && <div className="flex flex-wrap gap-2">{actions}</div>}
          </div>
          {children}
        </div>
      </main>
      <Toaster richColors position="top-right" />
    </div>
  );
}

export function StatusMark({ state }: { state: "done" | "todo" | "info" | "warn" }) {
  return (
    <span
      className={cn(
        "mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full text-[11px] font-bold",
        state === "done" && "bg-emerald-100 text-emerald-700",
        state === "todo" && "bg-rose-100 text-rose-700",
        state === "warn" && "bg-amber-100 text-amber-800",
        state === "info" && "bg-muted text-muted-foreground",
      )}
    >
      {state === "done" ? "✓" : state === "todo" ? "!" : state === "warn" ? "!" : "•"}
    </span>
  );
}

export function Step({ state, title, children }: { state: "done" | "todo" | "info" | "warn"; title: string; children?: ReactNode }) {
  return (
    <div className="flex gap-3 py-3">
      <StatusMark state={state} />
      <div className="min-w-0 flex-1">
        <div className="text-sm font-medium">{title}</div>
        {children && <div className="mt-1 text-sm text-muted-foreground">{children}</div>}
      </div>
    </div>
  );
}

export function Pill({ tone, children }: { tone: "green" | "amber" | "red" | "gray" | "blue"; children: ReactNode }) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium",
        tone === "green" && "bg-emerald-100 text-emerald-800",
        tone === "amber" && "bg-amber-100 text-amber-800",
        tone === "red" && "bg-rose-100 text-rose-800",
        tone === "gray" && "bg-muted text-muted-foreground",
        tone === "blue" && "bg-sky-100 text-sky-800",
      )}
    >
      {children}
    </span>
  );
}

export function LoadingBlock() {
  return <div className="rounded-xl border bg-background p-10 text-center text-sm text-muted-foreground">Loading…</div>;
}

export function ErrorBlock({ error }: { error: unknown }) {
  const message = error instanceof Error ? error.message : String(error);
  if (message.includes("UNAUTHENTICATED")) return <LoadingBlock />;
  return <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-800">Something went wrong: {message}</div>;
}
