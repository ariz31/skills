# Gemini Task adapter: Max

Use only real exposed tools and inspect their signatures. Reuse [Delegate's adapter](../../delegate/adapters/gemini-task.md) for all worker lifecycle operations. The top-level coordinator owns both cycles and outer remediation; workers and auditors never invoke nested workers.

| Portable operation | Gemini Task mapping if available |
|---|---|
| Dispatch scoped worker or fresh auditor | invoke_subagent |
| Check all dispatched workers on wakeup | conversations:list with only_return_subagents: true |
| Read results | conversations:read |
| Re-task | send_message |
| Deliver verified workspace file | google:show_file or actual Workspace link |

Use distinct worker roles and separate candidate revisions; keep both cycle reports and goal audit evidence. Do not pass prior scores to the fresh goal auditor. Do not re-use the candidate builder as independent auditor. If a tool or genuine independence is unavailable, use the canonical bounded sequential fallback. Never fabricate a conversation ID, status, audit, or artifact link.
