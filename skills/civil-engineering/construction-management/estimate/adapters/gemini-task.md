# Gemini Task adapter: Estimate

Use only actual exposed capabilities and authorized files. Inspect signatures; do not assume a tool exists.

| Operation | Preferred host mapping / fallback |
|---|---|
| Intake | ask_question when available, otherwise concise chat questions; two Estimate questions total, reuse Ask confirmation |
| Source retrieval | Authorized Workspace/Drive search and read; VM/file tools for uploaded PDFs, drawings or spreadsheets when available; retain page/cell/revision provenance |
| Pricing | Actual web/source retrieval; otherwise user rates or labeled benchmark/assumption |
| Worker orchestration | Delegate's [Gemini adapter](../../../../orchestration/delegate/adapters/gemini-task.md); native dispatch/status/read when exposed, otherwise four sequential roles |
| Calculation and artifact | Available spreadsheet/VM calculation and creation tools; verify exact workbook formulas or PDF rendering; otherwise structured report with limitations |
| Delivery | Actual Workspace link or supported file presentation; never invent path or URL |

One coordinator starts extraction and independent rate research when possible, waits for verified handoffs before assembly, then reconciliation and Delegate final audit. No nested dispatch. With Max use its two-cycle ownership; with Ask avoid duplicate intake. Do not claim independence without native independent reviewers. Do not upload private plans to external services without authorization.
