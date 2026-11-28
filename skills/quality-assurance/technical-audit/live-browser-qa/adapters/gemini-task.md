# Gemini Task adapter: Live Browser QA

Use only actual exposed capabilities and authorized targets. Inspect tool signatures; do not assume a tool exists.

| Operation | Preferred host mapping / fallback |
|---|---|
| Headless browser audit | Run Playwright / Chromium script via `execute_bash` (setting required `User-Agent` on external HTTP probes) to capture DOM metrics, `console`/`pageerror`, network `>=400`, and viewport PNGs |
| Auth-gated or interactive live site | Use `web_browser_agent:actuate` when signed-in browser context or live human takeover is needed; never request passwords in chat |
| Visual screenshot inspection | Inspect every captured PNG via `view_file` before reporting visual passes or defects |
| Multi-route parallelization | Optional canonical skill `delegate` (`adapters/gemini-task.md`) for 4+ independent routes; one coordinator aggregates findings with zero duplicate defects |
| Static fallback | If Playwright and `web_browser_agent:actuate` are unavailable, use `google:browse` or read-only HTTP fetch and explicitly mark runtime checks `UNVERIFIED` |
| Delivery | Present Markdown/HTML QA reports and annotated defect screenshots via `google:show_file`; include inline clickable links to audited public URLs |

Never execute destructive clicks (delete, checkout, submit production forms) without explicit user approval. Never fabricate console logs, HTTP status codes, or screenshot observations.
