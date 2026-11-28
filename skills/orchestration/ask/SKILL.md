---
name: ask
description: Clarify intent and resolve ambiguity before implementing anything. Activate whenever the user writes @ask or /ask, asks for ideas or brainstorming, or submits a high-ambiguity request where building immediately risks the wrong scope, format, or direction. Asks concise, crucial multiple-choice questions, states explicit assumptions, and verifies the user's intent in a short summary before execution.
---

# Ask

## Activation and preflight
Use for explicit @ask or /ask, brainstorming/ideation, or high-impact ambiguity in goals, scope, architecture, audience, constraints or format. Do not activate for clear low-risk tasks unless explicitly invoked, or repeat an already confirmed intent. Read available context first. Use the [Gemini Task adapter](adapters/gemini-task.md) only if actual tools exist; otherwise use numbered Markdown questions with lettered options.

## Intake contract
Do not write deliverables, edit files, perform mutating actions or dispatch implementation workers before intent confirmation. Identify crucial unknowns versus defaultable details. Do not ask about facts already available or trivial preferences.

- Ask an adaptive **3 to 8 crucial multiple-choice questions** matched to actual ambiguity: **3–4** for focused unknowns, **5–8** for multi-faceted, architectural, or high-stakes requests. If fewer than 3 genuine unknowns exist (or the prompt is already clear on explicit @ask or /ask), ask only the real blockers (0–2) or skip straight to **Assumptions** and **Intent Check**—never pad with trivial questions to hit a minimum, and never exceed 8.
- Each question has 2–5 concise mutually exclusive options; allow custom responses without redundant Other if the UI already provides free text. For brainstorming, offer concrete strategic directions and trade-offs.
- Gemini Task: 1–3 questions in one native call; 4–8 default to a single numbered Markdown turn, or 4–6 in at most two sequential native batches of ≤3 when preferred or dependent. 7–8 require Markdown. Zero questions skips the widget. Never claim Markdown was a native widget.
- Immediately below questions (or directly if no blockers), list concrete, overrideable defaults under **Assumptions**: scope, format, standards/units and stack as relevant.

## Intent verification
After answers, output a compact **Intent Check**:
- **Goal:** one sentence describing the intended result.
- **Key Choices:** selections and hard constraints.
- **Assumptions:** remaining defaults.
- **Deliverable:** exact format and scope.

Ask for confirmation or adjustments. Begin implementation only after confirmation, or explicit permission to proceed with disclosed defaults. If explicit Ask is invoked on an already clear request, present assumptions and the Intent Check for one-turn confirmation.

## Gates and recovery
PASS requires zero premature implementation, genuinely crucial concise questions, explicit non-blocking assumptions and clear Intent Check. Critical defects: implementation with unresolved high-impact ambiguity, more than 8 questions, padding, essay questions when choices fit, silent assumptions, verbose preambles or repeating the request.

If the user says “just go ahead” or “you decide,” lock disclosed defaults and proceed. For partial answers default secondary choices, disclose them, and cap clarification at 1–2 rounds unless a hard blocker remains. Never loop or interrogate. Three sharp questions beat eight mediocre ones.

When composing, run Ask first and pass verified intent into downstream skills. When standalone, ask at most two Estimate intake questions total (not two rounds). When `ask` is co-selected, Ask owns upfront clarification under its adaptive 3–8 question budget, including at most two Estimate-critical questions (e.g., VAT and permits); finish its Intent Check before implementation or worker dispatch, reuse every confirmed answer verbatim and cap remaining Estimate follow-ups at `max(0, 2 - estimate_questions_already_asked)`. Never repeat answered questions or bypass confirmation.

See [evaluation scenarios](evaluations/SCENARIOS.md).
