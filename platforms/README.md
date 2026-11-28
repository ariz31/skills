# Platform profiles

Select the profile matching the actual host, then verify real tool availability before execution. Profile names describe typical environments, not guaranteed entitlements.

- [Gemini Task](gemini-task.md)
- [Gemini Chat](gemini-chat.md)
- [ChatGPT Work](chatgpt-work.md)
- [ChatGPT Chat](chatgpt-chat.md)

## Host capability overview

| Capability | Gemini Task | Gemini Chat | ChatGPT Work | ChatGPT Chat |
|---|---|---|---|---|
| Native sub-agents | Usually exposed (`invoke_subagent`) | Rarely / No | Workspace-dependent | No |
| Structured multiple-choice UI | `ask_question` (hard cap: 3/call) | No (Markdown fallback) | Host-dependent | No (Markdown fallback) |
| Persistent sandbox & shell | Yes (`execute_bash`, `write_to_file`) | Limited / Code Interpreter | Workspace-dependent | Ephemeral Code Interpreter |
| Headless browser / visual QA | Sandbox Playwright or browser agent | No | Browser tool if enabled | Limited / No |
| Live web & source retrieval | `google:search`, `google:browse` | Search / URL fetch | Web / connectors | Web search |
| Native skill installation | Optional (`skills:save_skill` / `update_skill`) | Optional / UI | Optional / Custom GPTs | Optional / Manual |
| Deliverable presentation | `google:show_file` (Canvas/chip) & Drive | Inline / download | File export / Workspace | Inline / file download |

Common rules: verify real tools at runtime, honor authorization, load only relevant skills, never fabricate agents/tool outputs/links, and fall back to portable sequential execution with explicit `SELF-REVIEW` disclosure when native orchestration is absent.
