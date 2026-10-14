import { createFileRoute, Link } from "@tanstack/react-router";
import { operatorInfoFn } from "@/lib/api/public.functions";

// Meta requires a privacy policy URL for a Live app: App settings → Basic → Privacy Policy URL.
export const Route = createFileRoute("/privacy")({
  head: () => ({ meta: [{ title: "Privacy policy" }] }),
  loader: () => operatorInfoFn(),
  component: PrivacyPage,
});

function PrivacyPage() {
  const op = Route.useLoaderData();
  const operator = op.name ?? "the business operating this page";
  const contact = op.email ? <a href={`mailto:${op.email}`}>{op.email}</a> : "a direct message to the page";
  return (
    <main className="prose mx-auto max-w-2xl px-5 py-12 text-sm leading-relaxed [&_h1]:mb-6 [&_h1]:text-2xl [&_h1]:font-semibold [&_p]:mb-4 [&_a]:underline">
      <h1>Privacy policy</h1>
      <p>
        This service is operated by {operator}. It answers comments and direct messages sent to the Facebook Pages and Instagram accounts it manages,
        through Meta's official APIs.
      </p>
      <p>
        <b>What we store:</b> messages and comments you send to these accounts, your public name or username, and details you choose to share in the
        conversation (such as your email or phone number).
      </p>
      <p>
        <b>Why:</b> to reply to you, to send what you asked for, and to follow up on your request. Replies may be written by an automated assistant; a
        person on the team can step in at any time.
      </p>
      <p>
        <b>Sharing:</b> we do not sell your data. Message text is processed by our hosting, database and AI providers only to produce replies.
      </p>
      <p>
        <b>Retention and deletion:</b> see <Link to="/data-deletion">data deletion</Link>. Contact: {contact}.
      </p>
    </main>
  );
}
