import { createFileRoute } from "@tanstack/react-router";
import { operatorInfoFn } from "@/lib/api/public.functions";

// Meta requires data deletion instructions: App settings → Basic → User data deletion.
export const Route = createFileRoute("/data-deletion")({
  head: () => ({ meta: [{ title: "Data deletion" }] }),
  loader: () => operatorInfoFn(),
  component: DataDeletionPage,
});

function DataDeletionPage() {
  const op = Route.useLoaderData();
  const contact = op.email ? <a href={`mailto:${op.email}`}>{op.email}</a> : "a direct message to the page";
  return (
    <main className="mx-auto max-w-2xl px-5 py-12 text-sm leading-relaxed [&_h1]:mb-6 [&_h1]:text-2xl [&_h1]:font-semibold [&_p]:mb-4 [&_a]:underline">
      <h1>Data deletion</h1>
      <p>
        To delete the data we hold about you, send "delete my data" to the account you messaged, or write to {contact}. We delete your conversation and
        profile details within 30 days and confirm when it is done.
      </p>
      <p>To stop automated messages at any time, reply STOP.</p>
    </main>
  );
}
