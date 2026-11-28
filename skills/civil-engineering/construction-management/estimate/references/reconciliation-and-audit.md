# Reconciliation and audit contract

Apply with canonical skill `delegate`. Freeze estimate basis, shared source register and candidate revision. Use decimal arithmetic where available, without premature quantity rounding.

## Worker contracts and prompts

All roles receive requirement IDs, scope/revision, location/date/currency, units, pricing/tax/markup basis, evidence IDs and isolated ownership. Return inputs, results, assumptions, evidence and unresolved gaps; no nested agents or overwriting another role's evidence.

| Role | Owns | Must not touch | Done criteria / evidence |
|---|---|---|---|
| Extraction | Takeoff, WBS, plan specs, permit status | Prices/totals | Dimensions, equation, unit, page/grid/source, missing items |
| Market Pricing | Resource and permit rate register | Quantity invention, final BOQ | Dated source, location/spec, unit/pack, VAT, freight, currency, assumptions |
| Assembly | Candidate, mappings, build-ups, summaries | Raw evidence, independent verdict | Traceable BOQ/BOM, tax and permit lines, formulas, composite coverage |
| Reconciliation | Read-only source-to-candidate recomputation | Candidate edits | Every variance, scope gaps, duplicates, unit/tax/rounding checks and review mode |

Prompt templates:
- Extraction: "Own takeoff for [scope/revision]. Do not price. Return IDs, measurement equations, units, source/page and unknowns."
- Pricing: "Own rates for [location/date/spec]. Do not invent quantities. Return normalized rates, pack/tax/logistics/source evidence and confidence."
- Assembly: "Use approved extraction/pricing. Own candidate [revision]. Return BOQ/BOM, build-ups, tax/permits and formulas; do not alter evidence."
- Reconciliation: "Read exact [revision] and original evidence. Recompute without relying on candidate totals or editing it; report discrepancies, missing scope, critical defects and independence."

Extraction and independent rate research may overlap; confirm specifications before assembly, then reconcile. Re-audit after changes. Preserve accepted evidence. Without native agents label separate role passes SELF-REVIEW, not independent. Final Auditor is a distinct Delegate gate.

## Arithmetic
For measured BOQ quantity Q, resource consumption a, applicable waste fraction w and rate P:
- Net quantity = Q × a; gross usage = net × (1 + w). If consumption includes waste, incremental w = 0 with justification.
- Aggregate gross usage across linked lines before rounding indivisible packs: packs = ceil(total gross / pack size); purchase = packs × pack size. Allocate surplus premiums once; use continuous bulk quantities where justified.
- Direct BOQ rate = compatible normalized resource consumption × rates summed plus other direct costs. Amount = Q × rate plus explicit allocated purchase/rounding differences. Composite subcontract lines are separate nondecomposed costs; no duplicated component costs.
- BOM material cost = purchase × material rate on matching tax basis. Labor = hours × rate (crew vs person-hour explicit). Equipment = productive/rental hours × rate; mobilization/fuel either included or separate.
- Direct total = materials + labor + equipment + other direct costs. Permits, overhead, profit, contingency and taxes separate with declared bases and order; no silent compounding.

Reject negative/impossible quantities, nonfinite rates, dimensional mismatches and duplicate scope. Zero needs basis. Unknown quantity/rate remains null/unpriced, not zero. [Benchmark] is dated contextual comparison; [Assumed] unverified input; neither is a live quote. Normalize quote currency/exchange, pack/unit, VAT, freight and date.

## Zero-variance checks

Declare currency precision (PHP centavos default), rounding method and sum-of-rounded-lines or explicit adjustment policy. Use consistent scope and cost basis throughout.

| Check | Left | Right |
|---|---|---|
| Line extension | Line amount | Q × rate + documented allocations |
| Materials | BOQ material subtotal | BOM purchase cost including allocated surplus |
| Labor/equipment | BOQ resource subtotals | Matching schedules |
| Other direct | BOQ composite/other subtotal | Separate nondecomposed schedule |
| Direct | Sum BOQ lines | Sum resource + other direct costs |
| Permits/indirects | Summary | Incremental permit and markup lines |
| VAT | Summary VAT | Sum applicable tax calculations on declared basis |
| Total | Grand total | Direct + permits + indirects + applicable net tax, without double-counting |
| Net/gross | Gross − net | Applicable VAT on same scope |

Report each left/right value, signed difference, evidence, revision and verdict. Zero unexplained variance at declared precision is mandatory; a documented adjustment must be visible and justified, not a plug. Example: 3 units at 2.00 kg/unit with 10% waste = 6.60 kg; 5 kg packs require 2 packs = 10 kg. At PHP 20/kg purchase cost = PHP 200; allocate PHP 68 surplus above gross usage exactly once. Tax example in [PH reference](ph-compliance-and-vat.md).

Check source-to-scope completeness, duplicates, dimensions, rate provenance, permit status, VAT basis, missing data, exact delivered formulas/rendering and review independence. Delegate's >=9/10 gate remains separate; any unresolved essential requirement, critical defect or unexplained variance blocks PASS regardless of score. Reconcile exact revised candidate after targeted fixes; report unresolved requirements when execution limits are reached.
