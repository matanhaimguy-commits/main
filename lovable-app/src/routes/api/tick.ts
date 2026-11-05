import { createFileRoute } from "@tanstack/react-router";
import { guarded, tickPost } from "@/server/handlers.server";

// Called every minute by the database scheduler (pg_cron + pg_net), with a shared secret.
export const Route = createFileRoute("/api/tick")({
  server: {
    handlers: {
      POST: ({ request }) => guarded("tick", () => tickPost(request)),
    },
  },
});
