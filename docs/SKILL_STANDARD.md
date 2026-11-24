# Skill authoring standard

## Package

Every active skill has a globally unique lowercase kebab-case ID and a SKILL.md with YAML frontmatter containing name (matching its ID) and a useful description stating what it does and when to use it. Keep the main instructions concise. Use references/ for optional details, adapters/ for platform-specific instructions, and evaluations/ for test scenarios. Do not require network calls, scripts or special tools without a documented fallback or explicit capability requirement.

## Required content

- Purpose and activation criteria, including when not to use the skill.
- Inputs, constraints, assumptions and expected deliverables.
- Ordered execution procedure with evidence requirements.
- Quality gates, critical defects, fallback and failure recovery.
- Platform differences only where material.
- References and dependencies using stable identifiers or explicit relative paths.

For engineering skills, require units, governing equations, applicability, assumptions, independent numerical checks where feasible, and authoritative standards/edition when relevant. Never fabricate clauses or claim professional certification. Educational skills must specify learner level, objectives, accuracy and alignment of assessments. Artifact skills must validate the actual output, not merely its description.

## Registry contract (schema version 1)

Each skill entry includes id, name, version, status, category, subcategory, path, description, triggers, tags, outputs, required_dependencies, optional_dependencies, capabilities, platforms, references, and adapters. Paths are repository-relative. Versions use semantic versioning. Status is active, draft, or deprecated. Only active skills are selectable; required dependencies of active skills must also be active. Category and subcategory must exist in categories. Dependency IDs must exist; required dependency graph must be acyclic. Platform keys must correspond to documented profiles. No duplicated IDs or broken paths.

## Maintenance checklist

1. Read the current registry and related skills; avoid duplication.
2. Create or update the skill and related references, update registry and version.
3. Verify paths, frontmatter, triggers, dependency graph and platform fallback.
4. Evaluate positive and negative activation scenarios, capability degradation and output correctness.
5. Record meaningful limitations and never label unexecuted checks as tests passed.

Native installation is optional and user-controlled. The portable source is canonical. Do not make a native installation a prerequisite to library invocation.
