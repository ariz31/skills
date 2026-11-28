# ChatGPT Work

Optimize for multi-step research, file production, browser/connector checks, and artifact verification where workspace permissions allow. Do not assume a native sub-agent API or Gemini-specific tools exist.

## Skill execution matrix (all active skills)

| Skill | Execution mode on ChatGPT Work | Verification & delivery fallback |
|---|---|---|
| `ask` | Structured widget if exposed, else single numbered Markdown turn (0–8 crucial questions with lettered options) + Assumptions + Intent Check | Never fabricate widget usage |
| `delegate` | Native worker dispatch if exposed, else isolated sequential role passes | Label audit `SELF-REVIEW` unless genuine independent reviewer exists |
| `max` | Two bounded Delegate cycles + separate holistic audit (3-round outer cap) | Disclose `SELF-REVIEW` if single-agent; emit Gap Report on cap |
| `3d` | Single-file HTML via workspace file tools + Python/Node/browser checks when enabled | Static checks + explicit disclosure of unverified WebGL viewpoints |
| `animate` | `delegate` roles when active (+ `3d` if 3D) + deterministic HTML; video/GIF only if real codecs exist | Static timeline/physics checks + disclose unverified playback |
| `msdeck` | Single-file 16:9 HTML shell; inline SVG fallback if image retrieval unavailable | Static + available browser checks; honor explicit PPTX/PDF requests |
| `review` | Read-only source inspection via connectors/files; HTML dashboard or Markdown | Keep source untouched; label `SELF-REVIEW` without independent workers |
| `estimate` | Four role passes; Python/openpyxl/PDF verification where code execution exists | Zero-variance check in code; disclose unavailable live pricing or exports |
| `count` | Inspect image; use programmatic numbered overlays where available | Visual grid count; disclose unavailable overlays |
| `live-browser-qa` | Actual browser and authorized URL checks when exposed | Static review only when browser unavailable; never fabricate live evidence |
