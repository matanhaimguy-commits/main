export interface Issue {
  level: 'error' | 'warn';
  business: string;
  where?: string;
  message: string;
}

/** Records one finding of the audit. */
export type AddIssue = (level: Issue['level'], message: string, where?: string) => void;
