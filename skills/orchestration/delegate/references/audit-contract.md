# Strict Final Auditor contract

Audit the exact candidate artifact and original user request. Do not grade the producer's summary alone. Record artifact path/revision, audit mode (independent or self-review), and each requirement's evidence.

| Criterion | Maximum |
|---|---:|
| Requirement coverage | 3 |
| Accuracy and grounding | 3 |
| Format appropriateness | 2 |
| Polish and clarity | 2 |
| Total | 10 |

## Critical-defect veto

A score >= 9 is necessary but not sufficient. Fail if an essential requirement is omitted or unverified, a material engineering or calculation error exists, sources/evidence are fabricated, the requested artifact is unusable, or a critical safety/security constraint is violated. Deduct for lesser defects. Distinguish executed tests, static inspection, and unavailable checks. Do not run tests expressly excluded by the user; use appropriate allowed verification and explain what remains unverified.

## Report format

AUDIT MODE: INDEPENDENT or SELF-REVIEW
ARTIFACT: exact path/revision or content identifier
SCORE: X/10
VERDICT: PASS or FAIL
PROOF: checks actually performed and results
DEFECTS: numbered findings with requirement ID, severity, evidence and correction
TRACEABILITY: requirement → evidence → pass/fail/unverified

A self-review may report a score and verdict, but never claim independence. If a genuinely independent audit is explicitly required, its absence is a blocker. Re-audit after changes, using the revised artifact. No fabricated evidence.


### 0. Triage and Select Execution Mode

- If critical requirements, constraints, or target files are ambiguous, clarify them before spawning sub-agents so you do not waste a swarm on the wrong spec.
- Pick the execution shape that fits the problem:
  - **Parallel Fan-Out (Default):** Broad tasks that split cleanly into 2 to 6 independent workstreams (research facets, document sections, separate code modules, or multi-item audits).
  - **Iterative Challenge Loop:** Hard, tightly coupled problems (root-cause debugging, proofs, algorithmic optimization, or tricky refactors) where splitting artificially hurts quality. Run a focused Builder → Adversarial Challenger → Fixer cycle instead.
- Respect dependencies; do not launch a dependent workstream before its required inputs exist.

### 1. Plan, Shared Board, and Worker Contracts

- Identify the user's core objective, constraints, and target deliverable format (.md, .html, .pdf, .docx, .xlsx, source code, or a structured chat answer). If unnamed, choose the format best suited to the output.
- For multi-file or complex runs, write a lightweight shared board.md in the workspace containing the overall plan, shared conventions/interfaces, and each worker's dedicated scratch path (work/<worker-slug>/) so workers do not overwrite each other's files or drift on terminology. If no filesystem is available, maintain an equivalent structured plan in context.
- Partition Parallel Fan-Out tasks into 2 to 6 non-overlapping workstreams. Give every worker a strict 3-part brief:
  1. **Owns:** Exact scope, sections, or files assigned to this worker.
  2. **Must Not Touch:** Explicit out-of-scope boundaries to prevent duplication or edit collisions.
  3. **Done Criteria + Evidence:** Required output structure, citations, or test proof.
- Record requirement IDs and their expected verification evidence.

### 2. Dispatch Workers and Manage Lifecycle

- Launch worker sub-agents concurrently via the available native dispatch tool with a concise role (2 to 5 words) and a self-contained prompt referencing board.md (when used) and their 3-part contract.
- On every sub-agent wakeup, check all dispatched sub-agents via the available status/list tool and read completed outputs via the available read tool.
- **Per-worker failure recovery:** If one worker stalls, errors, or returns incomplete output, re-task or replace only that workstream using messaging or a fresh worker while preserving completed workers' verified outputs.
- **Scaled mid-pipeline check (4 to 6 workers):** On large runs, optionally dispatch a lightweight Workstream Verifier (1 per 2 to 3 workers) to check cross-worker consistency and catch broken assumptions before final assembly.

### 3. Assemble and Verify Output Format

- Combine verified worker outputs into a unified draft deliverable.
- **Keep the coordinator clean:** For large multi-file deliverables, long reports, or multi-module codebases, offload assembly to a dedicated Deliverable Assembler sub-agent—passing it the workers' output file paths rather than pulling all raw drafts into the main context. If unavailable, assemble directly.
- Confirm technical and format soundness before auditing:
  - .html: valid markup, clean responsive CSS, no broken layouts or missing assets.
  - .md: clean heading hierarchy, valid tables and links, no stray artifacts.
  - Code/data files: runnable, syntactically valid, and free of placeholder stubs.
  - PDF, DOCX and XLSX: check actual rendering or workbook integrity and formulas as applicable, using available tools.
- Save file-based deliverables to disk (or Workspace if requested) so the Final Auditor inspects the exact artifact rather than a summary.

### 5. Targeted Rework Until Accepted

- If the auditor returns VERDICT: FAIL, do not deliver the draft as a completed artifact.
- Route each listed defect to the responsible worker (messaging or fresh dispatch) or to the assembler for targeted fixes.
- Re-submit the revised artifact to the Strict Final Auditor for re-scoring.
- Repeat until VERDICT: PASS with SCORE >= 9/10, subject to actual execution limits and hard blockers.
- Only after passing the 9/10 gate, deliver the final output using the actual available delivery mechanism (Workspace link, generated file, or inline reply) and briefly report the final audit score and whether the review was independent.
- If a genuine hard blocker prevents acceptance, report the failing verdict, evidence, unresolved requirements and useful partial output explicitly as incomplete; never falsely certify.

## Gotchas

- **No nested sub-agents:** Worker, assembler, and auditor sub-agents must not spawn sub-agents under this workflow. Keep all orchestration, triage, and retry loops in the main agent.
- **Prevent lenient grading:** Require PROOF of executed checks and instruct the auditor to deduct points for any minor gap, formatting flaw, or unverified claim. A rubber-stamp 9/10 defeats the gate.
- **Check all sub-agents on every wakeup:** Multiple sub-agents finishing near the same time can trigger only one notification. Always check every worker's actual status.
- **Isolate worker failures:** Never discard good workstreams when one worker fails or stalls; replace or re-prompt only the failing slice.
- **Avoid infinite loops on hard blockers:** If a deliverable fails to reach 9/10 after 3 consecutive revision cycles due to missing user input, an inaccessible external source, or contradictory requirements, stop blind retries and identify the blocker or ask the user to resolve it. Stop earlier if further work is impossible.
- **Match delivery to format:** Do not paste long .md or .html deliverables into chat when a standalone file is expected, and verify the file exists and is accessible before presenting it.

## Composition boundaries

When used by a higher-order coordinator such as Max, run the requested cycle under the shared execution budget and keep intermediate accepted candidates internal until the outer gate is resolved. Do not create nested worker coordinators or independently reset retry budgets. When used by Review or a read-only audit, workers inspect only the audited source; remediation targets the report, not the source, unless the user separately authorizes source edits. Apply the 9/10 gate to the requested deliverable (the report for an audit), not to the source's separate verdict. When embedded in a larger artifact, coordinate on the integrated final candidate and honor all selected skill gates and artifact ownership.
