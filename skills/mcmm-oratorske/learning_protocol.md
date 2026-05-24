# Learning Protocol — як ідеально засвоїти новий урок MCMM Ораторського

> Метапромпт. Повторюй цей пайплайн для кожного нового уроку. 6 кроків, 3-5 годин AI-роботи на урок.
> **Ключова відмінність від mcmm-psychiatry**: ораторське має ПРАКТИЧНІ ВПРАВИ → окремий Agent E (Exercises extraction) у Step 2.

## Goal

Здати будь-який тест за уроком на 100%, відповідати на концептуальні питання без галюцинацій з посиланнями на slide/timestamp, **АНД мати готові вправи у форматі instruction script які я можу провести з Юрієм у діалозі**.

## Done when (SMART-критерії, всі мають бути ✅)

- [ ] `transcript.md` — дослівний transcript усього відео з timestamps (НЕ переказ)
- [ ] `slides.md` — кожен слайд у markdown (всі bullets, цитати, описи схем)
- [ ] `text.md` — повний супровідний текст сторінки уроку (**SKIP якщо <200 слів на сторінці** — у поточному блоці ораторського сторінки мають тільки ~70-120 слів опису, не повноцінний text. У такому випадку записати `text.md` = "N/A — page description only <X> words")
- [ ] `quiz.md` — quiz уроку з правильними відповідями + поясненнями. **Поточний блок ораторського НЕ МАЄ офіційного quiz на сторінках** — тому `quiz.md` буде **predicted/synthetic** (10-15 питань я сам генерую з claims з 4 правдоподібними дистракторами + поясненнями). Позначити frontmatter `quiz_type: synthetic` vs `official`.
- [ ] `claims.md` — кожна значуща теза як atomic claim: `[ID] [type: definition/technique/framework/historical/quote] [content] [verbatim quote] [source: slide N / video MM:SS / text §N]`
- [ ] **`exercises/ex-NN.md`** — кожна вправа з лекції витягнута як окремий файл з повним instruction script що Я можу провести з Юрієм у діалозі (sequence + критерії + adaptations)
- [ ] `synthesis.md` — 1-2 сторінки running understanding (контекст уроку в курсі, ключові тези, парадокси)
- [ ] `flashcards.md` — 50+ карток recall (Q→A) покривають усі claims
- [ ] **Self-quiz pass**: 30+ Bloom-taxonomy питань (10 recall + 10 understand + 5 apply + 5 analyze) — 100% accuracy
- [ ] **Якщо є фінальний тест курсу** — пройдено на 100% (або 95%+ при randomized question set)
- [ ] `README.md` уроку — quick summary (½ сторінки) для швидкого пригадування
- [ ] `course_overview.md` оновлено: урок додано в таблицю
- [ ] **Unique ratio gate**: transcript unique_lines/total_lines ≥ 0.8 (whisper anti-hallucination)

## Constraints

- НЕ переказувати — дослівний transcript. Whisper.cpp Metal на Apple Silicon = найвища точність.
- Кожен claim = **1 ідея** + verbatim quote + reference. Якщо в одному claim 2+ ідей — розщеплюй.
- Дати, імена, цифри — у claims з verbatim quote (НЕ парафраз).
- Не змішувати з general public speaking training data — цитувати лише матеріал лекції.
- Якщо лектор каже "як ми бачили в попередньому уроці..." — позначити cross-reference, не вигадувати.
- **Whisper команда (anti-hallucination, MEMORY rule #40 обов'язкова)**:
  ```
  whisper-cli -l uk -m large-v3 -f raw/audio.wav -otxt -osrt -of raw/transcript -t 8 -p 1 --max-context 0 --suppress-nst --print-progress
  ```
- **Pre-flight RAM check** (MEMORY rule #39): `vm_stat | awk '/Pages free/{print $3}'` — якщо < 100K → STOP, чекати
- **Max 2 паралельних whisper** одночасно
- **yt-dlp БЕЗ --remux** (RAM rule #39 — не тримати весь файл в RAM)
- **Verify whisper output**: `grep -v "^$" transcript.txt | sort | uniq -c | sort -rn | head -5` — якщо один рядок повторений >10 разів → RED FLAG, перезапустити; unique_ratio < 0.8 → перезапустити

## 6-step pipeline

### Step 1: Recon (1 background agent, 15-25 хв)

Зайти на сторінку уроку через Chrome MCP (Юрій залогінений). Описати ВСЕ що є.

**Чек-ліст recon**:

- Назва, тривалість, місце в курсі (попередній/наступний урок)
- Відео: player, прямий URL .mp4/iframe src, тривалість
- Презентація: формат, URL завантаження
- Супровідний текст: extracted full text
- Quiz: кількість питань, формат, чи доступні правильні відповіді
- **Кількість і типи вправ у лекції** (warmup / voice / breath / structure / presence) — це нова метрика для ораторського
- Додаткові матеріали (PDF reading list)
- Лектор
- SRT/VTT subtitles готові? URL

Output: `recon.md` + список URLs до завантаження.

### Step 2: Extract (4-5 паралельних background agents, 30-90 хв)

Кожен з цих агентів — окремий контекст, паралельно:

**Agent A — Audio → transcript** (whisper.cpp Metal):

- Pre-flight RAM check (`vm_stat`). Якщо free pages < 100K — wait
- Завантаж .mp4 через yt-dlp **БЕЗ --remux** у `raw/video.mp4`
- Extract audio через ffmpeg: `ffmpeg -i video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le raw/audio.wav`
- Whisper.cpp з language=uk, model=large-v3 з anti-hallucination flags:
  ```
  whisper-cli -l uk -m large-v3 -f raw/audio.wav -otxt -osrt -of raw/transcript -t 8 -p 1 --max-context 0 --suppress-nst --print-progress
  ```
- Verify: `grep -v "^$" raw/transcript.txt | sort | uniq -c | sort -rn | head -5` — топ-5 повторюваних, якщо ≥10 → RED FLAG
- Unique ratio gate: unique_lines / total_lines ≥ 0.8. Якщо < 0.8 → hallucination loop, перезапустити
- Формат `transcript.md`: `[MM:SS] лектор: текст\n[MM:SS] ...`
- Max 2 паралельних whisper одночасно (RAM rule)

**Agent B — Slides → markdown**:

- Якщо PDF: pdfplumber/pymupdf → text per page → markdown структура з заголовками
- Якщо PPTX: python-pptx → text + speaker notes
- Якщо inline reveal.js: Chrome MCP → extract DOM per slide
- Формат: `## Slide N: <title>\n- bullet 1\n- bullet 2\n[опис схеми/зображення]`

**Agent C — Page text → markdown**:

- Chrome MCP get_page_text (вже зібрано на recon) → cleanup UI/nav → markdown
- Розділ із автором, метою уроку, конспектом якщо є

**Agent D — Quiz** (synthetic для поточного блоку — на сторінках офіційного quiz нема):

- **Якщо quiz on-page** (mcmm-psychiatry case): Chrome MCP → витягни питання, варіанти, правильні відповіді → `quiz_type: official`
- **Якщо quiz відсутній** (поточний ораторський блок case): після Step 3 (Atomize) на основі `claims.md` згенерувати 10-15 predicted Q (3-4 single-choice + 4-5 open-ended + 2-3 application). Frontmatter `quiz_type: synthetic`. Це Agent D запускається **після** Step 3, не паралельно зі Step 2.
- Формат JSON: `{"q": "...", "options": [...], "correct": idx, "explanation": "...", "source_claim": "C-l05-NNN"}`

**Agent E — Exercises extraction** ⭐ КЛЮЧОВЕ для ораторського:

- Прочитати transcript + slides → знайти ВСІ вправи що лектор пропонує
- Кожну вправу витягти окремим файлом у `lessons/<lesson>/exercises/ex-NN.md`
- **Формат файлу вправи** (обов'язково ВСІ секції):

```markdown
---
name: <коротка назва вправи>
lesson: <lesson-folder-name>
type: warmup | voice | breath | structure | presence | articulation | rhythm | other
duration_min: <число хвилин>
difficulty: beginner | intermediate | advanced
needs_partner: yes | no
needs_recording: yes | no
---

# <Назва вправи>

## Мета

1-2 речення нащо ця вправа (що тренує, який скіл розвиває).

## Інструкція

Нумерований список кроків ТАК ЯК Я БУДУ ЇХ ВИКОНУВАТИ З ЮРІЄМ У ДІАЛОЗІ. Кожен крок = одна дія + те що я говорю Юрію.

1. **Я кажу Юрію**: «<точна фраза що я кажу як coach-agent>»
2. **Юрій робить**: <що очікую від нього — text / audio / запис відео>
3. **Я кажу**: «<наступна фраза>»
4. ...

## Що оцінювати

Критерії success (3-7 пунктів):

- [ ] Critère 1 — конкретний perceivable signal
- [ ] Critère 2 — ...

## Поширені помилки

Антипаттерни (3-5 пунктів):

- ❌ Помилка 1 — як виявити, як скорегувати
- ❌ Помилка 2 — ...

## Adaptations

- **Текст**: якщо Юрій надсилає письмову відповідь — що оцінюю
- **Голос (Wispr / audio file)**: якщо Юрій надсилає аудіо — на що звертаю увагу
- **Відеозапис**: якщо Юрій надсилає відео — додаткові критерії (mimic, постава)

## Verbatim quote

Як саме лектор пояснює цю вправу — дослівна цитата з timestamp:

> "<verbatim quote>" — [video MM:SS]
```

- ID-схема: `ex-NN.md` (ex-01, ex-02, ... у межах одного уроку)
- Якщо вправа має варіації — окремий файл на варіацію або секція "Варіації" в одному файлі

### Step 3: Atomize (1 background agent, 30-60 хв)

Пройти transcript + slides + text. Виділити atomic claims.

**Типи claims для ораторського**:

- `definition` — визначення терміну (напр. "магнетичний виступ")
- `fact` — окремий історичний факт (дата, подія)
- `technique` — техніка/прийом (напр. "техніка діафрагмального дихання")
- `framework` — фреймворк/структура виступу
- `classification` — класифікація (напр. типи аудиторій)
- `theory` — теорія/парадигма/концепція
- `methodology` — метод діагностики/тренування
- `quote` — пряма цитата лектора з кваліфікацією

**Формат claim**:

```
## [C-l05-014] technique

**Name**: Діафрагмальне дихання для голосу лідера
**Context**: <короткий контекст застосування>
**Mechanism**: <як працює, чого досягає>
**Source**: video 12:34, slide 14
**Verbatim quote**: "..."
**Cross-references**: [C-l05-002] (контекст резонансу) · [exercises/ex-03.md] (практика)
```

ID-схема: `C-<lesson-folder>-<NNN>` (C-l05-001, C-l05-002, ...). Якщо claim прив'язаний до вправи — cross-ref на `exercises/ex-NN.md`.

### Step 4: Synthesize (main session — orchestrator)

Цей крок — head-of-context аналіз. Не делегувати.

Прочитати claims.md + exercises/\*.md → побудувати `synthesis.md` (1-2 сторінки):

- **Контекст уроку** — де він у курсі, що передувало, що далі (cross-наскрізні зв'язки L5↔L7↔L8)
- **Ключова теза** уроку (1 речення)
- **3-5 sub-thesis** які підкріплюють ключову
- **Постаті** та їхні зв'язки (хто на кого вплинув, з ким лектор полемізує)
- **Парадокси / контр-точки** які лектор підкреслив
- **Зв'язки з іншими уроками** ораторського + з mcmm-psychiatry якщо релевантно
- **Applied to coaching** — як використовувати у роботі з клієнтами-коучами/експертами (Detective FM, МАЙСТЕРНЯ)
- **Exercises overview** — короткий перелік вправ цього уроку з типами (warmup/voice/...) і коли застосовувати

### Step 5: Build skill bundle (main + 1 agent для flashcards)

- `README.md` уроку — ½ сторінки quick summary + перелік exercises
- `flashcards.md` — 50+ карток (Q→A) покривають усі claims (НЕ exercises — для них окрема ритуальна практика)
- Оновити `course_overview.md` — додати урок у таблицю
- Оновити `SKILL.md` — оновити status table у кінці

### Step 6: Verify (1 background agent, 30 хв)

**Self-quiz pass**:

- Згенерувати 30+ Bloom-taxonomy питань:
  - 10× recall ("як називається техніка X?")
  - 10× understand ("чому діафрагмальне дихання важливе?")
  - 5× apply ("як використати рамку магнетичного виступу для коучингового кейсу 2026?")
  - 5× analyze ("порівняй техніку голосу лідера і техніку конструктивної критики — у чому подібність?")
- Кожне питання має правильну відповідь з посиланням на claim
- Orchestrator Claude відповідає на ВСІ 30 без читання claims.md (тільки head context) → перевіряє по claims → accuracy має бути 100%
- Будь-яке питання що не відповів коректно — повертайся в conspect, додай claim або розширюй synthesis

**Exercise sanity check** ⭐ (нове для ораторського):

- Прочитати кожен `exercises/ex-NN.md` свіжими очима
- **Test**: чи зможу я провести цю вправу з Юрієм у діалозі ТІЛЬКИ з цього файлу, без додаткового контексту?
- Якщо ні — додати недостаючі кроки в `## Інструкція` або уточнити `## Що оцінювати`
- Verify-checkmark: instruction sequence має містити фрази що Я говорю Юрію (in-character coach voice)

**Якщо є фінальний тест курсу**:

- Пройти. Якщо <100% — виявити прогалини, повернутися до Step 3 (claims).

## Анти-патерни

- ❌ Підсумовувати замість дослівного transcript ("лектор каже про важливість голосу" — це переказ, а не claim)
- ❌ Видавати загальні знання з public-speaking training data за матеріал курсу
- ❌ Пропускати "очевидні" слайди — кожен слайд має слід у `slides.md`
- ❌ Записувати один claim який містить 3 ідеї
- ❌ Цитувати з пам'яті — завжди verbatim з джерела
- ❌ Робити extraction sequentially — це паралелізується
- ❌ Записати вправу одним абзацом "робиш X" замість пронумерованої instruction sequence
- ❌ Пропустити `## Adaptations` для тексту/голосу/відео — Юрій надсилає різні формати
- ❌ Whisper без anti-hallucination flags (`--max-context 0 --suppress-nst`) — гарантовано спродукує loop
- ❌ Не verify unique_ratio після whisper — пропустиш 22-хв повтор

## Час

| Step                 | Time          | Mode                                         |
| -------------------- | ------------- | -------------------------------------------- |
| 1. Recon             | 15-25 хв      | 1 BG agent                                   |
| 2. Extract           | 40-110 хв     | 4-5 BG agents паралельно (з Exercises)       |
| 3. Atomize           | 30-60 хв      | 1 BG agent                                   |
| 4. Synthesize        | 20-40 хв      | main                                         |
| 5. Build             | 15-30 хв      | main + 1 BG agent (flashcards)               |
| 6. Verify            | 30-45 хв      | 1 BG agent (claims + exercise sanity)        |
| **Total wall-clock** | **2.5-5 год** | (паралелізм економить; вправи додають 30 хв) |

## Як запустити для нового уроку

1. Юрій надсилає URL уроку
2. Orchestrator Claude: "Запускаю learning_protocol.md для уроку <N>"
3. Виконати Steps 1-6
4. Final report: `✅ Lesson <N> indexed. {{N_claims}} claims, {{N_exercises}} exercises, {{N_flashcards}} flashcards, self-quiz {{accuracy}}%`
