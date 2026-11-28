# Gemini Task adapter: Review

Use only real exposed tools and inspect their signatures before calling them. Review is strictly **read-only** toward the audited source unless the user separately authorizes edits.

| Portable operation | Gemini Task mapping if available |
|---|---|
| Source inspection (read-only) | `view_file`, `execute_bash` (read-only commands such as `git status`, `git log`, `grep`, linters, or authorized non-mutating test runs), authorized Drive/Workspace read tools, or `google:browse` |
| Adversarial lens dispatch (`delegate`) | Canonical skill `delegate`'s `adapters/gemini-task.md` (`invoke_subagent`, `conversations:list` with `only_return_subagents: true`, `conversations:read`, `send_message`); workers own investigation and findings files in scratch space only—never source edits |
| Upfront scoping (optional `ask`) | Canonical skill `ask`'s `adapters/gemini-task.md` when audit scope, rubric priorities, or authorized checks are ambiguous |
| Interactive dark HTML dashboard build | `write_to_file` to generate the XSS-hardened single-file HTML report (or requested Markdown/structured chat output) |
| Report verification gate | `execute_bash` (HTML/JS static checks + headless Chromium/Playwright when available) to verify search/filter, expandable evidence cards, immutable score/verdict, and zero console errors; inspect via `view_file` |
| Final delivery | `google:show_file` on the verified HTML/Markdown report file (or direct structured chat when requested); never claim source files were modified |

Keep source verdict strictly separate from Delegate's 9/10 report quality gate. Without native subagents, execute sequential adversarial lenses and label the audit `SELF-REVIEW`. Never run destructive commands, commit/push changes, or mutate the audited repository/file.
