# Gemini Task

Optimize for autonomous deliverable execution, isolated worker scopes, shared workspace coordination, and evidence-based verification. Detect exposed sub-agent, shell, browser, question, and file tools before use; never invent tools or claim independence without real separate workers.

## Capability & adapter matrix (all active skills)

| Skill | Adapter | Primary Gemini Task tools | Fallback if tool unavailable |
|---|---|---|---|
| `ask` | [adapter](../skills/orchestration/ask/adapters/gemini-task.md) | Two-tier: `ask_question` (Tier 1: 1–3; Tier 2B: <=2 sequential <=3 batches, <=6 total) or single numbered Markdown turn (Tier 2A: 4–8, required for 7–8) | Numbered Markdown options + Assumptions + Intent Check in chat |
| `delegate` | [adapter](../skills/orchestration/delegate/adapters/gemini-task.md) | `invoke_subagent`, `conversations:list` (`only_return_subagents: true`), `conversations:read`, `send_message`, `google:show_file` | Bounded sequential role passes labeled `SELF-REVIEW` |
| `max` | [adapter](../skills/orchestration/max/adapters/gemini-task.md) | Reuses `delegate` adapter across 2 cycles + fresh unprimed Goal Auditor; unified 3-round outer remediation cap | Two sequential cycles + separate holistic `SELF-REVIEW` + Gap Report on cap |
| `3d` | [adapter](../skills/visualization/3d-modeling/3d/adapters/gemini-task.md) | `write_to_file`, `execute_bash` (Node/Python + Playwright), `view_file`, `google:show_file` | Static geometry/JS checks + disclose unverified WebGL/runtime |
| `animate` | [adapter](../skills/visualization/animation/animate/adapters/gemini-task.md) | `delegate` adapter (required in v0.8.0; conditional in v0.9.0) + `3d` adapter (when 3D) + `execute_bash` (Playwright/ffmpeg) + `google:show_file` | Sequential `SELF-REVIEW` + static timeline/math checks + disclose unverified playback |
| `msdeck` | [adapter](../skills/artifact-production/presentations/msdeck/adapters/gemini-task.md) | `write_to_file`, `image_agent:fetch_images`, `execute_bash` (6-viewport Playwright), `google:show_file` | Inline SVG fallback + static HTML/CSS/JS audit + disclose unverified viewports |
| `review` | [adapter](../skills/quality-assurance/review/adapters/gemini-task.md) | Read-only `view_file`/`execute_bash` + `delegate` adapter + `write_to_file` (HTML dashboard) + `google:show_file` | Sequential read-only lenses (`SELF-REVIEW`) + Markdown/chat report |
| `estimate` | [adapter](../skills/civil-engineering/construction-management/estimate/adapters/gemini-task.md) | `ask_question`, Drive/VM file read, `google:search`, `delegate` adapter, `execute_bash` (XLSX/PDF), `google:show_file` | Four sequential passes (`SELF-REVIEW`), labeled `[Benchmark]`/`[Assumed]`, structured Markdown |

Do not install or overwrite native skills unless explicitly requested. Keep one top-level coordinator for `delegate`/`max`; never nest sub-agents.
