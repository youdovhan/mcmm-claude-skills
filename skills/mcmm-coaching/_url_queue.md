# MCMM Coaching — URL Queue (updated 2026-05-20 12:15)

**Status legend:** ⬜ pending · 🔄 in-progress · 🎬 mcmm.creo recon done (YT URL extracted) · 🎙️ audio downloaded · 📝 whisper running · ✅ transcribed · ⚠️ BLOCKED

**RAM-safe:** 1 whisper-cli max at a time (per `feedback_heavy_bg_ram_safety.md`).
**Anti-hallucination flags:** `--max-context 0 --suppress-nst`.
**Model:** `/Users/detective/Claude-assets/meetings/models/ggml-large-v3-turbo.bin` (1.5GB) — НЕ `/Users/detective/.whisper-models/ggml-large-v3-turbo.bin` (corrupt, 178MB).
**Format:** input must be WAV 16kHz mono (ffmpeg convert from M4A first).

## Tier 1 — CORE for AI-стек coach speech (Conference 23-24.05.2026)

| #   | Slug                         | YT URL                                      | Status               |
| --- | ---------------------------- | ------------------------------------------- | -------------------- |
| 1   | m1l2-self-discovery          | https://www.youtube.com/watch?v=D7gAfcwI58M | 📝 whisper running   |
| 2   | m1l4-icf-competencies        | https://www.youtube.com/watch?v=ubR9rKdl-jI | 🎙️ WAV ready         |
| 3   | m2l3-coaching-thinking       | https://www.youtube.com/watch?v=YTr0ukf_HJQ | 🎬 (downloading m4a) |
| 4   | m3l2-active-listening        | https://www.youtube.com/watch?v=VE3xT5IKlD0 | 🎬 (downloading m4a) |
| 5   | m3l4-presence                | https://www.youtube.com/watch?v=qZImBRL3Y5Y | 🎬                   |
| -   | m2l1-coaching-process (Юлія) | https://www.youtube.com/watch?v=OG5n87kJGiE | 🎬                   |

## Tier 2 — рамка для presentations

| #   | Slug                            | YT URL                                      | Status |
| --- | ------------------------------- | ------------------------------------------- | ------ |
| 6   | m4l2-competency-7-awareness     | https://www.youtube.com/watch?v=FJocAB7NELY | 🎬     |
| 7   | m4l4-competency-8-client-growth | https://www.youtube.com/watch?v=xwdi5PgcbiQ | 🎬     |
| 8   | m5l4-coach-inner-position       | https://www.youtube.com/watch?v=5QUsvUAsdv4 | 🎬     |
| 9   | m9l2-mentor-coach-figure        | https://www.youtube.com/watch?v=IIaHEgblSfE | 🎬     |

## Tier 3 — depth

| #   | Slug                          | YT URL                                      | Status                                                      |
| --- | ----------------------------- | ------------------------------------------- | ----------------------------------------------------------- |
| 10  | m6l2-professional-map         | https://www.youtube.com/watch?v=iAvPoOtuIss | 🎬                                                          |
| 11  | m6l4-coach-awareness          | https://www.youtube.com/watch?v=5IH7PV0cr5k | 🎬                                                          |
| 12  | m7l4-client-states-patterns   | https://www.youtube.com/watch?v=MSsSoMymaLY | 🎬                                                          |
| 13  | m8l4-stoic-endurance          | https://www.youtube.com/watch?v=0JQNVOETH5g | 🎬                                                          |
| 14  | m9l4-mentor-coach-practice-2  | https://www.youtube.com/watch?v=JDiyXx41T5E | 🎬                                                          |
| 15  | m10l1-path-to-mastery         | -                                           | ⚠️ BLOCKED: video not embedded on platform (future lecture) |
| 16  | m10l3-final-coaching-sessions | -                                           | ⚠️ BLOCKED: video not embedded on platform                  |
| 17  | m10l4-art-of-listening        | -                                           | ⚠️ BLOCKED: video not embedded on platform                  |

## Notes for next session

- Тригерні слова Юрія для коучингу — пов'язано з виступом 23-24.05 на конференції MCMM
- Основний лектор: **Олексій Махонін** — НЕ extrapolate credentials, ВЕРИФІКУЙ self-intro у transcript first 30-50 рядків!
- Також лектори: **Юлія Козачкова** (менторські M2L1)
- Per memory `feedback_lecturer_attribution_per_lesson.md` — атрибуція ЛЕКТОРА PER LESSON, не extrapolate
- 15/18 YT URLs готові; 3 M10 lessons BLOCKED — пости поки не залиті
- Перевірити M10 після Conference (24.05)

## Resume command для наступної сесії

Whisper running у background для m1l2. Перевір `ps aux | grep whisper`. Якщо завершено — `transcript-cleanup.py` + наступний lesson.

```bash
# Перевірити запущений whisper
ps aux | grep whisper-cli | grep -v grep

# Якщо завершено — cleanup і перейти на m1l4
python3 /Users/detective/Claude/transcript-cleanup.py \
  /Users/detective/.claude/skills/mcmm-coaching/lessons/m1l2-self-discovery/raw/transcript.txt \
  /Users/detective/.claude/skills/mcmm-coaching/lessons/m1l2-self-discovery/raw/transcript.srt
mv /Users/detective/.claude/skills/mcmm-coaching/lessons/m1l2-self-discovery/raw/transcript.txt \
   /Users/detective/.claude/skills/mcmm-coaching/lessons/m1l2-self-discovery/transcript.txt

# М1L4 — WAV вже готовий
mkdir -p /Users/detective/.claude/skills/mcmm-coaching/lessons/m1l4-icf-competencies/raw
whisper-cli -m /Users/detective/Claude-assets/meetings/models/ggml-large-v3-turbo.bin \
  -l ru --output-txt --output-srt --max-context 0 --suppress-nst \
  -of /Users/detective/.claude/skills/mcmm-coaching/lessons/m1l4-icf-competencies/raw/transcript \
  /tmp/mcmm-coaching/audio/m1l4-icf-competencies.wav
```

## Base URL

`https://mcmm.creo.ua/courses/mcmm-i-potik-b5e6d16c-62a7-4f2a-a90e-0ceded3c6938`
