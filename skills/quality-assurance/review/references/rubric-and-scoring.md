# Review rubric and scoring

## Freeze scope and rubric

Record source identity/revision, requested outcomes, constraints, allowed checks and audit mode. Choose 4–6 relevant dimensions and positive weights totaling 100 before inspecting/scoring findings; record reasons. Example code review: functional correctness 30%, requirement coverage 25%, architecture 20%, security/reliability 15%, maintainability 10%. For a slide deck use accuracy, pedagogy, completeness, accessibility/interaction and visual clarity as appropriate. Preserve selected existing skill-specific rubrics and gates independently (e.g. 3D/Animate 95/100). No substitution or averaging away failure.

Score each dimension 0–10 from evidence: 10 = all scoped criteria supported with no identified defects; 9 = minor nonblocking issues; 7–8 = material but bounded deficiencies; 4–6 = major gaps; 0–3 = severe failure or essentially absent evidence. Document deductions and avoid counting one root cause repeatedly. Compute weighted sum = Σ(weight × score)/100. Compare unrounded values to thresholds and display precision consistently.

## Severity

| Severity | Definition |
|---|---|
| Critical | Essential requirement absent/unusable, material safety/security/correctness defect, fabricated evidence, or severe integrity violation. Blocks PASS. |
| Major | Material functional, technical, coverage or usability defect requiring substantive correction; blocks unconditional PASS. |
| Minor | Localized, nonessential defect with limited impact and concrete fix. |
| Nit | Cosmetic or preference-level improvement; label as such, not a functional defect. |

Each finding: stable ID, category, severity, exact location/revision, requirement, observed evidence, expected behavior, impact, recommended correction, verification criterion, confidence/status. Separate confirmed findings from hypotheses and unavailable checks. Unverified essential requirements block PASS; don't invent a critical defect merely because evidence is unavailable.

## Source verdict

- PASS: score >= 9, no unresolved Critical or Major defects, no unverified essential requirement, and all applicable domain gates passed.
- PASS WITH REVISIONS: score >= 7, no Critical defect or unverified essential requirement, no failed mandatory domain gate, and bounded remaining revisions; includes >=9 with Major findings. Do not call this unconditional acceptance.
- FAIL / REWORK REQUIRED: score < 7, any Critical defect, unverified essential requirement or failed mandatory domain gate. Distinguish verified failure from evidence blocker in report.
- If source is inaccessible, do not assign a fabricated numerical score; report UNVERIFIED/BLOCKED.

Delegate's separate report-quality gate requires >=9/10 with no critical report defects or unverified essential report requirements, even when the source verdict is FAIL. Preserve source verdict and scores across user tracking actions; re-audit revised source to change them. Provide requirement traceability and actual verification mode, including static vs executed vs unavailable checks.
