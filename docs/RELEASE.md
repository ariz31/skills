# Release and rollback runbook

The canonical source is the pinned repository commit. Native skill synchronization and tags are separate, explicitly authorized operations.

## Version history and staging

The v0.7.0 baseline is c5c08751b0827d2de5ff996b1315ac2e589bdf86. The implementation blueprint separates v0.8.0 (adaptive Ask, portability and platform parity) and v0.9.0 (invariants, lean skills, installation, automation, Count and Live Browser QA). For a consolidated PR, the v0.8.0 changes are an intermediate implementation milestone, not a claim that a v0.8.0 release tag was published. Publish only a reviewed, merged version whose registry version matches its tag.

Before merging or tagging, run:

    python3 scripts/validate_registry.py --check-triggers --format json
    python3 -m unittest discover -s tests -v
    python3 scripts/package_skill.py --all --platform gemini-task --format dir --output-dir /tmp/ariz31_staged
    python3 scripts/package_skill.py --all --platform gemini-task --format zip --output-dir /tmp/ariz31_zip

Verify all active skills, package contents and hashes, required and optional dependency acyclicity, zero escaped links, and exact candidate CI. Deterministic command/alias/install cases are machine-checked; semantic/composition cases remain behavioral evaluation specifications until separately executed on real hosts.

## Native sync

Follow [installation guidance](INSTALLATION.md). Inventory installed skills and compare versions/files before mutation. Ask and Estimate may have legacy drift: the Ask adapter must enforce the three-question native call limit and Estimate must cap standalone intake at two questions total, not rounds. Stage the tagged release; use --include-evals if scenario files are needed for full package parity. Confirm all replacements and disabled-skill changes, install required dependencies first, and verify actual installed resources and behavior. Count may already be installed under user:count; never overwrite it without confirmation. Install Live Browser QA only on explicit request; retire the local-only live-browser-qa-audit only after explicit confirmation. Native tools may not exist on every host; provide verified ZIPs or pinned source links instead.

## Rollback

Before tagging, revert the offending merge commit on main using git revert -m 1 and a normal non-force push. After tagging, never move or delete a published tag: revert the offending change, bump the registry patch version, run validation and publish a new annotated tag only when authorized. For native rollback, stage the prior known-good release and obtain explicit confirmation before replacing an installed skill. Disable or re-enable affected skills only with user approval. Verify the rollback's actual revision, inventory and behavior.
