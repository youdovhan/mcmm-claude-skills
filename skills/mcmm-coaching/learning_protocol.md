# Learning Protocol — MCMM Coaching

**Призначення:** 6-крок пайплайн індексації нового уроку Коучингу в skill `mcmm-coaching`. Адаптовано з `mcmm-ta/learning_protocol.md` + `mcmm-psychiatry/learning_protocol.md`.

**Прообрази:**

- `mcmm-psychiatry/learning_protocol.md` (14/14 уроків, avg accuracy 98.93%)
- `mcmm-ta/learning_protocol.md` (9 уроків, production-tested через 10-Q self-quiz, 96.25%)

---

## Передумови

- Локальний транскрипт лекції (Whisper.cpp output): `/Users/detective/.claude/skills/mcmm-coaching/lessons/<slug>/raw/transcript.srt` + `transcript.txt`
- Cleaned transcript: `/Users/detective/.claude/skills/mcmm-coaching/lessons/<slug>/transcript.txt` (після transcript-cleanup.py)
- Опційно — PDF слайдів з Google Drive (якщо доступний за лінком на mcmm.creo)
- Опційно — Obsidian notes Юрія: `/Users/detective/ObsidianVault/MCMM/<modulu>.md`

## 6-Step Pipeline

### Stage 1 — Recon (5-10 хв)

- Read transcript (mostly first 100 lines для self-intro + останні 50 для summary)
- **VERIFY lecturer self-intro** — first 30-50 lines. Не extrapolate з inventory! Per `feedback_lecturer_attribution_per_lesson.md`.
- Витягни meta: Module, Lesson, тема, тривалість, ключові постаті
- Знайди secondary sources зацитовані лектором (книги, статті, дослідники)
- Запиши skeleton `README.md` (тема, тривалість, основні концепти, **лектор-verified per primary source**)

### Stage 2 — Extract (10-20 хв)

- `transcript.txt` уже cleaned через `transcript-cleanup.py`
- Якщо bullet-point структура слайдів збереглася — додай як `slides_notes.md`
- Збережи timestamps якщо є у SRT

### Stage 3 — Atomize (30-60 хв) — НАЙВАЖЛИВІШЕ

Створи `claims.md` з 70-120 atomic claims у форматі:

```
### [COACH-MN-LM-001] definition: «Активне слухання»
**Claim:** Активне слухання — це техніка/практика повного присутности у моменті взаємодії з клієнтом, де коуч…
**Verbatim:** "Активне слухання — це …" (з transcript)
**Source:** transcript MM:SS / slide N / Obsidian §X
**Type:** definition | mechanism | framework | clinical_marker | historical | cross_ref | coaching_application
```

**Типи claims для коучингу:**

- `definition` — визначення концепта (presence, listening, awareness)
- `mechanism` — як працює (e.g. як саме presence створюється у моменті)
- `framework` — модель (ICF 8 компетенцій, 4 рівні слухання, etc.)
- `marker` — діагностична ознака у поведінці коуча/клієнта (e.g. ознака що коуч "впав" у роль експерта)
- `historical` — постаті, дати, школи (Whitmore, Gallwey, Sir John Whitmore, GROW, ICF history)
- `cross_ref` — зв'язок з іншими уроками коучингу / ТА / psychiatry
- `coaching_application` — як це застосовується у Юрієвих сесіях Detective FM

### Stage 4 — Synthesize (20-40 хв)

Створи `synthesis.md` з 9 секцій (running understanding):

1. **Контекст у курсі** — як цей урок зв'язаний з попереднім + наступним
2. **Ключова теза** — 1 речення, есенція уроку
3. **Sub-theses** — 5+ під-тверджень що підтримують головну тезу
4. **Постаті** — timeline (хто, коли, що додав) — наприклад: Whitmore 1992 GROW → ICF founding 1995 → Gallwey Inner Game 1974
5. **Парадокси / напруження** — де теорія сама себе тестує (напр. "presence vs ціль", "слухання vs керування")
6. **Cross-refs** — інші уроки коучингу (`m3l2-active-listening ↔ m3l4-presence ↔ m6l4-coach-awareness`) + ТА (`mcmm-ta/m1l3-contracts` для контракту з клієнтом) + psychiatry (`mcmm-psychiatry/l13-persdev` для red flags)
7. **Suspicious / open questions** — що лектор згадав мимохідь і варто перевірити
8. **Applied to coaching** — як Юрій буде цим користуватися у сесіях Detective FM (€39 / €300 / €1469 / €2969 / €5469)
9. **Key facts + mnemonics** — 5-10 цифр/імен/абревіатур для recall

### Stage 5 — Build (15-30 хв)

Створи:

- `quiz.md` — 10-15 predicted Q+A
- `flashcards.md` — 50-80 карток Bloom-distributed:
  - Recall 40% (definition, постать, дата)
  - Understand 25% (механізм, "чому")
  - Apply 20% (case → діагноз / інтервенція)
  - Analyze 15% (compare 2 концепти, identify пропущену змінну)
- `README.md` — quick summary (½ сторінки) з top-5 claims
- Update `course_overview.md` — додай рядок у таблицю з status `✅ indexed` + accuracy (якщо self-quiz прогнано)

### Stage 6 — Test (10-15 хв)

10-question self-quiz mix of types:

- 3 recall, 3 understand, 2 apply, 2 analyze
- Score self-honestly. Ціль ≥ 90%. <90% → дочитай claims / synthesis секцій що завалив.

---

## Special considerations для Coaching

1. **Lecturer ID verification:** primary-source self-intro у first 30-50 lines transcript. НЕ extrapolate з inventory.md (там може бути помилка). Per `feedback_lecturer_attribution_per_lesson.md`.
2. **Practical > theoretical bias:** коучинг — це передусім practice. Більшість claims `type: coaching_application` має посилання на «застосування у сесії Detective FM пакети €X».
3. **Cross-refs до Detective FM:** хороший claim має 2 джерела — verbatim з лекції + applied у Юрієвому пакеті.
4. **AI-стек coach речі (для Conference 23-24.05):** клами що працюють як bridge між класикою коучингу і AI-стеком (наприклад "AI-помічник для contract review" чи "AI-prompt для presence audit після сесії") — позначай тегом `[AI-CONFERENCE]` для швидкого виходу.
