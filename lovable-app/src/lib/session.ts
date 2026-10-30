import { redirect } from "@tanstack/react-router";
import { getSession } from "@/lib/api/session.functions";

/** `beforeLoad` for dashboard pages: sends visitors without a session to /login. */
export async function requireLogin() {
  const session = await getSession();
  if (!session.loggedIn) throw redirect({ to: "/login" });
  return { session };
}
