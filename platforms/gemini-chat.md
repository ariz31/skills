# Gemini Chat

Optimize for direct reasoning, concise responses, and real code/file execution where exposed. Do not assume Gemini Task sub-agent or `ask_question` tools exist in Chat.

## Skill execution matrix (all active skills)

| Skill | Execution mode on Gemini Chat | Verification & delivery fallback |
|---|---|---|
| `ask` | Single numbered Markdown turn (3–8 lettered options) + Assumptions + Intent Check | Never claim a native question widget was used |
| `delegate` | Bounded sequential role passes (parallel sub-agents only if actually exposed) | Label audit `SELF-REVIEW`; disclose non-independence |
| `max` | Two sequential Delegate cycles + separate holistic self-audit (shared 3-round cap) | Label `SELF-REVIEW`; return Gap Report if blocked |
| `3d` | Generate complete single-file HTML (save/Canvas if supported, else full source) | Static geometry/math inspection; disclose unverified WebGL rendering |
| `animate` | Sequential `delegate` roles when active (+ `3d` if 3D); single HTML artifact | Static timeline/equation verification; disclose unverified playback/exports |
| `msdeck` | Single-file 16:9 HTML shell with inline SVG when media fetch is unavailable | Static HTML/CSS/JS review; disclose unverified 6-viewport checks |
| `review` | Sequential read-only adversarial lenses; HTML dashboard or Markdown report | Label `SELF-REVIEW`; never modify audited source |
| `estimate` | Four sequential role passes; live search if exposed, else `[Benchmark]`/`[Assumed]` | Recompute totals deterministically; deliver Markdown or supported export |
