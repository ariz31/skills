# Gemini Task adapter: Ask

Use these mappings only when the actual tool interface exposes them. Do not invent tools or parameter schemas; inspect available signatures and adapt accordingly.

| Portable operation | Gemini Task tool |
|---|---|
| Present 1 to 3 structured multiple-choice questions | `ask_question` (1 to 3 questions, 2 to 5 options each, omit "Other" since free text is automatic) |
| Present assumptions and Intent Check summary | Concise Markdown response in chat |

When `ask_question` is available, use it for the crucial multiple-choice questions (keeping option labels short and mutually exclusive), and follow up with the **Assumptions** and **Intent Check** summary once answers return before executing any implementation or mutating tool calls. If `ask_question` is unavailable, fall back to clean multiple-choice options in plain chat text.
