# Animate strict audit (95/100)

Audit the exact final deliverable, user specification, shared board, phase schedule, source register and parameter contract. Use a real independent auditor via Delegate when available; otherwise label self-review. Score only evidence-supported behavior; do not award intended behavior or fabricate checks. Record artifact path/revision and audit mode.

| Criterion | Max | Evidence |
|---|---:|---|
| Scientific and technical accuracy | 30 | Source/equation checks, units, validation cases, numerical behavior, labeled assumptions and scales |
| Phase sequencing and continuity | 20 | Complete storyboard, boundary samples, deterministic replay/seek/loop, event and parameter revision checks |
| Visual fidelity and clarity | 20 | Actual rendered views/frames, accurate geometry, annotations, camera and legibility |
| Motion smoothness and rendering performance | 15 | Playback at representative rates, frame timing/responsiveness, no unintended jumps or leaks |
| UI and playback usability | 10 | Executed transport, controls hiding/recovery, fullscreen/fallback, desktop/mobile and accessibility checks |
| Code correctness | 5 | Actual source review, valid dependencies, centralized state, robust error handling |
| Total | 100 | PASS only at >=95 and no veto |

## Minimum verification matrix

1. Open exact delivered file via documented launch method; inspect console, initialization, actual initial paused frame and full playback.
2. Compare scientific quantities to independent expected values and tolerances. Verify physical-time independence across speed settings. Check source and model limitations.
3. Inspect every required phase and both sides of boundaries, including intentional events. Verify direct seek versus continuous play, reverse seek, step forward/back, replay, loops and phase repetition.
4. Exercise play/pause, speed changes, timeline, phase navigation, annotations, optional holds, camera manual/resume and reset. Confirm configuration revisions cannot display stale or mixed state.
5. Verify controls auto-hide during play and reveal on mouse/touch/keyboard; pause/focus accessibility, clean mode, fullscreen entry/exit or honest supported fallback, responsive layouts and reduced-motion behavior.
6. Inspect representative frames and actual playback for visual defects; observe performance and repeat interactions for resource issues. Verify requested export and audio only if applicable.
7. Review source for dead controls, invalid inputs, race conditions, clock duplication, incorrect dependencies and error states.

Critical vetoes: material technical error, missing essential phase, broken playback or seek restoration, unintended geometric discontinuity, unusable render, nonfunctional essential controls/fullscreen or promised fallback, fabricated evidence, or unverified essential requirement. A score above threshold cannot override a veto. Apply Delegate's separate 9/10 rubric and 3D's 95/100 rubric when applicable. Do not average scores. Report user-excluded or unavailable checks, and do not certify unverified essentials.

## Audit report

ARTIFACT: exact file/revision
MODE: independent or self-review
SCORES: six criterion scores and total /100; applicable additional gates
VERDICT: PASS or FAIL
PROOF: executed checks with expected/observed values, tolerances, screenshots or logs when actually available
DEFECTS: severity, requirement ID, evidence, correction and retest
LIMITATIONS: missing tools, assumptions, unexecuted checks and outstanding defects

Use targeted remediation and re-audit the revised artifact. If blocked, return useful provisional output with actual score/verdict and limitations rather than false certification.
