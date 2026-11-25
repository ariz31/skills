# Skill taxonomy

Categories and subcategories organize the library; they are not executable instructions. Skills are independently installable leaf directories with SKILL.md. The registry is the authoritative list of implemented skills.

| Category | Subcategories |
|---|---|
| orchestration | delegation, planning, execution |
| civil-engineering | structural, geotechnical, hydraulics, surveying, transportation, construction-management, materials-testing, environmental |
| education | instructional-materials, assessment, curriculum, pedagogy |
| visualization | 2d-illustration, 3d-modeling, interactive-simulations, cad, animation |
| research | literature-review, source-verification, methodology |
| data-analysis | statistics, data-cleaning, data-visualization |
| artifact-production | html, documents, spreadsheets, presentations, pdf |
| software-engineering | implementation, debugging, architecture, performance |
| quality-assurance | technical-audit, code-audit, artifact-audit, remediation |

## Storage and composition

Use skills/<category>/<skill-id>/SKILL.md for broad skills, or skills/<category>/<subcategory>/<skill-id>/SKILL.md when specialization warrants another folder. Keep globally unique stable skill IDs regardless of directory depth. A single canonical skill can have many tags and serve several categories. Do not duplicate Three.js instructions across civil engineering, architecture and teaching.

Example: a future interactive RC beam teaching simulation could combine reinforced-concrete-design, instructional-materials, threejs, html-artifact and delegate. These illustrative IDs are not registered implementations yet.

## Expansion

Add new subcategories to registry.json as needed. Prefer separate skills when the execution contract, prerequisites or deliverable materially differs; use references for variants that share the same workflow. Avoid category-level catch-all skills containing unrelated procedures.
