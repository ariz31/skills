# Rendering, interaction and delivery protocol

## Implementation

Use compatible pinned Three.js core and add-on imports. Prefer a single HTML deliverable with all authored data and code; embed dependencies/assets if offline self-containment is required and permitted. Otherwise disclose exact external assets and loading requirements (internet, local HTTP server, browser support). Avoid mixed versions, unresolved imports, CORS-dependent local paths, unlicensed asset reuse and secrets in HTML.

Configure scene/camera/renderer, color space, appropriate exposure, physically plausible lights/shadows and purposeful environment. Derive camera clipping and fit from model extent; avoid extreme near/far ratios. Resize using actual container dimensions, cap render pixel ratio as appropriate, and handle WebGL initialization/context loss gracefully.

Use material/geometry reuse, instancing for repeats, spatial chunking/LOD for large scenes, and dispose owned obsolete resources without disposing shared live assets. Prefer demand-driven rendering for static models, continuous frames only while needed. Measure actual frame performance when tools allow; report device/browser, resolution and scene complexity rather than asserting a universal FPS.

## Views and controls

Use perspective plus front/top/side/axonometric orthographic views where relevant. Provide fit, reset, orbit, pan, zoom, layer visibility and selection/inspection for complex models. Include meaningful component labels and dimensions, section planes and exploded/isolated modes when useful. Keep original geometry and presentation transforms separate; ensure clipping/visibility state and measurements are consistent. UI must remain usable on desktop and mobile without obscuring critical model content. Avoid adding unrelated features.

## Runtime verification matrix

1. Open exact delivered HTML via the promised launch method; confirm model appears and no fatal console or loading errors.
2. Inspect whole model, technical projections, critical connections and interior/cutaway views as applicable.
3. Exercise all implemented controls; verify state, reset, visibility, measurements and parameter changes.
4. Resize, test small-screen/touch behavior where possible, check text readability and interaction.
5. Inspect resource failures and test offline launch if promised. Check repeated updates and memory/resource disposal where applicable.

If a browser/runtime is unavailable, distinguish static review from runtime tests; never invent proof. If no file tool exists, provide complete code if practical, without a fictitious download.


## 3. Visual fidelity and interaction

- Use consistent PBR materials, plausible roughness/metalness, appropriate texture scale, correct normals, purposeful lights, physically credible shadows, color management and exposure. Handle glass, transparency, depth ordering and coplanar surfaces correctly.
- Combine realistic rendering with technical legibility. Preserve small details without gratuitous polygon density; never conceal geometric deficiencies with textures or shadows.
- Default to responsive orbit/pan/zoom, fit-to-model, perspective and orthographic presets, orientation reference, and logical component visibility. For complex assemblies, include object inspection and useful isolation controls. Add cutaways, exploded views, measurement, dimensions and layers when technically relevant.
- Support accurate dimension annotations and units, stable selection, useful camera presets, fullscreen when supported, touch and keyboard access, and compact controls with instant feedback. Every visible control must work. Preserve camera/selection on routine updates; reset only on request.
- For parametric models, validate inputs, regenerate dependent geometry consistently, and preserve all geometric relationships. If offering engineering calculations, derive them from verified equations, inputs and units; distinguish visualization from structural analysis.
- See this protocol for implementation details.

## 4. Build and deliver

- Default to a single HTML entry point containing authored code, model and UI. Prefer an offline self-contained file when practical. If external dependencies are needed, use pinned compatible Three.js/add-on versions, consistent imports, and explicit network/server requirements. A CDN-dependent HTML file is not offline self-contained.
- Use robust startup, resize, device-pixel-ratio management, error handling and WebGL capability feedback. Do not silently show a blank canvas. Use actual available libraries; never invent APIs.
- Use instancing, shared geometry/materials, suitable level of detail and resource disposal as applicable. Avoid unnecessary repeated scene rebuilding and idle rendering; preserve the requested detail and responsiveness.
- Separate model data, geometry builders, rendering, interaction and verification logically even within one HTML. No placeholders, dead controls, fake dimensions, broken assets or arbitrary source claims.
- Save and deliver the exact file when supported. If file creation is unavailable, provide complete HTML source if practical and disclose the limitation. Never invent artifact links.
