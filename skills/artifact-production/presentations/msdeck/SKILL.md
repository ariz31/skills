---
name: msdeck
description: Create minimalist single-file interactive 16:9 HTML learning presentations with edge-tap and swipe navigation, stepped explanations, technical media and integrated simulations. Invoke with @msdeck, /msdeck or clearly requested interactive HTML slide decks.
---

# MSDeck

Produce a usable interactive HTML presentation, not a slide outline. Default to one HTML entry point, canonical 1280×720 stage, minimal transparent icon controls and coherent visual teaching. Honor the user's requested format and audience.

## Activation and preflight

Use for explicit case-insensitive whole command tokens, or semantic requests for interactive HTML decks, stepped learning slides or swipeable web presentations. Do not substitute HTML for expressly requested PPTX, Google Slides, printable PDF, or a non-slide article; do not activate for incidental "deck" or informational questions. If explicit command conflicts with format, honor the format or clarify an essential conflict. If no subject is known, ask for it.

Identify audience/learner level, objectives, scope, sources, language, slide sequence, technical constraints, interaction, accessibility, offline requirement and delivery. For educational content map each slide and assessment to objectives; verify units, equations, worked steps, source attribution and technical applicability. Use supplied authoritative material first; distinguish assumptions and illustrative content.

Check file creation, source retrieval, JS execution, browser and WebGL availability. Load [navigation and stage](references/navigation-and-stage.md), [media and stepped solutions](references/media-and-stepped-solutions.md), and [verification gate](references/verification-gate.md). If references cannot be retrieved, do not claim full compliance; use core workflow and disclose unverified details, or stop if essential. Optional Delegate for complex multi-part work; select 3D when a real interactive 3D artifact is needed, Animate when phase-based playback/simulation is needed (Animate conditionally requires Delegate per Animate's rules). Resolve transitive dependencies, deduplicate selection, and use one coordinator. Ask must finish before implementation if selected.

## Workflow

1. Design a slide/step manifest with unique IDs, meaningful learning progression, step boundaries, content hierarchy, verified source register, expected interactions and acceptance evidence. Choose static, stepped 2D, or interactive 3D media for pedagogical value, not decoration. Use concise layouts, readable typography, high contrast and consistent margins.
2. Build one responsive presentation shell. Own document, slide/step index, navigation, fullscreen, lightbox, viewport scaling, global keyboard/pointer handling and focus. Use a 1280×720 logical stage with uniform contain scaling and no clipping; adapt safe areas and portrait viewport. Start at the first meaningful slide/step. Keep controls minimal but discoverable, labeled and reachable by keyboard/touch. Follow navigation reference.
3. Implement deterministic stepped solutions with one authoritative slide-step state and synchronized calculations, labels, diagrams, narration if requested and animations. Reverse, skip, revisit and reset without stale state or duplicate effects. Respect reduced motion. Use visual media rules, verified licensing/source records, aspect-preserving rendering and accessible click-to-zoom.
4. Integrate 3D and Animate as scoped components, not nested standalone documents or competing global controllers. MSDeck owns the shell; 3D owns geometry/scene/camera and local interactions; Animate owns simulation and timeline/playback. Use mount, resize, activate, deactivate, reset, dispose lifecycle and explicit step synchronization; pause inactive rendering and prevent gesture/key conflicts. Preserve their technical and quality contracts. Use one shared dependency set with pinned compatible versions, namespaced IDs/styles/events and a single authoritative state per component.
5. Deliver one HTML entry point with authored CSS/JS and assets inline where practical. Fully offline only if specified or actually achieved; disclose pinned external dependencies, network/server requirements and licenses. Never claim CDN-dependent delivery is offline. Avoid placeholders, broken images, dead controls, blank canvases, or unverified links. If retrieval unavailable use accurate inline SVG instead of broken remote images; if no WebGL provide a visible labeled fallback, not a silently missing essential model.
6. Verify the exact final file with the reference gate. Inspect multi-viewport rendering, step transitions, keyboard/pointer/swipe behavior, media, responsive stage, simulations, lightbox, accessibility and console. Apply all selected skill gates separately to the integrated final artifact; a shared audit may report each separately. Correct defects and recheck affected functionality, respecting shared execution limits. Deliver only actual file or complete source if file creation is unavailable, with opening instructions, actual evidence/verdict and limitations.

## Quality and fallback

No acceptance if essential navigation, step logic, content correctness, rendering, media, controls, or verification fails. Without browser execution, conduct static HTML/CSS/JS and source inspection, explicitly label runtime/viewport behavior unverified, and provide provisional output if essential checks cannot be established. No invented screenshots, executed checks, external image verification or file paths. Preserve the requested output; no silent format substitution.

See [evaluation scenarios](evaluations/SCENARIOS.md).

Use [Gemini Task adapter](adapters/gemini-task.md) when applicable.
