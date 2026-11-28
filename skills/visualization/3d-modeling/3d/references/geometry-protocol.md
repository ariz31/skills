# Geometry and source fidelity protocol

## Model register

For each critical dimension/component retain: stable ID, source identifier and revision/page/location, provenance class, value and unit, datum/frame, tolerance and uncertainty if known, and independent verification method. Track nominal design dimensions separately from measured as-built values. If a detail has no authoritative source, mark it estimated or illustrative in the UI or model metadata. Do not use false precision.

## Coordinate conventions

Default meters, right-handed Y-up, local origin near model. Define conversion for each drawing/GIS input (e.g., easting/northing/elevation), orientation and vertical datum. For geospatial data, record CRS, transformation, data date, vertical reference and resolution; use an appropriate projected metric CRS or local tangent frame rather than treating degrees as meters. Preserve geospatial offsets outside mesh coordinates to reduce floating-point errors. Verify at known control points when supplied.

## Domain-specific requirements

| Domain | Required checks where applicable |
|---|---|
| Architecture | Room/wall dimensions, thicknesses, levels, roof slopes, actual openings and frames, stairs, floor clearances, interior/exterior continuity. |
| Structural | Gridlines, member centerlines and faces, spans, section dimensions, offsets, bearings, support interfaces, foundation elevations, explicitly sourced reinforcement/connection details. |
| Roads/infrastructure | Horizontal and vertical alignment, stationing, centerlines, lane/shoulder widths, grades, crossfall/superelevation, curve radii, junctions, cross-section continuity and grade separation. |
| Terrain/site/vicinity | Survey/DEM resolution, elevations, contour intervals, terrain triangulation, slope continuity, building footprints, road topology and georeferencing; distinguish approximate footprints and building heights from verified geometry. |
| Mechanical/equipment | Manufacturer dimensions, interface/fastener positions, operating envelopes, assembly sequence, rotation axes, clearance and meaningful exploded views. |
| Hydraulics/utilities | Pipe diameters, invert/centerline elevations, slope, flow direction, junctions, fittings and interfaces; do not infer inaccessible services as fact. |
| Educational models | Correct governing relationships and units; visually distinguish schematic, exaggerated and physical scale; identify learning objectives and enable meaningful manipulation where appropriate. |

Use domain-specific skills when registered and relevant. Do not infer structural capacity, code compliance or surveyed accuracy from visual resemblance.

## Geometry verification

- Compare independently sourced critical dimensions to actual mesh extents in the proper local basis, or measure between transformed reference points.
- Validate mesh buffers, index ranges, finite transforms, appropriate normals, topology/watertightness when required, and unintended degenerate or inverted geometry.
- Test required interfaces, clearances and expected contacts using suitable geometric tests. A broad-phase AABB overlap is only a candidate, not proof of interference; distinguish intentional contact/overlap.
- Verify openings through actual geometry rather than painted rectangles where the opening is required.
- For parameterized inputs, test nominal, boundary and invalid values; verify dependent geometry after changes.
- For real-world models, report source uncertainty separately from computational/mesh tolerance. Only claim the accuracy demonstrable from both.


## 1. Define the modeling contract

- Identify subject, intended use, audience, scope, detail, drawings, specifications, dimensions, units, interaction and delivery requirements. Distinguish conceptual/educational models from measured reconstructions and engineering design representations.
- Prioritize supplied approved drawings/measurements, authoritative survey/GIS or manufacturer data, then identified secondary sources. Resolve or disclose discrepancies. Never invent survey coordinates, manufacturer dimensions, concealed construction, code compliance or precision.
- Maintain a dimension/component register with ID, source, value, unit, datum, provenance (measured, specified, derived, estimated, illustrative), uncertainty and justified acceptance tolerance. Numerical consistency is not proof of real-world accuracy.
- Define SI units (1 world unit = 1 m unless explicitly justified otherwise), right-handed Y-up coordinate frame, origin, axis mapping, orientation and datum. Keep georeferenced scenes in a local metric frame and preserve transformation metadata.
- Derive tolerances from intended use and source precision, not a universal arbitrary threshold. If data are missing, use explicitly labeled assumptions where reasonable; do not fabricate exact dimensions. If the requested real-world accuracy is unattainable, disclose that and deliver a labeled conceptual/partial result rather than certify it.

## 2. Construct source-driven geometry

- Build a semantic assembly tree: site/system, subassemblies, components and interfaces. Inventory every required component against the scope and source data.
- Use a single canonical dimension source and parametric geometry. Compute placements, rotations, sections, clearances, openings, connections, profiles and elevations from constraints rather than arbitrary offsets.
- Use appropriate geometry: extrusions, sweeps, curves, indexed meshes, triangulated surfaces, validated imported assets and constructive geometry where needed. Generic boxes are acceptable only for truly box-shaped items or explicitly labeled abstractions.
- Model relevant visible and hidden components, openings, elevations, supports, joints, slopes, transitions, interfaces and interior/exterior relationships. Do not add invented reinforcement or concealed services as verified facts.
- Separate physical geometry and presentation transforms. Exploded, exaggerated and cutaway views must be reversible and visibly labeled. Measurements refer to original physical geometry, not exploded spacing.
- Preserve stable component IDs, names, dimensions, provenance, materials, hierarchy and layer membership. Allocate detail by technical importance and viewing distance; never simplify away essential interfaces or dimensions.
- Apply the this geometry protocol when available for domain-specific requirements.
