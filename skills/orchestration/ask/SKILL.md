---
name: ask
description: Clarify intent and resolve ambiguity before implementing anything. Activate whenever the user writes @ask or /ask, asks for ideas or brainstorming, or submits a high-ambiguity request where building immediately risks the wrong scope, format, or direction. Asks concise, crucial multiple-choice questions, states explicit assumptions, and verifies the user's intent in a short summary before execution.
---

# Ask

Clarify intent, eliminate ambiguity, and align on scope before doing any implementation.

## When to Use

- The user includes `@ask` or `/ask` anywhere in the prompt.
- The user is asking for ideas, brainstorming, or exploring directions before committing to a build.
- The request has high ambiguity where critical decisions (goal, audience, scope, constraints, or deliverable format) would materially change the output.
- A complex task is about to trigger heavy work (such as multi-file generation, code changes, or `delegate`) and key requirements are still unstated.

## When Not to Use

- The request is clear, unambiguous, and low-risk (for example, a direct factual lookup or a fully specified single-step task) and the user did not invoke `@ask` or `/ask`.
- The user already confirmed the intent summary and told you to proceed with implementation.

## Capability Preflight

Check whether the host provides a native structured multiple-choice questioning tool. On Gemini Task, use [its adapter](adapters/gemini-task.md) when `ask_question` is available. On any other host, present clean multiple-choice options in plain Markdown text and let the user reply with option letters, numbers, or custom text. Never claim to have used a native prompt widget if none is available.

## Inputs, Constraints, and Outputs

- **Inputs:** The user's raw request plus any immediately available context (project files, prior messages, or workspace records that resolve trivial facts without bothering the user).
- **Hard Constraint:** Do not write deliverables, modify files, run mutating actions, or spawn implementation workers until the user confirms intent.
- **Outputs:**
  1. One short clarification turn containing only crucial multiple-choice questions and explicit assumptions.
  2. A concise **Intent Verification** summary listing what the user wants before starting implementation.

## Workflow

### 1. Triage Ambiguity Quickly

- Read available context first so you never ask for facts you can already verify.
- Separate **crucial unknowns** (decisions that change architecture, scope, audience, or format) from **defaultable details** (minor styling, naming, or secondary layout choices).
- Assume everything that can be safely assumed. Do not ask about minor preferences.

### 2. Ask Concise, Crucial Multiple-Choice Questions

- Keep the entire clarification message short and scannable.
- Ask an adaptive **3 to 8 crucial multiple-choice questions**: **3–4** for focused unknowns, **5–8** for multifaceted or high-stakes requests. If fewer than 3 genuine unknowns exist, ask only the real blockers (0–2) or skip to Assumptions and Intent Check. Never pad or exceed 8.
- Format each question as **2 to 5 mutually exclusive multiple-choice options**, phrased concisely as direct choices.
- Always allow the user to type a custom answer without padding the list with a redundant "Other" bullet when the UI already provides free text.
- If the user is asking for ideas (`@ask` or brainstorming), frame the multiple-choice options around concrete strategic directions or trade-offs rather than open-ended blanks.

### 3. State Explicit Assumptions Up Front

- Immediately below the questions (or before executing if no blocking questions remain), list every assumption you plan to make in a short **Assumptions** block.
- Make each assumption concrete and easy to override in one line (for example, target format, scope boundary, units/standards, or default stack).

### 4. Verify User Intent Before Implementation

- After the user answers (or at the end of the clarification step when only confirmation is needed), output a tight **Intent Check** block listing:

  - **Goal:** One sentence stating what will be built or produced.
  - **Key Choices:** The user's selected options and hard constraints.
  - **Assumptions:** Any defaults that remain active.
  - **Deliverable:** Exact output format and scope.

- End with a direct confirmation prompt (for example, "Confirm to proceed, or tell me what to adjust.").
- Begin implementation only after the user confirms (or explicitly says to go ahead with your defaults).
- If the user's request is already completely clear except for `@ask` being invoked explicitly, skip redundant questions, state your assumptions, and present the **Intent Check** block for a fast one-turn confirmation.

## Quality Gate and Critical Defects

A turn passes only when all criteria hold:

- Zero premature implementation, file edits, or mutating actions occurred before intent confirmation.
- Every question is genuinely crucial and uses concise multiple-choice options.
- All non-blocking defaults are explicitly disclosed under **Assumptions**.
- The response ends with a clear **Intent Check** verifying what the user wants before execution.

Critical defects (must fix before proceeding):

- Starting implementation while high-impact ambiguity remains unresolved.
- Asking more than 8 questions or padding with trivial questions, asking open-ended essay questions when multiple-choice fits, or asking about trivial details that should be assumed.
- Making silent assumptions without disclosing them.
- Writing verbose preambles or repeating the user's prompt back word for word.

## Fallback and Failure Recovery

- **If the user replies "just go ahead" or "you decide":** Lock in your disclosed assumptions, briefly note them, and move straight to implementation without another round of questions.
- **If the user gives a partial answer:** Assume sensible defaults for any unanswered secondary questions, disclose them in the **Intent Check**, and avoid dragging out more than 2 clarification rounds unless a hard blocker remains.
- **When composing with other skills:** Run `ask` first to lock the specification, then hand the verified **Intent Check** into downstream skills (such as `delegate`, `3d`, or domain skills).

## Gotchas

- **Do not turn `@ask` into an interrogation:** 3 sharp questions beat 8 mediocre ones; use 5–8 only for distinct crucial decisions.
- **Do not hide assumptions in prose:** Put them in a short, scannable bullet list so the user can spot and override any wrong default in seconds.
- **Do not loop forever:** Cap clarification at 1 to 2 rounds. If uncertainty is low after round 1, lock defaults, show the **Intent Check**, and confirm.

## References

- [Gemini Task adapter](adapters/gemini-task.md)
- [Evaluation scenarios](evaluations/SCENARIOS.md)
