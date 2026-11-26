---
name: max
description: Execute demanding tasks with two coordinated Delegate cycles, a fresh holistic goal audit, and bounded evidence-driven remediation. Invoke with @max, /max, or explicit requests for maximum rigor, double delegation or verified multi-cycle delivery.
---

# Max

Max is the outer execution coordinator, not another worker or a replacement for Delegate. Deliver the user's actual requested outcome, not a description of the work.

## Activation and preflight

Use for explicit commands (case-insensitive whole tokens), or clearly requested high-rigor multi-cycle execution. Do not trigger on incidental uses of "max", mathematical maximums, simple factual questions, or routine edits unless explicitly selected. If no task is known, ask for the objective. Honor scope, output format, permissions, and test restrictions. No mutation or external action without authorization.

Load required [Delegate](../delegate/SKILL.md), its audit contract, and [goal audit contract](references/goal-audit-contract.md). Resolve relevant domain/artifact skills at the same registry revision. If Ask is selected, complete its intent confirmation before implementation or dispatch. Missing required instructions are a compliance blocker; retrieve them or disclose inability. Detect actual worker, workspace, execution and verification capabilities; use [Gemini Task adapter](adapters/gemini-task.md) only on that host when supported.

## Execution

1. Freeze the original goal, requirement IDs, exclusions, artifact format, authorized actions, domain constraints, evidence and acceptance tests. Define a shared workspace/board when available and an execution budget (time/tool/work limits). Pin source revisions. One coordinator owns dispatch, integration and all retries; never nest subagents.
2. **Delegate cycle 1 — build:** Use Delegate's worker contracts, appropriate topology, assembly, exact-candidate verification and 9/10 gate. Preserve accepted workstreams and evidence. Keep the candidate internal; no premature delivery or publication. If the cycle cannot pass, stop on a hard blocker; otherwise use the bounded rework policy below.
3. **Delegate cycle 2 — adversarial improvement:** Provide the original requirements, exact cycle-1 candidate, and relevant evidence to fresh challengers or separate role passes. Reassess omissions, assumptions, correctness, integration and real usability. Repair only evidenced defects; do not rebuild good work or manufacture changes. Reassemble and apply Delegate's 9/10 gate to the revised candidate, retaining separate evidence for both cycles.
4. **Independent Goal Auditor:** When supported, dispatch a fresh auditor not involved in either cycle; provide original requirements, exact candidate identifier/content and verification access, not prior scores or desired findings. Assess actual goal fulfillment, including applicable domain gates. Use the goal audit contract; require 10/10, GOAL_ACHIEVED true, no unresolved defects or unverified essential requirements, and all selected skill gates on the same final revision. Share evidence across gates, not scores. Do not publish a perfect score as proof of absolute defect absence.
5. **Bounded remediation:** On rejection, target identified defects through the coordinator using Delegate's worker contracts. Recheck affected requirements, integration and any invalidated gate on the revised candidate; obtain a fresh goal audit when independent review is available. Allow at most three outer remediation rounds total, inclusive of rejected cycle gates; do not restart both full cycles or grant each nested skill a new retry budget. Delegate's internal targeted attempts must fit the shared execution budget, its own hard-blocker policy and the outer bound; stop earlier when blocked or further work is impossible. An outer round is one coordinated fix batch plus re-audit, not one per worker. Initial planned cycles and initial goal audit are not outer remediation rounds.
6. Deliver only the exact accepted artifact using the actual available mechanism. Report both cycle gates, goal verdict, other applicable gates, audit independence, concrete evidence and limitations. If exhausted, incomplete, or blocked, return useful verified partial results with the Gap Report; do not call them complete or certified.

## Fallback and critical defects

Without native workers, perform two distinct sequential role-based Delegate cycles and a separate holistic self-audit; record mode SELF-REVIEW, never invent agent identities or tool results. A 10/10 self-review is a scoped self-review result only; if independent verification is explicitly required, its absence blocks acceptance. Missing essential verification blocks PASS. Respect user exclusions on tests and distinguish allowed static evidence from unexecuted runtime checks. Unauthorized mutation, omitted required steps, invented proof, stale artifact evidence, failed selected gates, or presenting incomplete work as accepted are critical defects. A user-requested read-only review remains read-only even under Max; the candidate is the report, not the reviewed source.

See [evaluation scenarios](evaluations/SCENARIOS.md).
