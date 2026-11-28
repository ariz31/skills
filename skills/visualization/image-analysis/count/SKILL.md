---
name: count
description: Count clearly identifiable target objects in an uploaded image, render high-contrast numbered overlays directly onto the original image, and present a concise tabulated breakdown. Use when invoked with @count or /count, or whenever the user asks to count items, people, vehicles, or specific objects in an image.
---

# Count

Count clearly identifiable target objects in an uploaded image, draw high-contrast numbered overlays directly onto the original image, and return a concise Markdown table.

## 1. Activation & Non-Activation

- **Activate** on `@count`, `/count`, or requests to count objects, people, vehicles, equipment, or items in an uploaded/attached image with visual verification.
- **Do not activate** for counting words, lines, CSV/spreadsheet rows, database records, or text occurrences; use ordinary assistance or data tools instead.

## 2. Inputs, Constraints & Deliverables

- **Inputs:** Source image (PNG/JPEG/WebP) and target object class (default: primary distinct subjects if unspecified).
- **Hard Constraint:** Never use generative image-editing models to recreate the photo with numbers; generative models alter pixels and miscount. Always draw programmatically onto the original image (e.g., Python PIL/Pillow).
- **Deliverables:** (1) Annotated image saved and presented to the user; (2) Concise Markdown count table with verified **Total**.

## 3. Ordered Execution Procedure

1. **Inspect & Scope Target:** Load the original image at native resolution. Lock the exact target class. Apply strict counting: include only clearly identifiable instances; exclude heavily occluded, motion-blurred, or ambiguous shapes (disclose notable exclusions in one brief line after the table).
2. **Systematic Coordinate Scan:** Scan left-to-right, top-to-bottom. Assign sequential integers starting at `1`. Record each item's `(x, y)` center or bounding box `(x1, y1, x2, y2)` and a short distinguishing attribute (color, subtype, or zone).
3. **Programmatic Overlay (PIL/Pillow):** Copy the original image and draw markers scaled to image dimensions:
   - *Dense, small, or overlapping objects:* Compact circular badges with centered numbers.
   - *Larger, well-separated objects:* Clean bounding boxes with a numbered corner tag.
   - *Legibility:* Load a TrueType font (e.g., `DejaVuSans-Bold.ttf`) sized to ~2%–3% of the image's shorter side (never tiny default bitmap fonts). Use high-contrast fills (e.g., red or yellow) with contrasting stroke and text.
4. **Visual Verification Gate:** Inspect the rendered annotated image directly before responding. Confirm: (a) every marker sits on its intended object; (b) numbering is strictly `1..N` with zero gaps or duplicates; (c) `max(marker) == reported Total`. Fix and re-render if any check fails.
5. **Deliver Response:** Lead with the annotated image and a concise Markdown table:
   - *Standard counts (`<= 20`):* Columns `# | Item / Description | Location`, ending with **Total**.
   - *High-density counts (`> 20`):* Grouped summary by category, color, or zone with subtotals and **Total**.

## 4. Quality Gates, Critical Defects & Fallback

- **Critical Defects (Block Delivery):** Generative image recreation; marker-to-total mismatch; duplicate/skipped numbers; illegible microscopic labels; counting unverified/hallucinated objects.
- **Fallback:** If Python/PIL execution or file rendering is unavailable, report a visual-only count with spatial zone descriptions and explicitly disclose `ANNOTATION UNRENDERED (NO IMAGE EXECUTION RUNTIME)`.

## 5. References & Dependencies

- Follows global library invariants (`docs/INVARIANTS.md`).
- No required or optional skill dependencies.
- Platform adapter: [Gemini Task adapter](adapters/gemini-task.md).
