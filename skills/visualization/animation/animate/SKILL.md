---
name: animate
description: Create technically accurate, visually refined, phase-based animations and interactive simulations with adaptive Three.js, SVG, Canvas or CSS, a deterministic timeline, and minimal auto-hiding fullscreen controls. Invoke with @animate, /animate, or contextual requests to animate a process, model, mechanism or simulation. Always compose with delegate; use 3d for three-dimensional artifacts.
---

# Animate

Create a working animation, not a description of one. Default deliverable: one interactive HTML file, paused on the first meaningful frame. Honor explicit output and scope requirements. Provide video or GIF export only when requested and actually supported.

## 1. Activation and capability preflight

- Recognize @animate and /animate as case-insensitive explicit commands. Also match animate, animation, animated simulation, process animation, time-lapse, construction sequence, animated mechanism, motion visualization and equivalent creation/refinement requests semantically. Do not create unsolicited artifacts for informational questions or incidental animation mentions.
- Always activate the canonical delegate skill for production and audit, even for small animations; scale the workstreams to the task. Automatically activate 3d whenever the deliverable requires three-dimensional modeling or rendering, including existing Three.js model animation. Load other applicable domain skills without duplication.
- When ask is selected, finish its intent confirmation before dispatching implementation workers or editing artifacts. For ordinary clear animation requests, proceed directly with sensible disclosed defaults.
- Detect actual worker, workspace, browser, execution, file and export capabilities. Use Delegate's native orchestration when available; otherwise use its sequential role-based fallback, clearly identifying self-review. Do not invent agents, screenshots, export capabilities or verification.
- For native installations lacking dependency access, retrieve Delegate and 3D if applicable or request their contents; do not claim they ran. If a required dependency cannot be obtained, disclose the limitation and mark the result provisional.

## 2. Establish technical and presentation contracts

- Identify subject, intended audience, learning or presentation goal, scope, source evidence, dimensions, units, governing equations, constraints, intended duration, phases, deliverable format and interactions.
- Distinguish physics-based, data-driven and illustrative motion. Use authoritative evidence and verified equations where appropriate. Label assumed, estimated, schematic and exaggerated behavior; never imply illustrative animation is a validated engineering analysis.
- Select Three.js for genuine 3D or spatial interaction, SVG for crisp vector diagrams and moderate scene complexity, Canvas for dense or rapidly updated 2D visuals, and CSS for simple presentational motion. Choose based on accuracy, portability, detail and performance, not a fixed technology preference.
- Define the phase storyboard: stable ID, goal, start/end time, required initial/final state, source/equation or illustrative rationale, key events, camera, synchronized annotation, transition, duration and verification criteria. Include all technically meaningful stages without filler.
- Use adaptive phase durations that make important events understandable. Optional holds may pause at key events. Separate physical simulation time and presentation time, including any time compression or slow motion. See [motion physics](references/motion-physics.md).

## 3. Delegate the work

Use Delegate's worker contracts, lifecycle, isolation and final auditor. Establish a shared board (file if supported, otherwise structured context) before splitting work. Freeze common units, geometry IDs, interfaces, phase boundaries, state model, source register, visual conventions, output format and acceptance criteria. The coordinator owns integration; workers must not redefine shared contracts independently.

For parallelizable work, select 2 to 6 non-overlapping roles as appropriate: technical modeling/physics; timeline and state; geometry/rendering; presentation and annotations; controls and responsive UI; integration or verification. Assign individual phases only when dependencies and shared state permit. For tightly coupled simulations use Builder, Adversarial Challenger and Fixer rather than artificial partitioning. Preserve successful work and repair only failing slices. One coordinator controls dispatch and retries, with no nested agents.

## 4. Build deterministic animation architecture

Separate seven logical systems even in a single HTML file: simulation (physical state), timeline (phase/time mapping), geometry (semantic components), rendering (visual representation), presentation (camera and annotations), playback (controls and transport), configuration (validated inputs and recomputation). Establish one authoritative timeline and one canonical simulation state per parameter revision.

- Derive every visible state from the current timeline position and immutable parameter revision. Use analytical sampling, keyframes or deterministic fixed-step integration with reproducible checkpoints as appropriate. Seeking forward/backward, replay, phase skipping and looping must restore the correct state without accumulating mutations.
- Distinguish presentation clock, physical clock and render cadence. Use monotonic elapsed time; playback speed changes presentation progression only, not governing equations or numerical step size. Handle pause, inactive tabs, terminal frame, event holds and looping without drift or catch-up instability.
- Maintain boundary continuity except for explicitly modeled physical discontinuities (impact, fracture, contact, switching, topology change). Preserve stable geometry IDs and define reversible lifecycle changes. Never use cinematic easing on physical state if it changes the governing relationship.
- Validate parameter inputs and derived constraints. Pause or safely recompute when a change invalidates the solution; cancel stale work and atomically replace the timeline/state/geometry revision. Preserve playback position only if meaningful and valid, otherwise reset with clear feedback.
- Follow [timeline engine](references/timeline-engine.md) and [motion physics](references/motion-physics.md).

## 5. Presentation and playback

Make the visualization the primary canvas, with compact contextual phase indicator, collapsible information and parameter panels, and an auto-hiding playback overlay. Support play/pause, replay, scrub, previous/next phase, adjustable playback speed, frame stepping, optional loop/autoplay and phase repetition. Start paused and silent unless requested otherwise. Event holds must be optional or clearly communicated and resumable.

- Offer fullscreen presentation with all nonessential UI hidden during playback, and a dedicated clean mode. Restore controls on pointer, touch or keyboard interaction; keep keyboard focus visible and controls accessible when paused, focused or being used. Never trap the user in hidden controls or fullscreen. Use a viewport-maximized fallback if native fullscreen is unsupported, clearly labeled as such.
- Keep annotations synchronized to timeline and physical state. Include units, meaningful labels and short explanations when educational or technical; allow hide-all. Avoid permanently obstructing the subject. Provide phase-specific camera framing/transitions with manual override for applicable views; user camera manipulation must not fight automatic camera updates. Offer resume-auto-camera or reset.
- Use context-dependent transitions, adaptive technical/realistic/educational visual language, accurate geometry/materials and purposeful visual hierarchy. Do not add decorative motion that reduces comprehension. Support responsive desktop/mobile, touch, keyboard, reduced-motion preferences and sufficient contrast.
- Follow [presentation UI](references/presentation-ui.md) and [rendering and performance](references/rendering-performance.md).

## 6. Integrate and deliver

Default to one HTML file containing the authored model, animation, controls and data. Prefer offline self-containment when practical; disclose pinned external dependencies, internet/local-server requirements and launch instructions when necessary. No placeholders, dead controls, broken assets or simulated export buttons. If requested, produce real video/GIF export using available tools and codecs; verify the exported file and its timing. Audio is opt-in and must synchronize with the same timeline; do not assume recording support.

Save the actual artifact and verify the exact final version, not merely a summary. If file creation is unavailable, provide complete source if practical and explicitly disclose the limitation. Never invent a file path or download. Follow Delegate's targeted remediation loop.

## 7. Strict audit and acceptance

Require both Delegate's 9/10 gate and the Animate 95/100 gate; apply 3D's own 95/100 gate when selected. A single real audit may report each rubric separately with shared evidence. No averaging away defects. Use independent review when available, otherwise clearly labeled self-review.

| Criterion | Points |
|---|---:|
| Scientific and technical accuracy | 30 |
| Phase sequencing and continuity | 20 |
| Visual fidelity and clarity | 20 |
| Motion smoothness and rendering performance | 15 |
| UI and playback usability | 10 |
| Code correctness | 5 |
| Total | 100 |

PASS requires at least 95/100 with no critical defects or unverified essential requirements. Incorrect equations or physical behavior, missing phases, broken seeking/playback/state restoration, unintended geometry discontinuities, unusable rendering, inaccessible essential controls/fullscreen (or promised fallback), or fabricated evidence automatically fail. Verify the source, rendered playback, all phase boundaries, state reproducibility, parameters, speed independence, controls, fullscreen, mobile and performance using available tools. See [audit protocol](references/audit-protocol.md).

Fix and re-audit actual revised artifacts until accepted or a genuine blocker prevents further verification. Report unexecuted checks and missing tools honestly; a provisional artifact must not be called certified. Deliver the file, brief opening instructions, material assumptions, actual audit verdict/score and limitations. Do not claim professional engineering certification.
