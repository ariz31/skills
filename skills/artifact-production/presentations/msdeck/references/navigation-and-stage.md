# Navigation and stage contract

## Logical stage

Use 1280×720 CSS logical pixels, with scale = min(availableWidth/1280, availableHeight/720). Center the stage within safe-area-adjusted viewport, letterbox as needed, and use ResizeObserver or window resize fallback. Apply transform-origin consistently; derive pointer coordinates from the actual stage bounding rect rather than raw viewport coordinates. Use dynamic viewport units with fallback and honor orientation/fullscreen changes. Avoid page overflow, unreachable controls, or clipped text. At narrow portrait widths retain 16:9 and provide accessible controls and optional user-controlled readable zoom/reflow when needed; do not force orientation. Respect user browser zoom. Ensure physical touch targets remain usable (aim 44 CSS px), independently of scaled stage.

For canvas/WebGL set logical scene dimensions and aspect from its slot, update camera projection and backing buffer on resize, cap device pixel ratio where justified and avoid applying scale twice. Keep canvas in its allotted bounds. Test resizing, high DPR, rotation and fullscreen.

## Navigation

Use the actual stage edges: left/right 10% of width each, upper 80% of height for previous/next step, lower 20% for previous/next slide. Center 80% remains content. Boundary navigation is clamped unless explicitly configured otherwise. At the final step, next step advances to the first step of the next slide; previous step at first goes to the previous slide's final step; slide-skip goes to the target slide's first step. At deck boundaries no-op and communicate state. Show discoverable non-obstructive transparent icon-only controls with accessible names, focus indicators, tooltips and hit areas; keep them visible while focused/paused as applicable, and offer reachable alternatives to gestures.

One state transition per action. Use keyboard Left/Right for steps, PageUp/PageDown for slides, Home/End for deck boundaries, Escape to dismiss lightbox or leave fullscreen; do not steal typing, native controls or local component shortcuts. Fullscreen button is user-initiated, handles rejection and provides labeled viewport-maximized fallback; restore controls and focus on exit.

Use horizontal swipe only after sufficient distance/direction threshold, rejecting vertical scroll, multitouch, pointer cancellation, movement originating from interactive controls, and unintended repeated click after gesture. Never intercept canvas orbit, sliders, text selection, links, buttons, form inputs, editable elements, scrollable regions, lightbox or descendants of [data-no-swipe]. Do not cover interactive edge content with invisible overlays; reserve safe edge gutters or yield to interactive hit targets. Use pointer events with scoped touch-action, preserve native scrolling/zoom where appropriate. Respect reduced-motion.

## Embedded component contract

Each visualization has a unique root and exposes equivalent lifecycle operations: mount(root, context), resize(width,height,dpr), activate(step), deactivate(), reset(step), dispose(). The shell owns navigation and calls step transitions once; local timeline consumes the requested step and is authoritative for physical state, not a competing slide index. Define step-to-time mapping and policies for seek/revisit/replay. Pause inactive animation/render loops, remove listeners and dispose resources on teardown. Use component-local keyboard/pointer events, namespaced IDs and styles, shared pinned dependencies, no duplicate fullscreen or document-global playback handlers. Reconcile local camera override and global step changes without fighting user input.
