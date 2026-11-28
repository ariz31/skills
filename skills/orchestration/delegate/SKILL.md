---
name: delegate
description: Orchestrate multi-agent execution using structured worker contracts, shared workspace coordination, format-appropriate deliverable assembly, and an evidence-driven Strict Final Auditor gate requiring at least 9/10. Use for explicit delegation, parallelization, agents, swarms, divide and conquer, or complex multi-part deliverables requiring specialized workers.
---

# Delegate

Use for explicit delegation, parallel agents, swarms, divide-and-conquer or complex specialized multi-part deliverables. Avoid unnecessary delegation for simple single-step work. Resolve critical ambiguity before dispatch; if Ask is selected, finish its Intent Check.

Detect dispatch/status/messaging/workspace/delivery tools; use [Gemini Task adapter](adapters/gemini-task.md) if applicable. Without native workers use separate sequential role passes and label non-independent SELF-REVIEW; disclose if independence is mandatory.

## Workflow
1. Triage: Parallel Fan-Out (2–6 non-overlapping workstreams) for separable work, or Iterative Challenge Loop (Builder → Adversarial Challenger → Fixer) for tightly coupled tasks. Respect prerequisites and preserve completed verified work.
2. Freeze objective, constraints and output format. Record requirement IDs and evidence in shared board.md with conventions, interfaces and work/<worker-slug>/ scratch paths (or equivalent structured context). Give each worker **Owns / Must Not Touch / Done Criteria + Evidence** contracts. Avoid collisions and inconsistent terminology.
3. Dispatch independent workers concurrently if supported, with self-contained briefs and 2–5 word roles. On every wakeup check all workers and read completed outputs; re-task only stalled or failing workstreams. For 4–6 workers optionally use a Workstream Verifier per 2–3 workers.
4. Assemble verified outputs, offloading large multi-file deliverables to a dedicated assembler when available. Apply pre-audit format checks from the mandatory [audit contract](references/audit-contract.md): HTML layout/assets; Markdown headings/tables/links; code/data syntax and runnable completeness; PDF/DOCX/XLSX rendering or integrity/formulas. Save exact file candidates.
5. Dispatch a fresh independent Strict Final Auditor where possible, with original request, constraints and exact artifact. Require actual verification evidence, respecting user test limits. Apply the audit contract's rubric (coverage 3, accuracy 3, format 2, polish 2). Output SCORE, VERDICT, PROOF, DEFECTS. PASS only at ≥9/10 with zero critical defects or unverified essential requirements. Deduct for every gap; no rubber stamps.
6. On FAIL target listed defects to responsible workers/assembler, preserve accepted work, resubmit revised candidate. Stop blind retries after three consecutive cycles due to hard blockers (or earlier if impossible); report failing verdict, evidence and incomplete results. Deliver only the actual accessible file or requested format, with score and independence disclosure.

## Composition
Max owns shared cycles and retry budget; no nested coordinators or budget resets. Review's source remains read-only; remediation and Delegate's gate apply to the report, not its separate source verdict. Embedded components share the integrated final candidate, artifact ownership and independent skill gates. Load the mandatory audit contract for full workflow, verification, scoring and recovery details.
