// Every word that appears on screen. Headlines are verbatim from docs/research/ad-library-2026-11-05.md (Meta Ad
// Library, Israel, active ads, search "יועץ משכנתאות", 5 Nov 2026), typed on our own paper: no names, logos or
// screenshots. Drop order = this order (p1 is the hook slip; the cascade follows `cascade`).
(function (SS) {
  SS.content = {
    slips: {
      p1: { text: 'ההחזר על המשכנתא עלה? בדיקה חינם', stamp: 'חינם' },
      p2: { text: 'אבחון כלכלי בחינם וללא התחייבות', stamp: 'חינם' },
      p3: { text: 'השאירו פרטים לשיחת התאמה ראשונית ללא עלות.>>', stamp: 'ללא עלות' },
      p4: { text: 'השאירו פרטים עכשיו לבדיקה חינמית ללא התחייבות >>', stamp: 'חינם' },
      p5: { text: 'לתיאום פגישת ייעוץ ללא עלות >>', stamp: 'ללא עלות' },
      p6: { text: 'לבדיקה אונליין בכמה ניתן לחסוך >>', stamp: 'לחסוך' },
      p7: { text: 'בדקו כמה תוכלו לחסוך במשכנתא שלכם', stamp: 'לחסוך' },
      p8: { text: 'הפחתת התשלומים החודשיים>>', stamp: 'לחסוך' },
      o1: { text: 'בדקו אם מחזור חלקי רלוונטי >>' },
      o2: { text: 'קיבלתם אישור עקרוני?' },
      o3: { text: 'תשלום רק על בסיס הצלחה בלבד >>' },
      o4: { text: 'הטבת ייעוץ משכנתאות בפרויקט התקומה! לפרטים >' },
      o5: { text: 'לחצו כאן, לקבלת מידע נוסף!' },
      // its headline carries other numbers, so it lies face down: the only figures on screen are 8, 14 and the date
      o6: { text: '', back: true }
    },
    // the key line of each spoken line: [voice word index, on-screen word]. covers = voice words the captions skip.
    keys: [
      { line: 1, words: [[0, 'רק'], [1, 'שואלים'], [2, 'אתכם'], [3, 'מחיר?']], covers: [0, 3] },
      { line: 2, one: true, words: [[0, 'חיפשתי'], [1, '"יועץ'], [2, 'משכנתאות"']], covers: [0, 2] },
      { line: 3, tally: true, covers: [0, 2] },
      { line: 4, words: [[5, 'לפי'], [6, 'מה'], [8, 'בוחרים?']], covers: [5, 8] },
      { line: 5, words: [[0, 'תכלס,'], [1, 'לפי'], [2, 'המחיר.']], covers: [0, 2] },
      { line: 6, words: [[4, 'ככה'], [5, 'כותבים'], [6, 'בתחום.']], covers: [4, 6] },
      { line: 7, words: [[1, 'תפתחו'], [3, 'את'], [4, 'המודעה'], [5, 'שלכם.']], covers: [0, 5] },
      { line: 8, words: [[0, 'תכסו'], [1, 'את'], [2, 'שם'], [3, 'העסק']], covers: [0, 3] },
      { line: 9, words: [[0, 'המתחרה'], [2, 'היה'], [3, 'יכול'], [4, 'לכתוב'], [5, 'את'], [6, 'זה?']], covers: [0, 7] },
      { line: 10, words: [[0, 'אם'], [1, 'כן,'], [2, 'תחליפו'], [3, 'אותה.']], covers: [0, 3] },
      // the pointer stays up through line 12 so the top of the frame is never empty while the caret blinks (D3)
      { line: 11, words: [[0, 'למשל,'], [1, 'מה'], [3, 'קורה'], [4, 'אצלכם'], [5, 'בפגישה'], [6, 'הראשונה?']], covers: [0, 6] }
    ],
    source: ['ספריית המודעות של Meta · ישראל', 'מודעות פעילות · 5.11.2026'],
    tally: { count: 8, of: 'מתוך', total: '14' },
    sticker: '₪?',
    viewer: { label: 'המודעה שלכם', name: '[שם העסק]', headline: '[הכותרת]' },
    rival: { label: 'המודעה של המתחרה', name: '[שם העסק]', headline: '[הכותרת]' },   // the same headline, word for word
    retype: 'חינם',   // the old reflex, typed on "במשהו" and struck out on "לא"

    example: { label: 'דוגמה' },
    cta: 'שמרו · שלחו לחבר עם עסק'
  };
})((window.SS = window.SS || {}));
