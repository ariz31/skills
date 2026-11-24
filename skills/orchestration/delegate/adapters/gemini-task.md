# Gemini Task adapter: Delegate

Use these mappings only when the actual tool interface exposes them. Do not invent tools or parameter schemas; inspect available signatures and adapt accordingly.

| Portable operation | Gemini Task tool from the supplied workflow |
|---|---|
| Launch worker, assembler, auditor | invoke_subagent (role, self-contained prompt) |
| Inspect all worker statuses on wakeup | conversations:list with only_return_subagents: true |
| Read completed worker outputs | conversations:read |
| Re-task an existing worker | send_message |
| Replace failed worker | invoke_subagent |
| Deliver a workspace file | google:show_file or available Workspace link |

Launch 2–6 independent workers concurrently when appropriate. Keep the coordinator responsible for dispatch and retry loops; no nested delegation. Provide file paths to the assembler rather than importing all drafts. On every wakeup inspect all dispatched workers. If a named tool is unavailable, use a real equivalent or the canonical sequential fallback. Do not claim an independent audit if the host cannot supply it.
