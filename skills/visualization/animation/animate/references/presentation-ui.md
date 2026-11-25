# Minimal animation interface and presentation protocol

## Canvas-first design

Reserve most of the viewport for the subject. Keep phase title/indicator small; put configuration, phase list, details and explanation in collapsible panels. No blocking startup overlays or permanently large sidebars. Ensure initial camera/view fits important content. Design a consistent technical, realistic or educational visual language appropriate to the request. Offer mode switching only if useful and fully implemented.

Default paused at the first meaningful frame, silent, non-looping; autoplay, looping, phase repetition and optional event holds are configurable. Minimal overlay contains play/pause, replay, timeline with current/total time, previous/next phase, speed, frame steps, fullscreen and controls/menu access. Secondary controls can collapse into a compact accessible menu. Timeline and phase indicators must reflect actual state. Allow context-appropriate speed range with 1x default.

## Visibility behavior

Implement distinct paused, playing-visible, playing-hidden and clean-presentation states. Inactivity during playback may hide controls after a short configurable timeout (e.g. 2–3 seconds). Do not hide while paused, hovered, focused, dragging, interacting with a menu or when an error/required action needs attention. Pointer movement, touch tap, keyboard focus or a documented keyboard shortcut reveals controls; touch must not depend on hover. Clean mode hides nonessential overlays including annotations when requested, with a discoverable exit/reveal mechanism. Escape exits native fullscreen through browser behavior or leaves clean/viewport mode; restore focus appropriately. A hidden control must not intercept scene gestures or become an invisible keyboard focus trap.

Native fullscreen targets the containing presentation element, including controls. Request only on user gesture; handle rejection, fullscreenchange and external exit; resize correctly. If unavailable, offer clearly labeled viewport-maximized mode, not a false fullscreen indicator. Maintain playback time and camera during transitions. Make fullscreen controls reachable from mouse, touch and keyboard.

## Annotation and camera

Bind labels, callouts, quantities and phase explanations to timeline and physical state, not independent timers. Give important units and scale indicators. Use readable fonts, contrast, responsive placement and collision avoidance. Hide-all removes annotations without changing model state. Keep essential safety or scale disclosures accessible in information panel even when annotations are off.

For spatial scenes, define phase-specific camera target, framing and optional interpolated path; prevent clipping and disorientation. Manual orbit/pan/zoom or viewport override suspends auto-camera until explicitly resumed or reset. Seek updates auto-camera to the target phase when active; manual state remains stable. Use reduced-motion preference to suppress cinematic travel/easing, keep necessary physical motion manually controllable, and avoid forced autoplay. Provide keyboard-operable controls with visible focus, meaningful labels, touch-friendly targets and sensible mobile safe-area spacing.

Verify desktop/mobile portrait and landscape, narrow screens, fullscreen entry/exit/fallback, reveal/hide from each input method, pause/focus behavior, keyboard navigation, annotation toggle, camera override/resume and configuration panel usability.
