# Gemini Task adapter: 3D

Use only real exposed tools and inspect their signatures before calling them. Do not invent tools, screenshots, browser checks, or artifact links.

| Portable operation | Gemini Task mapping if available |
|---|---|
| Source & dimension retrieval | `google:search`, `google:browse`, authorized Workspace/Drive read tools, or `view_file` for uploaded drawings/specs/images |
| Authoring & parametric geometry checks | `write_to_file` to save the single HTML artifact; `execute_bash` (Node/Python) for static syntax, finite-number, and dimensional constraint checks |
| Browser rendering & visual audit | `execute_bash` with headless Chromium/Playwright (or `web_browser_agent:actuate` if local server + browser access apply) to capture multi-angle screenshots and console logs; inspect screenshots with `view_file` |
| Multi-agent orchestration (optional `delegate`) | Canonical skill `delegate`'s `adapters/gemini-task.md` (`invoke_subagent`, `conversations:list` with `only_return_subagents: true`, `conversations:read`, `send_message`) |
| Final delivery | `google:show_file` on the verified sandbox HTML path (opens in Canvas); never emit raw container paths in chat |

When headless browser or WebGL rendering is unavailable in the sandbox, run static JS/geometry validation via `execute_bash`, disclose that runtime WebGL rendering and visual viewpoints were not executed, and label the 95/100 audit provisional if visual/runtime checks are essential. When composed under `max`, share `max`'s unified 3-round outer remediation cap rather than adding a separate retry budget.
