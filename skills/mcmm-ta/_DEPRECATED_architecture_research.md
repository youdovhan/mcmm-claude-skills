# Research: Architecture for Full-Course MCMM Knowledge System

> Research date: 2026-05-19. Sources: Anthropic official docs (code.claude.com), Anthropic's `skill-creator` skill, Hedgineer case study, community articles, peer-reviewed papers on RAG personas and digital clones, RAG failure-mode literature.

> ⚠️ **CORRECTION 2026-05-19 (post-creation):** This document's persona-architecture examples below use `lecturer-isaienko` / "Світлана Ісаєнко" as the lecturer for TA — this is **INCORRECT**. Ісаєнко teaches Psychiatry only. TA lecturer is **Влада Березянська**. The persona pattern itself is valid; only the example name needs swapping. Also note: per Yurii's directive (2026-05-19) persona sub-agents are **deferred to Phase 2+** — not Phase 1. Phase 1 = discipline skills + Obsidian dossiers only. Current research kept for future reference.
>
> **UPDATE 2026-05-19:** Прізвище = Березянська, credentials per M1L3 line 99-114 (КН, EATA, USATAA, CTA — see `course_overview.md` Lecturer section for verbatim).

---

## TL;DR Recommendation

Build the course as **one skill per discipline** (≈7 skills), each following the existing `mcmm-psychiatry` pattern — this matches Anthropic's official guidance to "graduate to an index-plus-references composition when exceeding roughly 500 lines or 5,000 tokens for SKILL.md, or when multiple skills need to share reference material." Each discipline skill keeps its own `lessons/`, `symptom_atlas.md`, `claims.md` and coaching auto-trigger table. **Do not** build one mega-skill for the whole MCMM — at 60+ lessons and 7 disciplines, a single SKILL.md description would be truncated by the 1,536-character cap and the body would blow past the 500-line ceiling.

For lecturer personas and student dossiers, use **subagents, not skills**. The two primitives have a clean division of labor in Claude Code's official docs: skills are "knowledge that runs in the same context window as the current conversation"; subagents "run in their own context window with a custom system prompt … and return only the summary." A "what would Светлана Ісаєнко say?" question is fundamentally a separate-context task with its own persona system prompt — exactly the use case Anthropic documents for subagents. The subagent then `skills`-preloads the relevant discipline knowledge skill at startup, so the persona reasons from the lecturer's actual material. Student dossiers stay in Obsidian as one-file-per-person markdown — this is the dominant community pattern (Hedgineer, mindstudio, ericmjl, breadcrumbs) and aligns with the existing `ObsidianVault/People/` structure. Keep knowledge IN Obsidian, treat skills as **thin routers that point into the vault for syntheses and claims**, but keep one immutable copy of canonical transcripts inside the skill (for reproducibility — vault notes drift).

---

## A. Skill Architecture

### Official position from Anthropic

The `code.claude.com/docs/en/skills` page sets these hard constraints:

- **Description budget**: "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage." All skill names are always loaded; descriptions for least-used skills are dropped first when the listing budget (1% of context window by default) overflows.
- **SKILL.md ceiling**: "Keep SKILL.md under 500 lines. Move detailed reference material to separate files."
- **Lifecycle**: "When you or Claude invoke a skill, the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session." After auto-compaction, re-attached skills share a 25,000-token budget, "starting from the most recently invoked skill, so older skills can be dropped entirely after compaction if you have invoked many in one session."

This rules out a single `mcmm` mega-skill for 7 disciplines and 60+ lessons.

### When to split

Anthropic's own `skill-creator` skill (the canonical authoring guide) recommends the **"index-plus-references" pattern**: SKILL.md is the small entry point, and detail lives in subfolders Claude loads on demand:

```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

The Carlos Perez Medium synthesis of Anthropic guidance puts the threshold as: _"Skills graduate to an index-plus-references composition when exceeding roughly five hundred lines or five thousand tokens for SKILL.md, or when multiple skills need to share reference material."_

### Discipline-as-skill is the right grain

Hedgineer's company-wide deployment at scale organized skills into **seven domain-based verticals** (`ai`, `analytics`, `business`, `data-platform`, `infrastructure`, `research`, `ui`). Yurii's domain decomposes almost identically: ~7 disciplines (Coaching, TA, NLP, Philosophy, Mentorship, Marketing, Public Speaking, Business Strategy, Psychiatry). The 1:1 mapping is not a coincidence — domain boundaries are the natural skill boundaries because they correspond to **how the model needs to route**: a client describing a script pattern triggers TA; a client describing voice-quality anxiety triggers Public Speaking. Mixed disciplines are rare; cross-cutting belongs in the coaching auto-trigger tables, not in the skill body.

### Composing skills

Claude Code skills do not "call each other" the way functions do. Cross-references are by **markdown link** — Claude follows them on read, which means an mcmm-psychiatry claim like "see also TA injunctions on `not exist`" should be a link to `~/.claude/skills/mcmm-ta/lessons/03-injunctions/claims.md`, not a copy of the content. This eliminates the "synchronize across skills" problem that Hedgineer specifically warns about: _"every skill has exactly one canonical source."_ Skill bodies become routers; cross-cutting truth lives in one place per concept.

### Description writing for auto-trigger

Anthropic's own `skill-creator` is explicit: write **"pushy"** descriptions:

> "Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data."

Existing `mcmm-psychiatry` already does this well. Three traps to avoid that the docs surface:

1. **Description truncation** — at 1,536 chars combined `description + when_to_use`, "put the key use case first."
2. **Many similar skills compete for listing budget** — at 7 mcmm-_ skills, the listing should be fine (1% of a 1M-context Opus = ~10,000 chars, plenty for 7 × 1,536). But if you ever add 50 mcmm-_ skills (per-lecturer, per-lesson), you'll hit the cap and the model will lose visibility into them. **Avoid creating skills at lesson granularity.**
3. **Overlapping trigger phrases** — if `mcmm-ta` and `mcmm-coaching` both say "drama triangle," the model will guess wrong. Specialize triggers per discipline.

### Skills vs subagents — the dividing line

From the Claude Code docs (`/docs/en/skills`, end of page): _"Consider Skills instead when you want reusable prompts or workflows that run in the main conversation context rather than isolated subagent context."_ And from `/docs/en/sub-agents`: _"Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again."_

Translation for MCMM:

| Use                                                                        | Use a skill               | Use a subagent            |
| -------------------------------------------------------------------------- | ------------------------- | ------------------------- |
| Quick "what does ТА say about X" lookup mid-coaching session               | ✅                        | ✗ (overkill, breaks flow) |
| "Talk to Светлана as persona for 10 turns"                                 | ✗ (pollutes main context) | ✅                        |
| Cross-discipline synthesis ("compare TA injunctions to NLP meta-programs") | ✅ (read both)            | ✗                         |
| Quiz Yurii on full MCMM curriculum                                         | ✗                         | ✅ (long, isolated)       |
| Auto-trigger when client says "сценарій" in a session                      | ✅                        | ✗                         |

The **`skills` frontmatter field on a subagent** is the bridge: a `lecturer-isaienko` subagent declares `skills: [mcmm-coaching, mcmm-psychiatry]` and Claude Code "injects the full skill content into the subagent's context at startup."

---

## B. Persona Patterns

### Sub-agents are the right primitive for lecturer personas

The Claude Code subagents docs explicitly support this: _"Each subagent runs in its own context window with a custom system prompt … Subagents help you specialize behavior with focused system prompts for specific domains."_ The example "data scientist" subagent (in the docs) shows the same template Yurii needs — opening line "You are a [role specializing in X]" followed by behavioral protocol.

Concrete structure for each lecturer (one file per persona at `.claude/agents/lecturer-<surname>.md`):

```yaml
---
name: lecturer-berezianska
description: Влада Березянська — speak as her on TA topics. Use when Yurii asks "what would Влада say about this client case?", needs feedback in her voice, or wants her perspective on a TA-coaching dilemma.
model: opus
skills:
  - mcmm-ta
memory: user
---
You are Влада Березянська, a TA lecturer in the MCMM coaching program (кандидат наук, EATA + американська TA-асоціація, європейський CTA — per M1L3 line 99-114 self-intro)...
[knowledge constraints, hedging rules, style guide here]
```

The `memory: user` flag (per Claude Code docs) gives each persona a `~/.claude/agent-memory/lecturer-berezianska/` directory where she accumulates "feedback she's given Yurii's classmates over time" — this is the **dossier-bridge**: the lecturer remembers per-student feedback across sessions.

### Knowledge vs style separation

The PersonaAI paper (arXiv:2503.15489) is honest about a major limitation: their system "doesn't explicitly separate semantic knowledge from linguistic patterns. Instead, it embeds all user data uniformly … treats writing samples and factual information identically." This is exactly the failure mode to avoid for Yurii.

The cleaner separation pattern that emerged across sources:

1. **Style** → lives in the subagent's **system prompt** (markdown body). 50-200 lines of "she talks in metaphors of fishing; she rarely uses jargon; her favorite frame is 'клієнт вже знає відповідь, просто не дозволяє собі її почути.'"
2. **Knowledge** → lives in **preloaded skills** (her lectures, transcripts, claims). Retrieved deterministically by file read, not embedding similarity.
3. **Out-of-distribution hedge** → **explicit prompt rule**: "If the question is about a topic I have not lectured on (check my preloaded materials), I MUST say 'я цього не торкалася в лекціях, але як коуч я б подумала про…' and switch to general coaching frame." This mirrors the PersonaAI paper's "I DO NOT KNOW" pattern.

### Anthropic's official "stay in character" guidance

The Anthropic API docs page **"Keep Claude in character with role prompting and prefilling"** (platform.claude.com) recommends two things for persona reliability: (a) put the role definition in the system prompt, not in user turns; (b) use prefill ("Світлана: ") to anchor the voice. Both work in subagent definitions.

### Anti-pattern from voice-cloning literature

The "Digital Doppelgangers" paper (arXiv:2502.21248) is direct about the ethics with **living** experts: _"unauthorized divergence — the source person loses control when their clone generates novel responses, makes independent decisions that differ from their original intent."_ Two practical mitigations for Yurii's case:

1. **No public-facing persona output**. Treat lecturer personas as **internal mirrors** for Yurii's own study, not as content he publishes ("Світлана сказала…"). The personas help him think; they don't speak.
2. **Watermark the output**. Every lecturer-persona reply should end with a footer: _"Це симуляція думки [Викладач] на основі її лекцій MCMM. Реальна [Викладач] цього не казала."_ This protects against "puppet" confusion if a screenshot ever leaks.

---

## C. Student Dossier

### Pattern (well-attested across sources)

One file per person in the existing Obsidian vault structure:

```
ObsidianVault/People/
  Clients MOC.md          # index
  yurii-dovhan.md         # Yurii's own dossier
  classmate-X.md          # peers from MCMM cohort
  ...
```

Each file has YAML frontmatter (role, cohort, status) + standard sections (background, themes, lecturer-feedback-received, sessions-with-Yurii, current-edge). The MindStudio AI-CRM article describes this exact pattern: _"plain text … queryable via natural language through AI agents, with no database, no SaaS subscription, and no import/export friction."_

### Privacy considerations (this is the section Yurii needs to think about most)

The MindStudio article notes: _"The article does not address privacy concerns regarding storing third-party contact information."_ The literature on AI personas of living people (arXiv:2502.21248) is much stricter. Translation for the MCMM classmate dossier:

1. **Consent**: Classmates have not consented to being modeled in an AI system. Storing **facts** they shared in class (their stated theme, where they live, who their kids are) is one thing — that's just memory. Storing **inferences** about them, especially psychiatric or psychological speculation, is a different category. The CLAUDE.md "no esoteric" rule + the "AI helper not AI copy" rule already imply this; make it explicit for classmates.
2. **No classmate personas**. Build subagent personas only for **lecturers**, not for classmates. Lecturers are public figures of the course speaking in a teaching capacity; classmates are private students.
3. **Encryption-at-rest is not the issue; access boundary is**. The Obsidian vault is local-only. The exposure surface is: (a) Yurii's own publishing accidents (e.g. screenshotting a session that includes a classmate dossier), (b) backup leaks. Mitigate by **not synchronizing the `People/Clients MOC.md` subtree to any cloud** (currently fine — Obsidian local). Add a CLAUDE.md rule: skills must never output third-party classmate names or distinguishing details to a public surface (post, deck, landing, screenshot for Telegram).
4. **Right to be forgotten**. Add a manual purge process: if a classmate asks to be removed, `rm People/<classmate>.md` is sufficient because nothing else has retrieved them by embedding.

### Storage: Obsidian vs Notion vs custom JSON

Obsidian is the right choice and it's already there. Three reasons attested in the sources:

1. **"Plain text proved prescient for AI integration"** (ericmjl.github.io) — Markdown is what skills already read.
2. **No vendor lock-in** — same article: _"if you switch AI tools next year, your CRM comes with you."_
3. **The existing `mcmm-psychiatry` skill already reads from filesystem paths.** Adding `~/ObsidianVault/People/<name>.md` to a skill's reference list costs nothing.

**Do not** put classmate data in Notion. Notion is the **publishing surface** in Yurii's existing infra (per `feedback_notion_default_review_surface.md`), and publishing surfaces are the wrong place for private third-party records.

---

## D. Knowledge Corpus as Graph

The most consequential architectural question. The current `mcmm-psychiatry` is 4.7GB — **most of that is raw transcript and media**, not synthesized claims.

### Three options, evaluated

| Option                        | What lives where                                                                                                                 | Pros                                                                                    | Cons                                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **A. All in skill** (current) | Transcripts + syntheses + claims in `~/.claude/skills/mcmm-X/`                                                                   | Reproducible, self-contained, distributable as plugin                                   | Duplicates claims across skills if cross-cutting; bloats backup; hard to link to from Obsidian                   |
| **B. All in Obsidian**        | Knowledge in vault; skill is a 200-line router pointing at vault paths                                                           | Single source of truth, native links, AUTO-WRITE/recall already wired                   | Skill needs read access to vault (already true); if vault path changes everything breaks; not portable as plugin |
| **C. Hybrid (recommended)**   | Canonical immutable transcripts in skill; running syntheses + atomic claims in vault Knowledge tree; skill body links into vault | Reproducibility + living understanding; matches existing pipeline in CLAUDE.md rule #20 | More moving parts; need conventions for what lives where                                                         |

### Recommended split (C)

```
~/.claude/skills/mcmm-<discipline>/
├── SKILL.md                    # < 500 lines, router + auto-trigger table
├── course_overview.md          # frozen overview, ~ 1 lesson summary each
├── learning_protocol.md        # how Yurii is studying this
├── lessons/
│   └── NN-slug/
│       ├── transcript.md       # IMMUTABLE — verbatim source
│       └── flashcards.md       # for self-quiz (small, in-skill)
├── coaching/
│   └── auto_trigger_table.md   # client marker → lesson → intervention
└── _index.md                   # pointers into vault for living content

~/ObsidianVault/Knowledge/
├── Sources/src-mcmm-<discipline>-<lesson>/  # quality-scored conspect
├── Claims/c-NNNN.md            # atomic claims (cross-skill)
├── Syntheses/syn-<topic>.md    # running understanding
└── Verdicts/v-slug.md          # applied → linked back from skill auto-trigger
```

This mirrors what already exists in CLAUDE.md rule #20 (research pipeline). The skill is the **frozen teaching layer** (lecture-as-given); the vault is the **living synthesis layer** (what Yurii has done with it).

### Zettelkasten + AI literature backs this split

The codewithseb.com piece on Obsidian + Claude is explicit: knowledge stays in vault, AI agent traverses; the value of atomic notes is that each is **one concept linkable from many places**. The Zettelkasten-MCP project demonstrates the same: _"link-aware retrieval that expands search results by traversing the knowledge graph."_ For MCMM, this means: an injunction claim (`c-0042.md` "Not Exist") gets linked from `mcmm-ta/lessons/03-injunctions`, `mcmm-psychiatry/lessons/08-borderline`, AND `mcmm-coaching/lessons/02-life-positions` — three skills, one canonical source.

### What goes in the skill body vs vault note

Rule of thumb:

- **In skill**: source-of-truth transcripts, the auto-trigger table (because the table needs to be in-context for the model to route), the learning_protocol (how-to instructions only Yurii uses).
- **In vault**: claims (atomic), syntheses (Yurii's mental model — drifts over time), contradictions log, applied verdicts.
- **In both via link**: the skill's `lessons/NN/claims.md` is a short index that lists claim IDs; each ID resolves to `~/ObsidianVault/Knowledge/Claims/c-NNNN.md`.

---

## E. Anti-patterns / What NOT to Do

### 1. Don't build a skill per lecturer at 100k tokens each

A `lecturer-isaienko` skill at 100k tokens of her transcripts would (a) blow the 5k SKILL.md ceiling fast, (b) load every time Claude auto-matches "Світлана," polluting context. The right move is one **persona subagent per lecturer** that preloads the **already-built discipline skill**.

### 2. Don't trust RAG over the corpus without grounding rules

The "RAG Isn't Accuracy: 8 Confident Failure Modes" piece (Medium / ThinkingLoop) is the cautionary reading. For an "authoritative MCMM expert" system, mode #4 ("False Confidence from Context") is the deadly one: _"RAG does not just affect correctness. It affects how wrongness feels."_ Concrete mitigation:

- Every persona reply that paraphrases a lecturer **must** cite the lesson file (`lessons/03-injunctions/transcript.md:142`).
- If no citation is possible, the persona must hedge: "я цього не пам'ятаю з лекцій."
- This is also a `read-as-client` guard (CLAUDE.md golden rule) — Yurii's clients in coaching sessions should never get a quote attributed to a lecturer that was actually invented.

### 3. Don't let chunking deletes context

RAG failure mode #5 (Medium / ThinkingLoop) — for psychotherapy material in particular, "rule X applies, EXCEPT in case Y" is the norm (e.g. "borderline structure, EXCEPT in attachment-trauma profile"). If you chunk the transcript and retrieve only chunk-1, you lose the exception. Mitigation: **don't chunk transcripts**. Read whole lesson files. Modern Opus 4.7 1M context lets a lecturer subagent preload an entire discipline.

### 4. Knowledge decay is real and silent

ragaboutit.com on "knowledge decay": _"enterprises monitor retrieval speed and accuracy but ignore staleness metrics entirely — creating dangerous invisibility."_ For MCMM specifically, the course evolves (new lectures every season); the symptom_atlas and coaching auto-trigger table need a "last-updated" footer per skill and a quarterly review. Add to CLAUDE.md or to the discipline-level `_index.md`: `last_audit: YYYY-MM-DD; next_audit: +90d`.

### 5. Don't let persona divergence go unflagged

"Digital Doppelgangers" arXiv:2502.21248: _"unauthorized divergence … if a clone engages in behaviors that differ from the original person's intent, does it remain an accurate representation?"_ This is why every persona reply needs the simulation watermark (see §B). The reply _is_ a divergence by construction — Yurii is asking the model to extrapolate from her lectures to a new client case. The watermark keeps that explicit.

### 6. Don't create "lesson skills" or "concept skills"

Tempting to make `mcmm-ta-life-positions` a skill. Don't. Three reasons:

- It will overlap-trigger with `mcmm-ta` itself, causing routing ambiguity.
- It blows the listing budget if scaled to 60+ lessons.
- It moves canonical truth out of the lesson file into a different layer (against Hedgineer's "one canonical source" rule).

Lessons are **files inside discipline skills**, not skills themselves.

---

## Cited Sources

1. [Extend Claude with skills — Claude Code official docs](https://code.claude.com/docs/en/skills) — primary reference for ceilings, frontmatter, lifecycle.
2. [Create custom subagents — Claude Code official docs](https://code.claude.com/docs/en/sub-agents) — primary reference for subagent design, `skills` preload, memory.
3. [Anthropic skill-creator skill (GitHub)](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) — canonical authoring guide, anti-patterns, description optimization.
4. [Skills (Anthropic blog announcement)](https://claude.com/blog/skills) — official framing.
5. [How we built a Company-Wide knowledge layer with Claude Skills (Hedgineer)](https://www.hedgineer.io/content/claude-skills-knowledge-layer/) — real production case study with 7 verticals.
6. [Claude Code Skills Architecture: 4 Layers That Keep Your AI Agent Fast and Focused (MindStudio)](https://www.mindstudio.ai/blog/claude-code-skills-architecture-progressive-context-loading) — progressive disclosure layers.
7. [Structuring Agents, Skills, and MCPs: Best Practices from Anthropic (Carlos Perez, Medium)](https://medium.com/intuitionmachine/structuring-agents-skills-and-mcps-best-practices-from-anthropic-9312849ccea6) — granularity thresholds, monolithic-vs-index pattern.
8. [PersonaAI: Leveraging RAG and Personalized Context for AI-Driven Digital Avatars (arXiv:2503.15489)](https://arxiv.org/html/2503.15489v1) — RAG persona system; hedging via "I DO NOT KNOW"; honest about knowledge/style not being separated.
9. [Digital Doppelgangers: Ethical and Societal Implications of Pre-Mortem AI Clones (arXiv:2502.21248)](https://arxiv.org/html/2502.21248v1) — consent and divergence for living-person clones.
10. [The AI-Powered Zettelkasten: Combining Obsidian's Linking with Claude's Reasoning (Code With Seb)](https://www.codewithseb.com/blog/ai-zettelkasten-obsidian-claude-knowledge-graph) — Obsidian + Claude knowledge-graph pattern.
11. [Mastering Personal Knowledge Management with Obsidian and AI (ericmjl)](https://ericmjl.github.io/blog/2026/3/6/mastering-personal-knowledge-management-with-obsidian-and-ai/) — vault as source of truth, skills encode workflows.
12. [Build an AI CRM in Obsidian: Named Markdown Files (MindStudio)](https://www.mindstudio.ai/blog/ai-crm-obsidian-markdown-codex-contact-management) — one-file-per-person dossier pattern.
13. [RAG Isn't Accuracy: 8 Confident Failure Modes (ThinkingLoop, Medium)](https://medium.com/@ThinkingLoop/rag-isnt-accuracy-8-confident-failure-modes-568cfe855694) — failure modes for expert-clone systems.
14. [The Knowledge Decay Problem: How to Build RAG Systems That Stay Fresh at Scale](https://ragaboutit.com/the-knowledge-decay-problem-how-to-build-rag-systems-that-stay-fresh-at-scale/) — staleness as silent debt.
15. [A Mental Model for Claude Code: Skills, Subagents, and Plugins (Dean Blank, Level Up Coding)](https://levelup.gitconnected.com/a-mental-model-for-claude-code-skills-subagents-and-plugins-3dea9924bf05) — knowledge-vs-worker split heuristic.
16. [Keep Claude in character with role prompting and prefilling (Anthropic API docs)](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/keep-claude-in-character) — official persona-stability guidance.

---

## Open Questions for Yurii (decide before building)

1. **Persona scope**: lecturers only (recommended), or do you want personas for **classmates** too? Privacy literature says no for classmates; only build personas for **public-teaching figures** who appeared in the course in a teaching role. Confirm.

2. **Persona output policy**: are lecturer-persona replies for your **internal study only**, or do you intend to ever paraphrase them in coaching with clients ("як казала Світлана…")? If the latter, every reply must cite a verifiable lesson timestamp — and arguably you should ask the lecturer's permission to attribute publicly.

3. **Cohort-mate dossier policy**: do you actually need classmate dossiers in this system at all, or are they nice-to-have? If yes — write the privacy guard in CLAUDE.md before building (no auto-publish of any path under `People/Clients MOC.md` or `People/classmates/`).

4. **Where does living synthesis live**: option C (hybrid) is recommended, but it requires you to be disciplined about `Claims/` being the home for atomic claims across skills. If you'd rather keep it all in skills (option A), accept the duplication tax. Decide once, document in CLAUDE.md.

5. **Lecturer corpus completeness**: for which 3-4 lecturers do you have **enough material** (≥10 hours of lectures, transcribed) to build a defensible persona? Don't build a persona for a lecturer with only 1-2 lessons captured — the hedge rate would exceed the signal rate.

6. **Persona model choice**: opus for slow, expensive, careful persona replies vs sonnet for cheaper. Recommend opus for personas (they reason about nuanced cases), inherit for the discipline-skill auto-triggers (lighter lookups).

7. **Plugin packaging**: do you ever want to ship `mcmm-*` as installable plugins to share with anyone (cohort-mate, a future student)? If yes, build with the directory layout the Plugins doc requires from day one; if no, keep it local in `~/.claude/skills/`.

8. **Quarterly audit cadence**: add a scheduled task / cron to surface "last audit > 90 days" per skill so knowledge decay doesn't silently rot the corpus.
