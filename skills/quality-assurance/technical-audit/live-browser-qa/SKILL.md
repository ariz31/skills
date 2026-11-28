---
name: live-browser-qa
description: Execute evidence-based live browser QA audits against deployed URLs or local web servers, checking DOM rendering, console and network errors, responsive viewports, and interactive flows with screenshot evidence. Use when invoked with @live-browser-qa, /live-browser-qa, @browser-qa, or when auditing a live web app or site.
---

# Live Browser QA

Perform evidence-based, read-only-by-default quality assurance against a live web URL or local dev server using real browser rendering, console/network telemetry, responsive viewport checks, and reproducible defect reporting.

## 1. Activation & Non-Activation

- **Activate** on `@live-browser-qa`, `/live-browser-qa`, `@browser-qa`, `/browser-qa`, or requests to QA-test a live website, deployed PWA, or local web server for rendering, console/network, responsive, or interactive defects.
- **Do not activate** for static source-code/document reviews without runtime browser inspection (use `review`), backend-only unit/API tests, or building a new app from scratch.

## 2. Inputs, Safety Guardrails & Deliverables

- **Inputs:** Target URL(s) (or local dev server command/port), priority user flows, target viewports (default: Desktop `1440x900`, Tablet `768x1024`, Mobile `390x844`), and optional acceptance criteria.
- **Safety & Auth Guardrails:** Read-only by default. Never submit destructive production mutations (deletes, purchases, account changes, form spam) without explicit user authorization. Never ask for or log plaintext passwords or secrets; pause and report if an auth wall or CAPTCHA blocks execution.
- **Deliverables:** Prioritized QA Defect & Verification Report (Markdown or interactive HTML if requested) with captured evidence (viewport screenshots, exact console/page errors, failed network `4xx`/`5xx` requests, DOM overflow metrics, and step-by-step repros).

## 3. Ordered Execution Procedure

1. **Lock Audit Matrix:** Enumerate target routes, viewports, and non-destructive interactive flows. Verify target reachability first.
2. **Live Telemetry Sweep:** Load each route in a real browser engine (e.g., headless Chromium/Playwright or live browser agent). Capture:
   - Uncaught `pageerror` exceptions and `console.error` / severe `console.warn` entries.
   - Failed network responses (`status >= 400`, failed assets, CORS blocks, broken images `naturalWidth === 0`).
   - Layout integrity (`documentElement.scrollWidth <= innerWidth` horizontal overflow check, clipped controls, broken z-index/overlays).
3. **Interactive Flow & State Check:** Exercise requested non-destructive flows (navigation, modals, tabs, filters, form validation, theme/state toggles). Verify DOM state transitions and zero post-interaction console errors.
4. **Responsive Viewport Sweep & Evidence Capture:** Capture screenshots across Desktop, Tablet, and Mobile viewports for every audited route and every discovered defect. Inspect captured screenshots directly to catch visual regressions that DOM metrics miss.
5. **Triage & Report:** Classify findings by severity (`P0 Blocker`, `P1 High`, `P2 Medium`, `P3 Low`) with exact route, viewport, repro steps, observed vs. expected behavior, and evidence pointer. Separate **Verified Pass**, **Confirmed Fail**, and **Unverified / Blocked** checks.

## 4. Quality Gates, Critical Defects & Fallback

- **Critical Defects (Audit Invalid):** Marking unexecuted checks as `PASS`; fabricating console/network logs or screenshots; performing unauthorized destructive production actions; omitting viewport evidence for claimed visual bugs.
- **Fallback:** If live browser execution is unavailable (or blocked by auth/network), perform static HTML/HTTP inspection only if permitted, label the audit `STATIC-ONLY (RUNTIME UNVERIFIED)`, and never issue an overall `PASS`.

## 5. Composition & References

- Follows global library invariants (`docs/INVARIANTS.md`).
- **Optional `delegate`:** Use parallel workers when auditing 4+ independent routes or multi-app suites.
- **Optional `review`:** Compose when the user wants a scored rubric dashboard alongside live QA evidence.
- Platform adapter: [Gemini Task adapter](adapters/gemini-task.md).
