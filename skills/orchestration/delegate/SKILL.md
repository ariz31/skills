---
name: delegate
description: Orchestrate multi-agent execution using structured worker contracts, shared workspace coordination, format-appropriate deliverable assembly, and an evidence-driven Strict Final Auditor gate requiring at least 9/10. Use for explicit delegation, parallelization, agents, swarms, divide and conquer, or complex multi-part deliverables requiring specialized workers.
---

# Delegate

Orchestrate multi-agent execution using structured worker contracts, shared workspace coordination, format-appropriate deliverable assembly, and an evidence-driven Strict Final Auditor gate that only accepts outputs scoring at least 9/10.

## When to Use

- The user explicitly asks to "delegate", "split the task", "implement agents", or "use agents".
- The user requests parallel sub-agents, multi-agent workflows, a swarm, or a "divide and conquer" approach.
- The user wants a multi-part deliverable built by specialized agents and verified by a strict quality auditor before delivery.
- Avoid unnecessary delegation for simple, single-step tasks unless explicitly requested.

## Capability preflight

Detect the actual tools for dispatch, status, messaging, workspace and delivery. On Gemini Task, use [its adapter](adapters/gemini-task.md) when the named tools are available. On any other host, use equivalent real tools. If native workers are unavailable, implement the same contracts as sequential role passes, preserve outputs separately where possible, and explicitly label the final audit as non-independent self-review. Never fabricate worker identities, messages or execution evidence. If the user explicitly requires independent workers and none are available, disclose the limitation.

## Workflow

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

### 4. Run the Evidence-Driven Final Auditor (9/10 Gate)

- Spawn an independent auditor sub-agent with role Strict Final Auditor when native independent workers are available. Otherwise perform a separate explicitly non-independent audit pass.
- Pass the original user request, all constraints, and the exact deliverable content or file path.
- Instruct the auditor to execute verification checks—running code or tests, inspecting rendered HTML/PDF/images, and checking calculations or source URLs—rather than grading prose alone. Respect explicit user limits on tests; distinguish static verification from runtime checks.
- Require strict scoring on this 10-point rubric:
  1. **Requirement Coverage (3 pts):** Every user requirement, constraint, and edge case is completely satisfied with zero placeholders or omissions.
  2. **Accuracy and Grounding (3 pts):** All facts, calculations, code, and source links are verified against real execution or primary sources and are internally consistent.
  3. **Format Appropriateness (2 pts):** The chosen format matches the user's request and fits the content, with clean structure and valid rendering.
  4. **Polish and Clarity (2 pts):** Presentation, writing, or code quality is publication-ready, concise, and free of visual or structural defects.
- Require the auditor to output:
  - SCORE: X/10
  - VERDICT: PASS (only when SCORE >= 9 and no critical defects or unverified essential requirements) or VERDICT: FAIL (whenever SCORE < 9 or a critical defect/verification gap exists)
  - PROOF: Concrete verification checks actually executed (commands run, test results, rendering/link checks or explicit static inspection)
  - DEFECTS: Numbered list of specific, verifiable issues that must be fixed to reach at least 9/10 and remove blockers
- Use [audit-contract.md](references/audit-contract.md) for evidence and traceability requirements.

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
