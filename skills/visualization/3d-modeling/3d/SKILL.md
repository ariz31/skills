---
name: 3d
description: Create engineering-accurate, source-grounded, high-fidelity interactive Three.js models, defaulting to a single HTML file. Activate explicitly with @3d or /3d, or contextually for 3D, three dimensional, Three.js, threejs, WebGL modeling, 3D CAD, building or terrain reconstruction, interactive 3D simulations, parametric geometry, cutaways and exploded models when the task calls for a 3D artifact.
---

# 3D

## Objective and activation

Produce the highest defensible geometric accuracy and visual fidelity for the source evidence and intended use. Default deliverable: a working interactive Three.js model in a single HTML file. Maintain editable parametric source geometry and semantic component metadata.

Recognize `@3d` and `/3d` as explicit commands (case-insensitive), including when combined with other skill commands. The former skill name `threejs-modeling` and its `@threejs-modeling` and `/threejs-modeling` forms remain invocation aliases. Recognize 3D, 3-D, three dimensional, three-dimensional, Three.js, threejs, THREE JS, 3D model, 3D visualization, 3D simulation, WebGL model, 3D reconstruction, 3D CAD, 3D terrain, BIM visualization, digital twin, cutaway and exploded view; match case-insensitively and semantically. A bare `@3d`, `/3d`, "3D" or "Three.js" invokes this skill; if no modeling subject is known, ask for the subject. Automatically activate for creation, refinement, repair, verification or conversion of 3D models; no exact skill name is required. Explicit invocation selects this skill, but does not override the user's requested output or justify creating an unsolicited model. Do not divert purely informational questions, image-only requests or incidental mentions of 3D into model creation. Honor explicit output constraints.

## 1. Define the modeling contract

- Identify subject, intended use, audience, scope, detail, drawings, specifications, dimensions, units, interaction and delivery requirements. Distinguish conceptual/educational models from measured reconstructions and engineering design representations.
- Prioritize supplied approved drawings/measurements, authoritative survey/GIS or manufacturer data, then identified secondary sources. Resolve or disclose discrepancies. Never invent survey coordinates, manufacturer dimensions, concealed construction, code compliance or precision.
- Maintain a dimension/component register with ID, source, value, unit, datum, provenance (measured, specified, derived, estimated, illustrative), uncertainty and justified acceptance tolerance. Numerical consistency is not proof of real-world accuracy.
- Define SI units (1 world unit = 1 m unless explicitly justified otherwise), right-handed Y-up coordinate frame, origin, axis mapping, orientation and datum. Keep georeferenced scenes in a local metric frame and preserve transformation metadata.
- Derive tolerances from intended use and source precision, not a universal arbitrary threshold. If data are missing, use explicitly labeled assumptions where reasonable; do not fabricate exact dimensions. If the requested real-world accuracy is unattainable, disclose that and deliver a labeled conceptual/partial result rather than certify it.

## 2. Construct source-driven geometry

- Build a semantic assembly tree: site/system, subassemblies, components and interfaces. Inventory every required component against the scope and source data.
- Use a single canonical dimension source and parametric geometry. Compute placements, rotations, sections, clearances, openings, connections, profiles and elevations from constraints rather than arbitrary offsets.
- Use appropriate geometry: extrusions, sweeps, curves, indexed meshes, triangulated surfaces, validated imported assets and constructive geometry where needed. Generic boxes are acceptable only for truly box-shaped items or explicitly labeled abstractions.
- Model relevant visible and hidden components, openings, elevations, supports, joints, slopes, transitions, interfaces and interior/exterior relationships. Do not add invented reinforcement or concealed services as verified facts.
- Separate physical geometry and presentation transforms. Exploded, exaggerated and cutaway views must be reversible and visibly labeled. Measurements refer to original physical geometry, not exploded spacing.
- Preserve stable component IDs, names, dimensions, provenance, materials, hierarchy and layer membership. Allocate detail by technical importance and viewing distance; never simplify away essential interfaces or dimensions.
- Apply the [geometry protocol](references/geometry-protocol.md) when available for domain-specific requirements.

## 3. Visual fidelity and interaction

- Use consistent PBR materials, plausible roughness/metalness, appropriate texture scale, correct normals, purposeful lights, physically credible shadows, color management and exposure. Handle glass, transparency, depth ordering and coplanar surfaces correctly.
- Combine realistic rendering with technical legibility. Preserve small details without gratuitous polygon density; never conceal geometric deficiencies with textures or shadows.
- Default to responsive orbit/pan/zoom, fit-to-model, perspective and orthographic presets, orientation reference, and logical component visibility. For complex assemblies, include object inspection and useful isolation controls. Add cutaways, exploded views, measurement, dimensions and layers when technically relevant.
- Support accurate dimension annotations and units, stable selection, useful camera presets, fullscreen when supported, touch and keyboard access, and compact controls with instant feedback. Every visible control must work. Preserve camera/selection on routine updates; reset only on request.
- For parametric models, validate inputs, regenerate dependent geometry consistently, and preserve all geometric relationships. If offering engineering calculations, derive them from verified equations, inputs and units; distinguish visualization from structural analysis.
- See [rendering and delivery protocol](references/rendering-delivery.md) for implementation details.

## 4. Build and deliver

- Default to a single HTML entry point containing authored code, model and UI. Prefer an offline self-contained file when practical. If external dependencies are needed, use pinned compatible Three.js/add-on versions, consistent imports, and explicit network/server requirements. A CDN-dependent HTML file is not offline self-contained.
- Use robust startup, resize, device-pixel-ratio management, error handling and WebGL capability feedback. Do not silently show a blank canvas. Use actual available libraries; never invent APIs.
- Use instancing, shared geometry/materials, suitable level of detail and resource disposal as applicable. Avoid unnecessary repeated scene rebuilding and idle rendering; preserve the requested detail and responsiveness.
- Separate model data, geometry builders, rendering, interaction and verification logically even within one HTML. No placeholders, dead controls, fake dimensions, broken assets or arbitrary source claims.
- Save and deliver the exact file when supported. If file creation is unavailable, provide complete HTML source if practical and disclose the limitation. Never invent artifact links.

## 5. Verify the exact final artifact

- Verify inventory, units, finite dimensions, geometry validity, coordinate transforms, openings, connections, clearances, intentional/unintentional intersections and datum alignment. Check actual assembled geometry against independent source values or calculations rather than merely echoing generator inputs.
- Use local-axis measurements, reference points, analytical comparisons, section sampling and bounding boxes as appropriate; a world-axis bounding box alone cannot verify a rotated member's length or actual shape.
- If browser execution is available, render the exact HTML, inspect multiple meaningful viewpoints and close-ups, check the console, exercise every supplied control, resize/mobile behavior, parameter updates and any promised offline mode. Inspect visual defects such as floating elements, clipping, bad normals, z-fighting or overlapping UI.
- Record actual checks, expected/observed values, tolerances, errors, assumptions and unverified items. Distinguish static inspection, visual inspection and runtime execution. Never fabricate browser results, screenshots, independent auditors or numerical proof.
- Apply the following 100-point rubric, scoring only evidence-supported performance:

| Criterion | Points |
|---|---:|
| Geometric and dimensional accuracy | 30 |
| Component completeness | 20 |
| Spatial and technical correctness | 15 |
| Visual fidelity | 15 |
| Interactivity and usability | 10 |
| Rendering performance | 5 |
| Code quality | 5 |

PASS requires at least 95/100 AND no critical defects or unverified essential requirements. Incorrect critical dimensions, material engineering errors, fabricated source data, incomplete essential components, unusable rendering, or nonfunctional essential controls automatically fail. See [audit protocol](references/audit-protocol.md) for evidence and reporting.

## 6. Rework and platform adaptation

- Fix defects and recheck the affected model plus integrated artifact until PASS or a real execution/data blocker. Do not inflate scores or retry blindly. If unable to pass, deliver useful results explicitly as provisional/incomplete with blockers and actual verification coverage.
- For complex jobs, optionally compose with Delegate. Preserve its worker contracts and independent audit when available. The stricter 95/100 Three.js gate still applies; Delegate's 9/10 gate cannot override it. Do not assume agents or browsers exist.
- On Gemini Task/ChatGPT Work, use actual available workspace, browser and worker tools to verify the file. On chat-only environments, use real execution tools where available; otherwise perform static review and disclose missing runtime or independent checks. Native installation is optional; this main file contains the core workflow even if supporting references cannot be loaded.
- Deliver the artifact, concise instructions for opening it, scope/assumptions, and actual audit score/verdict and verification limitations. This is not a professional engineering certification.

## Embedded and audit-only composition

When a presentation skill owns the requested single-file artifact, supply a scoped scene/component rather than a second HTML document; the shell owns stage, navigation and global fullscreen, while 3D owns geometry, camera, local rendering and model interactions. Define mount/resize/activate/deactivate/reset/dispose behavior, preserve logical canvas dimensions and local gesture ownership, pause inactive rendering, and verify the integrated candidate. For audit-only requests, inspect the existing source and apply the 3D rubric without unsolicited rebuilding or modification.
