# Green Life Albania: Voice of the Albanian buyer (VOC, local)

Collected 2026-10-20. Every quote below is copied verbatim with the original spelling (typos, missing diacritics and emoji kept). Nothing is paraphrased inside quote marks. Reviewer names are left out. People named in news articles are given by role and area only.

**Total: 64 verbatim Albanian quotes** (31 Google Maps reviews, 2 Facebook comments, 31 news and civic quotes from Albanian residents). A further 6 supporting items (English reviews, politicians, brand-written text) are listed separately and **not counted**.

---

## 0. What worked and what failed

| Source | Result |
|---|---|
| Google Maps (Apify `compass/crawler-google-places`, newest first, personal data off, max 150 reviews per place, cap $1.50) | **Worked.** All 7 targets were found, plus 4 neighbours. Of 378 reviews, 112 had text, and of those about 45 were in Albanian. Most reviews are stars only or one word. Green Life Albania: 29 reviews, 13 with text (6 in Albanian). Aquafilter: 3 reviews, all stars only. The "Filtra Uji Water Boutique" pin had 6 reviews, all stars only. "SV Filter Technik" turned out to sell car and oil filters, so it was dropped. Run aborted after the data landed to save spend. |
| Instagram (Apify `apify/instagram-scraper`, 12 posts each) | **Almost empty.** @greenlifealbania: 12 posts (6 to 19 Oct 2026), 0 buyer comments (the only comment is the brand's own caption). The handles @bluefilters.al and @albuji.al do not exist. |
| Facebook (Apify `apify/facebook-posts-scraper`, 62 posts from greenlifealbania, bluefiltersalbania, albafilters) | **Almost empty.** Only 2 buyer comments in total, both on Blue Filters and both asking the price. Green Life and Albafilters posts had no comments. Ad comments are not reachable with these tools. |
| Firecrawl search | **Failed:** the account is out of credits. |
| Reddit / forums in Albanian | **Nothing usable found.** The search returned only English expat threads. |
| YouTube (TranscriptAPI search) | Only brand videos and old TV clips came up, so comments were not scraped. |
| Albanian news (Exa search and fetch): ACQJ, Reporter.al/BIRN, Shteg.org, Lapsi, TV Klan, BoldNews/Ora News, Citizens.al, CNA, Euronews, Classlifestyle | **Worked.** This is the richest source of buyer voice on tap water, bidona and depozita. Shteg.org (10 Apr 2026) and Gazeta Shqip (27 Jan 2026, the chlorine-smell complaints) contain no resident quotes word for word, so they are used for context only. |

Apify spend: the Maps run was capped at $1.50, Instagram at $0.15 and Facebook at $0.25, with one RAG call of about $0.01. The tool did not report the exact charge. All runs were small (12 places and 378 reviews, 12 IG posts, 62 FB posts), so the total stays under the $2 cap.

Source keys used in the table:

- **GM-GL** Green Life Albania: https://www.google.com/maps/search/?api=1&query=Green%20Life%20Albania&query_place_id=ChIJv4eTtU4xUBMRMRRKanJ--bs
- **GM-BFT** Blue FILTERS Tirana: https://www.google.com/maps/search/?api=1&query=Blue%20FILTERS%20Tirana&query_place_id=ChIJkRTRiF4xUBMRtAEhelEdODU
- **GM-BFAL** Blue Filters AL - Filtra Uji: https://www.google.com/maps/search/?api=1&query=Blue%20Filters%20AL%20-%20Filtra%20Uji&query_place_id=ChIJ3Uhx9McxUBMRbuj30z3XkB8
- **GM-ALBUJI** Filtra Uji Tiranë - Albuji: https://www.google.com/maps/search/?api=1&query=Filtra%20Uji%20Tiran%C3%AB%20-%20Albuji&query_place_id=ChIJQ40mY7wxUBMRHsJURpqJ_dE
- **GM-ALBA** ALBAFILTERS SH.P.K: https://www.google.com/maps/search/?api=1&query=ALBAFILTERS%20SH.P.K&query_place_id=ChIJs8spdVA6UBMRsjXHsZwedWE
- **GM-WB** Water Boutique sh.p.k (Filtra uji) Tiranë: https://www.google.com/maps/search/?api=1&query=Water%20Boutique%20sh.p.k%20-%20(Filtra%20uji)%20Tiran%C3%AB&query_place_id=ChIJby2pkeIxUBMROPBbhF-wkc8
- **ACQJ** https://www.acqj.al/tirana-qe-nuk-pi-dot-uje-nga-rubineti/ (4 Sep 2025)
- **REP** https://www.reporter.al/2025/10/11/ne-tirane-uji-i-pijshem-rrjedh-vetem-ne-premtime/ (11 Oct 2025)
- **LAPSI** https://lapsi.al/2025/07/05/43-familje-ne-selite-te-tiranes-kater-dite-pa-uje-qytetaret-po-e-blejme (5 Jul 2025)
- **KLAN** https://tvklan.al/vetem-1-ore-uje-ne-dite-ne-ish-kombinat (29 Sep 2025)
- **BOLD1** https://boldnews.al/2025/10/22/kodra-e-diellit-thahet-per-uje-banoret-vetem-e-blejme-ukt-nuk-na-pergjigjet/ (22 Oct 2025)
- **BOLD2** https://boldnews.al/2025/06/09/video-shkoza-dy-jave-pa-uje-banoret-ujesjellesi-nuk-zgjidh-problemin-na-thone-lutuni-zotit/ (9 Jun 2025)
- **CIT** https://newsletter.citizens.al/p/tre-vjet-pas-rritjes-se-cmimit-banoret-e-tiranes-ende-nuk-kane-uje-ne-cezmat-e-tyre (27 Aug 2019)
- **CNA-M** https://www.cna.al/aktualitet/alarm-per-ujin-e-pijshem-ne-maliq-banoret-e-teroves-dhe-pendavinjit-n-i454082 (3 Feb 2026, Maliq, outside Tirana)
- **CLASS** https://www.classlifestyle.com/d/132/174/9952/si-eshte-gjendja-e-ujit-te-pijshem-ne-tirane-analizat-vene-alarmin/ (27 Aug 2016)
- **EURO** https://euronews.al/e-kemi-ujin-me-lire-se-kamza-dhe-korca-veliaj-edhe-ne-londer-blejne-uje/ (6 Apr 2023)
- **FB-BF** Blue Filters Albania Facebook posts (comment links are in the table)

---

## 1. Quote table (coded)

Column codes:

- **Desire** (the deeper desire): SAF = safety, HLT = health, FAM = family, MON = money, TIM = time and effort, STA = status, BEL = belonging, PEACE = peace of mind.
- **Stars** are given for reviews only.
- A dash means no signal in the quote.

### 1a. Google Maps reviews, 1 to 3 stars (fears and failures)

| # | quote | source | date | stars | want | desire | identity | fear | failed solution | trigger |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | "Kompania me jokorrekte ne treg!!!!! 3 orare na kane len per te ardhur tekniku per te rregulluar nje problem te pajisjes. Jo vetem qe nuk lajemrojne por edhe kur I telefonoj vetem nxjerrin justifikime!! Suportin teknik kompanite duhet ta kene me kryesoren,se per pajisje uji mund ti blini jashte per 500€,jo 2000€." | GM-BFT | 2025-06-25 | 1 | a technician who comes when promised | MON, TIM, respect | a buyer who paid premium and expects premium service | being abandoned after the sale; overpaying 4x | premium-price system with poor after-sales | the device broke and needed repair |
| 2 | "Aspak profesional, shpjegojne cdo gje me fjale te medha pervec pjeses qe kapari eshte i pakthyeshem dhe njerezit detyrohen ta blejne perndryshe humbin kaparin. Zero yje do ju jepja po te ishte e mundur." | GM-BFAL | 2020-05-16 | 1 | honest terms before paying | MON, control | someone who will not be fooled | pressure selling; a non-refundable deposit ("kapari") | a sales visit that used big words | the in-home demo and deposit moment |
| 3 | "Uje i pa perdorshem, me prani bakteresh dhe materialesh te ngurta si ai i pa filtruari! Keshtu shkruhet ne analizen e ISHP te kryer ne daten 24 mars 2023 per mostrat e analizuara nga uji i dale prej ketyre filtrave. Analiza u krye vetem per qellime konsumi, per nje linje rezidenciale, te pajisur me filter ne maj 2022. ISHP-se nuk iu dha informacion per marken apo kompanine e filtrit. per te ardhur keq edhe nga reagimi jo transparent i kompanise" | GM-ALBUJI | 2023-03-28 | 1 | proof that the filter really cleans | SAF, HLT | a careful checker who tests and verifies | the filter does nothing ("si ai i pa filtruari"); bacteria | a filter installed in May 2022 that failed a lab test | an independent lab test (ISHP) of the filtered water |

Non-Albanian low-star reviews (supporting only, not counted): "1200e ????" (GM-BFT, 2026-01-20, 1 star, a price shock); "It was nice but am not sure if there are perfect prices or water filters" (GM-WB, 2026-01-23, 2 stars); "Parking problem" (GM-BFAL, 2023-03-06, 1 star).

### 1b. Google Maps reviews, 5 stars (desires and winning words)

| # | quote | source | date | stars | want | desire | identity | fear | failed solution | trigger |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | "Uji me i mir, Kemi shpetuar nga bidonat. FALIMINERIT" | GM-ALBA | 2023-05-02 | 5 | to stop buying and carrying bottles | TIM, MON, relief | freed from a daily chore | going back to bidona | bidona / bottled water | being tired of hauling bidona |
| 5 | "Faleminderit, për shërbimin tuaj, por më e rëndësishmja është që jepni garanci 10 vjeçare." | GM-ALBA | 2024-12-17 | 5 | a long guarantee | PEACE, MON | a prudent buyer thinking long term | the device dying with no one responsible | – | comparing guarantees before buying |
| 6 | "Sistemet me te mira sot per sot. Mos e lodhni veten me sisteme te tjera te pacertifikuara. Flitet per shendet, jo per para." | GM-BFAL | 2021-04-14 | 5 | a certified system | HLT, SAF | puts health before money; advises others | uncertified, cheap systems | "sisteme te tjera te pacertifikuara" | comparing systems |
| 7 | "Vlerë e shtuar në shtëpine tonë. Jeni më të mirët, një bravo e madhe 👏" | GM-BFAL | 2021-04-15 | 5 | an upgrade to the home | STA, FAM | proud homeowner | – | – | after installation |
| 8 | "Kemi perdorur Filtrat e Albuji ne ambientet e zyrave qendrore, gjithashtu dhe ne shtepite e stafit tone. Per te qene me te sigurt per cilesine dhe konsumimin e ujit te pijshem.  Stafi shume shume i sjellshem dhe korrekt, kemi ngelur shume te kenaqur nga sherbimi!" | GM-ALBUJI | 2023-12-13 | 5 | certainty about drinking water | SAF, PEACE | an employer who looks after people | uncertainty about tap-water quality | – | a business decision for office and staff homes |
| 9 | "Super Kompani, sherbim , cilesi , garanci, jetegjatesi! BRAVO👍" | GM-GL | 2025-01-07 | 5 | a durable system with a guarantee | PEACE, MON | a satisfied long-term owner | – | – | – |
| 10 | "Produket me te mira ne treg ,super i kenaqur qe te jem klient i juaji 😊" | GM-GL | 2025-11-24 | 5 | the best on the market | STA, BEL | proud to be "klient i juaji" | – | – | – |
| 11 | "Prej shum vitesh klient i knaqur👍" | GM-GL | 2025-11-24 | 5 | reliability over years | PEACE | a loyal long-term client | – | – | – |
| 12 | "Biznesi me i mire ne fushen e shendetit" | GM-GL | 2018-09-20 | 5 | health | HLT | health-conscious | – | – | – |
| 13 | "Kam me shume se 4 vote we e kam vendosur ne shtepi dhe jam shume i kenaqur." | GM-BFAL | 2021-04-29 | 5 | a system that lasts | PEACE | an experienced owner | – | – | – |
| 14 | "Jemi me fat qe kemi zgjedhur Bluefilters." | GM-BFAL | 2021-07-04 | 5 | to have chosen right | STA, PEACE | a smart chooser | choosing wrong | – | – |
| 15 | "Super Blue Filters ne Shqipëri, cilesia e ujit shume e mire, stafi dhe shërbimi ne kohe dhe sipas standardeve Europiane nga Ledio dhe Berti, cunat mete mire te Blue Filters, Flm guys you are the best 💙💙👍👍" | GM-BFT | 2026-03-26 | 5 | on-time service and good water | STA, PEACE | someone who expects European standards | late or sloppy service | – | – |
| 16 | "Ja vlenn!!" | GM-BFT | 2026-01-20 | 5 | worth the money | MON | a satisfied investor | wasting money | – | – |
| 17 | "Jane kompani shume korrekte, shume te sjwllshwm e te edukuar." | GM-ALBUJI | 2026-04-22 | 5 | respectful people in the home | respect, trust | – | rude or unreliable installers | – | home visit |
| 18 | "Sherbim te shkelqyer,paisje filtrimi me kualitet te larte." | GM-ALBUJI | 2026-04-20 | 5 | quality equipment | SAF | – | – | – | – |
| 19 | "Shume i kenaqur me filtrat. Sherbimi i klientit shume mire." | GM-ALBUJI | 2026-04-21 | 5 | customer service | PEACE | – | – | – | – |
| 20 | "Game e gjere produktesh, sherbim i shpejte, staf profesional. Shume e kenaqur me filtrin e ujit te pijshem." | GM-ALBUJI | 2023-08-15 | 5 | fast service and drinking water | TIM | – | – | – | – |
| 21 | "Jemi shume te kenaqur me sherbimin!!Jua sugjeroj te gjitheve te behen kliente te Albujit,zgjedhja me e mire qe mund te beni.." | GM-ALBUJI | 2022-10-24 | 5 | to make the best choice | STA, BEL | an advocate who recommends to others | – | – | – |
| 22 | "Kualiteti dhe cilesia me e mirë ne tregun Shqiptar. 👌🏻" | GM-ALBUJI | 2022-10-24 | 5 | the best in Albania | STA | – | – | – | – |
| 23 | "Cilesi dhe korektese per tu admiruar! Jam shume i kenaqur." | GM-BFAL | 2021-04-19 | 5 | correctness (keeping one's word) | trust | – | – | – | – |
| 24 | "Produkte fantastike! Faleminderit stafit per shpjegimin ne detaje dhe per sherbimin." | GM-BFT | 2021-06-29 | 5 | to understand what they buy | control, SAF | an informed buyer | being sold blind | – | the explanation and demo stage |
| 25 | "I kenaqur dhe shum korrekt me nderrimin e filtrit" | GM-ALBA | 2023-09-27 | 5 | cartridge change done right | PEACE, TIM | – | being forgotten after the sale | – | cartridge change |
| 26 | "Faliminderit albafilters per montimin e fiktrit te ujit" | GM-ALBA | 2024-09-29 | 5 | a clean installation | TIM | – | – | – | installation |
| 27 | "Sistemi me i mire dhe me cilesor. Sherbim si asnje kompani tjeter 👏" | GM-BFT | 2021-06-16 | 5 | service above the rest | PEACE | – | – | other companies (implied) | – |
| 28 | "Shërbim ,asistencë e përsosur,thjesht ,korekt" | GM-BFT | 2021-06-16 | 5 | assistance | PEACE | – | – | – | – |
| 29 | "Filtri me i mire" | GM-ALBA | 2025-11-07 | 5 | the best filter | STA | – | – | – | – |
| 30 | "Nuk diskutohet qe jane me te mir. Jam super i kenaqur." | GM-BFAL | 2021-04-17 | 5 | certainty of choice | STA | – | – | – | – |
| 31 | "Me te mirettt" | GM-BFT | 2026-01-29 | 5 | the best | STA | – | – | – | – |

Supporting, not counted. Green Life's own English 5-star reviews, all from 2025-01-07 or 2026-03-16, contain useful wording: "crystal-clear, pure, and much healthier than before!!!", "I have been using it for the last 7 years", "I definitely recommend them to every family." The burst of 7 reviews on one day (2025-01-07) looks like a solicited batch.

### 1c. Facebook comments (competitor page)

| # | quote | source | date | stars | want | desire | identity | fear | failed solution | trigger |
|---|---|---|---|---|---|---|---|---|---|---|
| 32 | "Sa kushtojn keta filtrat" | FB-BF https://www.facebook.com/bluefiltersalbania/posts/pfbid0282SjfHXidymnqcKiFa8C45wyqmDEGy9oBgKXf7t1TYXWZwYT9naUArU7rbMeTYddl?comment_id=1086687543732050 | 2026-09-14 | – | the price | MON | a price-first shopper | an unknown or hidden price | – | seeing a post or ad |
| 33 | "Pershendetje,ky sistem hydrion,cfare permasash ka,vendoset pishte lavapjates dhe sa kushton?" | FB-BF https://www.facebook.com/bluefiltersalbania/posts/pfbid02i1gpig8qYtFgj5pcWByAH2NRX1QRjZMiemg36wpqoNWMpsftgCGhJjbWNNMVHKrSl?comment_id=1642693844186750 | 2026-10-09 | – | fit under the sink, and the price | MON, practicality | a practical home planner | it won't fit; the price | – | kitchen planning |

### 1d. Albanian residents in news and civic reports (tap water, bidona, depozita, filters)

| # | quote | source | date | stars | want | desire | identity | fear | failed solution | trigger |
|---|---|---|---|---|---|---|---|---|---|---|
| 34 | "Nuk jam e sigurt për cilësinë. Në pallatin përballë uji vjen me erë të keqe. Kush e di çfarë ngatërrese ujërash ka ndodhur. Ne kemi blerë një filtër që kushton 100 mijë lekë në vit vetëm për të pirë ujë dhe për të larë frutat," (resident, "21 Dhjetori") | ACQJ | 2025-09-04 | – | to be sure about the water | SAF, PEACE | a cautious family that acted | invisible cross-contamination ("ngatërrese ujërash") | tap water; now a filter at 100k lek/year (cost noted) | the neighbour building's water smelled |
| 35 | "Vjen deri në katër të mbasdites, pastaj ndalet. Kthehet prapë nga ora 7:30 deri në dhjetë të darkës. Unë nuk kam depozitë, ndaj më shkon mbasditja kot pa bërë punë. Në darkë që duhet të pushoj, laj enët dhe rrobat," (resident, Rruga e Kavajës) | ACQJ | 2025-09-04 | – | water when needed | TIM | a working woman whose evenings are taken | – | no depozita; living by the schedule | daily water schedule |
| 36 | "Për fëmijët duhet të blej ujë të ambalazhuar, pasi uji i rubinetit është i turbullt dhe ka erë të fortë klori" (father, Unit 2) | REP | 2025-10-11 | – | safe water for the kids | FAM, HLT | the protective father | turbid water and chlorine reaching the children | bottled water | having children |
| 37 | "Dmth fatura e UKT shkon 2300-2700, plus uji që blejmë për të pirë, 2400 lekë në muaj kam llogaritur. Rreth 5000 lekë" (same father) | REP | 2025-10-11 | – | to stop paying twice | MON | a household budget-keeper | money draining every month | bottled water at 2,400 lek/month | doing the monthly maths |
| 38 | "Kam katër fëmijë, më i vogli është 3 vjeç, për të mbijetuar dhe jo jetuar kam sajuar depozitën brenda në shtëpi edhe pse bën zhurmë, s’kam çfarë bëj" (father of four, Unit 10) | REP | 2025-10-11 | – | to live, not just survive | FAM, dignity | the provider who improvises for his kids | his family left without water | a noisy pumped depozita inside the home | young children at home |
| 39 | "Depozitat janë shpëtimi ynë, nuk mund t’i heqin. Prej premtimeve vetëm fjalë kemi marrë" (resident, Astir) | REP | 2025-10-11 | – | a reliable own reserve | SAF, control | self-reliant, has stopped trusting promises | losing her own solution | promises from the authorities | the plan to remove rooftop tanks |
| 40 | "Na kanë thënë prej dekadash se do të ketë ujë 24 orë, por kjo nuk ndodh kurrë," (resident, Astir) | REP | 2025-10-11 | – | 24-hour water | PEACE | disillusioned | endless broken promises | waiting for the state | – |
| 41 | "Po ngjitesha në shkallë, kur hasa me një deputet të PS. Më pyeti për problemet e zonës, përveç rrugës më jetësore është uji i thashë. Qeshi e më tha do e sjellim sepse do hyjmë Evropë. Ç’ Evropë e zezë thua, në nevojtore të shkojmë s’kemi ujë" (father, Unit 10) | REP | 2025-10-11 | – | basic dignity now | dignity, STA | wants to live like Europe, mocked by promises | humiliation | political promises | an election campaign |
| 42 | "Kemi marrë edhe numrin e gjelbër të UKT-së, por nuk përgjigjen. Kur përgjigjen thonë që zona 1 ka ujë, ndërkohë që ujë nuk ka," (69-year-old resident, centre) | REP | 2025-10-11 | – | someone who answers | respect, SAF | an elderly carer for a sick husband | being ignored and lied to | the UKT hotline | water cut for days |
| 43 | "Furnizohemi me ujë nga ora 6:00 deri në 8:00 të mëngjesit; në orën 13:00 vjen vetëm për një orë, dhe ka raste pasdite nuk kemi fare," (same resident) | REP | 2025-10-11 | – | continuous water | TIM | – | – | living by the schedule | – |
| 44 | "Nuk dimë si ta përballojmë. Unë jam pensionist, me pensionin po blejë edhe ujë tani" (pensioner, Selitë) | LAPSI | 2025-07-05 | – | affordable water | MON | a pensioner on a fixed income | water eating into the pension | bought water | a 4-day outage in a heatwave |
| 45 | "Me bidonë, kemi bërë ankesa pa fund por kemi 4 ditë pa ujë." (resident, Selitë) | LAPSI | 2025-07-05 | – | water at home | TIM | – | – | bidona; complaints | an outage |
| 46 | "Kemi katër ditë që telefonojmë, por na thonë të njëjtën gjë: do ta raportojmë. Nuk merret asnjë masë konkrete" (resident, Selitë) | LAPSI | 2025-07-05 | – | action | respect | – | no one takes responsibility | phoning UKT | an outage |
| 47 | "As gjysmë ore nuk na vjen. Një herë në mëngjes, një herë në darkë. Në 6:30 të mëngjesit vjen dhe në darkë, vetëm gjysmë ore. Mbushim nga një pus që kemi afër, me korentin tonë. Lekët i paguajmë, fatura na vjen. Problem e kemi" (resident, Kombinat) | KLAN | 2025-09-29 | – | water for the money paid | MON, fairness | – | paying for nothing | a well with their own electricity | summer |
| 48 | "Nga dy orë. S’kemi 6 orë gjithsej. As pus, asgjë nuk kemi. Blejmë në treg për të pirë, kemi ato të famshmet depozita" (resident, Tirana) | KLAN | 2025-09-29 | – | drinking water | MON, TIM | – | – | buying drinking water at the market; depozita | – |
| 49 | "Problem është se çahen tubat. I kanë vënë të kalbëta" (resident, Kombinat) | KLAN | 2025-09-29 | – | clean pipes | SAF | – | rotten pipes contaminating water | – | pipe bursts |
| 50 | "S’na thonë gjë fare. Vetëm vijnë kur shikojnë sahatet, aty nuk neglizhojnë" (resident, Kombinat) | KLAN | 2025-09-29 | – | to be informed | respect | – | being milked for money and ignored | – | meter reading |
| 51 | "Faturat i paguajmë rregullisht, por ujë nuk kemi," (resident, Kodra e Diellit) | BOLD1 | 2025-10-22 | – | fairness | MON | a law-abiding payer | paying for nothing | – | a 3-month shortage |
| 52 | "Na thonë do vijë uji për 30 minuta, por është gënjeshtër," (resident, Kodra e Diellit) | BOLD1 | 2025-10-22 | – | the truth | trust | – | being lied to | UKT promises | – |
| 53 | "Autoboti vjen, por për 300 e ca familje nuk mjafton as për 10 minuta," (resident, Kodra e Diellit) | BOLD1 | 2025-10-22 | – | enough water | SAF | – | – | the water truck (autobot) | – |
| 54 | "Pa ujë nuk ka jetë," (woman resident, Kodra e Diellit) | BOLD1 | 2025-10-22 | – | water = life | FAM, HLT | – | – | washing with cans of sun-warmed water | – |
| 55 | "Jane marr çdo dite ne telefon dhe shprehja e tyre eshte, lutjuni zotit se do te vije uji." (resident, Shkozë, written complaint) | BOLD2 | 2025-06-09 | – | a real answer | respect | – | helplessness | phoning UKT | a 2-week outage |
| 56 | "Po jetojmë në kushte të papërshtatshme për higjienë, familjet kanë fëmijë të vegjël, të moshuar, të sëmurë – dhe askush nuk mban përgjegjësi." (same complaint) | BOLD2 | 2025-06-09 | – | hygiene for the family | FAM, HLT | a protector of vulnerable relatives | illness; no one responsible | – | heat over 40°C |
| 57 | "Kemi me shume se 10 dite pa uje ne shtepi . Eshte 40 grad dhe ne kemi 10 dite pa u lare dhe pa kryer nevojat tona normalisht ." (resident, Shkozë, written complaint) | BOLD2 | 2025-06-09 | – | to wash, normal life | dignity | – | – | waiting | heatwave |
| 58 | "Kemi dy vjet që jetojmë këtu, rezistencën e bolierit e kam ndërruar dy herë se bën shtresë gëlqere dhe nuk ngroh, lavatricen e e bleva të re, po tani e kam gati për ta hedhur se është mbushur me dhera nga uji" (resident, Yzberisht) | CIT | 2019-08-27 | – | appliances that last | MON | a homeowner protecting investments | limescale and dirt destroying the boiler and washing machine | replacing parts again and again | the boiler broke twice; new washing machine ruined |
| 59 | "Nuk kemi pasur asnjë njoftim dhe asnjë përgjigje për pyetjet tona. Ne blejmë bidona me ujë dhe po ashtu i mbushim ata me ujë për ti përdorur për tualetin. Duhet të bëj dush, të laj fëmijën dhe rrobat vetëm gjatë kohës që ka ujë. Është e vështirë kur do të gatuash, të lash dhe të pastrosh si dhe të kujdesesh për veten dhe dy fëmijë." (mother of two, Blloku) | CIT | 2019-08-27 | – | an easy household routine | TIM, FAM | a mother carrying the load | – | bidona for drinking and the toilet | summer schedule |
| 60 | "Ishte ora 16:30 kur u ktheva nga puna dhe mbeta në dush pasi iku uji. Që atë ditë, për afro një javë shkoj nga të afërmit e mi. Nuk ka lajmëruar askush për kufizimet në ujë" (resident, Ali Dem) | CIT | 2019-08-27 | – | a shower at home | dignity, TIM | – | being caught out mid-shower | going to relatives | the water cut mid-shower |
| 61 | "Më pyesin kur do vijë uji, pse s’ka ujë, nuk jetojmë dot më këtu, nuk po lahemi dot në këtë vapë." (building administrator relaying residents, Astir) | CIT | 2019-08-27 | – | to be able to wash | dignity | – | – | the water truck (bot) into the depozita | heat |
| 62 | "Nuk pihet, nuk mund të gatuhet me të, nuk mund të lahen rrobat me të, nuk mund të lahen dhëmbët me të…" (Prof. Përparim Kabo, Tirana resident, after testing his tap water at home) | CLASS | 2016-08-27 | – | water you can use for everything | HLT, SAF | an informed citizen who tested it | heavy metals and microbes ("vret") | tap water | an at-home water test |
| 63 | "Përpara se të flasim për një vend me orientim europian, të bejmë një vend normal që pi ujë që nuk vret!" (same) | CLASS | 2016-08-27 | – | normality | HLT, STA | a European-minded citizen | water that kills | – | – |
| 64 | "Ata kanë ujë të pijshëm, në tiranë uji nuk është i pijshëm. Në Korçë nuk ble njeri ujë. unë e ble ujin." (TV host R. Rakipllari to the mayor, on air) | EURO | 2023-04-06 | – | drinkable tap water | MON, STA | a Tirana resident who buys his water | – | buying water | – |

Also outside Tirana, coded but **not counted**, as context on chlorine and smell: CNA-M (3 Feb 2026, Maliq): "E kemi pasur gjithmonë të mirë ujin, por prej rreth dy javësh ka aromë shumë të keqe dhe nuk pihet. Ujin e blejmë edhe për të gatuar. Edhe rrobat kur i lajmë, mbeten me aromë të keqe."

Not buyers, so **not counted**:

- A Tirana councillor and doctor in REP: "Qytetarët paguajnë dy herë: një herë faturën e UKT-së dhe një herë bidonët me ujë të blerë në market, duke u kthyer viktimë e mashtrimit institucional".
- Shteg.org (10 Apr 2026), in the narrator's own framing: "Banorët e Tiranës paguajnë dy fatura."
- Green Life's own blog (7 Jan 2026), which is brand-written: "Nuk ishte çështje luksi, por sigurie."

---

## 2. Summary

### 2.1 Top 5 themes, ranked by frequency × intensity

Frequency is the number of quotes out of 64. Intensity is scored 1 to 3 from the emotional charge of the wording.

| Rank | Theme | Freq | Intensity | Score | Typical words |
|---|---|---|---|---|---|
| 1 | **"I can't trust what comes out of the tap", especially for my children.** Turbid water, chlorine smell, rotten pipes, invisible cross-contamination; tap water is used only for washing, never for drinking. | 12 | 3 | 36 | "i turbullt", "erë të fortë klori", "Kush e di çfarë ngatërrese ujërash", "Nuk jam e sigurt për cilësinë", "Për fëmijët", "ujë që nuk vret" |
| 2 | **Someone who keeps their word: service, guarantee, aftercare.** This is the core of every 5-star review ("korrekt", "në kohë", "garanci 10 vjeçare"); its absence drives the 1-star reviews ("3 orare", "justifikime"). | 22 | 1.5 | 33 (high frequency, mostly mild wording; 1-star rows are intense) | "korrekt", "sherbim", "garanci, jetegjatesi", "nderrimin e filtrit", "3 orare na kane len" |
| 3 | **Paying twice and carrying bidona.** The UKT bill plus 2,400 lek a month of bottled water, bidona hauled from the market, a pension spent on water. | 13 | 2.5 | 32 | "Kemi shpetuar nga bidonat", "Rreth 5000 lekë", "Lekët i paguajmë, fatura na vjen", "me pensionin po blejë edhe ujë" |
| 4 | **Abandonment and broken promises: no one answers, no one is responsible.** Directed at UKT, but it carries straight over into fear of filter companies. | 10 | 3 | 30 | "nuk përgjigjen", "është gënjeshtër", "lutjuni zotit", "askush nuk mban përgjegjësi", "Prej premtimeve vetëm fjalë" |
| 5 | **Proof and standards: certified, European, tested.** Wanting proof that the filter really works. | 7 | 2.5 | 18 | "pacertifikuara", "sipas standardeve Europiane", "analizen e ISHP", "si ai i pa filtruari", "Flitet per shendet, jo per para" |

Smaller themes:

- Limescale damaging the boiler and washing machine (1 strong quote, plus a brand claim). This supports the case for whole-house WH500/WH750 systems but is under-voiced.
- Dignity during summer cuts (washing, showers). This is about quantity, not quality, so it is out of scope for filters. It still sets the emotional backdrop and makes depozita water a second quality worry (CIT: residents do not use depozita water even for dishes).

### 2.2 The single dominant desire

**Certainty that the water my family drinks and cooks with is safe, without depending on anyone.** This is safety and peace of mind for the family, and it is reached through self-reliance.

Buyers do not ask for "pure water" in the abstract. They ask to stop doubting:

- "Nuk jam e sigurt për cilësinë"
- "Per te qene me te sigurt"
- "Për fëmijët duhet të blej…"

They also ask to stop relying on UKT, the market and bidona:

- "Kemi shpetuar nga bidonat"
- "Depozitat janë shpëtimi ynë"

Money (paying twice) is the rational justification that sits on top of this desire. It is not the desire itself.

### 2.3 Identity frame

**"The responsible head of the household who stopped waiting for the state and solved it for his home."** This is a prudent, informed parent (or employer) who:

- puts health over money: "Flitet per shendet, jo per para"
- refuses to be fooled: "Ç' Evropë e zezë thua", "kapari i pakthyeshëm"
- expects European standards: "sipas standardeve Europiane", "një vend normal që pi ujë që nuk vret"
- is proud of the choice afterwards: "Jemi me fat qe kemi zgjedhur", "Vlerë e shtuar në shtëpine tonë", "super i kenaqur qe te jem klient i juaji"

Second voice: the mother or carer who carries the daily load ("të laj fëmijën", "të kujdesesh për veten dhe dy fëmijë").

### 2.4 Top 5 fears

1. **Invisible contamination reaching the children:** bacteria and sewage, chlorine, turbidity, "ngatërrese ujërash". "Për fëmijët… i turbullt dhe ka erë të fortë klori."
2. **Being abandoned and lied to by whoever is supposed to deliver.** UKT never answers. For filters this becomes the technician who does not show up: "3 orare na kane len… vetem nxjerrin justifikime".
3. **Paying twice or overpaying:** the bill plus bidona at about 5,000 lek a month; a premium system that costs 4x ("500€, jo 2000€", "1200e ????"); pressure sales with a non-refundable deposit ("kapari eshte i pakthyeshem").
4. **The filter doesn't really work:** "Uje i pa perdorshem… si ai i pa filtruari" (ISHP lab test on filtered water); uncertified systems.
5. **Water destroying the home's appliances:** limescale and dirt in the boiler and washing machine ("rezistencën e bolierit e kam ndërruar dy herë").

### 2.5 Failed solutions and why they failed

| Solution tried | Why it failed (buyers' words) |
|---|---|
| Bidona / bottled water from the market | It costs money every month ("2400 lekë në muaj", "me pensionin po blejë edhe ujë"), it is physical work, and it means "paying twice" |
| Depozita on the roof or in the home (with a pump) | It is noisy ("edhe pse bën zhurmë"), it stores dirty water with limescale that residents won't use even for dishes (CIT), and it is under threat of a government removal plan |
| Wells (pus) with their own electricity | Unknown quality and extra electricity cost ("me korentin tonë") |
| Water trucks (autobot) | Never enough ("nuk mjafton as për 10 minuta") |
| Calling UKT or the hotline | "nuk përgjigjen", "do ta raportojmë", "lutjuni zotit", "është gënjeshtër" |
| A cheap, uncertified or unverified filter | The lab test showed it did nothing; the company was not transparent |
| A premium filter from a company with weak aftercare | No-show technicians and excuses; the price felt like 4x |
| Replacing appliance parts | The boiler element was changed twice and the new washing machine was ruined; the cause (the water) was never treated |

### 2.6 Trigger moments (when they start looking)

- **A visible water event:** muddy or red water (Komuna e Parisit, Apr 2025), chlorine-smell waves (Jan 2026 complaints), the neighbour's building smelling ("Në pallatin përballë uji vjen me erë të keqe").
- **Children:** a new baby or small kids ("Për fëmijët…", "më i vogli është 3 vjeç").
- **Summer and heat-wave outages** (June to September), when bidona use spikes and people do the monthly maths ("Rreth 5000 lekë").
- **An appliance breaks from limescale** (boiler element, washing machine).
- **Moving into a new apartment** ("Kemi dy vjet që jetojmë këtu").
- **Seeing a post or ad and asking the price** ("Sa kushtojn keta filtrat", "sa kushton?").
- **For existing owners:** cartridge-change time and repair needs, when loyalty is won or lost.

### 2.7 Ten phrases worth using in Albanian ads (the buyers' own words)

The original spelling is in quotes. The ad-ready form fixes only the diacritics and keeps the wording.

1. "Kemi shpetuar nga bidonat" → **Kemi shpëtuar nga bidonat.** (GM-ALBA, 2023)
2. "Flitet per shendet, jo per para" → **Flitet për shëndet, jo për para.** (GM-BFAL, 2021)
3. "Nuk jam e sigurt për cilësinë" → **Nuk jam e sigurt për cilësinë**, used as the problem hook. (ACQJ, 2025)
4. "Për fëmijët duhet të blej ujë të ambalazhuar" → **Për fëmijët… duhet të blej ujë.** (REP, 2025)
5. "Per te qene me te sigurt per cilesine… e ujit te pijshem" → **Për të qenë më të sigurt.** (GM-ALBUJI, 2023)
6. "Vlerë e shtuar në shtëpine tonë" → **Vlerë e shtuar në shtëpinë tonë.** (GM-BFAL, 2021)
7. "Lekët i paguajmë, fatura na vjen" or "Faturat i paguajmë rregullisht, por ujë nuk kemi" → the **pay-twice** hook. (KLAN / BOLD1, 2025)
8. "garanci 10 vjeçare" / "garanci, jetegjatesi" → **Garanci. Jetëgjatësi.** (GM-ALBA 2024, GM-GL 2025)
9. "Ja vlenn!!" → **Ja vlen.** (GM-BFT, 2026)
10. "Pa ujë nuk ka jetë" → **Pa ujë nuk ka jetë.** (BOLD1, 2025)

Also strong:

- "Kush e di çfarë ngatërrese ujërash ka ndodhur" (fear hook)
- "Prej shum vitesh klient i knaqur" (loyalty proof)
- "Mos e lodhni veten me sisteme te tjera te pacertifikuara"
- "për të mbijetuar dhe jo jetuar" (for ads about the old way)

### 2.8 Implications for the pitch (from the evidence only)

- The winning promise is **certainty plus someone who shows up.** Five-star words are about service and correctness, not technology. One-star words are about no-shows, price shock and filters that don't work. Green Life's own 5-star reviews already lean on "garanci, jetegjatesi" and "prej shum vitesh". Long-term owners (7 and 10 years) are its unfair advantage.
- **Proof beats claims.** The single most damaging review in the category is a lab test after filtering. A before/after test at the customer's tap answers the fear "si ai i pa filtruari".
- **Price is asked publicly and shocks privately** ("Sa kushtojn", "1200e ????", "500€, jo 2000€"). Framing against "Rreth 5000 lekë" a month of bidona plus the UKT bill uses the buyers' own maths.
- **Gap:** almost no buyer voice exists yet on shower filters or whole-house systems (limescale, skin and hair). The only strong quote is about the boiler and washing machine. Those products need their own voice research (for example DM or call notes from Green Life's own customers).

---

# Voice of the buyer: home water filters (broad market, English)

Under-sink filters/RO, whole-house filters and softeners, shower filters, installed by a technician at home.
Research date: 2026-10-20. 62 verbatim quotes from 40+ sources (Reddit, Amazon, Home Depot, ConsumerAffairs, Trustpilot, ProductReview, Quora, forums, plus news reports that quote buyers by name).

**Rules used**
- Every quote is copied exactly from the source, with the original spelling and typos. `…` marks text left out. Nothing is paraphrased inside quote marks.
- Dates are when the post, review or article was published. "undated" means the page showed no date (accessed 2026-10-20). Rows from a Reddit mirror (reddit.sentinel-team.org) give the snapshot date.
- How Reddit was reached: direct access was blocked, so threads were pulled with Apify `trudax/reddit-scraper-lite` in 3 runs (about $1.2 total, under the $1.5 cap).
- YouTube comments are not included. No tool available in this session could read comments within budget, so none were collected rather than invented.

**Coding key:** want = surface want · desire = deeper desire · identity = who they are or want to be seen as · fear · failed = failed solution tried and why · trigger = trigger moment · ad words = exact words worth reusing. "—" means the quote does not show it.

---

## 1. Quotes

| # | quote | source | date | want | desire | identity | fear | failed solution | trigger | ad words |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | "I'm currently 34 weeks pregnant and we just bought a house that likely has a lead water main (undisclosed and we didn't know before buying the house unfortunately)… And just the idea of lead in the water is freaking me out. I've only been drinking and cooking with bottled water since moving in but that won't work once our baby is here (I can't wash her bottles or mix formula in water that has lead). I'm panicking a little about this (or maybe panicking a lot)." | reddit.com/r/WaterTreatment/comments/1x3ife4 | 2026-10-11 | under-sink lead filter, fast | safety, family | expectant mother, new homeowner | lead harming the baby; no time to wait for test | bottled water (won't work once baby comes) | pregnancy + buying a house | "I can't wash her bottles or mix formula in water that has lead" |
| 2 | "I'm an exhausted dad of 2 under 2 and am tired of replacing AquaTru's tiny counter top tank multiple times a day… I primarily use this water for the babies formula, sippy cups, and to fill their baby bottle washer tanks and water warmer… I am not very knowledgeable in this area and to top it off am incredibly sleep deprived." | reddit.com/r/WaterTreatment/comments/1scwqi4 | 2026-04-05 | under-sink replacement | time, family safety | exhausted dad | getting it wrong for the babies | countertop RO: tiny tank, constant refills | babies, daily formula routine | "exhausted dad", "tired of replacing… multiple times a day" |
| 3 | "We just had a newborn, so I'm extra concerned about possible bacteria, biofilm, or contaminants growing inside the filters or lines while it was sitting in the heat… Would you avoid using this water for baby formula until it's addressed?" | reddit.com/r/WaterTreatment/comments/1qfk3so | 2026-01-17 | confirmation the RO is safe | safety, certainty | new parent | the filter itself breeds bacteria | own RO, unsure it's still safe after a move | newborn + moving house | "extra concerned… baby formula" |
| 4 | "I took a shower this morning and literally smelled like bleach afterwards. It's getting ridiculous… I need something that absolutely kills the chlorine smell, stops the hard water from destroying my appliances, and makes the water actually safe for my kids to drink." | reddit.com/r/WaterTreatment/comments/1sfvcj4 | 2026-04-08 | RO or whole-house | safety, family, protect home | mom/homeowner | kids' safety; appliances destroyed | descaling espresso machine 3x a month | bleach smell after a shower | "makes the water actually safe for my kids to drink" |
| 5 | "But I really don't want to pay a plumber another grand just to install the damn thing… I also looked at SpringWell for a whole-house setup but honestly half their reviews look like sponsored bot spam so I don't even know anymore… Are the replacement filters gonna bankrupt me every six months… I'm so tired of buying heavy packs of bottled water at Costco." | same thread (u/LipNat) | 2026-04-08 | clear choice, fair price | money, time | homeowner on a budget | install cost; filter cost; fake reviews | bottled water packs (heavy) | same | "so tired of buying heavy packs of bottled water" |
| 6 | "3 to 5k is insane! Yeah there is absolutely no way my husband would let us drop that much just on water… Maybe I should just stick to filtering the kitchen sink for now and let the appliances die… Tap water still tastes like a pool though" | same thread (u/LipNat) | 2026-04-08 | cheaper option | money | wife who needs spouse buy-in | overspending "just on water" | — | seeing a $3-5k quote | "Tap water still tastes like a pool" |
| 7 | "They claim to be "project managers" to get your guard down. They are in fact just salesmen. And they WILL lie to you and over promise but under deliver… he went through this whole unnecessary demo and PowerPoint and I'm like dude just give me the quote and go. He wasted 2 hours of my time… for $12,385..... Literally wtf." | reddit.com/r/WaterTreatment/comments/1u6vl93 | 2026-06-15 | honest quote, no show | not being a sucker, time | savvy homeowner | lies, overpricing, proprietary filters | dealer in-home pitch (Costco/EcoWater partner) | in-home consultation | "just give me the quote" |
| 8 | "I can't believe I signed the contract, and THEN did research on the subject lol. I started spiraling over the price" | same thread (u/Morbins) | 2026-06-16 | way out of the contract | money, self-respect | regretful buyer | stuck in a financed contract | dealer contract | buyer's remorse after signing | "signed the contract, and THEN did research" |
| 9 | "When I was talking to the salesman about being past the 3 day cancellation period, he made it seem like I was out of luck. Said it was pretty "iron clad". He would've said anything to keep a sale. So scummy. It feels illegal what he was trying to do." | same thread (u/Morbins) | 2026-06-16 | cancel | fairness | — | being trapped by a salesman | dealer | trying to cancel | "He would've said anything to keep a sale" |
| 10 | "I am a new homeowner and basically I entered a raffle at an Albuquerque festival and was "qualified" the Ecowater Systems water filtration program… he quoted me 9,460 but then gave a 1,000 discount… Total the monthly cost to finance this would be $119. Is this worth it or is it a scam?" | reddit.com/r/WaterTreatment/comments/1o0i394 | 2025-10-07 | price check | money | new homeowner | scam | — | raffle lead, then in-home visit | "Is this worth it or is it a scam?" |
| 11 | "My husband and I just bought our dream house… the water is very smelly… We spent about 12k on a new system… the technician mentioned in a house like ours, we should spend the extra money and do a whole home RO… But I just can't decide if it's worth it or if I'll regret not doing it in the future…help!" | reddit.com/r/WaterTreatment/comments/1n73bpu | 2025-09-03 | decide on an $8k upsell | home pride, no regret | owner of a "dream house" | regret either way | — | buying a house with sulfur/iron well water | "I'll regret not doing it" |
| 12 | "I had Culligan for years. Make sure to read that warranty with a microscope… I just got rid of my entire Culligan system because they wouldn't honor their lifetime warranty… Culligan is an expert at separating you from your money." | same thread (u/AdditionalReturn6201) | 2025-09-03 | warranty honored | fairness, money | burned ex-customer | warranty loopholes; forced paid maintenance | dealer brand system | warranty claim refused | "read that warranty with a microscope" |
| 13 | "I regret getting an Aquasana osmosis whole house water system but I have already sunk $3k into it and don't want to pay more to have it removed. I don't want to give the company another dime." | reddit.com/r/WaterTreatment/comments/1r3ange | 2026-02-13 | cheaper replacement filters | money, control | regretful owner | lock-in to one company's filters | branded whole-house system | ongoing filter cost | "I don't want to give the company another dime" |
| 14 | "Over the last few years I tried to get someone to come maintenance the unit, but had no luck, the original company that installed it went under… This sounds like an extremely high quote for media replacement, and they didn't explain why I should replace the unit." | reddit.com/r/WaterTreatment/comments/1wwfl8y | 2026-10-03 | affordable service | security, money | homeowner | installer disappears; service overcharge | installed softener with no one to service it | maintenance due, $2,500/$4,000 quote | "they didn't explain why" |
| 15 | "Generally speaking these whole home water filtration people are known to be a borderline scam. Especially if you recently bought a home they all magically show up at the same time. Just get multiple quotes." | Reddit (u/TheHeretic) via reddit.sentinel-team.org/posts/1tyg5jm | posted ~2026-01 (snapshot 2026-06-12) | fair quote | not being exploited | new homeowner | scam | — | buying a home | "they all magically show up at the same time" |
| 16 | "It's not crazy. I paid around 4.9k for the same setup… Whole house water softening / filtering has been excellent for us. Our skin is much better after showers, and we don't buy filters in our fridge." | same thread (u/davidgotmilk) | posted ~2026-01 (snapshot 2026-06-12) | whole-house | comfort, simplicity | satisfied owner | — | fridge filters | — | "Our skin is much better after showers" |
| 17 | "I repeatedly took permission from work and stayed home for confirmed service appointments, only for technicians not to turn up… I am so Happy with my setup, any issues I know what to do, without waiting for appointments." | Reddit (India) via reddit.sentinel-team.org/posts/1viyvfi | snapshot 2026-08-14 | reliable service | time, control | working professional | no-show technicians | rental purifier service, then bottled jars (expensive, sun-exposed plastic) | repeated missed appointments | "without waiting for appointments" |
| 18 | "we went from bottled delivery to a countertop filter a few months back mainly because the 20L bottle cycle got exhausting with 2 kids in the house… in hindsight we probably overpaid on bottled water for way longer than we needed to before switching" | Reddit (r/dubai) via reddit.sentinel-team.org/posts/1urt8c0 | snapshot 2026-07-10 | stop bottled delivery | time, money | parent of 2 | wasted money | 20L bottled delivery | exhaustion with kids | "the 20L bottle cycle got exhausting" |
| 19 | "I never trusted the water and always thought it tasted bad so I've drank bottled my whole life, but I'm sick of the idea that the microplastics are doing the same or worse to my body… It just feels like an uphill battle to have clean water that won't cause health problems… We have a multi-filtered shower head but it stops working extremely fast like within weeks when it's supposed to last 3 months." | reddit.com/r/WaterTreatment/comments/1wpg8ff | 2026-09-24 | RO that handles PFAS | health | health-anxious | cancer cluster; microplastics | bottled water (microplastics); shower filter died in weeks | local pollution, declining health | "an uphill battle to have clean water" |
| 20 | "A lot of the information out there seems dominated by shills, affiliate marketers, sponsored reviews, and disguised advertising… Between the potential microplastics, the cost, the constant trips to buy and haul it home, the space it takes up, and the environmental impact, it's becoming hard to justify long-term… I'm concerned about ingesting mold spores, biofilm, or anything else that could grow inside a filtration system." | reddit.com/r/WaterTreatment/comments/1wdj9rc | 2026-09-11 | bottled-quality water at home | health, trust | chemically sensitive renter | shills; biofilm in the filter | Big Berkey (still had issues); bottled water | — | "the constant trips to buy and haul it home"; "not marketing copy" |
| 21 | "there is no way to sanitize the lines, fittings, etc and there's no way to even know what the hell is going on with the system… i cant realistically feel comfortable using this for like 5+ years without a proper sanitization" | reddit.com/r/WaterTreatment/comments/1qfk3so (u/ShelfofPregnantHens) | 2026-02-04 | a way to verify and clean | certainty | owner | invisible contamination inside the unit | tankless RO with no visibility | — | "no way to even know what… is going on with the system" |
| 22 | "I have the same unit and water tested positive for bacteria immediately after install." | same thread (u/TaxReasonable9025) | 2026-02-01 | safe system | safety | — | the filter made the water worse | tankless RO | a bacteria test | "tested positive for bacteria" |
| 23 | "I probably went overboard after getting spooked by the Tap Score results… Just have kids in the home and want to make sure the water quality is great." | reddit.com/r/WaterTreatment/comments/1n38md8 (u/revo_87) | 2025-08-30 | the right setup | family safety | parent, novice researcher | getting it wrong; overspending | basic whole-house carbon not enough | lab water test | "want to make sure the water quality is great" |
| 24 | "I'm trying to avoid spending several thousand dollars on something that doesn't provide much real-world benefit, but I also don't want to regret skipping it if it's one of those "I wish I had done it while the walls were open" decisions." | reddit.com/r/sgv/comments/1vcejg4 | 2026-08-01 | yes/no on whole-house | no regret, protect home | remodeling homeowner | wasted money vs. regret | — | full home remodel | "I wish I had done it while the walls were open" |
| 25 | "I lived in Arcadia for over 10 years and the water was incredibly hard. My clothes would fade from it over time… If you can afford it, I would get the whole house filter and softener… It would be pretty nice to just pull water from the tap" | same thread (u/Retell) | 2026-08-01 | whole-house | convenience | homeowner | slow damage to belongings | pitchers/fridge "ad-hoc" filters | noticing the difference after moving | "just pull water from the tap" |
| 26 | "Whole house softener + reverse osmosis drinking water is a non negotiable for me." | same thread (u/Larry-Zoolander) | 2026-08-04 | softener + RO | standard of living | convinced owner | — | — | — | "non negotiable" |
| 27 | "After a shower, my skin feels hydrated and not dry. It's hard to describe." | same thread (u/Murdoc1984) | 2026-08-01 | softener | comfort | homeowner | — | — | — | "my skin feels hydrated and not dry" |
| 28 | "I honestly can't deal with the skin dryness and how my hair has been feeling lately since moving to a new apartment… I'm not sure if they actually make a noticeable difference or worth it." | reddit.com/r/WaterTreatment/comments/1tw1ihv | 2026-06-03 | shower filter | looks, comfort | renter | buying something that does nothing | — | moving to a new apartment | "can't deal with the skin dryness" |
| 29 | "My landlord saw my shower filter during a maintenance check and told me I had to take it down because it could cause "backpressure issues" in the building pipes." | same thread (u/Chris834702015455049) | 2026-06-04 | keep the filter | control | renter | landlord rules | — | landlord inspection | — |
| 30 | "my skin was actually becoming off putting to look at… I was truly skeptical that a $20 shower filter could be so effective, but to this day, I swear that's what saved my skin and hair." | reddit.com/r/washingtondc/comments/1ntjmro | 2025-09-29 | shower filter | appearance, confidence | 25-year-old guy | — | retinoid didn't fix it | moving to DC | "saved my skin and hair" |
| 31 | "I could not believe how soft and healthy my hair and skin felt when I went back to Maine on break. The difference was shocking." | same thread (u/pecanorchard) | 2025-09-29 | — | comfort | student | — | — | visiting home with soft water | "The difference was shocking" |
| 32 | "When I moved here my hair got thinner and started falling out. I lived with it for too long. Now my skin is softer and my hair is shinier and my shower water feels like a spa… Your quality of life will improve and your hair will be happier." | reddit.com/r/DCBitches/comments/1w0spwp | 2026-08-28 | shower filter | appearance, self-care | woman, "beauty tip" sharer | hair loss | — | moving | "my shower water feels like a spa"; "I lived with it for too long" |
| 33 | "My bleached hair goes brassy ONLY when I live in this city, and it's from mineral deposits even with a filter … sigh." | same thread (u/SnowboardSquirrel) | 2026-08-28 | protect colored hair | appearance | colored-hair owner | — | shower filter doesn't stop minerals | — | — |
| 34 | "I recently saw a reel of someone online talking about whether tap water is actually safe to use for baby formula, which of course probably freaked so many parents out… Most parents don't really want a huge Brita filter in their fridge because we barely have space as it is, let's be real." | reddit.com/r/FeedingCurious/comments/1ud4vgi | 2026-06-23 | formula-safe water | family safety, convenience | formula-feeding parent | contaminants in formula | Brita (takes fridge space) | social media reel | "is tap water actually safe… for baby formula" |
| 35 | "With all that said, I didn't feel like doing all that research and testing so I just opted for bottle water" | same thread (u/Ejohns10) | 2026-06-23 | easy answer | time, low effort | parent | — | — (chose bottled to skip the research) | new baby | "didn't feel like doing all that research" |
| 36 | "we did test it and also installed uv filter to kill bacterias just in case (I know its probably overkill, but better safe than sorry)." | same thread (u/WonderfulTwist4936) | 2026-06-23 | UV for well | safety | cautious parent | bacteria | — | baby | "better safe than sorry" |
| 37 | "I got a wife and a 18 month old at home. I just feel like it's the responsible thing to do… Yeah, I just pulled the trigger and ordered the filters + housings. No need to drink excess arsenic. And it's not like it's a $5000 setup." | r/WaterTreatment, quoted in thecooldown.com/green-home/arsenic-private-well-homeowner-orders-filters/ | 2026-10-15 | arsenic filter | family safety, responsibility | husband/father | arsenic | — | well test: 8 ppb arsenic | "it's the responsible thing to do" |
| 38 | "This is what my whole house filter looks like 2 minutes after installing [the] new filter. Is this normal?" | r/WaterTreatment, quoted in thecooldown.com/green-home/midwest-homeowner-whole-house-filter-brown/ | 2026-10-16 | reassurance | certainty | homeowner | what's in the city water | — | seeing the brown cartridge | "2 minutes after installing" (proof visual) |
| 39 | "He was telling us that we were just trying to kill our kids because the water is so bad and that we are bad parents for not getting a system in the home." | Brianna Gower, clarksvillenow.com (military families / softener liens) | 2023-10-24 | — | dignity | young parents of a NICU baby | being shamed as parents | — | "free gift" mailer, then a water test | anti-pattern: never shame parents |
| 40 | "The guy came and started showing us all these tests and everything and said, 'This could give your daughter cancer'… We had to pay them $7,300. It was a wild and unexpected amount" | Catherine Peterson, same article | 2023-10-24 | — | money, family | military family, new homeowner | hidden lien | dealer system on monthly payments | move-in phone call | anti-pattern: hidden total cost |
| 41 | "We had just bought our house… A letter came in the mail… It was like a welcome-to-the-neighborhood gift. We didn't know it was a water company." / "I knew something was wrong because the interest rate was through the roof" | Vanessa and Paolo Gilles, floridaphoenix.com | 2022-12-08 | — | trust | new homeowners | deception; financing | dealer system | new-homeowner mailer | anti-pattern |
| 42 | "I wanted to be healthy and have healthy water to drink… If I had something on paper that said this is unsafe, I probably would've paid the money" | Dean Skultety, cbsnews.com/sacramento (Call Kurtis) | 2016-11-07 | water purifier | health | new dad | unsafe water | — | new baby, then a "free" test kit | "healthy water to drink" |
| 43 | "I was thinking, am I doing this right? I should be contacting my children to see, but like I say, he didn't give me the opportunity to do that… I said, holy mackerel, this is a lot of money. I mean, I'm on a fixed income" | Bob Dobson, 77, thehalifaxtimes.com | 2024-07-25 | time to think | security | senior on a fixed income | pressure; can't consult family | $7,879 dealer contract | unsolicited phone call, free test | "am I doing this right?" |
| 44 | "Once they have your money they don't want to talk to you again. They don't want anything to do with you… We felt we had been betrayed." | Stephen O'Reilly, cbc.ca/news/canada/ottawa | 2014-02-13 | removal/refund | fairness | new resident | abandonment after the sale | $4,000 under-sink system | moving + scratch-ticket "free test" | "once they have your money" |
| 45 | "We were lied to in order for someone to take advantage and basically take our money." | Dan Farrell, same article | 2014-02-13 | service | trust | family new to well water | lied to; no service | $8,000 RO + sediment; no one came when it broke | first time on well water | — |
| 46 | "I feel like he's using people's fears to install a very expensive system." | Rachel Brummert, wsoctv.com (hidden camera) | 2017-11-08 | — | honesty | consumer advocate | fear-selling | — | free-test mailbox flyer | "using people's fears" |
| 47 | "The plumber was barely in the door and upon realizing I was not home began a campaign of fear with the dangers of chlorine to the unborn, how he bought one for his pregnant wife, etc… Just hearing this made my ears hot since I knew he was purposefully trying to manipulate my wife" | angrywoodchucksblog.com | 2012-02-19 | — | protect family from manipulation | husband/protector | manipulation through the spouse | — | plumber service call | — |
| 48 | "Talk to a lot of water people, and never believe the guys who come to your house to "test your water". They're full of crap and tricks… if you have to change it every 6 months, that's a pretty expensive venture and one more thing to remember." | quora.com (smarter investment: whole house vs point of use) | undated | — | money, low hassle | skeptic | in-home testers; upkeep | — | — | "one more thing to remember" |
| 49 | "Point-of-use are actually PITA to use and you will find yourself avoiding the use." | same Quora page | undated | whole-house | convenience | — | — | point-of-use filters | — | — |
| 50 | "However, after a couple months with the new system, I have regretted ever making the purchase. Our mineral deposit problems have never been worse… after spending some $2600 I feel I'm stuck." | consumeraffairs.com (Pentair/Pelican) | 2022-01-16 | working softener | money | homeowner (Arizona) | stuck with a system that doesn't work | salt-free system (didn't stop scale) | old softener died | "I feel I'm stuck" |
| 51 | "More than that, the so called experts misguided me to buy a wrong product… A hard & costly lesson learnt with Pelican water filters" | consumeraffairs.com (Pentair/Pelican) | 2022-01-27 | right product | trust | homeowner | wrong advice | $3K whole-house system didn't fix calcification | — | — |
| 52 | "Spent BIG dollars (4.6k)… the leak ruined my cabinetry under the sink (brand new build too)… Sounds like they are all about support and nice and helpful when purchasing the system but once they have your money they do not want to know you !!!" | productreview.com.au/listings/great-water | ~2021 ("5y" before 2026) | after-sales service | security | new-build owner | water damage; no accountability | installed whole-house + kitchen filter | — | — |
| 53 | "Today, 11/14/24 I came home to this filter kit leaking… Nonetheless, this thing is trash. Do not buy." | homedepot.com GE whole-house filter reviews | 2024-11-15 | — | protect home | homeowner | leak/flood | DIY whole-house housing | came home to a leak | — |
| 54 | "Is costs money for a plumber to install this...and as soon as the problems show their ugly face - you need a plumber to come BACK to take it out and put ANOTHER IN." | same page | 2019-07-13 | — | money | — | paying twice | GE housing leaks | — | — |
| 55 | "I purchased this product from HomeDepot in June of 2020 (my house has lead pipe)… I've had enough, I've spent $1,300 on this project so far with nothing to show for it" | homedepot.com Express Water reviews p2 | 2020-10-23 | lead protection | family safety | owner of a home with lead pipes | money wasted | 3-stage whole-house unit kept leaking | lead pipe | — |
| 56 | "3 weeks after installing it, there was a dramatic drop in water pressure… 2 stars for intentionally creating a system that requires you to use their filters only." | amazon.com/gp/customer-reviews/R1LSX68J6J4FBY | 2024-01-31 | standard filters | money, control | family of 4 | proprietary lock-in; pressure loss | whole-house cartridges clogged in 3 weeks | — | — |
| 57 | "Myself, I wasn't overly concerned about using that water, but with all the talk about all the chemicals and crap that's in our water, my wife decided so would no longer even drink that water and turned to drink bottled spring water, which has nano plastics in it and produces all that plastic waste from all those bottles… knowing that my wife could easily maintain the system herself if she ever needs to." | amazon.com iSpring RO500AK review | 2024-05-06 | tankless RO | family harmony, health | husband solving it for his wife | chemicals, nano plastics | whole-house + fridge filter, wife still drank bottled | wife stopped drinking tap | "all the talk about all the chemicals" |
| 58 | "You know what they say "happy wife, happy life", she was so concerned about not having the filter available" | amazon.com iSpring RO500AK review | 2022-09-09 | working RO | harmony | husband | going back to unfiltered | distilling at home (sludge) | — | "happy wife, happy life" |
| 59 | "my wife loves it most because shes so sensitive with her sink and now being able to wash her face and hair with filtered water is life changing for her… To me it's worth every penny to get cleaner filtered water knowing what they put in our water these days." | amazon.com Frizzlife DW10 review (Jim) | 2024-01-25 | filters at every tap | health, care | husband | "what they put in our water" | — | — | "life changing"; "worth every penny" |
| 60 | "We live in Speedway, Indiana, and the city's water quality has been borderline in its annual testing over the last few years.So, we felt we needed to do something to protect ourselves and the fur babies." | amazon.com CuZn UC-200 review (Douglas M.) | 2024-06-05 | under-sink filter | protection | pet parent | borderline city water | still drink bottled water for themselves | annual water report | "protect ourselves and the fur babies" |
| 61 | "We recently had triplets and have been making baby formula by the pitcher, and wanted to be able to use filtered water… The difference in flavor is night and day. My wife is pickier about her water than I am, and will now freely use the kitchen tap for drinking water." | amazon.com Filtrete 3US-AS01 review | undated | under-sink filter | family, convenience | father of triplets | — | fridge filter too slow for pitchers | triplets / formula | "night and day"; "freely use the kitchen tap" |
| 62 | "I've tried a few different shower heads to make my hard water less harsh on my hair but really felt like they weren't doing anything they claimed (or what the reviews said)… I wish I would have found this a long time ago!" | amazon.com Canopy filtered shower head (KittyKat) | 2026-05-03 | shower filter that works | appearance | skeptical repeat buyer | another dud | cheap shower heads did nothing | hard water | "I wish I would have found this a long time ago" |

### Supplementary quotes (same coding, short form)

| # | quote | source | date | want | desire | identity | fear | failed solution | trigger | ad words |
|---|---|---|---|---|---|---|---|---|---|---|
| 63 | "I was skeptical of a filtered shower head. I was wondering if it was marketing hype, or maybe not?" | amazon.com Canopy (R H. and L. Finch) | 2026-02-09 | proof | — | skeptic | hype | — | — | "marketing hype, or maybe not?" |
| 64 | "So before I pulled a Demi Moore and started washing my hair with bottled water, I decided to bite the bullet and buy this water filter.LET ME JUST SAY THAT MY HAIR IS AMAZING TODAY." | amazon.com Natural Rapids shower filter (top review) | undated | shower filter | appearance | "bad hair day" person | — | masks, pricier shampoo | good hair out of town, bad at home | "MY HAIR IS AMAZING TODAY" |
| 65 | "I am not sure why I waited so long in purchasing a shower filter. I have lived in Florida 8yrs and the water here is so hard." | amazon.com AMORIX shower filter (top review) | undated | shower filter | appearance | Floridian | — | — | — | "why I waited so long" |
| 66 | "It's cheap, but a hassle to remember to take the empties, re-fill them, and lug them home." | early-retirement.org RO thread | 2019-04-28 | RO at one sink | time, health (blood pressure) | retiree | salty softened water | refilling gallon jugs at stores | — | "lug them home" |
| 67 | "But the empty bottles stacked up, steadily accumulating on bedside tables, countertops and the floor of our car… We tried a Brita pitcher in the past, but filling it up was a constant chore. It never seemed to hold enough water… It really gives us peace of mind, especially when we're cooking or filling sippy cups for our two babies here at home!" | laurienrose.com | 2019-05-06 | RO | peace of mind, family | parents of two babies | crypto advisory | bottled 24-packs; Brita; basic under-sink (no taste change) | local treatment failure | "peace of mind… filling sippy cups" |
| 68 | "I almost have to pinch myself each time I go to the grocery store when I realize I don't have to bring those accursed jugs anymore!" | beabree.com | 2007-06-27 | RO | time, relief | mom | — | 5-gallon refill jugs | hauling jugs in summer heat | "those accursed jugs" |
| 69 | "Another advantage has been the lack of empty plastic water bottles around the house. I can't tell you how quickly our recycling container would fill up with those things." | ourhomefromscratch.com | 2013-11-05 | RO | tidy home | DIY homeowner | — | fridge filter ("quickly got sick of") | — | "If you drink a lot of bottled water, then I'd jump to get one" |
| 70 | "My Wife only drinks bottlef water and i was done hauling in 5 gallon jugs." | irv2.com RO thread (RV Norm) | thread 2016-11-28 | RO | time | husband | — | 5-gallon jugs | — | "done hauling" |
| 71 | "After the arrival of my second boy (now six months old) that develops redness after bathing, I've determined to upgrade the water filtration system… Initially, I thought the salesman at Home Comfort Center wanted to upsell me on some "useless" large micron sediment filter… And boy I was wrong" | forums.redflagdeals.com | 2018-02-06 | whole-house | protect the child | father | baby's skin | — | new baby's skin redness | "redness after bathing" |
| 72 | "the wife threw the brita into the garbage after a week and refuses to drink tap water at all now… the water taste way, way better, and I end up drinking more of it." | forums.redflagdeals.com (Waterdrop K19) | 2026-02-23 | RO | health habit | husband | — | Brita | — | "I end up drinking more of it" |
| 73 | "So hard that the previous owner "gifted" us 6 bottles of lime/scale/rust remover… Was it worth it? We feel it was worth every penny… There is zero chlorine odor in shower, which makes it extra relaxing." | ourfunctionalfarmhouse.com | 2020-04-25 | whole-house + softener | comfort, protect home | new homeowner | — | scrubbing scale | moving; shower odor | "zero chlorine odor in shower" |
| 74 | "Moved into the new house in October and by March the toilets were barely running because the float valve was plugged up… the washing machine and dishwasher were very ashy and building scale." | plumbingforums.com (Aggie83) | thread 2024-08-04 | softener | protect home | new homeowner | appliance damage | vinegar soaking | moving into a house | — |
| 75 | "I was tired of the lime and calcium build up. My two month old dishwasher's heating element is white with build up… I felt it was important to protect my plumbing and washers." | automaticwasher.org | 2008-01-14 | softener | protect investment | appliance owner | new appliance ruined | — | scale on a new dishwasher | "protect my plumbing and washers" |
| 76 | "The plumber had literally been here the day before (Thursday) to install a sediment filter (I have really hard water). I discovered our water heater leaking later that day." | reddit.com/r/homeowners/comments/1po5ebh (u/Sonarav) | 2025-12-16 | — | protect home | homeowner | water heater failure | — | water heater leak | — |
| 77 | "With the water filtration hooked up, I'm showing 338PPM and straight tap water I'm getting a reading of 347PPM… How is this going to improve the quality of the water?" | thereviewindex.com (Frizzlife under-sink, Amazon reviews) | undated (page updated 2021-07-18) | proof | certainty | DIY tester | it doesn't work | carbon under-sink (TDS barely moved) | TDS meter reading | — |
| 78 | "If you need specific contaminant removal like nitrates—which they advertise—test it yourself and don't assume it's working just because your TDS reads low." | ca.trustpilot.com/review/aquatruwater.com | 2025 (page 2025-08-17) | proof | certainty | data-driven buyer | claims not met | countertop RO | own nitrate testing | — |
| 79 | "Good water, crap company." | ca.trustpilot.com/review/aquatruwater.com | 2026-03-07 | filters, service | — | — | filter price hikes; no support | — | — | — |
| 80 | "Unfortunately, one year in, it started giving us problems where the water would slow to a trickle when first turned on and it has only gotten worse" | Costco review quoted in chowhound.com | 2026-02-09 | — | — | — | the unit degrades | Brondell RO ($80 proprietary filters every 6 months) | — | — |
| 81 | "I've had 3+ negative reviews the past couple of months… complaining about effectively having to drink water from the tap… It's really making me feel depressed and defeated as a host that I can't do anything right." | community.withairbnb.com | 2019-10-08 | stop bad reviews | reputation | Airbnb host | bad reviews | gallon jug of filtered water in the room | guest reviews: "forced to drink water from the bathroom" | — |
| 82 | "Since we live by the lake, none of our neighbors drink the water. So that's the first strike against us. We use bottled water at our house and provide it at the rental." | airhostsforum.com | 2021-11-08 | drinkable water for guests | reputation | rental host | — | bottled water for guests | starting to host | "first strike against us" |
| 83 | "IW sucks. Our water stinks of Chlorine (worse after rain as it gets an extra dose of Chlorine because the river water is dirtier) tastes foul and is full of microscopic physical contaminates - yet its fit to drink." | boards.ie (Ireland) | 2025-02-11 | RO | — | — | distrust of the utility | Brita jug | rain makes it worse | "stinks of Chlorine" |
| 84 | "I'm not afraid to drink our tap water but nobody in my house does regularly." | diychatroom.com | 2023-12-27 | whole-house | family preference | dad | — | Brita in the fridge | — | — |
| 85 | "So I'm tired of buying bottles of water and contributing to so much waste I produce with the plastic. I can stand drinking faucet water but I know it's bad and it's time to get a real filter." | r/BuyItForLife (tH3_R3DX), quoted on thegigabrain.com | undated ("1 year ago") | real filter under $150 | health, eco | — | tap water "bad" | bottled water | — | "time to get a real filter" |
| 86 | "When my towns water was deemed cancerous, I'd fill up 5 gal jugs for less than $10." | reddit.com/r/BestofRedditorUpdates/comments/171wt1t (u/AhFFSImTooOldForThis) | 2023-10-07 | safe water cheap | safety, money | budget-conscious | cancer | jug refills | town water declared unsafe | — |

Totals: 62 main quotes plus 24 supplementary, so **86 verbatim quotes**. Quotes #39-47 come from news reports that name the buyer. They are the words of real buyers and would-be buyers, kept mainly as evidence of the dealer-scam fear.

---

## 2. Summary

### 2.1 Top 6 themes (ranked by frequency × intensity)

| Rank | Theme | Frequency (quote #s) | Intensity | Note |
|---|---|---|---|---|
| 1 | **"Am I being scammed?" Dealer distrust, pressure, financing, lock-in, abandonment** | 26: #5, 7-15, 17, 39-48, 50-52, 56, 79 | Very high: "So scummy. It feels illegal", "kill our kids", liens, "I feel I'm stuck" | The biggest reason people delay. Even happy buyers price-check on Reddit before signing. |
| 2 | **Protecting the baby/kids (formula, pregnancy, lead, "the responsible thing")** | 19: #1-4, 18, 23, 34-37, 39, 40, 42, 55, 61, 67, 71 (+#57-60 as protecting a spouse/pets) | Very high: "panicking a lot", "freaking me out", sleep-deprived | The strongest trigger, and it puts the buyer under time pressure. |
| 3 | **"Does it actually work, and will the filter itself become the problem?" (proof, biofilm, leaks, pressure, proprietary filters)** | 18: #3, 13, 19-22, 28, 33, 53-56, 62, 63, 77, 78, 80 | High: "no way to even know what… is going on", "came home to this filter kit leaking" | Doubt after buying, plus fear of water damage. |
| 4 | **Bottled-water fatigue (hauling, cost, plastic, microplastics, space)** | 16: #5, 17-20, 35, 57, 66-70, 72, 82, 85, 86 | Medium-high: "so tired", "accursed jugs", "exhausting" | The most common failed solution. Its pain is time and effort, and lately microplastics. |
| 5 | **Skin and hair (hard water/chlorine in the shower, "since I moved")** | 14: #16, 25, 27-33, 59, 62-65, 71 | Medium-high for looks: "off putting to look at", "hair… falling out" | An identity theme (looking good); bought fast and cheap as shower filters. |
| 6 | **Smell/taste of chlorine plus protecting the home and appliances** | 14: #4, 6, 11, 24, 25, 38, 73-76, 83, 84 (+#81 hosts) | Medium: "smelled like bleach", "tastes like a pool", "let the appliances die" | Sensory trigger plus a homeowner's ROI case. |

### 2.2 Dominant desire
**Certainty that the water I give my family is safe, without becoming a water expert and without being taken advantage of.**
The want on the surface is "clean water from the tap". Underneath it are three things:
- **Safety and peace of mind for the family:** "makes the water actually safe for my kids to drink", "the responsible thing to do", "peace of mind… sippy cups".
- **Relief from effort:** "just pull water from the tap", "done hauling", "without waiting for appointments".
- **Not feeling like a sucker:** "signed the contract, and THEN did research", "just give me the quote".

Buyers want to feel they protected their family *and* made a smart, fair decision.

### 2.3 Identity frames
1. **The protective parent (strongest)**: expecting moms, "exhausted dad of 2 under 2", parents of triplets, formula feeders, a "wife and 18 month old" father (#1-3, 23, 34-37, 61, 67, 71). Also its mirror, the **husband who solves it for his wife** ("happy wife, happy life", "my wife… refuses to drink tap water", #57-59, 72).
2. **The new homeowner / "dream house" owner**: just bought, often targeted by mailers and raffles, wants to do it right "while the walls are open" (#1, 10, 11, 15, 24, 40, 41, 73, 74).
3. **The savvy skeptic who refuses to be a sucker**: does research, distrusts shills and dealers, wants an itemized quote and standard parts (#5, 7-9, 13, 20, 48, 63, 77, 78).
4. **The health-conscious / chemically sensitive**: microplastics, PFAS, cancer clusters, "what they put in our water" (#19, 20, 57, 59, 85).
5. **The homeowner protecting appliances and the home**: espresso machine, water heater, dishwasher, clothes fading, scale (#4, 6, 24, 25, 73-76).
6. **The appearance-focused renter / young adult**: hair, skin, "my shower water feels like a spa", landlord limits (#28-33, 62-65).
7. **Hosts and landlords**: guest reviews, "first strike against us" (#81, 82). Small in volume but a clear business case.

### 2.4 Top 6 fears
1. **Being scammed, upsold or pressured**: inflated quotes ($8k-$12k), fake "free tests", 3-day contract traps, financing with hidden liens, and "they all magically show up" after you buy a house (#7-12, 15, 39-47).
2. **Harming my child**: lead in formula, arsenic, bacteria in a newborn's water (#1-3, 34, 37, 42).
3. **It doesn't really work / I can't verify it**: TDS barely moves, claims not met, "marketing hype, or maybe not?", shills everywhere (#20, 28, 62, 63, 77, 78).
4. **Ongoing cost and lock-in**: proprietary filters, "bankrupt me every six months", "don't want to give the company another dime" (#5, 13, 48, 56, 79, 80).
5. **The system becomes the hazard**: leaks and water damage, pressure loss, bacteria or biofilm inside the unit (#21, 22, 52-56, 80).
6. **Being abandoned after the sale**: the company goes under, technicians don't show, warranty loopholes, "once they have your money" (#12, 14, 17, 44, 52).

### 2.5 Top failed solutions (and why they failed)
- **Bottled water / jug refills / delivery**: heavy, constant hauling, cost adds up, plastic waste, and now microplastics anxiety (#5, 18-20, 57, 66-70, 85, 86).
- **Pitchers (Brita, ZeroWater)**: small, a constant chore, take fridge space, family still won't drink tap (#34, 67, 72, 83, 84).
- **Pushy dealer systems (Culligan, EcoWater, RainSoft-type)**: overpriced, warranty loopholes, proprietary parts, no service later (#7-13, 39-45, 50-52).
- **Cheap shower filters**: work at first or not at all, cartridges die in weeks, don't soften (#19, 33, 62).
- **Countertop RO / fridge filters**: tiny tanks, slow, refill all day (#2, 61, 69).
- **DIY cartridge whole-house housings**: leaks, pressure drops, clogged in weeks, plumber has to come back (#53-56).
- **Under-sink units with no visibility**: owners can't tell whether they still work or are growing bacteria (#21, 22, 77).

### 2.6 Trigger moments
1. **New baby or pregnancy** (#1-3, 34, 42, 61, 71).
2. **Buying or moving into a house** (the most common entry point for the scam-mailer path too) (#1, 10, 11, 15, 24, 40, 41, 73, 74).
3. **A sensory moment**: shower smelled like bleach, water "tastes like a pool", sulfur smell (#4, 6, 11, 73, 83).
4. **A test or report result**: Tap Score, well test, annual water report, TDS meter (#23, 37, 60, 77).
5. **Visible evidence**: brown cartridge, scale, dead espresso machine or water heater, faded clothes (#4, 25, 38, 74-76).
6. **Moving city and noticing skin or hair** (#28, 30-32, 64, 65).
7. **Social media or news**: a reel about formula water, "town's water deemed cancerous" (#34, 86).
8. **Renovation ("walls are open")** and **guest complaints for hosts** (#24, 81).

### 2.7 Ten phrases worth adapting into ads
| # | Exact buyer words (source quote) | Possible ad use |
|---|---|---|
| 1 | "makes the water actually safe for my kids to drink" (#4) | Headline for parents |
| 2 | "I'm so tired of buying heavy packs of bottled water" (#5) | Problem hook |
| 3 | "just pull water from the tap" (#25) | Outcome line |
| 4 | "it's the responsible thing to do" (#37) | Identity line for parents and partners |
| 5 | "just give me the quote" (#7) | Anti-dealer promise: a fixed quote up front, no demo |
| 6 | "Why didn't I do this sooner" (Home Depot Express Water review, see note) / "I wish I would have found this a long time ago" (#62) | Testimonial frame |
| 7 | "I wish I had done it while the walls were open" (#24) | Renovation and new-home angle |
| 8 | "my shower water feels like a spa" (#32) | Shower and whole-house benefit |
| 9 | "the constant trips to buy and haul it home" (#20) | Bottled-water pain |
| 10 | "without waiting for appointments" (#17) / "no way to even know what… is going on with the system" (#21) | Promise: on-time technicians and visible filter status |

Note on #6: "Why didn't I do this sooner is my only complaint." comes from an undated Home Depot review (homedepot.com/p/reviews/Express-Water-3-Stage-…/308246491/2). It is not numbered in the table above.

### 2.8 Implication for the pitch (from the evidence, not invented)
The category's biggest barrier is not belief in clean water. It is **distrust of the people who install it**. A technician-installed brand wins by being the opposite of the dealer stereotype:
- a fixed, itemized price with no living-room demo;
- no scare tests, and never shaming parents;
- standard, affordable filters and a clear filter schedule;
- technicians who arrive on time and come back;
- proof the system works (before/after testing) and a visible filter status.

Lead with the parent, homeowner and "done hauling" outcomes. Use the anti-scam promise to answer the reason people delay.
