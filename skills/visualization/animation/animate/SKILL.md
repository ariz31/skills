---
name: animate
description: Create technically accurate, visually refined, phase-based animations and interactive simulations with adaptive Three.js, SVG, Canvas or CSS, a deterministic timeline, and minimal auto-hiding fullscreen controls. Invoke with @animate, /animate, or contextual requests to animate a process, model, mechanism or simulation. Compose with delegate for complex animations (optional for simple 2D); use 3d for three-dimensional artifacts.
---

# Animate

Create working phase-based animation, default one interactive HTML file paused on the first meaningful frame. Honor explicit formats. Activate for @animate, /animate or contextual creation/refinement of motion, mechanism, process, time-lapse and simulations, not informational or incidental mentions.

## 1. Preflight and composition
Delegate is required for ≥3 phases, any 3D/Three.js animation, physics/data-driven simulation or parameter recomputation, custom multi-panel UI, audio synchronization, video/GIF export, or explicit `@delegate`/`@max` composition. For simple single-component illustrative 2D CSS/SVG/Canvas with ≤2 phases and no solver, Delegate is optional; a single-agent fast path is allowed. Select `3d` whenever 3D modeling/rendering is required.
Finish Ask's Intent Check first if selected. Detect actual workspace, worker, browser, file and export tools. Use [Gemini Task adapter](adapters/gemini-task.md) when applicable; unavailable required dependencies block certification.

## 2. Technical contract
Identify subject, audience, source evidence, units, dimensions, equations, scope, interactions, duration and phases. Distinguish physics-based, data-driven and illustrative motion; label assumptions, schematic/exaggerated behavior. Choose Three.js for 3D, SVG for crisp vectors, Canvas for dense 2D and CSS for simple motion. Define storyboard with stable IDs, phase boundaries, initial/final states, rationale, events, camera, annotations, transitions, duration and criteria. Separate physical and presentation time; adapt durations without filler. Load [motion physics](references/motion-physics.md).

## 3. Execution mode and delegation
Apply the conditional criteria in §1. When Delegate is active, use its worker contracts and shared board; freeze units, geometry IDs, interfaces, phase boundaries, state model, sources, output and gates. Partition 2–6 roles as appropriate: physics, timeline/state, geometry/rendering, presentation, controls, integration/verification. Use Builder → Challenger → Fixer for tightly coupled work; preserve verified slices.

## 4. Deterministic architecture
Separate simulation, timeline, geometry, rendering, presentation, playback and configuration. One canonical state and authoritative timeline per immutable parameter revision. Derive state from timeline position using analytical samples, keyframes or fixed-step integration/checkpoints; seek/replay/reverse/loop must reproduce state. Separate physical clock, presentation clock and render cadence; speed never changes equations or integration step. Preserve continuity except modeled physical discontinuities; no cinematic easing of physical equations. Validate inputs, cancel stale work and atomically replace revisions, preserving position only if valid. Load [timeline engine](references/timeline-engine.md).

## 5. Presentation and playback
Canvas-first, compact phase indicator, collapsible information/parameters, auto-hiding controls. Play/pause, replay, scrub, phase navigation, speed, frame step, loop/autoplay/phase repeat when applicable. Start paused and silent; holds communicated and resumable. Fullscreen or labeled viewport fallback, clean mode, restore controls on pointer/touch/keyboard, visible focus and no traps. Synchronized annotations, units and hide-all; camera framing with manual override/reset. Responsive touch/keyboard/reduced-motion and contrast. Load [presentation UI](references/presentation-ui.md) and [rendering/performance](references/rendering-performance.md).

## 6. Deliver
One verified HTML file by default; disclose pinned dependencies and offline/server needs. No dead controls or placeholders. Video/GIF only if requested and actual codecs available; verify timing/playability. Audio opt-in, synchronized. Provide opening instructions, assumptions, verdict and limitations.

## 7. Audit
Mandatory [audit protocol](references/audit-protocol.md): Animate ≥95/100; Delegate ≥9/10 only when active; 3D ≥95/100 when active. No averaging. Verify equations, phase coverage/continuity, reproducible state, rendered playback, parameter revisions, speed independence, controls, fullscreen, mobile and performance. Incorrect physics, missing phases, broken seek/restoration, unintended discontinuities, unusable rendering, inaccessible controls or fabricated proof veto acceptance. When composed under `max`, share its unified 3-round outer remediation cap (no separate nested retry budget); at exhaustion or a hard blocker, deliver verified partial results with a Gap Report.

## Embedded/audit-only
Shell owns stage/navigation/global fullscreen/focus; Animate owns local timeline/playback. Implement mount/resize/activate/deactivate/reset/dispose, pause inactive rendering, synchronize shell steps and avoid competing handlers. Verify integrated candidate. Audit-only is read-only.
