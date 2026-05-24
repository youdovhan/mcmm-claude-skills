---
name: mcmm-oratorske
description: База знань з ораторського мистецтва у курсі MCMM (Master Class of Mental Medicine, mcmm.creo.ua) — наскрізна дисципліна, 4 уроки розкидані по модулях 5/7/8/10 (capstone). Лектор — **Денис [Чернишов *unverified прізвище*]** (whisper hesitates Чернушов/Чернощов/Чернишов; primary-source L2688 self-name + L1491 Юрій addressing + L3373 Аліна; "КМС-рівень, не олімпійський чемпіон" анти-перфекціоністична педагогіка). Використовуй коли Юрій просить підготуватись до виступу, написати/оцінити мовлення, провести вправу з ораторського мистецтва, відповісти на питання з курсу. ТАКОЖ використовуй коли клієнт-коуч/експерт у Юрія приходить із запитом на публічність. Тригери — 'ораторське', 'риторика', 'виступ', 'голос лідера', 'спікер', 'голос', 'дикція', 'присутність', 'переконати аудиторію', 'як говорити', 'промова', 'магнетичний виступ', 'mcmm урок ораторського', 'дай вправу на голос', 'тренуй мене', 'покритикуй виступ', **'мистецтво слухати', '4 рівні слухання', 'закрите слухання', 'інформаційне слухання', 'емпатичне слухання', 'інтеграційне слухання', 'генеративне слухання', 'ННК Розенберг', 'ненасильнича комунікація', 'Денисова межа', '5-крок ННК', '11 помилок оратора', 'Compass 1-5', 'третій елемент', 'камерний тест', 'КМС-рівень оратор', 'Денис Чернишов', 'TEA-app маски любви', 'психологічний театр'**.
---

# MCMM Ораторське мистецтво — Course Knowledge Base

База знань з **наскрізної дисципліни «Ораторське мистецтво»** на платформі MCMM (Master Class of Mental Medicine, [mcmm.creo.ua](https://mcmm.creo.ua/)).

## Що це і навіщо

Цей скіл існує щоб **відповідати на питання + проводити вправи з ораторського мистецтва без галюцинацій** — лише матеріал лекцій, з посиланнями на slide/timestamp. Юрій вчиться на курсі і хоче ідеально володіти матеріалом (теорія + практика виступу) та використовувати у роботі з клієнтами-коучами/експертами що готуються до публічних виступів.

**Принцип**: не змішувати загальні відомості з ораторського мистецтва (з training data) з матеріалом лекції. Якщо немає в `lessons/<lesson>/claims.md` або в `lessons/<lesson>/exercises/` — кажи "цього немає в матеріалах курсу" і пропонуй джерело.

**Особливість дисципліни**: ораторське — НАСКРІЗНА (не окремий модуль), 3 уроки розкидані по модулях 5/7/8. Тому це **практико-орієнтований скіл з вправами** — кожна вправа має `exercises/ex-NN.md` з повною інструкцією що я можу провести з Юрієм у діалозі.

## Структура

```
mcmm-oratorske/
├── SKILL.md                       # цей файл (master entry)
├── learning_protocol.md           # метапромпт для вивчення нового уроку
├── course_overview.md             # структура наскрізної дисципліни
└── lessons/
    └── l05-osnovy/                # урок: основи ораторської майстерності
        ├── README.md              # quick summary
        ├── transcript.md          # дослівний transcript відео (з timestamps)
        ├── slides.md              # презентація як markdown
        ├── text.md                # супровідний текст уроку
        ├── claims.md              # atomic claims (1 ідея + verbatim quote + source ref)
        ├── synthesis.md           # running understanding теми
        ├── quiz.md                # quiz курсу з відповідями + поясненнями
        ├── flashcards.md          # 50+ flashcards для recall
        ├── exercises/             # практичні вправи з повною інструкцією
        │   ├── ex-01.md           # 1 вправа = 1 файл з instruction sequence
        │   └── ex-NN.md
        └── raw/                   # оригінальні файли (mp4/pdf/srt/json)
```

## Як використовувати

### 1. Юрій питає концептуальне ("чим відрізняється голос лідера від звичайної мови?")

1. Read `course_overview.md` — знайди до якого уроку це належить
2. Read `lessons/<lesson>/synthesis.md` — running understanding
3. Read `lessons/<lesson>/claims.md` — atomic claims з цитатами
4. Відповідай **тільки** на основі claims з посиланнями (slide N / video MM:SS / text §N)
5. Якщо в claims немає — скажи прямо: "цього немає в матеріалах уроку X". Не вигадуй.

### 2. Юрій просить "склади тест по уроку X" або "перевір мене"

1. Read `lessons/<lesson>/quiz.md` — офіційні питання курсу з відповідями
2. Read `lessons/<lesson>/flashcards.md` — додаткові питання для тренування (Bloom-розподіл: 40% recall / 25% understand / 20% apply / 15% analyze)
3. Запропонуй формат (single-choice / open-ended / mixed) і кількість (10/20/30/50)
4. Прийми відповіді → дай feedback з посиланням на claim

### 3. Юрій просить "напиши конспект уроку X"

1. Read `lessons/<lesson>/synthesis.md` — це і є конспект high-level
2. Read `lessons/<lesson>/claims.md` — для деталей
3. Збери у короткий конспект на 1-2 сторінки (це не переказ — це структуровані claims зі студентським зв'язуванням)

### 4. Юрій каже "давай вправу X" / "потренуй мене" / "проведи мене через вправу на голос"

1. Read `lessons/<lesson>/exercises/<ex-NN>.md` — повна інструкція вправи
2. **НЕ імпровізуй** — слідуй `## Інструкція` step-by-step
3. Веди Юрія через sequence: говори що сказано у `## Інструкція`, чекай відповідь (text або голос через Wispr / audio file)
4. Оцінюй відповідь Юрія за `## Що оцінювати` критеріями
5. Якщо Юрій робить типову помилку — звертай увагу на `## Поширені помилки`
6. Адаптуй формат за `## Adaptations` (text / голос / відеозапис)
7. У кінці — короткий feedback + посилання на verbatim quote лектора з timestamp

### 5. Юрій просить "вивчи новий урок X"

→ застосуй `learning_protocol.md` (6-крок пайплайн: recon → extract → atomize → synthesize → build → verify). У Step 2 додатково — Agent E (Exercises extraction).

## Анти-патерни

- ❌ Видавати загальні знання з public speaking training data за матеріал курсу
- ❌ Відповідати без посилання на slide/timestamp/section
- ❌ Підсумовувати "своїми словами" замість дослівних claims
- ❌ Якщо немає в claims — мовчки додумати з training data
- ❌ **Проводити вправу без instruction script — наосліп; завжди читати `ex-NN.md` спочатку**
- ❌ Імпровізувати критерії оцінки вправи замість читати `## Що оцінювати`
- ❌ Скорочувати інструкцію вправи "для зручності" — кожен крок sequence важливий

## Course context

**MCMM** = Master Class of Mental Medicine. Курс у межах потоку "MCMM I потік". Ораторське — **НАСКРІЗНА дисципліна** (не окремий модуль), 4 уроки (з M10L4 capstone) розкидані по модулях:

- М5 (27.11–01.12) — Основи ораторської майстерності
- М7 (19.02–23.02) — Голос лідера. Від конструктивної критики до магнетичних виступів
- М8 (18.03–22.03) — Сила присутності. Як будувати виступи, що спонукають до дії
- **М10 (15.05–18.05) — Мистецтво слухати: як глибоке розуміння змінює комунікацію (CAPSTONE)**

URL формат тих самих lessons — як у `mcmm-psychiatry/course_overview.md`. Деталі — `course_overview.md`.

## Lecturer attribution (per-lesson, CRITICAL)

⚠️ **Денис [Чернишов *unverified прізвище*]** — primary lecturer для всіх 4 уроків Ораторського мистецтва. Whisper транскрибував непослідовно (Чернушов / Чернощов / Чернишов). Primary-source verification:

- **L2688 M10L4:** Денис сам себе називає — "Не дивитися, що я, Денис Чернушов, умний"
- **L1491 M10L4:** Юрій звертається — "Денис Чернощов чуть-чуть попав в яму"
- **L3373 M10L4:** Аліна закриває — "Денис, дякую вас за цей прекрасний курс"
- **L15-16 M10L4:** Self-positioning "завершающий четвертый урок со мной" → continuity 4 уроків

**STATUS прізвища:** `[unverified]` — потребує external cross-check через IG/Threads/MCMM лектори-список. Memory: `/Users/detective/.claude/projects/-Users-detective-Claude/memory/reference_denys_chernyshov_oratorske_lecturer.md`.

**Continuity inference (НЕ primary-source per-lesson):** Денис явно каже "4-й завершальний урок со мной" → ймовірна continuity для l05/l07/l08 (попередні уроки Дениса). Потребує окремого recon для кожного.

## Status: lessons indexed

**Наскрізна дисципліна «Ораторське мистецтво» — 4/4 уроки ✅ INDEXED.** Status update 2026-05-24.

| #     | Lesson                                                                    | Module             | Lecturer                          | Status                     | Folder                               |
| ----- | ------------------------------------------------------------------------- | ------------------ | --------------------------------- | -------------------------- | ------------------------------------ |
| 1     | Основи ораторської майстерності                                           | М5 (27.11–01.12)   | Денис (inference)                 | ✅ INDEXED                 | `lessons/l05-osnovy/`                |
| 2     | Голос лідера. Від конструктивної критики до магнетичних виступів          | М7 (19.02–23.02)   | Денис (inference)                 | ✅ INDEXED                 | `lessons/l07-holos/`                 |
| 3     | Сила присутності. Як будувати виступи, що спонукають до дії               | М8 (18.03–22.03)   | Денис (inference)                 | ✅ INDEXED                 | `lessons/l08-syla/`                  |
| **4** | **Мистецтво слухати: як глибоке розуміння змінює комунікацію (CAPSTONE)** | **М10 (15-18.05)** | **Денис [Чернишов *unverified*]** | **✅ atomized 2026-05-24** | `lessons/m10l4-mystetstvo-slukhaty/` |

### M10L4 — CAPSTONE Ораторське (2026-05-24 atomized)

**M10L4 «Мистецтво слухати» = 4-й і фінальний урок дисципліни** (Денис: "завершающий четвертый урок со мной" L15-16). Це **трикомпонентний бутерброд:**

1. **Compass 1 — повторення-концентрат 11 типових помилок оратора** з попередніх 3 уроків (головна №1: фокус на собі замість на аудиторії)
2. **Compass 2 — CORE THEORY: 4 рівні слухання** (нова таксономія, унікальна для M10L4):
   - **Рівень 1: Закрите** — фізично присутній, психологічно НІ. Внутрішній діалог. "Бойцовский клуб" anchor
   - **Рівень 2: Інформаційне** — утилітарний контакт. Аргументи, конкретика. Псевдо-безпека
   - **Рівень 3: Емпатичне** — слухаю стан, дихання, паузи. Ризик "розплисти у вайб"
   - **Рівень 4: Інтеграційне/Генеративне** — народжується "третій елемент" (метафора чоловік+жінка → дитина). Коуч-сесія = Рівень 4
3. **Compass 3 — ННК Розенберга, Денисова 5-крок версія** (інновація — 5-й крок "межа"):
   - 1. Факт (камерний тест — "якщо можна зняти на камеру → це факт")
   - 2. Почуття
   - 3. Потреба
   - 4. Просьба
   - 5. **Межа (Денисова інновація)** — "що я зроблю сам, якщо просьба не виконана"; реальна дія, без угрози/маніпуляції
4. **Compass 4 — Контент з травми vs здорової психіки** (⚠️ HIDDEN-IN-WARM tier; Денис свідомо обмежує доступ — "не даю в відкритий доступ")
5. **Compass 5 — closing meta-rules + bounded knowledge framework**

**8 живих виступів учасниць** (Василь / Юлія / Аліна / Лера / Ірина / Кристина / Анна / Наталя / Анастасія) з deep debrief Дениса (50%+ часу уроку) — WARM/TRUSTED tier, НЕ для cold-public adaptation.

**CRITICAL для Conference 23-24.05.2026 — AI-демо Юрія Довгана (L3082-3263)**:

- Юрій за 2 години оцифрував 11 годин лекцій Дениса (361 ідея + 37 практик + 22 учасники + 12 програм)
- Денис live test → бот генерує згенерувати виступ "польза раннього підйому, школярі 9 клас + тон друга" → success
- Денисова реакція: "я в цьому динозавр" + "круто, що це становиться можливим"
- **Юрієва Big Idea для ринку (L3231-3242):** "контент має переходити на такий рівень і на щось нижче я не готовий розраховувати"
- Democratization frame (L3450-3459): "Натали зробила сайт для ретриту. Юлі страницю просто перфекту..."

**Disclaimer (Денис, C-41):** ННК НЕ працює з нарциссами/абюзерами/психопатами; ефективна у 80% робочих/побутових ситуацій, НЕ панацея.

> Детально — `lessons/m10l4-mystetstvo-slukhaty/synthesis.md` (22 розділи, 1047 рядків) + `claims.md` (92 atomic claims з audience tier tags). Exam rehearsal master file → `/Users/detective/Claude/MCMM_EXAM_REHEARSAL.md`.

**Inventory:** 361 atomic claims · 37 practical exercises · 5377 слів per-lesson synthesis · 4192 слова cross-synthesis (5 концептуальних осей L1↔L2↔L3) · 160 слайдів · 387KB HTML каталог (3-view SPA з copy-to-Claude). Verdict: `Knowledge/Verdicts/v-oratorske-mystetstvo.md`. Cross-synthesis: `Knowledge/Syntheses/syn-oratorske-mystetstvo.md`.

**Per-lesson артефакти** (після ingestion усі lessons матимуть):

- `raw/` — video.mp4, audio.wav, transcript.srt, transcript.txt, slides.pdf (де є)
- `transcript.md` — whisper.cpp large-v3 з anti-hallucination flags (`--max-context 0 --suppress-nst`)
- `slides.md` — текст слайдів (де є презентація)
- `claims.md` — atomic claims (definition / technique / framework / cross_ref / тощо)
- `synthesis.md` — running understanding (контекст / ключова теза / sub-thesis / applied to coaching)
- `exercises/ex-NN.md` — кожна вправа окремо з повним instruction script
- `README.md` — quick summary + status table + top claims
- `quiz.md` — Q1 + 10-15 predicted training Q
- `flashcards.md` — 50+ Bloom-distributed cards
- `verify.md` — 30 self-Q з self-grading проти claims.md (target ≥95% accuracy)

**Для індексації наступних уроків**: використовуй `learning_protocol.md` (6-крок пайплайн з Agent E для вправ). Anti-hallucination flags whisper.cpp обов'язкові (див. MEMORY rule #40).

## Coaching mode — використання у клієнтських сесіях Юрія

Цей скіл активується **проактивно** під час Юрієвих сесій (Detective FM, МАЙСТЕРНЯ, мастермайнди), коли:

- Клієнт-коуч / експерт каже про підготовку до виступу (лекція, презентація, voiceover, voice tweet)
- Клієнт має страх сцени / "застрягає в горлі" / "монотонність"
- Юрій явно просить «дай йому вправу на голос/присутність»

### Ритуал реакції (3 кроки)

1. Уточни запит: який саме виступ, аудиторія, формат (live/recorded), скільки часу до виступу
2. Підбери вправу: Read відповідну `lessons/<lesson>/exercises/ex-NN.md` що матчиться з запитом (warmup / voice / breath / structure / presence)
3. Скажи Юрію: «Дивись MCMM Ораторське L<N> exercises/ex-NN — там вправа на <тема>. Інструкція готова, можу провести з тобою або з клієнтом».

### Знаряддя в скілі для coaching

| Файл                             | Призначення                                                      |
| -------------------------------- | ---------------------------------------------------------------- |
| `lessons/lXX/exercises/ex-NN.md` | Повна інструкція вправи (instruction sequence + критерії оцінки) |
| `lessons/lXX/synthesis.md`       | Глибше пояснення коли треба деталь                               |
| `lessons/lXX/claims.md`          | Atomic твердження з verbatim цитатами лектора                    |
| `course_overview.md`             | Знайти урок за темою/модулем                                     |
| `exercises_catalog.html`         | Browser SPA з усіма 37 вправами (HOME/FOCUS/ALL views)           |

### Reference docs у Obsidian (для productization)

| Файл                                                                                                                                                                        | Коли відкривати                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `Knowledge/Syntheses/syn-oratorske-mystetstvo.md`                                                                                                                           | Cross-synthesis 4192 слова — 5 концептуальних осей наскрізної дисципліни L1↔L2↔L3                                      |
| [Knowledge/References/reference_detective_fm_oratorske_protocols.md](/Users/detective/ObsidianVault/Knowledge/References/reference_detective_fm_oratorske_protocols.md)     | Step-by-step протоколи 5 пакетів Detective FM (€39 / €300 / €1469 / €2969 / €5469) — відкрити перед клієнтською сесією |
| [Knowledge/References/reference_maysternya_presence_for_ai_experts.md](/Users/detective/ObsidianVault/Knowledge/References/reference_maysternya_presence_for_ai_experts.md) | Backbone content для модуля МАЙСТЕРНЯ «Presence для AI-експерта» — 3 уроки за 5 axes                                   |
| `Knowledge/Verdicts/v-oratorske-mystetstvo.md`                                                                                                                              | Verdict applied_to_skill з 3 zones practice                                                                            |
