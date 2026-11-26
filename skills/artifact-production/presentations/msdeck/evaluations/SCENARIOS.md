# MSDeck evaluation specifications

Specifications, not executed platform tests.

| Scenario | Expected behavior |
|---|---|
| @MSDeck create a hydraulics lecture | Case-insensitive activation; one 16:9 interactive HTML deck with objective-aligned steps. |
| Create a PowerPoint or printable handout | Do not silently substitute HTML. |
| What is a slide deck? | Informational response, no unsolicited artifact. |
| @msdeck with no subject | Ask for subject. |
| Left/right upper 80% edges | Previous/next step; correct boundary behavior. |
| Lower 20% edges | Skip slide, target first step. |
| Swipe from canvas/slider/input/lightbox | Local control wins; no slide change. |
| Swipe then synthesized click | One navigation transition only. |
| Reverse/revisit solved calculation | Correct synchronized diagram and equation state. |
| 390×844, 844×390 and tablet rotation | Contained 16:9, reachable controls, no clipping. |
| Lightbox keyboard/Escape | Accessible dialog and restored focus. |
| Fullscreen denied | Labeled viewport-maximized fallback. |
| Missing external image retrieval | Accurate authored SVG; disclose unverified source media. |
| @msdeck @3d @animate | One HTML shell, scoped component lifecycles, Delegate loaded transitively once; all gates. |
| Inactive WebGL/animation slide | Pause expensive loops; restore deterministic state on revisit. |
| Offline requested with CDN dependency | Not accepted as offline until dependency resolved and verified. |
| Browser unavailable | Static evidence only, provisional if essential runtime unverified. |
