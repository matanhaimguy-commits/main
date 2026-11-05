import { createFileRoute } from "@tanstack/react-router";
import { connectStart, guarded } from "@/server/handlers.server";

// "Connect Facebook & Instagram": sends the admin to Meta's login dialog.
export const Route = createFileRoute("/api/connect/start")({
  server: {
    handlers: {
      GET: ({ request }) => guarded("connect start", () => connectStart(request)),
    },
  },
});
