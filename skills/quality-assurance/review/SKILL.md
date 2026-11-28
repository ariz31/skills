---
name: review
description: Conduct evidence-based adversarial reviews of code, plans, presentations, documents or designs using Delegate, adaptive rubrics and actionable findings. Invoke with @review, /review, @reviewer, /reviewer or explicit critical review requests.
---

# Review

Audit an existing artifact against the user's intended goal and produce a traceable review report. Default for a standalone detailed audit is a single-file interactive dark HTML dashboard; honor explicit Markdown, structured chat or other supported report formats. Review is read-only toward the audited source unless the user separately authorizes changes.

## Activation and preflight

Recognize case-insensitive whole command tokens and aliases; load once. Use for substantive critical review, code/technical/artifact audit, rubric evaluation or adversarial review. Do not trigger from incidental mentions, literature-review explanations, quick fact checks or direct copy-edit/rewrite without requested audit. If no artifact or objective is known, request only missing essentials. Do not invent source content.

Pin the artifact/repository revision and identify goal, audience, format, audit scope, constraints, authorized actions, evidence sources and user-excluded checks. Resolve required canonical skill `delegate` and its audit contract, plus [rubric and scoring](references/rubric-and-scoring.md) and [dashboard spec](references/dashboard-ui-spec.md). If Ask is selected, confirm intent before dispatch. Missing required dependency instructions block compliant execution; missing required references must be retrieved or disclosed. Load selected domain skills to apply their existing rubrics, not to create unsolicited artifacts. Detect actual native worker, browser, file and execution capabilities.

## Workflow

1. Freeze the exact source revision and requirement inventory. Choose 4–6 weighted rubric dimensions totaling 100%, severity criteria, applicable domain-specific gates and acceptance thresholds before scoring. Record verification scope and unavailable evidence. Keep source unchanged, including when combined with Max or Delegate. Any actual remediation needs separate user authorization.
2. Use Delegate to partition non-overlapping adversarial audit lenses (e.g. correctness, coverage, security/reliability, usability, architecture, evidence), or use its tightly coupled challenge topology. Worker contracts own investigation and report findings only; no source edits, branches, PRs, external publication, destructive checks or nested agents. Read-only local checks and explicitly authorized non-mutating execution are permitted; respect exclusions. Preserve strong evidence; distinguish confirmed defects, risks, assumptions and unverifiable claims.
3. Consolidate and deduplicate findings by stable ID/root cause. Require exact location/revision, observed evidence, expected behavior/requirement, severity, impact, actionable correction and a verification criterion. Avoid unsupported claims, cosmetic inflation or double-counted deductions. Record positive coverage and unverified essentials; independently check material findings when possible.
4. Score against the frozen rubric and critical-defect veto. Apply selected domain rubrics separately; a generic score cannot override a failed domain gate. Distinguish verdict for audited source from Delegate's 9/10 gate for quality of the review report itself. A well-evidenced FAIL on source can be a high-quality PASS on report.
5. Produce the requested report. For dashboard, implement secure, accessible search/filter, expandable evidence cards, resolution tracking and prioritized remediation plan per reference. Status checkboxes are user-tracked, not proof of fixes; original score/verdict are immutable. Delegate may repair the report, never the audited source without authorization. Verify report against exact evidence and requested format, apply Delegate's report gate, rework report only within actual execution limits.
6. Return verified report/file, scope, source verdict and report audit mode, limitations and actionable next steps. No claim of code changes, independent verification or resolved findings without evidence.

## Fallback and critical defects

When native workers unavailable, run distinct sequential adversarial lenses and report SELF-REVIEW; never fabricate agents. If independent verification is explicitly required and unavailable, label provisional/blocked. If file creation unavailable, provide complete HTML source where practical or requested Markdown/structured report. If browser unavailable, static-check dashboard and disclose runtime controls unverified. Missing source, stale revision, invented evidence, unauthorized source mutation, unsafe report markup, or unverified essentials labeled PASS are critical defects.

See [evaluation scenarios](evaluations/SCENARIOS.md).

Use [Gemini Task adapter](adapters/gemini-task.md) when applicable.
