# Learning Protocol — як ідеально засвоїти новий урок MCMM

> Метапромпт. Повторюй цей пайплайн для кожного нового уроку. 6 кроків, 3-5 годин AI-роботи на урок.

## Goal

Здати будь-який тест за уроком на 100% і відповідати на концептуальні питання без галюцинацій, з посиланнями на slide/timestamp.

## Done when (SMART-критерії, всі мають бути ✅)

- [ ] `transcript.md` — дослівний transcript усього відео з timestamps (НЕ переказ)
- [ ] `slides.md` — кожен слайд у markdown (всі bullets, цитати, описи схем)
- [ ] `text.md` — повний супровідний текст сторінки уроку
- [ ] `quiz.md` — quiz уроку з правильними відповідями + поясненнями (якщо quiz є на сторінці)
- [ ] `claims.md` — кожна значуща теза як atomic claim: `[ID] [type: definition/fact/historical/classification/theory] [content] [verbatim quote] [source: slide N / video MM:SS / text §N]`
- [ ] `synthesis.md` — 1-2 сторінки running understanding (контекст уроку в курсі, ключові тези, парадокси)
- [ ] `flashcards.md` — 50+ карток recall (Q→A) покривають усі claims
- [ ] **Self-quiz pass**: 30+ Bloom-taxonomy питань (10 recall + 10 understand + 5 apply + 5 analyze) — 100% accuracy
- [ ] **Якщо є фінальний тест курсу** — пройдено на 100% (або 95%+ при randomized question set)
- [ ] `README.md` уроку — quick summary (½ сторінки) для швидкого пригадування
- [ ] `course_overview.md` оновлено: урок додано в таблицю

## Constraints

- НЕ переказувати — дослівний transcript. Whisper.cpp Metal на Apple Silicon = найвища точність.
- Кожен claim = **1 ідея** + verbatim quote + reference. Якщо в одному claim 2+ ідей — розщеплюй.
- Дати, імена, цифри — у claims з verbatim quote (НЕ парафраз).
- Не змішувати з general psychiatry training data — цитувати лише матеріал лекції.
- Якщо лектор каже "як ми бачили в уроці 3..." — позначити cross-reference, не вигадувати посилання.

## 6-step pipeline

### Step 1: Recon (1 background agent, 15-25 хв)

Зайти на сторінку уроку через Chrome MCP (Юрій залогінений). Описати ВСЕ що є.

**Чек-ліст recon**:

- Назва, тривалість, місце в курсі (попередній/наступний урок)
- Відео: player, прямий URL .mp4/iframe src, тривалість
- Презентація: формат, URL завантаження
- Супровідний текст: extracted full text
- Quiz: кількість питань, формат, чи доступні правильні відповіді
- Додаткові матеріали (PDF reading list)
- Лектор
- SRT/VTT subtitles готові? URL

Output: `recon.md` + список URLs до завантаження.

### Step 2: Extract (3-4 паралельні background agents, 30-90 хв)

Кожен з цих агентів — окремий контекст, паралельно:

**Agent A — Audio → transcript** (whisper.cpp Metal):

- Завантаж .mp4 через yt-dlp/curl у `raw/video.mp4`
- Extract audio через ffmpeg: `ffmpeg -i video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le raw/audio.wav`
- Whisper.cpp з language=uk, model=large-v3 (або v3-turbo для швидкості): `whisper-cli -l uk -m large-v3 raw/audio.wav -ot --output-srt --output-txt`
- Формат transcript.md: `[MM:SS] лектор: текст\n[MM:SS] ...`
- НЕ редагуй автоматично — залиш whisper output. Якщо в whisper "Пінел" а правильно "Пінель" — це окремий post-edit pass.

**Agent B — Slides → markdown**:

- Якщо PDF: pdfplumber/pymupdf → text per page → markdown структура з заголовками
- Якщо PPTX: python-pptx → text + speaker notes
- Якщо inline reveal.js: Chrome MCP → extract DOM per slide
- Формат: `## Slide N: <title>\n- bullet 1\n- bullet 2\n[опис схеми/зображення]`

**Agent C — Page text → markdown**:

- Chrome MCP get_page_text (вже зібрано на recon) → cleanup UI/nav → markdown
- Розділ із автором, метою уроку, конспектом якщо є

**Agent D — Quiz extraction** (якщо є):

- Якщо quiz on-page: Chrome MCP → витягни питання, варіанти, правильні відповіді (можливо доведеться відповісти 1 раз щоб побачити correct)
- Якщо quiz в окремому модулі: окрема навігація + extraction
- Формат JSON: `{"q": "...", "options": [...], "correct": idx, "explanation": "..."}`

### Step 3: Atomize (1 background agent, 30-60 хв)

Пройти transcript + slides + text. Виділити atomic claims.

**Типи claims**:

- `definition` — визначення терміну
- `fact` — окремий історичний факт (дата, подія)
- `historical_figure` — постать (роки життя, внесок)
- `classification` — класифікаційна система чи її пункт
- `theory` — теорія/парадигма/концепція
- `methodology` — метод діагностики/лікування
- `quote` — пряма цитата лектора з кваліфікацією

**Формат claim**:

```
## [C-007-014] historical_figure

**Name**: Філіп Пінель (Philippe Pinel)
**Years**: 1745-1826
**Significance**: Зняв ланцюги з душевнохворих у Бісетрі (1793), вважається засновником сучасної психіатричної ери.
**Source**: video 12:34, slide 14
**Verbatim quote**: "Пінель у 1793 році вперше зняв ланцюги..."
**Cross-references**: [C-007-002] (контекст моральної терапії)
```

ID-схема: `C-<lesson>-<NNN>` (C-007-001, C-007-002, ...).

### Step 4: Synthesize (main session — orchestrator)

Цей крок — head-of-context аналіз. Не делегувати.

Прочитати claims.md → побудувати `synthesis.md` (1-2 сторінки):

- **Контекст уроку** — де він у курсі, що передувало, що далі
- **Ключова теза** уроку (1 речення)
- **3-5 sub-thesis** які підкріплюють ключову
- **Постаті** та їхні зв'язки (хто на кого вплинув)
- **Парадокси / контр-точки** які лектор підкреслив
- **Зв'язки з іншими уроками** курсу (cross-refs)
- **Applied to coaching** — що з цього Юрій може використати у своїй коучингoвій практиці (DETECTIVE FM)

### Step 5: Build skill bundle (main + 1 agent для flashcards)

- `README.md` уроку — ½ сторінки quick summary
- `flashcards.md` — 50+ карток (Q→A) покривають усі claims. Spaced repetition format.
- Оновити `course_overview.md` — додати урок у таблицю
- Оновити `SKILL.md` — оновити status table у кінці

### Step 6: Verify (1 background agent, 30 хв)

**Self-quiz pass**:

- Згенерувати 30+ Bloom-taxonomy питань:
  - 10× recall ("у якому році Пінель зняв ланцюги?")
  - 10× understand ("чому Пінелевий жест важливий?")
  - 5× apply ("як використати моральну терапію в коучингу 2026?")
  - 5× analyze ("порівняй Пінеля і Тьюка — у чому подібність методів?")
- Кожне питання має правильну відповідь з посиланням на claim
- Орchестратор Claude відповідає на ВСІ 30 без читання claims.md (тільки head context) → перевіряє по claims → accuracy має бути 100%
- Будь-яке питання що не відповів коректно — повертайся в conspect, додай claim або розширюй synthesis

**Якщо є фінальний тест курсу**:

- Пройти. Якщо <100% — виявити прогалини, повернутися до Step 3 (claims).

## Анти-патерни

- ❌ Підсумовувати замість дослівного transcript ("лектор каже про важливість Пінеля" — це переказ, а не claim)
- ❌ Видавати загальні знання з training data за матеріал курсу
- ❌ Пропускати "очевидні" слайди — кожен слайд має слід у `slides.md`
- ❌ Записувати один claim який містить 3 ідеї
- ❌ Цитувати з пам'яті — завжди verbatim з джерела
- ❌ Робити extraction sequentially — це паралелізується

## Час

| Step                 | Time        | Mode                           |
| -------------------- | ----------- | ------------------------------ |
| 1. Recon             | 15-25 хв    | 1 BG agent                     |
| 2. Extract           | 30-90 хв    | 3-4 BG agents паралельно       |
| 3. Atomize           | 30-60 хв    | 1 BG agent                     |
| 4. Synthesize        | 20-40 хв    | main                           |
| 5. Build             | 15-30 хв    | main + 1 BG agent (flashcards) |
| 6. Verify            | 30 хв       | 1 BG agent                     |
| **Total wall-clock** | **2-4 год** | (паралелізм економить)         |

## Як запустити для нового уроку

1. Юрій надсилає URL уроку
2. Orchestrator Claude: "Запускаю learning_protocol.md для уроку N"
3. Виконати Steps 1-6
4. Final report: `✅ Lesson N indexed. {{N_claims}} claims, {{N_flashcards}} flashcards, self-quiz {{accuracy}}%`
