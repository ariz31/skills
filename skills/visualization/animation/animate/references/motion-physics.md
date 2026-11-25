# Motion and scientific correctness protocol

Classify every material motion track as physics-based, measured/data-driven or illustrative. Document equations, units, coordinate frame, sign conventions, boundary/initial conditions, parameter sources, applicability and limitations. Use applicable domain skill and authoritative sources when needed. If measurements or governing data are absent, label assumptions and do not claim exact real-world response.

For engineering animations, derive state from correct relationships rather than arbitrary visual tweening. Validate limiting cases, independent reference calculations or benchmarks, equilibrium/conservation where applicable, dimensional consistency, and numerical stability/convergence for integration. Select appropriate solver and step size; do not use arbitrary frame delta as physical timestep. For measured trajectories, document sampling/interpolation and avoid unsupported extrapolation.

Map physical time to presentation time explicitly. Slow motion, time compression, event holds, displacement amplification, schematic vectors and exploded spacing must be visibly disclosed when material to interpretation. Display physical time and scale where needed. Camera, fades and annotation easing are presentation effects; they must not change force, displacement, acceleration, flow, stress, contact or other governing quantities. Illustrative motion may use easing only when not misrepresented as physics.

Domain examples (not mandatory phases for every task):
- Construction: excavation, foundation, structure, enclosure and finishing in valid dependency order; component appearance follows installation rather than unexplained teleportation.
- Earthquake response: initial condition, ground excitation, response and residual state; distinguish input motion from structural response and disclose damping/model assumptions and amplification.
- RC response: elastic, cracking, yielding and ultimate stages only where supported by the modeled system; do not imply failure modes not calculated.
- Surveying: setup, orientation, observation, computation and plotting with consistent instrument/target geometry.
- Hydraulics: initial/boundary conditions, development and response; vector magnitudes and time scaling correspond to the model.
- Mechanical assembly: component IDs, constraints, joint axes, clearances and sequence; distinguish exploded presentation from physical positions.

At intentional events such as fracture, impact or topology change, use physically meaningful pre/post states and explain the discontinuity. Verify both sides. Reject material scientific errors even if the animation looks smooth.
