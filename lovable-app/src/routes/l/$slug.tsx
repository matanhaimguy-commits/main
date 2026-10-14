import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { leadFormInfoFn, submitLeadFn } from "@/lib/api/public.functions";

// The public lead form. It works for everyone, whatever Meta lets the app receive: comment replies and
// Instagram instant replies link here, and every submission lands in the Inbox as a qualified lead.
export const Route = createFileRoute("/l/$slug")({
  validateSearch: (s: Record<string, unknown>): { s?: string } => (typeof s["s"] === "string" ? { s: s["s"] } : {}),
  loader: ({ params }) => leadFormInfoFn({ data: { slug: params.slug } }),
  head: ({ loaderData }) => ({ meta: [{ title: loaderData?.name ?? "Contact" }, { name: "robots", content: "noindex" }] }),
  component: LeadFormPage,
});

const T = {
  en: {
    title: "Leave your details",
    intro: "Fill this in and we will get back to you.",
    name: "Name",
    phone: "Phone / WhatsApp",
    instagram: "Instagram (optional)",
    need: "What do you need?",
    needHint: "e.g. more clients for my clinic",
    send: "Send",
    sending: "Sending…",
    consent: "By sending, you agree that we contact you about your request.",
    privacy: "Privacy policy",
    thanks: (n: string) => `Thank you, ${n}! We have your details and will contact you soon.`,
    after: "Or choose a time yourself",
    errPhone: "Please check the phone number.",
    errName: "Please write your name.",
    errBusy: "Too many requests right now. Please try again in a while.",
    errOther: "Something went wrong. Please try again, or message us on Instagram.",
    missing: "This form is not available.",
  },
  sq: {
    title: "Lër të dhënat e tua",
    intro: "Plotëso formularin dhe të kontaktojmë së shpejti.",
    name: "Emri",
    phone: "Telefoni / WhatsApp",
    instagram: "Instagram (nuk është e detyrueshme)",
    need: "Çfarë të duhet?",
    needHint: "P.sh. më shumë klientë për klinikën time",
    send: "Dërgo",
    sending: "Po dërgohet…",
    consent: "Duke dërguar, pranon që të të kontaktojmë për kërkesën tënde.",
    privacy: "Politika e privatësisë",
    thanks: (n: string) => `Faleminderit, ${n}! I morëm të dhënat dhe të kontaktojmë së shpejti.`,
    after: "Ose zgjidh vetë orarin",
    errPhone: "Kontrollo numrin e telefonit.",
    errName: "Shkruaj emrin tënd.",
    errBusy: "Shumë kërkesa për momentin. Provo përsëri pak më vonë.",
    errOther: "Diçka nuk shkoi. Provo përsëri ose na shkruaj në Instagram.",
    missing: "Ky formular nuk është i disponueshëm.",
  },
  he: {
    title: "השאירו פרטים",
    intro: "מלאו את הטופס ונחזור אליכם בהקדם.",
    name: "שם",
    phone: "טלפון / וואטסאפ",
    instagram: "אינסטגרם (לא חובה)",
    need: "במה נוכל לעזור?",
    needHint: "למשל: יותר לקוחות לקליניקה שלי",
    send: "שליחה",
    sending: "שולח…",
    consent: "בשליחה אתם מסכימים שניצור איתכם קשר בנוגע לפנייה.",
    privacy: "מדיניות פרטיות",
    thanks: (n: string) => `תודה, ${n}! קיבלנו את הפרטים ונחזור אליכם בהקדם.`,
    after: "או בחרו מועד בעצמכם",
    errPhone: "בדקו את מספר הטלפון.",
    errName: "כתבו את שמכם.",
    errBusy: "יותר מדי פניות כרגע. נסו שוב מאוחר יותר.",
    errOther: "משהו השתבש. נסו שוב או כתבו לנו באינסטגרם.",
    missing: "הטופס אינו זמין.",
  },
} as const;

function LeadFormPage() {
  const info = Route.useLoaderData();
  const { slug } = Route.useParams();
  const { s } = Route.useSearch();
  const [f, setF] = useState({ name: "", phone: "", instagram: "", need: "", website: "" });
  const [state, setState] = useState<"idle" | "sending" | "done">("idle");
  const [error, setError] = useState<string | null>(null);
  const t = T[info?.language ?? "en"];
  const rtl = info?.language === "he";

  if (!info) {
    return <main className="mx-auto max-w-md px-5 py-16 text-center text-sm text-muted-foreground">{t.missing}</main>;
  }

  const send = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setState("sending");
    try {
      const res = await submitLeadFn({ data: { slug, ...f, source: s } });
      if (res.ok) {
        setState("done");
        return;
      }
      setError(res.reason === "phone" ? t.errPhone : res.reason === "name" ? t.errName : res.reason === "busy" ? t.errBusy : t.errOther);
    } catch {
      setError(t.errOther);
    }
    setState("idle");
  };
  const field = (k: keyof typeof f) => ({ value: f[k], onChange: (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => setF({ ...f, [k]: e.target.value }) });

  return (
    <main dir={rtl ? "rtl" : "ltr"} className="min-h-screen bg-neutral-50 px-5 py-10">
      <div className="mx-auto max-w-md rounded-2xl border bg-white p-6 shadow-sm">
        <div className="mb-1 text-xs font-medium uppercase tracking-wider text-muted-foreground">{info.name}</div>
        <h1 className="mb-2 text-2xl font-semibold leading-tight">{info.title ?? t.title}</h1>
        {state === "done" ? (
          <div className="space-y-5">
            <p className="text-base">{t.thanks(f.name.trim().split(/\s+/)[0] ?? "")}</p>
            {info.afterUrl && (
              <Button asChild variant="outline" className="w-full">
                <a href={info.afterUrl} rel="noreferrer">
                  {info.afterTitle ?? t.after}
                </a>
              </Button>
            )}
          </div>
        ) : (
          <form onSubmit={send} className="space-y-4">
            <p className="text-sm text-muted-foreground">{info.intro ?? t.intro}</p>
            <div className="space-y-1.5">
              <Label htmlFor="name">{t.name}</Label>
              <Input id="name" autoComplete="name" required maxLength={80} {...field("name")} />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="phone">{t.phone}</Label>
              <Input id="phone" type="tel" inputMode="tel" autoComplete="tel" required maxLength={30} dir="ltr" {...field("phone")} />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="instagram">{t.instagram}</Label>
              <Input id="instagram" maxLength={40} dir="ltr" placeholder="@" {...field("instagram")} />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="need">{t.need}</Label>
              <Textarea id="need" rows={3} maxLength={600} placeholder={t.needHint} {...field("need")} />
            </div>
            {/* Bots fill every field; people never see this one. */}
            <input type="text" tabIndex={-1} autoComplete="off" aria-hidden className="hidden" {...field("website")} />
            {error && <p className="text-sm text-rose-700">{error}</p>}
            <Button type="submit" className="w-full" disabled={state === "sending"}>
              {state === "sending" ? t.sending : t.send}
            </Button>
            <p className="text-xs text-muted-foreground">
              {t.consent}{" "}
              <Link to="/privacy" className="underline">
                {t.privacy}
              </Link>
            </p>
          </form>
        )}
      </div>
    </main>
  );
}
