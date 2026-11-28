# Gemini Task adapter: MSDeck

Use only real exposed tools and inspect their signatures before calling them. Do not fabricate media checks, multi-viewport screenshots, or offline claims.

| Portable operation | Gemini Task mapping if available |
|---|---|
| Technical & visual source retrieval | `google:search`, `google:browse`, `image_agent:fetch_images` (for real reference imagery when online), or `view_file` for user-supplied assets/slides |
| Authoring single-file 16:9 HTML deck | `write_to_file` to save the self-contained HTML entry point; inline accurate SVG diagrams when offline self-containment is requested or remote media cannot be verified |
| Scoped `3d` / `animate` components | Canonical skill `3d` / `animate` adapters integrated into one shared HTML shell (`mount`/`resize`/`activate`/`deactivate`/`reset`/`dispose` lifecycle); never emit a second standalone HTML document |
| Multi-agent orchestration (optional `delegate`) | Canonical skill `delegate`'s `adapters/gemini-task.md` for complex multi-slide or simulation-heavy decks |
| 6-viewport & interaction verification gate | `execute_bash` with headless Chromium/Playwright to verify 1280x720 uniform contain scaling, 10% edge-tap zones (80% step / 20% slide split), swipe/keyboard navigation, `#deck-lightbox`, step reversal/reset, and zero console errors across desktop/tablet/portrait viewports; inspect captures with `view_file` |
| Final delivery | `google:show_file` on the verified HTML file (opens in Canvas); honor explicit non-HTML requests (PPTX/Google Slides/PDF) via their native tools instead of substituting HTML |

If headless browser verification is unavailable, run static HTML/CSS/JS inspection via `execute_bash`, explicitly report viewport/runtime checks as unverified, and never fabricate screenshot evidence.
