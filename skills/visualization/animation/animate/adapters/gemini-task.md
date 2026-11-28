# Gemini Task adapter: Animate

Use only real exposed tools and inspect their signatures before calling them. Do not invent tools, agents, screenshots, video codecs, or verification runs.

| Portable operation | Gemini Task mapping if available |
|---|---|
| Multi-agent orchestration (`delegate` when active) | Canonical skill `delegate`'s `adapters/gemini-task.md` (`invoke_subagent`, `conversations:list` with `only_return_subagents: true`, `conversations:read`, `send_message`); sequential role passes with `SELF-REVIEW` label if subagents are unavailable |
| 3D geometry & rendering (when `3d` selected) | Canonical skill `3d`'s `adapters/gemini-task.md` in the same shared workspace |
| Authoring & timeline/physics checks | `write_to_file` for the single HTML artifact; `execute_bash` (Node/Python) to verify phase boundaries, deterministic seek/reset invariants, and syntax |
| Rendered playback & viewport audit | `execute_bash` with headless Chromium/Playwright to test play/pause, scrubbing, phase stepping, speed independence, fullscreen/clean mode, mobile viewport, and zero console errors; inspect captured keyframes with `view_file` |
| Optional video / GIF export | `execute_bash` (Playwright frame capture + `ffmpeg`) only when explicitly requested and codecs exist; verify output file timing and playability (do not substitute generative `video_generation:*` tools for deterministic physics/engineering simulations unless the user explicitly asks for AI-generated video) |
| Final delivery | `google:show_file` on the verified HTML artifact (and exported media file if requested); never invent download links |

Keep one coordinator owning dispatch, shared board, and retry limits; never nest subagents. If browser playback cannot be executed, perform static code/math verification, explicitly disclose unverified runtime playback, and do not mark runtime-dependent criteria as passed. When composed under `max`, share `max`'s unified 3-round outer remediation cap.
