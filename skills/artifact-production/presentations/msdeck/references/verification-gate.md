# MSDeck verification gate

Inspect the exact final HTML, not a preview or summary. Record candidate identifier, environment, actual checks, expected/observed behavior, limitations and defects. No fabricated test results.

## Required checks

- Content/learning: objectives, sequence, source claims, equations/units, independent worked-result checks, assessment alignment and no placeholder content.
- Static: valid structure, unique IDs, scoped styles/events, pinned compatible dependencies, complete assets, valid navigation state and no unsafe markup injection.
- Browser when available: load the actual artifact at 960×620, 1280×720 and 1600×900 plus 390×844 portrait, 844×390 landscape, 768×1024 tablet; inspect actual screenshots/rendering if supported. Verify no unintended overflow/clipping, broken images, blank essential canvas or uncaught console errors; meaningful first slide.
- Navigation: both edge zones and 80/20 split, first/last slide/step, previous/next, skip, reverse, repeated visits, keyboard, pointer cancellation, swipe vs vertical scroll and interactive hit targets; no double transitions.
- Controls: lightbox open/close/focus restoration, fullscreen success/denial/exit, resize/orientation, touch, keyboard focus, accessible labels, reduced-motion, usable contrast.
- Embedded components: correct resize and coordinates, model interaction and deterministic phase/step synchronization, inactive slide pause, reactivation, resource cleanup, no duplicate handlers, and all selected 3D/Animate/Delegate gates independently passed on the integrated candidate.
- Delivery: file exists, opens as documented, asset/license records present; test offline only when promised, with network disabled when possible. Disclose network/server requirements.

## Acceptance

PASS only when every essential requirement has evidence, all selected gates pass, no critical defects remain and the final candidate is usable. Critical defects include incorrect core content, broken navigation/step state, unreadable/clipped essential content, missing media or visualization, uncontrolled gesture conflicts, inaccessible essential controls, unverified essential rendering, invented checks and format substitution. Fix and re-verify affected checks and integration. If browser/runtime unavailable, inspect static source and label runtime, gesture and viewport checks UNVERIFIED; do not claim browser PASS or full acceptance for missing essential verification. Deliver useful provisional result with exact limitations. Optional checks not performed are disclosed, not treated as passed.
