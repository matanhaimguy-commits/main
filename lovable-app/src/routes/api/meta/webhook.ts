import { createFileRoute } from "@tanstack/react-router";
import { guarded, webhookGet, webhookPost } from "@/server/handlers.server";

// Meta's webhook callback URL: https://<your app>/api/meta/webhook
export const Route = createFileRoute("/api/meta/webhook")({
  server: {
    handlers: {
      GET: ({ request }) => guarded("webhook verification", () => webhookGet(request)),
      POST: ({ request }) => guarded("webhook", () => webhookPost(request)),
    },
  },
});
