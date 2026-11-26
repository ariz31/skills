# Interactive review dashboard

Default detailed standalone deliverable: one HTML entry point, dark surfaces #000000 / #0d1117, readable high-contrast typography, compact responsive layout, and accessible controls. Honor explicitly requested alternate format. Inline authored CSS/JS and prefer offline self-containment; optional KaTeX CDN must be pinned, disclosed, and have readable plain-text fallback. No network dependency for core audit data or controls.

## Required sections and behavior

- Executive header: exact audited artifact/revision, scope, audit mode, date if known, source verdict, weighted score, limitations and separate report-quality gate.
- Rubric: dimension scores, weights, progress bars with text equivalents, rationale, critical veto and unverified requirements.
- Findings: stable revision-bound IDs, severity/category, location, evidence, expected behavior, impact, actionable correction, verification criterion, status and confidence. Accessible expandable cards and one-click copy with clipboard-denial/manual copy fallback.
- Filters: severity/category pills with counts, text search across findings, reset/empty-state, Expand/Collapse All. Combine filters predictably and maintain keyboard focus; no hidden critical finding count ambiguity.
- Prioritized action plan: critical blockers first, dependency-aware remediation order, owner if known, verification criteria; recommendations do not execute modifications.
- Resolution tracking: local checkboxes with persistent user-reported status; clearly distinguish "marked resolved" from verified fix. Namespace localStorage by report schema version and audited artifact/revision or report identifier; validate parsed stored data, gracefully handle denied/quota/corrupt storage with in-memory state. Reset affects only this report after user action. Never modify original score, severity, evidence or verdict based on local tracking.

## Security and accessibility

Treat source excerpts, filenames, URLs, finding text and stored values as untrusted data. Render via textContent or context-appropriate escaping; never interpolate untrusted content into executable HTML/script or event attributes. Safely serialize inline JSON (escape script-closing sequences and HTML-sensitive characters); validate URL schemes and use noopener/noreferrer for external links. No eval, remote execution, secrets, or automatic source edits. Use semantic landmarks, buttons, labels, visible focus, aria-expanded and status announcements, contrast, reduced-motion and responsive layout. Copy does not expose hidden secrets.

Verify actual report renders and all filters, search, expand/collapse, copy, storage fallback and reset work on desktop and mobile; check no uncaught errors, overflow or broken dependencies. Static fallback must explicitly disclose runtime unverified. Report is a snapshot, not a live source monitor or remediation tool.
