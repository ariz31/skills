# ChatGPT Chat

Optimize for direct reasoning, available web/file connectors, ephemeral code execution, and concise file delivery. Do not assume persistent filesystems, background sub-agents, or headless browsers.

## Skill execution matrix (all active skills)

| Skill | Execution mode on ChatGPT Chat | Verification & delivery fallback |
|---|---|---|
| `ask` | Single numbered Markdown turn (0–8 crucial questions with lettered options) + Assumptions + Intent Check | Plain chat Markdown only |
| `delegate` | Sequential role passes in chat/sandbox | Explicitly label audit `SELF-REVIEW` |
| `max` | Two bounded sequential cycles + separate holistic self-review (3-round cap) | Label `SELF-REVIEW`; block if independent audit is explicitly mandatory |
| `3d` | Complete single-file HTML (downloadable file if available, else full source) | Static code/geometry check; disclose unverified WebGL rendering |
| `animate` | Sequential roles when active (+ `3d` if 3D); single HTML file or complete source | Static timeline/equation audit; disclose unverified runtime/exports |
| `msdeck` | Single-file 16:9 HTML with inline SVG fallback | Static inspection; disclose unverified multi-viewport rendering |
| `review` | Read-only sequential lenses on supplied files/snippets; HTML or Markdown | Label `SELF-REVIEW`; never claim source edits |
| `estimate` | Four sequential passes; Python arithmetic verification if Code Interpreter is active | `[User]`/`[Market]`/`[Benchmark]` tags; structured Markdown or downloadable XLSX |
| `count` | Inspect image; use programmatic numbered overlays where available | Visual grid count; disclose unavailable overlays |
| `live-browser-qa` | Actual browser and authorized URL checks when exposed | Static review only when browser unavailable; never fabricate live evidence |
