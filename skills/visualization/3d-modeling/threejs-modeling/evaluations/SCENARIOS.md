# Three.js skill evaluation specifications

These scenarios are specifications, not executed platform test results.

| Input / condition | Expected behavior |
|---|---|
| "3D model of a two-storey house" | Activate skill; single interactive HTML by default; dimensions, exterior/interior and source assumptions. |
| "threejs residential solar setup; hide house" | Activate; component layers and functioning solar-only mode; no invented electrical specifications. |
| "3-D terrain of Burnham Park with nearby streets" | Activate; geospatial sources, CRS/datum and source-resolution limits; no fabricated survey accuracy. |
| "Create a cutaway of a reinforced concrete beam" | Activate on semantic 3D intent; sourced geometry and clearly illustrative reinforcement when unsupplied. |
| "3D" without context | Activate and request only the missing subject. |
| "What is Three.js?" | Informational response; no unsolicited artifact creation. |
| "Generate a static image of a 3D-looking house" | Do not substitute a Three.js artifact for requested image. |
| Rotated 3 m member | Check local/reference-point length; do not use world AABB alone. |
| Road intersection at different elevations | Distinguish grade separation from collision; preserve continuity and elevations. |
| Requested exact as-built building with no drawings | Disclose lack of evidence; clearly labeled approximate model or request essential sources. |
| CDN-dependent file described as offline | Fail delivery verification until corrected or disclosed and approved scope met. |
| Auditor scores 98 with a material critical dimension error | Fail regardless of total; correct and recheck. |
| Browser and sub-agent tools unavailable | Static review, honest limits and no invented evidence or independent audit. |
| "Delegate creation of a 3D simulation" | Compose both skills; 95/100 gate remains binding. |
