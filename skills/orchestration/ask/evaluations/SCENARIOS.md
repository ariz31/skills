# Ask evaluation scenarios

These are evaluation specifications, not executed test results.

| Scenario | Expected behavior |
|---|---|
| User writes `@ask help me design a teaching app for hydraulics` | Activate `ask`; do not build yet; ask 2 to 3 crucial multiple-choice questions (audience, core simulation focus, output format), list assumptions, and verify intent before implementation. |
| User writes `/ask` on a mostly clear prompt | Activate `ask`; skip trivial questions, disclose assumptions, and output a concise **Intent Check** for fast confirmation before building. |
| User asks "give me ideas for a civil engineering dashboard" (no explicit tag, high ambiguity) | Auto-activate `ask`; offer 2 to 3 multiple-choice direction/scope questions, state defaults, and verify intent before generating code. |
| User asks "What is the formula for Euler buckling load?" | Do not activate `ask`; answer directly without unnecessary questions. |
| User replies "just go ahead with your defaults" after round 1 | Lock disclosed assumptions and proceed directly to implementation without another question round. |
| Host lacks a native structured question widget | Present clean lettered multiple-choice options in Markdown and state assumptions clearly; never claim a UI widget was used. |
| Composed with `delegate` on a vague multi-part project | Run `ask` first to confirm the **Intent Check**, then pass the verified spec to `delegate` workers. |
