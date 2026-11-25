# ariz31/skills

A portable, composable skill library for civil engineering analysis, university teaching, research, technical visualization and artifact production, optimized for Gemini Chat/Task and ChatGPT Chat/Work.

## Invoke the library

In any supported chat or work environment, say:

> Use ariz31/skills to complete my request. Read ROUTER.md and registry.json from the current default branch, discover the relevant skills automatically, and follow their instructions using the capabilities actually available.

The repository is not an automatically installed plugin. The assistant must have repository access (GitHub connector or web retrieval), or the user must provide the files. Invocation is a conversational convention, not a guarantee of execution or persistent installation.

- [Router](ROUTER.md): selection, composition, execution and fallback.
- [Registry](registry.json): machine-readable catalog of available skills.
- [Taxonomy](docs/TAXONOMY.md): categories and planned specialization.
- [Authoring standard](docs/SKILL_STANDARD.md): contracts and contribution requirements.
- [Platform profiles](platforms/README.md): capability-aware execution.
- [Ask](skills/orchestration/ask/SKILL.md): intent clarification, multiple-choice disambiguation, explicit assumptions, and pre-implementation verification. Invoke with `@ask`, `/ask`, ideation prompts, or high-ambiguity requests.
- [Delegate](skills/orchestration/delegate/SKILL.md): multi-agent coordination and strict auditing.
- [3D](skills/visualization/3d-modeling/3d/SKILL.md): source-grounded interactive 3D models with a 95/100 technical quality gate. Invoke with `@3d`, `/3d`, 3D, Three.js, threejs or related modeling terms. The former skill name `threejs-modeling` remains an invocation alias.

## Gemini native installation

When the interface supports native skills, users may choose to install an individual skill using its SKILL.md and any needed adapter/reference files. See [installation guidance](docs/INSTALLATION.md). Do not automatically create or install native skills.

## Status

The active skills are Ask, Delegate, and 3D. Other categories and subcategories are reserved for future specialized skills; they are not implemented merely by being listed. Platform functionality is capability-dependent and must be checked at runtime.

## Design principles

Canonical skills are small, independently executable and composable. A hierarchical taxonomy organizes them; metadata enables cross-category discovery. Load only relevant instructions. Verify actual deliverables, disclose blockers and never fabricate tool execution or independent review.
