# Skill taxonomy

Categories and subcategories organize the library; they are not executable instructions. Skills are independently installable leaf directories with SKILL.md. The registry is the authoritative list of implemented skills.

| Category | Active Subcategories (Implemented Skills) | Planned / Reserved Subcategories (Not Implemented) |
|---|---|---|
| `orchestration` | `delegation` (`delegate`), `planning` (`ask`), `execution` (`max`) | — |
| `civil-engineering` | `construction-management` (`estimate`) | `structural`, `geotechnical`, `hydraulics`, `surveying`, `transportation`, `materials-testing`, `environmental` |
| `visualization` | `3d-modeling` (`3d`), `animation` (`animate`), `image-analysis` (`count`) | `2d-illustration`, `interactive-simulations`, `cad` |
| `artifact-production` | `presentations` (`msdeck`) | `html`, `documents`, `spreadsheets`, `pdf` |
| `quality-assurance` | `artifact-audit` (`review`), `technical-audit` (`live-browser-qa`) | `code-audit`, `remediation` |
| `education` | — | `instructional-materials`, `assessment`, `curriculum`, `pedagogy` |
| `research` | — | `literature-review`, `source-verification`, `methodology` |
| `data-analysis` | — | `statistics`, `data-cleaning`, `data-visualization` |
| `software-engineering` | — | `implementation`, `debugging`, `architecture`, `performance` |

## Storage and composition

Use skills/<category>/<skill-id>/SKILL.md for broad skills, or skills/<category>/<subcategory>/<skill-id>/SKILL.md when specialization warrants another folder. Keep globally unique stable skill IDs regardless of directory depth. A single canonical skill can have many tags and serve several categories. Do not duplicate Three.js instructions across civil engineering, architecture and teaching.

Example: a future interactive RC beam teaching simulation could combine reinforced-concrete-design, instructional-materials, threejs, html-artifact and delegate. These illustrative IDs are not registered implementations yet.

## Expansion

Add new subcategories to registry.json as needed. Prefer separate skills when the execution contract, prerequisites or deliverable materially differs; use references for variants that share the same workflow. Avoid category-level catch-all skills containing unrelated procedures.


9 categories, 40 subcategories: 10 active and 30 planned/reserved.
