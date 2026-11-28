# Rendering, performance and delivery protocol

Choose renderer by subject and requirements: Three.js for true spatial scenes (compose with 3d), SVG for crisp structured vector scenes, Canvas for dense dynamic 2D content, CSS for simple presentational transforms. Hybrid approaches are valid if all layers share the canonical clock and state. Use geometry and materials faithful to the source and intended level of detail. Avoid gratuitous effects, occlusion, layout shifts and contradictory lighting. Keep component IDs stable across phases.

Use one coordinated render loop; do not allocate a new loop on every play/seek. Prefer demand-driven rendering while paused unless user interaction or required effects need frames. Minimize per-frame allocation and DOM churn, batch updates, reuse assets, use instancing/LOD for appropriate 3D scenes, scale device pixel ratio when necessary and dispose obsolete resources safely. Resize using actual container dimensions and preserve state. For computationally heavy solvers, use precomputed or asynchronous results when supported with cancellation/revision checks; do not block controls. Reduce decorative quality before sacrificing essential model detail or accuracy.

Measure rather than promise universal FPS. Record device/browser, viewport/DPR, model complexity, representative frame timing, dropped frames or observed responsiveness, and memory/resource behavior when available. Verify repeated replay, seeks and parameter changes for leaks or duplicated listeners. Handle asset failures, unsupported WebGL and initialization errors with clear feedback; never deliver a silent blank canvas.

Single HTML is the default. Embed authored state, timeline, scene and controls; use pinned compatible library imports and disclose all external dependencies and launch requirements. Do not describe a CDN-dependent file as offline. Verify the actual launch method and offline behavior if promised. Protect accessibility and ensure essential controls work even when optional features fail.

If export is requested and supported, select real available format/codec, dimensions, frame rate and duration. For deterministic export sample frames at explicit timestamps instead of recording unreliable wall-clock frames when feasible. Synchronize opt-in audio, captions and camera; exclude controls by default unless requested. Validate file existence, decodability, first/last frames, duration and timing. If video/GIF generation is unavailable, disclose and still provide working HTML when appropriate; do not create fake export actions or mislabel formats.


## 6. Integrate and deliver

Default to one HTML file containing the authored model, animation, controls and data. Prefer offline self-containment when practical; disclose pinned external dependencies, internet/local-server requirements and launch instructions when necessary. No placeholders, dead controls, broken assets or simulated export buttons. If requested, produce real video/GIF export using available tools and codecs; verify the exported file and its timing. Audio is opt-in and must synchronize with the same timeline; do not assume recording support.

Save the actual artifact and verify the exact final version, not merely a summary. If file creation is unavailable, provide complete source if practical and explicitly disclose the limitation. Never invent a file path or download. Follow Delegate's targeted remediation loop when Delegate is active.
