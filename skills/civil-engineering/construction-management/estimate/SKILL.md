---
name: estimate
description: Produce construction cost estimates, BOQ, BOM, unit price lists and project pricing reports with mandatory Delegate coordination, traceable quantities and rates, permit and tax treatment, and zero-variance reconciliation. Use for @estimate, /estimate or substantive construction estimating.
---

# Estimate

Auditable construction planning estimates, BOQ/BOM, unit pricing and permit-inclusive pricing. Use explicit @estimate /estimate or substantive construction estimating; not rough budgets, isolated conversions, non-construction BOMs or read-only review without production request. Review source stays read-only.

## Preflight
Inspect actual drawings, schedules, specs, photos, spreadsheets and quantities. Record revisions, scale, scope, location, currency, price date, procurement/VAT basis, permits, labor/equipment, waste, overhead/profit, contingency and exclusions. SI/PHP for Philippines unless directed. Document measurement rules, equations, units, applicability, standard/edition, conversion; no dimensions inferred from unscaled images. Load required canonical skill delegate and [reconciliation contract](references/reconciliation-and-audit.md); Philippine projects require [compliance and VAT](references/ph-compliance-and-vat.md), otherwise verify local rules. Use [Gemini Task adapter](adapters/gemini-task.md) if supported.

## Workflow
1. **Intake:** Resolve scope, location, currency, VAT, permit status and deliverable from context. When standalone, ask at most two Estimate intake questions total (not two rounds). When `ask` is co-selected, Ask owns upfront clarification under its adaptive 3–8 question budget, including at most two Estimate-critical questions (e.g., VAT and permits); finish its Intent Check before implementation or worker dispatch, reuse every confirmed answer verbatim and cap remaining Estimate follow-ups at `max(0, 2 - estimate_questions_already_asked)`. Never repeat answered questions or bypass confirmation. State safe defaults as [Assumed]. After cap, give conditional estimates or gap report if essential facts remain missing.
2. **Freeze basis:** Versioned scope/WBS, stable line IDs, source register, quantity formulas/units, pricing basis, tax classes, rounding and assumption/unknown ledger. Identify exclusions, alternates, provisional sums, duplication, owner supplies and secured permits. Keep waste distinct from markups.
3. **Mandatory Delegate:** One coordinator; four roles with contracts from reconciliation reference:
   - Document Extraction: source-linked takeoff/specs, permits, gaps.
   - Market Pricing: dated local rates, unit/tax/freight/currency normalization; start independently where possible, finalize against specs.
   - BOQ/BOM Assembly: wait for verified extraction/pricing; own candidate, mappings, unit costs, taxes and totals.
   - Independent Reconciliation: recompute from original evidence read-only after assembly; coordinator fixes and re-audits.
   Apply separate Delegate Strict Final Auditor gate to exact candidate. Max owns its two cycles and shared budget; no extra cycle. Review report gate and source verdict are separate.
4. **Deliver:** Honor Markdown/PDF/XLSX/structured chat. Include basis, project/date/scope/exclusions/uncertainty; BOQ IDs, descriptions, measured quantity/unit, resource or documented composite rate, unit cost, amount/evidence; BOM resource IDs, specs, net/waste/purchase quantities, pack conversions, rates/amounts and BOQ mappings; separate labor/equipment; unit-price build-ups, dated sources, permit register, taxable/exempt/pass-through subtotals, VAT, overhead/profit/contingency, total; reconciliation, variances, gaps, sensitivity/range, review mode and verdict. XLSX linked basis/BOQ/BOM/rates/permits/summary/audit sheets with formula and displayed-total checks; inspect actual PDF rendering.

## Gates and fallback
Zero unexplained variance at stated currency precision for extensions, mappings, summaries, tax and total; only explicit rounding, never balancing plugs. Every material number sourced or labeled [Assumed]/[Benchmark]. Unknown ≠ zero; check scope, units, duplication, waste and tax normalization. Delegate ≥9/10, no critical defects or unverified essentials; targeted rework within Delegate/Max limits. Veto invented evidence, unknown essential quantity/rate/tax basis, false secured status, double counting, unexplained variance, unsupported independence or unverified essential output.

Without agents execute four separate sequential roles and label reconciliation/final audit SELF-REVIEW. Required independence blocked if unavailable. Without web use user rates or defensible dated assumptions/benchmarks, never fake quotes; unsupported rates unknown. If parsing fails use readable extracts or ask within cap, never unseen data. If export/verification unavailable, provide supported structured output and disclose gaps. See [evaluation specifications](evaluations/SCENARIOS.md).
