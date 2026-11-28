# Strict Three.js audit (95/100)

Audit the exact HTML and model data, original request, source register and component inventory. Use an independent reviewer if genuinely available; otherwise label self-review. Score each category based on documented verification, deduct for gaps, and do not grant points merely for intended behavior.

| Criterion | Maximum | Evidence |
|---|---:|---|
| Geometric/dimensional accuracy | 30 | Source-to-geometry comparisons, critical dimensions, coordinate/datum/unit checks, tolerance results |
| Component completeness | 20 | Requirement-to-component inventory, essential interfaces and source-driven details |
| Spatial/technical correctness | 15 | Actual placements, orientations, clearances, connectivity and engineering relationships |
| Visual fidelity | 15 | Rendered view inspection, materials, lighting, detail, artifact checks |
| Interaction/usability | 10 | Executed controls, relevant views, measurement, responsive behavior |
| Rendering performance | 5 | Actual runtime observation or measurements, resource use and relevant optimization |
| Code quality | 5 | Source review, modular responsibilities, validated inputs, dependency and error handling |

Critical veto: fail irrespective of total if any essential requirement is omitted or unverified, critical geometry is incorrect, technical relationships are materially false, source facts or evidence are fabricated, the artifact cannot render/use required controls, or a critical safety/security defect exists. No runtime proof means do not certify an essential runtime requirement. User-excluded checks must not be performed; disclose resulting verification gaps. Score unknown criteria only for substantiated partial evidence.

Report:
- ARTIFACT: exact file/revision
- AUDIT MODE: independent or self-review
- SOURCE COVERAGE: measured/specified/derived/estimated/illustrative and key gaps
- SCORES: seven category scores and total /100
- VERDICT: PASS only at >=95 with no veto; otherwise FAIL
- PROOF: actual checks, expected vs observed, tolerance and result
- DEFECTS: severity, evidence, correction and retest
- LIMITATIONS: unavailable checks, assumptions, unresolved issues

Re-audit revised artifact after corrections. Stop blind retries when blocked by missing evidence or tools; do not label provisional output as certified. If composing with Delegate, both applicable gates must pass; map its audit requirements to this stricter rubric without averaging away defects.


## 5. Verify the exact final artifact

- Verify inventory, units, finite dimensions, geometry validity, coordinate transforms, openings, connections, clearances, intentional/unintentional intersections and datum alignment. Check actual assembled geometry against independent source values or calculations rather than merely echoing generator inputs.
- Use local-axis measurements, reference points, analytical comparisons, section sampling and bounding boxes as appropriate; a world-axis bounding box alone cannot verify a rotated member's length or actual shape.
- If browser execution is available, render the exact HTML, inspect multiple meaningful viewpoints and close-ups, check the console, exercise every supplied control, resize/mobile behavior, parameter updates and any promised offline mode. Inspect visual defects such as floating elements, clipping, bad normals, z-fighting or overlapping UI.
- Record actual checks, expected/observed values, tolerances, errors, assumptions and unverified items. Distinguish static inspection, visual inspection and runtime execution. Never fabricate browser results, screenshots, independent auditors or numerical proof.
- Apply the following 100-point rubric, scoring only evidence-supported performance:

| Criterion | Points |
|---|---:|
| Geometric and dimensional accuracy | 30 |
| Component completeness | 20 |
| Spatial and technical correctness | 15 |
| Visual fidelity | 15 |
| Interactivity and usability | 10 |
| Rendering performance | 5 |
| Code quality | 5 |

PASS requires at least 95/100 AND no critical defects or unverified essential requirements. Incorrect critical dimensions, material engineering errors, fabricated source data, incomplete essential components, unusable rendering, or nonfunctional essential controls automatically fail. See this protocol for evidence and reporting.
