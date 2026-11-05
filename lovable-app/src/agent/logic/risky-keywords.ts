import type { Funnel } from '../config/schema';
import { matchesKeyword, normalize } from './text';

// Ordinary words that show up in comments. Used to show what a risky keyword would catch.
const COMMON_WORDS = (
  'about above across after again against agent ago agree ahead almost alone along already also although always ' +
  'amazing among another answer anyone anything appreciate area around article artist awesome back beautiful ' +
  'because before begin behind believe best better between beyond birthday book bought brand bring broken brother ' +
  'business busy came cancel cannot care catch change cheap check child choose class clean close code color come ' +
  'comment company content cool could course cover crazy create custom daily dark dear deal details different ' +
  'dinner discount done download dream drive early easy enough even event every everyone exactly expensive family ' +
  'feeling find fine first follow follower food free friend from front full funny game gift girl give glad going ' +
  'good great group guide guidelines guided misguided guy hair happy hard have hello help here hope house idea ' +
  'important inspire inspiring interest job join just keep kind know last later learn less life like link live ' +
  'love lovely made make many message mind money month more morning much music need never news next nice night ' +
  'nothing offer only open order other page people perfect phone photo place plan please post price product ' +
  'question quick ready real really reason recipe reply right same save send share shop show sign since site ' +
  'some something soon sorry start still story style sure take team thank thanks that there thing think this ' +
  'time today together tomorrow tried true trying update video wait want watch week what when where which while ' +
  'with without women wonderful work world would wow yes yesterday young ' +
  'מדריך מדריכה הדרכה שלום תודה רבה מה קורה איך כמה עולה מחיר מחירים אפשר פרטים בבקשה מעולה מדהים יפה אהבתי ' +
  'רוצה צריך צריכה שולחת שולח הודעה הודעות פרטי בפרטי לינק קישור קבוצה קורס סדנה וובינר מתנה חינם הנחה מבצע ' +
  'משלוח הזמנה הזמנתי לקוח לקוחה עסק עסקים שיווק פרסום ממומן קמפיין תוכן סרטון ריל רילס סטורי פוסט עוקבים ' +
  'אינסטגרם פייסבוק טיקטוק וואטסאפ טלפון מייל אתר חנות מוצר שירות פגישה שיחה ייעוץ זמן היום מחר אתמול בוקר ערב ' +
  'לילה שבוע חודש שנה תמיד אף פעם כן לא אולי ממש מאוד יותר פחות הכי גם רק עוד כבר עכשיו אחר כך אחרי לפני ' +
  'משפחה חבר חברה ילדים בית אוכל מתכון עוגה ספר ספרים שיר מוזיקה בגדים שמלה נעליים תיק צבע גודל מידה'
).split(/\s+/);

export function riskyMatches(keyword: string, mode: Funnel['match']): string[] {
  if (mode === 'exact') return [];
  const k = normalize(keyword);
  return COMMON_WORDS.filter((w) => w !== k && matchesKeyword(w, keyword, mode)).slice(0, 6);
}
