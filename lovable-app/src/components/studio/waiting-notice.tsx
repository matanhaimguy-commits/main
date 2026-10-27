/** "2 pieces are waiting on you." above the list; nothing when none are. */
export function WaitingNotice({ count }: { count: number }) {
  if (count === 0) return null;
  return (
    <div className="mb-4 rounded-xl border border-amber-200 bg-amber-50 p-3 text-sm text-amber-900">
      {count === 1 ? "1 piece is waiting on you." : `${count} pieces are waiting on you.`}
    </div>
  );
}
