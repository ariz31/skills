# Gemini Task adapter: Count

Use only actual exposed capabilities and authorized files. Inspect tool signatures; do not assume a tool exists.

| Operation | Preferred host mapping / fallback |
|---|---|
| Image inspection | Inspect uploaded image via `view_file` (or native image input) at full resolution; never guess unseen regions |
| Programmatic annotation | Run a Python 3 script using `Pillow` (`PIL`) via `execute_bash` reading from the uploaded file path and writing `<output_name>_annotated.png` into the deliverable output directory |
| Forbidden tool guard | Never call `image_gen:generate_image` or generative photo editors to place numbers onto the image |
| Visual verification | Inspect the rendered `<output_name>_annotated.png` via `view_file` to verify marker placement, legibility, and `1..N` parity before delivery |
| Delivery | Present the annotated PNG via `google:show_file` (returning `[file-tag: ...]`) alongside the concise Markdown table in chat |
| Fallback | If `execute_bash` or `Pillow` is unavailable, deliver a visual-only spatial table and explicitly disclose that annotated image rendering was unavailable |

Do not invent file paths or claim visual verification without inspecting the rendered output image. Keep chat prose minimal so the annotated image and table lead.
