type Fields = Record<string, unknown>;

export interface Logger {
  info(msg: string, fields?: Fields): void;
  warn(msg: string, fields?: Fields): void;
  error(msg: string, fields?: Fields): void;
}

function write(level: string, msg: string, fields?: Fields) {
  const line = JSON.stringify({ t: new Date().toISOString(), level, msg, ...fields }, (_k, v) =>
    v instanceof Error ? { name: v.name, message: v.message } : v,
  );
  (level === 'error' ? process.stderr : process.stdout).write(line + '\n');
}

export const log: Logger = {
  info: (m, f) => write('info', m, f),
  warn: (m, f) => write('warn', m, f),
  error: (m, f) => write('error', m, f),
};

export const silentLog: Logger = { info() {}, warn() {}, error() {} };
