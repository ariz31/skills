# Gemini Task adapter: Ask

Use these mappings only when the actual tool interface exposes them. Do not invent tools or parameter schemas; inspect available signatures and adapt accordingly.

## Two-tier dispatch for the `ask_question` 3-question cap

Gemini Task's `ask_question` tool enforces a hard limit of **at most 3 questions per call** (2 to 5 mutually exclusive options each; omit `"Other"` because free-text input is provided automatically). Select the dispatch tier from the actual question count:

| Tier / Question Count | Gemini Task mapping |
|---|---|
| **0 questions** (explicit `@ask`/`/ask` on already-clear prompt) | Skip `ask_question`; output **Assumptions** + **Intent Check** directly in chat for one-turn confirmation. |
| **Tier 1: 1 to 3 questions** | Call `ask_question` once (1–3 questions, 2–5 options each, omit `"Other"`, set `is_multi_select: true` where multiple choices apply). After answers return, output **Assumptions** + **Intent Check** in chat before any implementation. |
| **Tier 2A: 4 to 8 questions (Default — Single Markdown Turn)** | Present all 4–8 numbered questions (each with 2–5 lettered options `a–e`) plus the **Assumptions** block in one concise Markdown chat message so the user can reply in a single turn (e.g., `1a, 2c, 3b, 4a, 5d`). Never call `ask_question` with >3 questions, and never claim a native widget was used. |
| **Tier 2B: 4 to 6 questions (Sequential `ask_question` Batches)** | Use only when the user prefers interactive widgets or Round 1 answers unlock Round 2 questions: dispatch **at most 2 sequential `ask_question` calls** of `<=3` questions each (`<=6` questions total, e.g., `3+3`), waiting for answers between calls before emitting **Assumptions** + **Intent Check** (strictly honoring `ask/SKILL.md:87,94`'s 2-round clarification cap). For **7–8 questions**, **Tier 2A (single Markdown turn) is required**. |
| **Assumptions & Intent Check** | Concise Markdown response in chat (always required before mutating or implementation tool calls). |

If `ask_question` is unavailable on the current session, fall back to Tier 2A (clean numbered Markdown questions with lettered options) for any count from 1 to 8.
