# Count evaluation specifications

Specifications, not executed platform tests.

| Scenario | Expected behavior |
|---|---|
| `@count` with photo of 8 parked cars | Programmatic PIL numbered overlays `1..8` on original image; itemized `# | Item / Description | Location` table; Total = 8. |
| `/COUNT` (uppercase) with unlabeled fruit photo | Case-insensitive activation; defaults to primary distinct subjects; numbered markers + table. |
| "How many chairs are in this classroom photo?" | Semantic activation without explicit `@count`; annotated image + itemized or grouped table. |
| "Count the words in this Markdown file" | Negative trigger: do NOT activate `count`; use ordinary text/script counting. |
| "Count rows where status == active in data.csv" | Negative trigger: do NOT activate `count`; handle as tabular data query. |
| High-density photo with 35+ people | Compact circular badges (not overlapping boxes); grouped summary table by zone/color with subtotals + verified Total. |
| Partially occluded / blurry background objects | Exclude unverifiable shapes from `1..N` count; add one brief exclusion disclosure line after table. |
| Marker numbering gap or mismatch during check | Visual verification catches mismatch; re-render before delivery; never ship `max(marker) != Total`. |
| Generative image tool available alongside Python | Strictly use Python PIL/Pillow on original pixels; refuse generative recreation. |
| Python / VM execution unavailable | Visual-only spatial breakdown with explicit `ANNOTATION UNRENDERED` fallback disclosure. |
