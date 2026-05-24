# Learning Protocol — MCMM Transactional Analysis (ТА)

**Призначення:** 6-крок пайплайн індексації нового уроку ТА в skill `mcmm-ta`. Адаптовано з `mcmm-psychiatry/learning_protocol.md` під text-only джерела (повні транскрипти лекцій уже є локально, відео-recon не потрібен).

**Прообраз:** `mcmm-psychiatry/learning_protocol.md` (14/14 уроків, avg accuracy 98.93%).

---

## Передумови

- Локальний транскрипт лекції (Whisper.cpp output): `/Users/detective/Claude/mcmm_mN_lM_transcript.txt`
- Конспект з Obsidian: `/Users/detective/ObsidianVault/MCMM/MCMM Модуль N.md` (секція по уроку)
- Опційно — авторські notes: `/Users/detective/Claude/mcmm_mN_lM_notes.md`

## 6-Step Pipeline

### Stage 1 — Recon (5-10 хв)

- Read обидва джерела (transcript + Obsidian notes)
- Витягни meta: Module, Lesson, тема, тривалість, ключові постаті ТА (Берн, Штайнер, Карпман, Гулдінги, Ернст, Erskine&Zalcman, James&Jongeward, Mary&Bob Goulding, Crossman)
- Знайди secondary sources зацитовані лектором (книги: Берн "Games People Play", "Sex in Human Loving", Штайнер "Scripts People Live", Hay "Working it Out at Work"...)
- Запиши skeleton `README.md` (тема, тривалість, основні концепти)

### Stage 2 — Extract (10-20 хв)

- Copy `transcript.txt` → `lessons/lN-slug/transcript.md` з cleanup:
  - Видали повторювані фрагменти hallucination'ів (артефакти Whisper)
  - Зроби paragraph breaks (Whisper output = monolithic)
  - Збережи timestamps якщо є
- Якщо є `notes.md` — додай як `lessons/lN-slug/notes_original.md`
- Якщо є PDF слайдів — extract в `slides.md`

### Stage 3 — Atomize (30-60 хв) — НАЙВАЖЛИВІШЕ

Створи `claims.md` з 70-120 atomic claims у форматі:

```
### [TA-LN-001] definition: «Транзактний аналіз»
**Claim:** ТА — теорія особистості, комунікації та психотерапії, створена Е. Берном (1958-1970)
**Verbatim:** "Транзактний аналіз — це …" (з transcript)
**Source:** transcript MM:SS / slide N / Obsidian §X
**Type:** definition | mechanism | framework | clinical_marker | historical | cross_ref | coaching_application
```

**Типи claims для ТА:**

- `definition` — визначення концепта (его-стан, гра, сценарій)
- `mechanism` — як працює (контамінація, формула B, рекет)
- `framework` — модель (структурна 1-3 порядку, сценарна матриця, ОК-corral)
- `marker` — діагностична ознака у мові/поведінці клієнта
- `historical` — постаті, дати, школи (Berkeley, Cathexis, Redecision)
- `cross_ref` — зв'язок з іншими уроками ТА або psychiatry
- `coaching_application` — як це застосовується в коучингу

### Stage 4 — Synthesize (20-40 хв)

Створи `synthesis.md` з 9 секцій (running understanding):

1. **Контекст у курсі** — як цей урок зв'язаний з попереднім + наступним
2. **Ключова теза** — 1 речення, есенція уроку
3. **Sub-thesis** — 5+ під-тверджень що підтримують головну тезу
4. **Постаті** — timeline (хто, коли, що додав) — Berne 1958 → Steiner 1971 → Goulding 1979 → Erskine 1979 → ...
5. **Парадокси / напруження** — де теорія сама себе тестує (напр. "автономія vs приналежність")
6. **Cross-refs** — інші уроки ТА (`m2l2-ego-states ↔ m5l3-games`) + psychiatry (`mcmm-psychiatry l13-persdev` для розрізнення сценарію vs РОЗ)
7. **Suspicious / open questions** — що лектор згадав мимохідь і варто перевірити
8. **Applied to coaching** — як Юрій буде цим користуватися в сесіях
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
- Update `course_overview.md` — додай рядок у таблицю з status `✅ DONE` + accuracy

### Stage 6 — Verify (20-30 хв)

- Створи `verify.md` з 30 cross-claim Q
- Прогони self-quiz: для кожної Q подивись чи відповідаєш правильно тільки з `claims.md` + `synthesis.md`
- Запиши accuracy %
- **Pass gate: ≥ 95%**. Якщо нижче — повернись до Stage 3, додай пропущені claims.

---

## Anti-hallucination

ТА — широка дисципліна, багато матеріалу з training data. Жорсткі правила:

❌ **НЕ** змішувати training data знання про ТА з матеріалом лекції Влади Березянської (TA lecturer у MCMM; primary-source M1L3 line 99-114).
✅ Якщо концепт є в claims — вільно цитуй.
✅ Якщо концепт є в training data, але **не** в claims — додай позначку: "(_з ТА-літератури, не озвучено в курсі MCMM_)".
❌ **НЕ** додумувати приклади ігор / драйверів якщо лектор їх не наводив.

## Cross-cutting check

Перед фіналізацією уроку — пройди:

- ✅ Чи додав я постатей у спільний `_postati.md` (опціонально)?
- ✅ Чи додав я ігри у `games_atlas.md`?
- ✅ Чи додав я драйвери/заборони/позиції у `script_atlas.md`?
- ✅ Чи додав я рекетні почуття у `feelings_atlas.md`?
- ✅ Чи додав я coaching applications у `coaching/client_decoder.md`?

## Pattern для нового уроку (виклик)

```
"Створи l<N>-<slug>/ за learning_protocol.md.
Джерела:
- transcript: /Users/detective/Claude/mcmm_mX_lY_transcript.txt
- notes Obsidian: /Users/detective/ObsidianVault/MCMM/MCMM Модуль X.md (секція 'Урок Y')
- optional: /Users/detective/Claude/mcmm_mX_lY_notes.md
Acceptance: ≥95% on 30 verify Q."
```
