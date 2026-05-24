# HOW TO USE — MCMM Claude Skills

Три шляхи підключення бази знань залежно від твого setup'у.

---

## 1) Claude Code (рекомендовано)

**Найкращий варіант** — skills автоматично активуються коли ти питаєш про MCMM-теми. Claude сам розпізнає трігерні слова з `SKILL.md` і підтягує relevant lesson.

### Установка (один раз)

```bash
# Перейти у директорію Claude Code skills
cd ~/.claude/skills

# Clone repo
git clone https://github.com/youdovhan/mcmm-claude-skills.git mcmm

# (опційно) Зв'язати кожну skill окремо — щоб бачити їх як top-level
# По одній на кожну дисципліну:
for s in skills/*/; do
  name=$(basename "$s")
  ln -sf "$PWD/mcmm/$s" "./$name"
done

# Restart Claude Code
```

### Як це працює

Кожна skill має `SKILL.md` з трігерами:

```yaml
---
name: mcmm-coaching
description: База знань з дисципліни Коучинг у курсі MCMM... Тригери: "Махонін", "ICF", "коучингова сесія", "активне слухання", "присутність коуча"...
---
```

Коли ти питаєш Claude "розкажи про активне слухання за Махоніним" — Claude бачить тригер, активує `mcmm-coaching` skill, читає relevant `lessons/<lesson>/synthesis.md` + `transcript.txt`, відповідає на основі verbatim quotes.

### Приклад запиту у Claude Code

```
> розкажи що Лана говорить про 4 рівні слухання
```

Claude активує `mcmm-coaching` → читає `lessons/m3l2-active-listening/synthesis.md` → відповідає з verbatim цитатами.

### Update коли репо оновиться

```bash
cd ~/.claude/skills/mcmm
git pull
# Restart Claude Code
```

---

## 2) Claude.ai (browser) або Claude API

Skills у вигляді як у Claude Code тут не працюють — треба **руками** копіювати content.

### Варіант A — System prompt

1. Відкрий [Projects у Claude.ai](https://claude.ai/projects) → створи новий "MCMM Reference"
2. У "Project knowledge" завантаж relevant `SKILL.md` + `lessons/<lesson>/synthesis.md` як файли
3. У "Custom instructions" встав:

```
Ти — AI-асистент Юрія Довгана. Використовуй знання з прикріплених MCMM-skills для відповідей про коучинг, психіатрію, ТА, маркетинг тощо. Завжди цитуй лекторів verbatim, з посиланням на конкретний lesson (напр. "Лана у m3l2 каже:..."). Якщо запит виходить за межі attached knowledge — скажи прямо.
```

4. Питай як звичайно — Claude з Project відповідатиме з контекстом

### Варіант B — Single-skill як system prompt у API

```python
import anthropic

client = anthropic.Anthropic()

# Завантажити SKILL.md як system prompt
with open("skills/mcmm-ta/SKILL.md") as f:
    skill_content = f.read()

# Завантажити relevant synthesis як user-attached context
with open("skills/mcmm-ta/lessons/m10l2-adaptatsii-protsesualna-model/synthesis.md") as f:
    lesson_synthesis = f.read()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=f"Ти експерт з MCMM. Ось знання дисципліни:\n\n{skill_content}\n\nКонтекст уроку:\n{lesson_synthesis}",
    messages=[
        {"role": "user", "content": "Поясни 6 особистісних адаптацій Влади за Kahler reframing"}
    ]
)

print(response.content[0].text)
```

---

## 3) ChatGPT / Gemini / інші LLM

Як reference context. Skill metadata тут не активується автоматично — копіюй content вручну.

### ChatGPT (web)

1. Відкрий [ChatGPT Projects](https://chatgpt.com/projects) → новий проєкт "MCMM Knowledge"
2. У "Files" завантаж `synthesis.md` + `claims.md` потрібного уроку
3. У "Instructions" встав опис ролі: "Ти експерт з курсу MCMM, відповідай на основі attached materials..."
4. Питай у проєкті

### Gemini (gemini.google.com)

1. У Gem'і Gemini Advanced — створи Custom Gem "MCMM Reference"
2. У "Knowledge" attach `lessons/<lesson>/synthesis.md` + `transcript.txt`
3. У instructions: "Цитуй verbatim з MCMM transcripts, attribute до конкретного лектора (Лана / Махонін / Влада / Ходяков etc)"

### Manual flow (будь-який LLM)

Просто скопіюй текст із `transcript.txt` уроку → у prompt:

```
Ось транскрипт уроку Mcmm m3l2 (Лана про активне слухання):
---
[paste content of transcript.txt]
---

Питання: Розкажи що Лана каже про 4 рівні слухання, з конкретними цитатами.
```

---

## Структура skill — що читати

```
skills/mcmm-<discipline>/
├── SKILL.md              ← metadata, тригери, опис коли активувати
└── lessons/
    └── m<N>l<N>-<slug>/
        ├── README.md     ← brief overview уроку
        ├── transcript.txt ← повний clean verbatim текст
        ├── transcript.srt ← з timecodes (якщо є)
        ├── synthesis.md  ← consolidated understanding (главна для quick reference)
        ├── claims.md     ← atomic claims (1 рядок = 1 цитата + контекст)
        └── flashcards.md ← spaced-repetition Q/A (для іспиту)
```

**Швидкий вибір:**

- **Хочеш зрозуміти суть уроку:** `synthesis.md`
- **Хочеш verbatim цитати лектора:** `transcript.txt`
- **Хочеш атомарні твердження для контенту/Q&A:** `claims.md`
- **Готуєшся до іспиту:** `flashcards.md` + `../EXAM_REHEARSAL.md`

---

## Приклади запитів — копіюй і пробуй

### Коучинг (Лана, Махонін, Козачкова)

```
"Поясни 4 рівні слухання за Ланою (mcmm-coaching m3l2)"
"Як ICF 8 компетенцій лягають на coaching session structure?"
"Дай скрипт демо-сесії за позицією коуча Махоніна"
"Компетенція 7 vs 8 — у чому ріжниця?"
```

### Транзактний аналіз (Влада)

```
"6 особистісних адаптацій Joines/Mountain — recap"
"Doors of Contact 3×3 matrix — як визначити open vs trap door у клієнта"
"5 драйверів (Be Strong / Be Perfect / Please / Try Hard / Hurry Up) — поведінкові маркери"
"Трикутник Карпмана vs Контракт Sills — чим відрізняється підхід"
```

### Психіатрія (Бережний)

```
"Що Бережний каже про РДУГ діагностику?"
"Шизофренія vs шизоїдна адаптація — diff diagnosis"
"Pharma m14 — основні класи препаратів"
"Коли коуч маршрутизує клієнта до психіатра — RED FLAGS"
```

### Маркетинг (Махонін)

```
"7 компонентів спокусливого оферу (m8l6)"
"Customer Journey Map 8 етапів — для коуч-послуги"
"Продуктова лінійка 5-tier — приклад для коуча"
"Snickers коли голодний — як працює інсайт-через-біль"
```

### NLP (Ходяков)

```
"Метамодель — порушення з прикладами"
"VAKOG калібрування — як визначити у клієнта"
"Логічні рівні Ділтса — для self-discovery коуча"
"Бекхард D×V×F>R — приклад розрахунку"
```

### Бізнес-стратегія (Гончар)

```
"План vs Стратегія через Ділтса — Гончар"
"ORID фреймворк — як вести стратсесію"
"Express-діагностика 7 функцій — checklist"
"Як провести стратегічну сесію за m9l5 workflow"
```

### Філософія

```
"Чотири причини Аристотеля — приклад для коуч-сесії"
"Дихотомія Епіктета — як обʼяснити клієнту"
"Категоричний імператив Канта — sales ethics"
```

### Ораторське (Денис)

```
"Дай вправу на голос (mcmm-oratorske)"
"11 помилок оратора — checklist перед виступом"
"4 рівні слухання Дениса (m10l4)"
"5-крок ННК Розенберга — у конфліктній комунікації"
```

### Розбір/менторські (Козачкова, Махонін, Волков, Чекальська)

```
"Що Чекальська каже про кортизольний мозок? (m5l7)"
"Pricing discipline Юлин — як ставити ціну"
"AI як другий мозок коуча — capstone m10l6"
"Instagram упаковка коуча — Юлин підхід"
```

---

## Іспит

Перед іспитом — пройди [`EXAM_REHEARSAL.md`](./EXAM_REHEARSAL.md):

- 66 cross-skill питань
- 12 quick-reference tables
- Cover'ить усі 9 disciplines

```bash
# Відкрити в Markdown viewer
glow EXAM_REHEARSAL.md
# або у Claude — попроси: "проведи мене через EXAM_REHEARSAL по 5 Q за раз"
```

---

## Troubleshooting

**Q:** Claude Code не бачить skills після clone?
**A:** Restart Claude Code. Якщо все ще немає — перевір `~/.claude/skills/mcmm/skills/` (має бути nested structure). Або зроби symlinks per-skill (див. Установка вище).

**Q:** Skill активувалась, але дає generic відповідь без verbatim цитат?
**A:** Уточни запит до конкретного lesson (напр. "за m3l2" або "у Махоніна"). Trigger words у `SKILL.md` бувають wide — конкретний lesson дає точнішу відповідь.

**Q:** Хочу додати свої правки/notes до уроку?
**A:** Fork repo → додай файл `notes.md` у `lessons/<lesson>/` → твої personal insights окремо від verbatim бази. Не редагуй verbatim transcripts — це primary source.

**Q:** Як відрізнити Юрієвий synthesis vs verbatim лектора?
**A:** `transcript.txt` = verbatim лектор. `claims.md` = атомарні цитати з attribution. `synthesis.md` = AI-generated consolidated understanding (з hedged-tendency disclaimers). `Personal-insight-Yurii` блоки у synthesis позначені окремо — це Юрієва особиста interpretation з менторських сесій.

---

🤖 Built with Claude Code (Opus 4.7) — repo як живий артефакт MCMM I потоку.
