import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link } from "@tanstack/react-router";
import type { ReactNode } from "react";
import { CopyField } from "@/components/app/copy-field";
import { Shell } from "@/components/app/shell";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getOverview } from "@/lib/api/setup.functions";
import { requireLogin } from "@/lib/session";

export const Route = createFileRoute("/guide")({
  head: () => ({ meta: [{ title: "Meta app guide · Social Agent" }, { name: "robots", content: "noindex" }] }),
  beforeLoad: requireLogin,
  component: GuidePage,
});

function Section({ title, children }: { title: string; children: ReactNode }) {
  return (
    <Card>
      <CardHeader className="pb-3">
        <CardTitle className="text-base">{title}</CardTitle>
      </CardHeader>
      <CardContent className="space-y-2 text-sm leading-relaxed [&_li]:ml-5 [&_ol]:list-decimal [&_ol]:space-y-2 [&_ul]:list-disc [&_ul]:space-y-1">
        {children}
      </CardContent>
    </Card>
  );
}

function GuidePage() {
  const o = useQuery({ queryKey: ["overview"], queryFn: () => getOverview() }).data;
  return (
    <Shell title="Create the Meta app" description="About 20 minutes, once. The values to paste are filled in for you below.">
      <div className="space-y-4">
        <Section title="Before you start">
          <ul>
            <li>An Instagram professional (business or creator) account linked to your Facebook Page, and you are an admin of the Page.</li>
            <li>
              In the Instagram app: Settings → Messages and story replies → Message controls → Connected tools → turn on <b>Allow access to messages</b>.
            </li>
            <li>A second Instagram/Facebook account for testing. Comments from the business account itself are ignored on purpose.</li>
          </ul>
        </Section>

        <Section title="1. Create the app">
          <ol>
            <li>
              Go to <b>developers.facebook.com → My Apps → Create App</b>. If asked for a use case, pick <b>Other</b>, then app type <b>Business</b>.
              Connect your Business portfolio if asked.
            </li>
            <li>
              Add these products (<b>Add product</b> in the left menu): <b>Facebook Login for Business</b>, <b>Messenger</b>, <b>Instagram</b> (the "API
              setup with Facebook login" option) and <b>Webhooks</b>.
            </li>
          </ol>
        </Section>

        <Section title="2. App settings → Basic">
          <p>Paste these two, add an app icon, a category and a contact email, then Save:</p>
          <div className="rounded-lg border p-3">
            <CopyField label="Privacy Policy URL" value={o?.urls.privacy} />
            <CopyField label="User data deletion URL" value={o?.urls.dataDeletion} />
          </div>
          <p>
            On the same screen, copy the <b>App ID</b> and the <b>App Secret</b> (click Show) into{" "}
            <Link to="/settings" className="underline">
              Settings
            </Link>{" "}
            here, and Save.
          </p>
        </Section>

        <Section title="3. Facebook Login → Settings">
          <p>
            Paste this into <b>Valid OAuth Redirect URIs</b> and Save:
          </p>
          <div className="rounded-lg border p-3">
            <CopyField label="Redirect URI" value={o?.urls.callback} />
          </div>
          <p className="text-muted-foreground">
            If your app shows a <b>Configurations</b> tab instead of permissions: create one (login variation General, token type User access token,
            the permissions listed at the bottom of this page) and paste its ID in Settings → "Facebook Login configuration ID".
          </p>
        </Section>

        <Section title="4. Roles and Live mode">
          <ol>
            <li>
              <b>App roles → Roles:</b> add your second (test) Facebook account as a <b>Tester</b>, and accept the invite from that account.
            </li>
            <li>
              Switch the app from <b>Development</b> to <b>Live</b> with the toggle at the top of the Meta dashboard.
            </li>
          </ol>
        </Section>

        <Section title="5. Connect and register">
          <p>
            Go to{" "}
            <Link to="/connect" className="underline">
              Connect
            </Link>
            : press <b>Connect Facebook &amp; Instagram</b>, tick your Page and its Instagram account, choose the business for the Page, then press{" "}
            <b>Register webhooks</b>.
          </p>
        </Section>

        <Section title="Meta's review (to answer strangers)">
          <p>
            Until your app has <b>Advanced Access</b>, Meta only delivers messages from people with a role on the app (you and your testers). Anyone
            else gets error 200/2018028. When the test account works end to end, go to <b>App Review → Permissions and features</b> and request
            Advanced Access for:
          </p>
          <p className="font-mono text-xs">
            pages_messaging, pages_manage_metadata, pages_read_engagement, pages_manage_engagement, instagram_basic, instagram_manage_messages,
            instagram_manage_comments, business_management
          </p>
          <p>Complete Business Verification. Meta asks for a short screen recording: your tester comments, receives the DM, taps, and gets an answer.</p>
        </Section>
      </div>
    </Shell>
  );
}
