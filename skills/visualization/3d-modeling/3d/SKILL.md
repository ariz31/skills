---
name: 3d
description: Create engineering-accurate, source-grounded, high-fidelity interactive Three.js models, defaulting to a single HTML file. Activate explicitly with @3d or /3d, or contextually for 3D, three dimensional, Three.js, threejs, WebGL modeling, 3D CAD, building or terrain reconstruction, interactive 3D simulations, parametric geometry, cutaways and exploded models when the task calls for a 3D artifact.
---

# 3D

Produce defensible high-fidelity, source-grounded parametric Three.js models, default one interactive HTML file. Activate for explicit @3d, /3d, legacy threejs-modeling aliases, or semantic creation/refinement/repair/verification/conversion requests for genuine 3D, CAD, WebGL, BIM, terrain, digital twin, cutaway or exploded models. A bare invocation without a subject requires the subject. Do not create unsolicited models for informational, image-only or incidental requests; honor requested format.

## 1. Define contract
Identify use, audience, scope, detail, drawings/specifications, dimensions, units, interactions and delivery. Prioritize approved drawings, measurements, authoritative survey/GIS/manufacturer sources, then identified secondary sources; disclose conflicts and uncertainty. Distinguish conceptual models from measured reconstruction or design. Maintain source-linked dimension/component IDs, values, units, datum, provenance and justified tolerance. Never invent exact dimensions, coordinates, concealed components or compliance. Use SI (1 unit = 1 m unless justified), right-handed Y-up, origin/orientation/datum and local metric coordinates with georeferencing transforms.

## 2. Geometry
Use a semantic assembly hierarchy and complete inventory. Canonical parametric dimensions drive placements, rotations, profiles, openings, connections, clearances and elevations. Choose accurate extrusions, sweeps, curves, meshes or validated assets; boxes only when appropriate or labeled abstractions. Model relevant visible/hidden components and interfaces without invented reinforcement or services. Separate physical geometry from reversible labeled exploded/cutaway presentation; measure original geometry. Preserve stable IDs, names, dimensions, provenance, materials and layers. Load [geometry protocol](references/geometry-protocol.md) for detailed requirements.

## 3. Visual fidelity and interaction
Use appropriate PBR materials, plausible texture scale, correct normals, lights, shadows, transparency and color management. Balance technical legibility, detail and performance. Default responsive orbit/pan/zoom, fit, perspective/orthographic presets, orientation and component visibility; inspection, isolation, measurements and cutaways as relevant. Support units, annotations, touch, keyboard, fullscreen, compact working controls and instant feedback. Preserve camera/selection on updates. Validate inputs and regenerate dependent geometry consistently; engineering calculations require verified equations and units.

## 4. Build and deliver
Follow [rendering and delivery](references/rendering-delivery.md). Prefer self-contained single HTML; pin compatible dependencies and disclose network/server needs. Robust startup, resize, DPR, error and WebGL feedback; never silently blank. Use instancing, shared resources, LOD/disposal as applicable. Separate model, geometry, rendering, interactions and verification; no placeholders, fake dimensions, dead controls or broken assets. Save verified artifact or complete source with limitation.

## 5. Verify
Load [audit protocol](references/audit-protocol.md). Check inventory, finite dimensions, geometry, transforms, connections, clearances, intersections and datum; compare actual assembled geometry against independent source/calculation using local-axis measurements and sections, not world AABB alone. If browser available, render exact HTML, inspect multiple viewpoints/close-ups, console, all controls, mobile/resize, parameters and promised offline mode. Record expected/observed values, tolerances, evidence and gaps.

PASS ≥95/100 and no critical defects or unverified essential requirements: geometry 30, completeness 20, spatial/technical 15, visual 15, interaction 10, performance 5, code 5. Incorrect critical dimensions, engineering errors, fabricated sources, incomplete essentials, unusable rendering or broken essential controls veto PASS.

## 6. Rework and composition
Fix and recheck actual candidate. When composed under `max`, share its unified 3-round outer remediation cap (no separate nested retry budget); at exhaustion or a hard blocker, deliver verified partial results with a Gap Report. For complex tasks optionally select Delegate; its 9/10 cannot override 3D's 95/100. Use [Gemini Task adapter](adapters/gemini-task.md) when available. Disclose unverified runtime/independence and actual verdict; provide opening instructions and assumptions. Embedded scene supplies mount/resize/activate/deactivate/reset/dispose, pauses inactive rendering and respects shell navigation/fullscreen. Audit-only stays read-only; verify integrated candidate.
