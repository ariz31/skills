# Media and stepped solutions

## Technical pedagogy

Use the learner level, objective and prerequisite knowledge to plan the explanation. For computational problems present givens/units, assumptions, governing relation, symbolic substitution, numeric calculation, result with precision/units, and independent reasonableness check as relevant. Reveal one meaningful logical step at a time; synchronize diagram highlights, labels and algebra with the same step ID. Provide concise captions/alt text and non-motion alternatives. Keep earlier steps visible when useful; never change values or formula semantics during a purely visual transition.

Store slide manifest, step state, solution data and visualization state separately. Derive rendered state from slide/step and validated parameter revision, not accumulation of DOM effects. Reverse/skip/revisit/reset must restore correct state; use deterministic time mapping for animation, maintaining physical time independently of playback speed. Respect reduced-motion and pause on inactive slides. Apply Animate for phase-based simulations and 3D for actual 3D modeling when relevant.

## Visual sourcing

Prefer original accurate SVG/diagrams for technical content. For external images verify source, depicted subject, usage/license and attribution; do not fabricate provenance or use unverified assets as evidence. Inspect actual images, including a contact sheet for batches when supported; reject mismatched, distorted, low-resolution, watermarked, or irrelevant content. If inspection/retrieval unavailable, prefer authored SVG and disclose unavailable external image checks. Inline verified raster assets as correctly typed base64 data URIs, generally downsample to at most 760 px on the long edge for ordinary slide media; retain higher resolution when essential for legibility, zoom or technical detail and document the exception. Do not upscale or destroy diagnostic detail. Preserve aspect ratio using object-fit: contain, meaningful alt text and captions; no stretch or crop of required content. Record source URL/author/license for retrieved assets.

## Lightbox

Use a single #deck-lightbox or equivalent namespaced accessible dialog for zoomable images. Open by click or keyboard, display full available asset without distortion, provide zoom/reset/close controls and keyboard support. Escape closes lightbox before other shortcuts; restore focus to trigger and prevent background navigation/scroll while open. Do not trap users without an exit. Provide labeled fallback if dialog API unavailable. Avoid injecting untrusted markup or remote scripts.
