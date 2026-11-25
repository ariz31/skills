# Deterministic timeline and state protocol

## Shared contract

Use a single ordered phase schedule with finite positive presentation durations (instantaneous events represented separately), unique stable IDs, cumulative start/end times, deterministic boundary ownership and explicit initial/final states. Use half-open intervals [start,end) except the final endpoint, which belongs to the final phase. Record key events, event hold policy, camera/annotation tracks and mapping to physical time. No gaps or unintended overlaps.

Define logically separate functions for phaseAt(presentationTime), physicalTimeAt(presentationTime, phase), sampleState(physicalTime, parameters, revision), samplePresentation(presentationTime, state), and render(state, presentation). Equivalent architecture is acceptable. Keep rendering pure with respect to physical state. Use seeded randomness where needed. Explicitly define handling of intentional discontinuities and reversible creation/destruction of objects.

## Clock and transport

Use monotonic elapsed time (e.g. requestAnimationFrame timestamp/performance.now), not frame counts. Track authoritative position, duration, playback rate, play/pause state, loop mode, current parameter revision and optional consumed-event state. Clamp or wrap position explicitly. On pause, retain exact position; on resume, reset wall-clock anchor. Rate changes preserve position and do not change numerical integration step. Avoid competing timers and stale callbacks. On visibility loss, use an explicit pause or elapsed-time policy; do not advance a physics solver with a huge variable step. For reduced motion, default to paused and suppress unnecessary camera/decorative transitions.

Implement:
- seek(t): clamp to valid range; reconstruct full state and synchronize phase, geometry, annotation, camera (unless manual), progress and time display.
- play/pause/replay: predictable start, stop, and restart including terminal position.
- previous/next phase: jump to defined phase boundaries, not an arbitrary visual offset.
- step forward/backward: advance by declared presentation-frame interval or documented simulation step; pause first. Do not tie stepping to display refresh.
- loop whole timeline or selected phase: explicitly restore boundary state and reset event consumption. Avoid accidental loop of a non-looping terminal state.
- event hold: cross event exactly once in the chosen forward-play interval; pause at event, allow explicit resume and disable holds for continuous playback if desired. Seeking is not playback and must not trigger side effects or trap the user.

## Reconstructing physics state

Analytical/state-function animations sample directly. Stateful solvers use fixed physical timesteps, immutable input revisions, deterministic initial conditions and checkpoints keyed by revision and physical time. Include velocities, history-dependent variables, topology, contact and random generator state as required. On backward seek restore a valid checkpoint and recompute forward, or use verified precomputed trajectory data. Interpolate display samples only when justified; never interpolate across discrete events as if continuous. Numerical stability and accuracy must determine timestep and interpolation. Avoid incrementally mutating geometry to represent state.

Parameter change: validate, create a new revision, cancel or ignore stale results, recompute affected trajectory/schedule/geometry and atomically commit coherent state. Pause during invalidating changes. Retain normalized or physical position only when semantically valid; otherwise reset and explain. Never mix frames from different revisions.

## Verification

Compare identical target times reached through uninterrupted playback, forward and backward seek, phase jump, replay and different playback rates, using declared numerical tolerances. Verify each boundary just before/at/after, including first and final frame, optional holds, loops and discontinuities. Test repeated scrubbing, rate changes, pause/resume, hidden tab, and parameter revisions. Record state values or checksums and timing evidence; do not assert determinism from code structure alone.
