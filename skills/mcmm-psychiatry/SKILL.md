---
name: mcmm-psychiatry
description: База знань з курсу MCMM "Психіатрія — наука про душу" (Master Class of Mental Medicine, mcmm.creo.ua) + coaching layer для Юрієвих клієнтських сесій. Використовуй ЗАВЖДИ коли Юрій питає про теми психіатрії з курсу MCMM, історію психіатрії, нозологію, ключові постаті (Пінель, Крепелін, Фройд, Кречмер, Блойлер тощо), парадигми психіатрії, нюанси DSM/МКБ за матеріалом курсу, або просить пройти/перевірити тест по уроках MCMM. ТАКОЖ використовуй проактивно — коли клієнт у сесії описує психіатричний симптом, при підозрі на психотичний регістр у клієнта, коли треба маршрутизувати клієнта до психіатра, при питаннях типу 'це не до мене?' / 'це психіатрія?' про клієнта. Тригери — "MCMM урок N", "психіатрія MCMM", "урок з психіатрії", "тест по психіатрії MCMM", "історія психіатрії", "як Пінель", "що в курсі MCMM про X", "переклади лекцію", "складімо тест", "розкажи з курсу психіатрії", "конспект MCMM", "це психіатрія?", "це не до мене?", "клієнт описує голоси/марення/манію", "red flag у клієнта".
---

# MCMM Psychiatry — Course Knowledge Base

База знань з курсу **"Психіатрія — наука про душу"** на платформі MCMM (Master Class of Mental Medicine, [mcmm.creo.ua](https://mcmm.creo.ua/)).

## Що це і навіщо

Цей скіл існує щоб **відповідати на питання з курсу психіатрії без галюцинацій** — лише матеріал лекцій, з посиланнями на slide/timestamp. Юрій вчиться на курсі і хоче ідеально володіти матеріалом (тести, дискусії, застосування у коучингу).

**Принцип**: не змішувати загальні відомості psychiatry (з training data) з матеріалом лекції. Якщо немає в `lessons/<lesson>/claims.md` — кажи "цього немає в матеріалах курсу" і пропонуй джерело.

## Структура

```
mcmm-psychiatry/
├── SKILL.md                       # цей файл (master entry)
├── learning_protocol.md           # метапромпт для вивчення нового уроку
├── course_overview.md             # структура всього курсу
└── lessons/
    └── l07-history/               # урок 7: історія психіатрії
        ├── README.md              # quick summary
        ├── transcript.md          # дослівний transcript відео (з timestamps)
        ├── slides.md              # презентація як markdown
        ├── text.md                # супровідний текст уроку
        ├── claims.md              # atomic claims (1 ідея + verbatim quote + source ref)
        ├── synthesis.md           # running understanding теми
        ├── quiz.md                # quiz курсу з відповідями + поясненнями
        ├── flashcards.md          # 50+ flashcards для recall
        └── raw/                   # оригінальні файли (mp4/pdf/srt/json)
```

## Як використовувати

### Юрій питає концептуальне ("що говорить Пінель про звільнення хворих?")

1. Read `course_overview.md` — знайди до якого уроку це належить
2. Read `lessons/<lesson>/synthesis.md` — running understanding
3. Read `lessons/<lesson>/claims.md` — atomic claims з цитатами
4. Відповідай **тільки** на основі claims з посиланнями (slide N / video MM:SS / text §N)
5. Якщо в claims немає — скажи прямо: "цього немає в матеріалах уроку X". Не вигадуй.

### Юрій просить "склади тест по уроку X" або "перевір мене"

1. Read `lessons/<lesson>/quiz.md` — офіційні питання курсу з відповідями
2. Read `lessons/<lesson>/flashcards.md` — додаткові питання для тренування
3. Запропонуй формат (single-choice / open-ended / mixed) і кількість (10/20/30/50)
4. Прийми відповіді → дай feedback з посиланням на claim

### Юрій просить "напиши конспект уроку X"

1. Read `lessons/<lesson>/synthesis.md` — це і є конспект high-level
2. Read `lessons/<lesson>/claims.md` — для деталей
3. Збери у короткий конспект на 1-2 сторінки (це не переказ — це структуровані claims зі студентським зв'язуванням)

### Юрій просить "вивчи новий урок X"

→ застосуй `learning_protocol.md` (6-крок пайплайн: recon → extract → atomize → synthesize → build → verify)

## Анти-патерни

- ❌ Видавати загальні знання з psychiatry training data за матеріал курсу
- ❌ Відповідати без посилання на slide/timestamp/section
- ❌ Підсумовувати "своїми словами" замість дослівних claims
- ❌ Якщо немає в claims — мовчки додумати з training data

## Course context

**MCMM** = Master Class of Mental Medicine. Курс психіатрії в межах потоку "MCMM і потік". URL формат: `https://mcmm.creo.ua/courses/mcmm-i-potik-<id>/psixiatriya-<id>/urok-N-<slug>-<id>`.

Деталі структури курсу — `course_overview.md` (наповнюється у міру вивчення уроків).

## Status: lessons indexed

**Модуль 10 «Психіатрія» — 14/14 уроків ✅ COMPLETE.** Status update 2026-05-13.

> ⚠️ URL slug `urok-N` НЕ збігається з lesson order у модулі (адмінський артефакт). Lessons 1-3 use `urok-7/8/9`, lessons 4-14 use `urok-4..urok-14`. Використовуй цю таблицю як authoritative.

| #   | Lesson                                                              | Status  | Verify                 | Folder                       |
| --- | ------------------------------------------------------------------- | ------- | ---------------------- | ---------------------------- |
| 1   | Психіатрія. Наука про душу. Історія психіатрії                      | ✅ DONE | 96.7%                  | `lessons/l07-history/`       |
| 2   | Психіатрія. Структура нервової системи                              | ✅ DONE | 98.3%                  | `lessons/l02-nervsys/`       |
| 3   | Психіатрія. Мозаїка психіки: емоції і воля                          | ✅ DONE | 96.7%                  | `lessons/l03-emo-will/`      |
| 4   | Мозаїка психіки: пам'ять, увага                                     | ✅ DONE | **100%** ⭐            | `lessons/l04-memory/`        |
| 5   | Мозаїка психіки: мислення                                           | ✅ DONE | **100%** ⭐            | `lessons/l05-thinking/`      |
| 6   | Мозаїка психіки: відчуття та сприйняття                             | ✅ DONE | **100%** ⭐            | `lessons/l06-percept/`       |
| 7   | Шизофренія                                                          | ✅ DONE | 98.3%                  | `lessons/l07-schizo/`        |
| 8   | Біполярний афективний розлад                                        | ✅ DONE | 98.3%                  | `lessons/l08-bipolar/`       |
| 9   | Депресія                                                            | ✅ DONE | **100%** ⭐            | `lessons/l09-depress/`       |
| 10  | Тривожні розлади                                                    | ✅ DONE | **100%** ⭐            | `lessons/l10-anxiety/`       |
| 11  | Посттравматичний стресовий розлад                                   | ✅ DONE | 96.7%                  | `lessons/l11-ptsd/`          |
| 12  | Істерія (конверсійні, дисоціативні розлади)                         | ✅ DONE | **100%** ⭐            | `lessons/l12-hyster/`        |
| 13  | Аномалії розвитку особистості                                       | ✅ DONE | **100%** ⭐            | `lessons/l13-persdev/`       |
| 14  | Основні принципи психофармакотерапії                                | ✅ DONE | **100%** ⭐            | `lessons/l14-pharma/`        |
| Q/A | Q/A сесія з лікарем-психіатром Бережним Германом (Академія Ісаєнко) | ✅ DONE | 100% (10/10 self-quiz) | `lessons/m10l5-qa-isaienko/` |

**Module 10 summary**: 14/14 теоретичних уроків + 1 Q/A live сесія = 15 ✅ · Avg accuracy **98.93%** · **8 PERFECT** scores (L4, L5, L6, L9, L10, L12, L13, L14) · Pass gate ≥95% хорошо в усіх 14.

**Q/A сесія (m10l5-qa-isaienko)** — лектор Бережний Герман (НЕ сам Ісаєнко), 2 год 44 хв, 14 тематичних блоків Q/A, 90 atomic claims з тегами [MED]/[AWARE]/[ROUTE]/[BOUND]/[NEURO]. Найважливіший урок для **boundary психіатр-коуч** і **протоколу маршрутизації**.

**Per-lesson артефакти** (всі lessons мають):

- `raw/` — video.mp4, audio.wav, transcript.srt, transcript.txt, slides.pdf (де є)
- `transcript.md` — whisper.cpp large-v3 з anti-hallucination flags (`--max-context 0 --suppress-nst`)
- `slides.md` — текст слайдів (де є презентація; L7/L8/L14 — без слайдів)
- `claims.md` — 70-160 atomic claims (definition / mechanism / clinical_form / cross_ref / тощо)
- `synthesis.md` — running understanding 9 секцій (Quick thesis + Anatomy + Key insights + Cross-cutting + Diagnostic logic + Cross-refs + Suspicious + Applied to coaching + Key facts + Mnemonics)
- `README.md` — quick summary + status table + top claims
- `quiz.md` — Q1 (recon або prediction) + 10-15 predicted training Q
- `flashcards.md` — 70-112 Bloom-distributed cards (Recall 40% / Understand 25% / Apply 20% / Analyze 15%)
- `verify.md` — 30 self-Q з self-grading проти claims.md (target ≥95% accuracy)

**Lecturer**: Світлана Володимирівна Ісаєнко (Dr. Isaenko, КМН, ХНМУ 2011, Сабурова дача 8.5 років, EPA, перший психіатр в Україні з відкритим Instagram з 2018, 5 книг, 372K followers @dr_isaenko, MCMM partnership). Деталі — у `course_overview.md` секція «Lecturer(s)».

**2026-05-15 add-on**: `symptom_atlas.md` (844 рядки, 282 симптоми A→Я + по уроках + 10 diagnostic patterns) для швидкого lookup під час coaching/екзамену. Source: synthesis.md з L3-L13.

**Для індексації наступних модулів**: використовуй `learning_protocol.md` — 6-крок пайплайн працює як шаблон (recon → extract → atomize → synthesize → build → verify). Anti-hallucination flags whisper.cpp обов'язкові (див. MEMORY rule #40).

## Status: Exam ✅ COMPLETE

**Module 10 fully closed 2026-05-15.** Final exam case-study (повний психічний статус пацієнтки з F20.0 параноїдної шизофренії з парафренним синдромом) написаний:

- Source: `exam/transcript_patient.md` (whisper Russian, 21:19, 419 lines)
- Methodichka: `exam/methodichka_ua.md` (13-секційний бланк психічного статусу)
- Atlas: `symptom_atlas.md` (282 симптоми L3-L13 для cross-ref)
- **Result:** `exam/psychiatric_status.md` (469 lines) + `exam/psychiatric_status.html` (rendered, 70 KB, self-contained CSS)

13 секцій + Синдромологічний висновок (8 синдромів) + DDX vs F22/F25/F31.5/F23/органіка → F20.0 з парафренним синдромом + Coaching note для Юрія.

## Coaching mode — використання у клієнтських сесіях Юрія

Цей скіл активується **проактивно** під час Юрієвих сесій (Detective FM, МАЙСТЕРНЯ, мастермайнди), коли:

- Клієнт описує переживання / симптом, що має психіатричний відтінок
- Юрій явно просить «це психіатрія чи я можу працювати?»
- У тексті/відео/чаті клієнта спливає red-flag (див. нижче)

### Ритуал реакції (3 кроки)

1. **Швидкий lookup** через `symptom_atlas.md` (а не через synthesis) — там 282 симптоми A→Я з прив'язкою до уроку та секції synthesis. Знаходимо відповідний урок MCMM.
2. **Сказати Юрію**: «Дивись MCMM L<N> synthesis §<секція> — там Світлана Володимирівна про <концепт>». Стиль — короткий suggestion, не лекція.
3. **Якщо red-flag (10 ознак — див. `exam/psychiatric_status.md` секція Coaching note)** — додатково: «🚩 це шизофренічний/маніакальний/суїцидальний регістр, mandatory routing до психіатра, не коучинг».

### Якщо клієнт каже…

Швидкий quick-ref (повна таблиця в `exam/psychiatric_status.md` Coaching note):

| Клієнт                                                 | Урок MCMM                                 | Дія                                                            |
| ------------------------------------------------------ | ----------------------------------------- | -------------------------------------------------------------- |
| «Голос у голові наказує»                               | L7 §2.6 + L6 §3                           | 🚩 imperative voice → психіатр невідкладно                     |
| «Думки читають / викрадають»                           | L7 §2.7 Кандинського-Клерамбо             | 🚩 шизофренічний регістр → психіатр                            |
| «У мене особлива місія» (з анозогнозією + фантастика)  | L7 §2.5 парафренна стадія                 | 🚩 → психіатр                                                  |
| «Мене переслідують» (без альтернативи в думках)        | L7 §2.5 параноїдальна форма               | 🚩 → психіатр                                                  |
| «Я не я / як з боку дивлюсь на себе»                   | L11 §2 (PTSD dissociative) ↔ L12 §2 (F44) | Розрізнити: травма vs psyhотика                                |
| «Не сплю 4+ днів, безмежна енергія, ризикую грошима»   | L8 §2 Манія                               | 🚩 → психіатр (ризик БАР)                                      |
| «Все чорно, нічого не хочу, ранкова інсомнія»          | L9 §2-3 Депресія                          | Скрінінг суїцидальності + психіатр якщо тяжке                  |
| «Панічні атаки, серце вилітає»                         | L10 §2.5 Panic disorder                   | Коучинг + травматерапія може; SSRI за психіатром               |
| «Ритуали, перевіряю газ 50 разів»                      | L10 §3 ОКР                                | Коучинг обмежений; CBT + SSRI за психіатром                    |
| «Перфекціонізм паралізує»                              | L13 §анкастний                            | Коучинг працює добре, в межах характеру                        |
| «Я як вампір емоційно, всіх використовую» (без сорому) | L13 §дисоціальний                         | Коучинг малоефективний (ego-syntonic), психотерапія/психіатрія |

### Cardinal rule (з L7 §2.9 кейсу малпрактики)

> **НЕ скасовувати медикаменти. НЕ замінювати психіатра. НЕ переконувати клієнта що достатньо тренувати mindset.**

Якщо у Юрія клієнт на медикаментах від психіатра — продовжуємо коучинг паралельно, з дозволу психіатра і при стабільному стані з збереженою критикою.

### Знаряддя в скілі для coaching

| Файл                                       | Призначення                                           |
| ------------------------------------------ | ----------------------------------------------------- |
| `symptom_atlas.md`                         | A→Я lookup симптомів з прив'язкою до synthesis секцій |
| `exam/psychiatric_status.md` Coaching note | 10 red flags + cardinal rule + skarga→urok таблиця    |
| `lessons/lXX/synthesis.md`                 | Глибше пояснення коли треба деталь                    |
| `lessons/lXX/claims.md`                    | Atomic твердження з verbatim цитатами лектора         |
