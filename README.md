# MCMM Claude Skills

> **Master Class of Mental Medicine (I потік)** — атомізована база знань як набір Claude Code skills.
> 9 дисциплін · 479 файлів · 200K+ рядків verbatim quotes + atomic claims з 11 уроків транскриптів.

База підготовлена Юрієм Довганом ([@yurii_dovhan](https://instagram.com/yurii_dovhan)) для **personal study reference** і поділена з учасницями MCMM-мастермайнду. Призначення — підготовка до іспиту, швидкий пошук цитат лекторів, навігація by-discipline у власній практиці коучингу/психології.

---

## Кому це для

- Учасники MCMM I потоку (mcmm.creo.ua), які пройшли курс і хочуть лишити собі робочу базу знань
- Коучі / психологи / помагаючі практики / ментори, які працюють з AI як co-pilot і шукають per-discipline knowledge base
- Усі хто хоче побачити, як виглядає **атомізована база знань для AI-агента** на прикладі живого курсу (формат: SKILL.md + lessons + claims + synthesis + flashcards)

---

## Що тут є — 9 дисциплін

| Skill                    | Лектор(и)                                                                         | Уроки індексовано         |
| ------------------------ | --------------------------------------------------------------------------------- | ------------------------- |
| `mcmm-business-strategy` | Юлія Гончар (Course Advisors)                                                     | 3/3 (m7l5 / m8l5 / m9l5)  |
| `mcmm-coaching`          | Лана (Світлана Нагорна) + Олексій Махонін + Юлія Козачкова (менторські)           | 14 уроків                 |
| `mcmm-marketing`         | Олексій Махонін                                                                   | 3/4 (m5l5 / m6l5 / m8l6)  |
| `mcmm-nlp`               | Віталій Ходяков (Erickson Ukraine, PCC ICF)                                       | 4 уроки                   |
| `mcmm-oratorske`         | Денис [Чернишов *unverified прізвище*]                                            | 4 уроки + capstone        |
| `mcmm-philosophy`        | unverified (Зігмунд Фройд Університет UA + Київська школа економіки)              | 4 уроки                   |
| `mcmm-psychiatry`        | Герман Бережний (Академія Ісаєнка) + invited Q/A                                  | 14 уроків                 |
| `mcmm-rozbir`            | Юлія Козачкова + Олексій Махонін + Михайло Волков + Тетяна Чекальська (multi-lec) | 3/4 (m1l7 / m5l7 / m10l6) |
| `mcmm-ta`                | Влада Березянська (КН + EATA + USATAA)                                            | 11 уроків                 |

**Multi-lecturer sessions** (m1l7 розбір Махонін+Волков+Козачкова, m10l6 capstone Козачкова+Махонін) мають **per-turn attribution** у транскрипті — кожна репліка позначена за primary-source verification.

---

## Структура repo

```
mcmm-claude-skills/
├── README.md              ← ти тут
├── EXAM_REHEARSAL.md      ← 66 Q cross-skill rehearsal + 12 quick-reference tables
├── HOW_TO_USE.md          ← як підключити до Claude Code / Claude.ai / ChatGPT / Gemini
├── LICENSE                ← MIT
└── skills/
    ├── mcmm-business-strategy/
    │   ├── SKILL.md       ← metadata + тригери + опис коли активувати
    │   ├── lessons/
    │   │   └── m9l5-strategic-session/
    │   │       ├── README.md
    │   │       ├── transcript.txt    ← clean verbatim transcript
    │   │       ├── transcript.srt    ← з timecodes
    │   │       ├── synthesis.md      ← consolidated understanding
    │   │       ├── claims.md         ← atomic claims (1 ідея = 1 рядок)
    │   │       └── flashcards.md     ← spaced-repetition Q/A
    │   └── ...
    ├── mcmm-coaching/
    └── ... (ще 7 disciplines)
```

Кожна skill = standalone директорія з `SKILL.md` (metadata + опис коли активувати) + `lessons/` (по-lesson breakdown).

---

## Як використати — 3 шляхи

Детально → [`HOW_TO_USE.md`](./HOW_TO_USE.md). Коротко:

### 1) Claude Code (рекомендовано)

```bash
cd ~/.claude/skills
git clone https://github.com/youdovhan/mcmm-claude-skills.git mcmm
# restart Claude Code → skills auto-loaded на основі трігерних слів
```

Після цього у будь-якому проєкті — кажеш Claude "розкажи що Лана говорить про активне слухання" → Claude активує `mcmm-coaching` skill і дає відповідь на основі transcripts.

### 2) Claude.ai / Claude API

Копіювати content окремого `SKILL.md` як **system prompt**, плюс прикріпити relevant `lessons/<lesson>/synthesis.md` як attachment.

### 3) ChatGPT / Gemini

Як reference context — копіюй `synthesis.md` потрібного уроку, питай "що тут головна теза?", "як це застосувати в коучингу?".

---

## Приклади запитів

```
"Поясни 6 особистісних адаптацій Влади (mcmm-ta m10l2)"
"Як Лана говорить про активне слухання? (mcmm-coaching m3l2)"
"Які 11+ типів воронок у Махоніна? (mcmm-rozbir m7l6 — BLOCKED)"
"Що Бережний каже про РДУГ діагностику? (mcmm-psychiatry)"
"План vs стратегія за Юлією Гончар через Ділтса (mcmm-business-strategy m7l5)"
"7 компонентів спокусливого оферу Махоніна (mcmm-marketing m8l6)"
"Дай вправу на голос від Дениса (mcmm-oratorske)"
"Метамодель НЛП — приклади порушень (mcmm-nlp m1l5 Ходяков)"
"Категоричний імператив Канта простими словами (mcmm-philosophy m5l2)"
"Гормональний backbone burnout-у — що казала Чекальська? (mcmm-rozbir m5l7)"
```

---

## Content stats

- **9 disciplines** (від bizstrat до psychiatry)
- **479 files** у repo (after media-stripped)
- **200K+ markdown lines** verbatim quotes + atomic claims + syntheses + flashcards
- **11+ повних уроків** з full transcript + claims + synthesis
- **700+ atomic claims** (формат: 1 claim = 1 verbatim quote + контекст)
- **66 cross-skill questions** у [`EXAM_REHEARSAL.md`](./EXAM_REHEARSAL.md)

---

## Disclaimers

> ⚠️ **Personal study reference, not public MCMM distribution.**
> Це Юрієва особиста база для підготовки до іспиту та власної практики. Поширення обмежене учасницями його мастермайнду. Якщо ви потрапили на цей repo не як учасник MCMM I потоку — будь ласка, поважайте, що це не курс і не його заміна. Курс — https://mcmm.creo.ua/.

> ✓ **Verbatim primary-source verified per-lesson.**
> Кожна attribution лектора привʼязана до конкретного timestamp у transcript (наприклад M1L3 L2688 self-intro). Де primary-source не знайдено — позначено caveat `[unverified]` (наприклад прізвище Дениса "Чернишов" — whisper hesitates).

> ⚠️ **Lecturer attribution caveats:**
>
> - **Denys [Чернишов *unverified*]** — whisper transcribes як Чернушов / Чернощов / Чернишов; primary-source confirmed first name + role only
> - **Філософія лектор** — continuity verified (арістотеліанець-феноменолог), прізвище unverified
> - **Multi-lecturer sessions** (m1l7, m10l6) — per-turn attribution за speaker patterns + sub-discipline matching

> ⚠️ **TRUSTED-tier claims (Personal-insight-Yurii) включені.**
> Деякі claims містять Юрієві власні рефлексії з сесій (наприклад m10l2, m7l7) — це **TRUSTED-only** контент, не для cold marketing у вашу аудиторію. Це memos з менторських розмов, тримати у внутрішній практиці.

> ⚠️ **Деякі уроки BLOCKED (Workspace policy):**
>
> - `mcmm-marketing/m9l6` (Big Idea)
> - `mcmm-rozbir/m7l6` (Воронки)
> - `mcmm-rozbir/m7l7` (Піраміда Ділтса)
>
> Ці уроки не включені — Workspace platform відмовила у whisper transcription.

---

## Credits

- **Автор курсу MCMM:** Олексій Махонін, Юлія Козачкова (creo.ua)
- **Atomization by AI:** Юрій Довган + Claude Code (Opus 4.7 1M)
- **Призначення:** Personal pre-exam preparation + MCMM mastermind reference
- **Інфраструктура:** Claude Code skills + atomic Obsidian knowledge base methodology

---

## Як update коли курс продовжуватиметься

```bash
# 1. Додати новий урок локально в Юрієвій інфрі
cd ~/.claude/skills/mcmm-<discipline>/lessons/
mkdir m<N>l<N>-<slug>/
# whisper transcribe → atomize → claims/synthesis/flashcards (per `feedback_research_first_for_replication.md`)

# 2. Sync у public repo (rsync без raw/)
cd /path/to/mcmm-claude-skills
rsync -av --exclude='raw/' --exclude='_progress/' \
  --exclude='*.wav' --exclude='*.mp4' --exclude='*.webm' --exclude='*.pdf' \
  ~/.claude/skills/mcmm-<discipline>/ skills/mcmm-<discipline>/

# 3. Commit + push
git add skills/mcmm-<discipline>/
git commit -m "Add m<N>l<N>: <Lesson title> by <Lecturer>"
git push
```

---

## Питання / помилки

Знайшли помилку атрибуції лектора, неточну цитату, broken claim? Open issue на GitHub або напишіть Юрію у Telegram [@yuri369pay](https://t.me/yuri369pay).

Усі лектори згадані у repo — справжні люди з MCMM I потоку. Якщо ви — один із лекторів і хочете щось правити/видалити — пишіть Юрію прямо.

---

🤖 Atomized using Claude Code. База знань як живий артефакт — додається з кожним новим уроком.
