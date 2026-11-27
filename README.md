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
- [Animate](skills/visualization/animation/animate/SKILL.md): phase-based animations and simulations with deterministic playback, minimal fullscreen UI and a 95/100 audit. Invoke with `@animate`, `/animate` or animation requests; automatically composes with Delegate and 3D when applicable.

- [Max](skills/orchestration/max/SKILL.md): two coordinated Delegate cycles, holistic 10/10 goal audit and bounded remediation. Invoke with `@max` or `/max`.
- [MSDeck](skills/artifact-production/presentations/msdeck/SKILL.md): minimalist interactive 16:9 HTML learning presentations with step navigation, simulations and zoomable media. Invoke with `@msdeck` or `/msdeck`.
- [Review](skills/quality-assurance/review/SKILL.md): read-only adversarial review and evidence-based scoring with interactive HTML dashboard or requested report format. Invoke with `@review`, `/review`, `@reviewer` or `/reviewer`.

- [Estimate](skills/civil-engineering/construction-management/estimate/SKILL.md): construction cost estimates, BOQ/BOM, unit pricing, Philippine permit/VAT planning and zero-variance reconciliation with mandatory Delegate. Invoke with `@estimate` or `/estimate`.

## Gemini native installation

When the interface supports native skills, users may choose to install an individual skill using its SKILL.md and any needed adapter/reference files. See [installation guidance](docs/INSTALLATION.md). Do not automatically create or install native skills.

## Status

The active skills are Ask, Delegate, Max, 3D, Animate, MSDeck, Review, and Estimate. Other categories and subcategories are reserved for future specialized skills; they are not implemented merely by being listed. Platform functionality is capability-dependent and must be checked at runtime.

## Design principles

Canonical skills are small, independently executable and composable. A hierarchical taxonomy organizes them; metadata enables cross-category discovery. Load only relevant instructions. Verify actual deliverables, disclose blockers and never fabricate tool execution or independent review.
