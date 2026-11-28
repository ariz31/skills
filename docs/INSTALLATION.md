# Invocation and optional installation

## Dynamic invocation (read-only default)
Use the README prompt; pin the default-branch commit and retrieve ROUTER.md, registry.json, docs/INVARIANTS.md and selected skills/references. Runtime invocation never calls native save/update. No installation is required.

## Explicit install, sync, and update commands
Commands are case-insensitive. Only explicit user requests trigger writes:
- install ariz31/skills: all active skills.
- install ariz31/skills <id> (space/comma-separated IDs or aliases): selected skills and transitive required dependencies; ask whether relevant optional dependencies should be installed.
- sync ariz31/skills: inventory missing and drifted active skills; show missing-install and drift-update lists plus the local-versus-remote diff; obtain one explicit confirmation of the reconciliation plan before writes. Leave local-only skills untouched.
- update ariz31/skills [id]: refresh matching already-installed skills only; show local vs remote version/commit/content and obtain confirmation.

## Duplicate protection and dependency order
Inventory installed user:<id> before writes. For existing skills or already_exists, stop for that skill and present ID, local file/version state, pinned remote version and key differences. Ask Update, Skip or Install under a user-supplied alternate name. Never auto-overwrite, re-enable disabled skills, or delete local-only skills. Report disabled status and seek separate explicit permission before enabling. If removal is requested and no delete tool exists, direct the user to the host Skills Manager. Install required dependencies first in topological order. Conditional Animate dependencies are resolved at runtime (see its SKILL.md). For alternate names use --rename <new_name> with one selected skill. Retire superseded local browser QA only on explicit confirmation, through available enable/disable tools or host UI.

## Gemini Task native installation
Inspect actual signatures. Single-file packages: skills:save_skill(content=...), or confirmed skills:update_skill(name=..., content=...). Multi-file: python3 scripts/package_skill.py --skill <id> --platform gemini-task --format dir --output-dir /tmp/ariz31_staged; use its resolved absolute skill_dir with skills:save_skill or confirmed skills:update_skill(name=..., skill_dir=...). Bundle invariants by default. Check response status: created/updated record ID, version, commit and files; already_exists stop and confirm; error disclose exact error and fallback. Verify installed contents, enabled status and version using real inventory tools (lookup_skills/get_skill_resources where exposed); never claim parity without checking.

## ChatGPT and manual ZIP fallback
If native tools unavailable, python3 scripts/package_skill.py --skill <id> --platform portable --format zip --output-dir dist (or --all, preferably with --bundle-invariants). Deliver verified ZIP for manual host import/Project Files/Custom GPT Knowledge, not a claim of native installation. If shell unavailable, provide pinned raw.githubusercontent.com/ariz31/skills/<commit_sha>/<path> URLs for SKILL.md, invariants, adapters and references. Host support varies. Dynamic read-only invocation remains available.
