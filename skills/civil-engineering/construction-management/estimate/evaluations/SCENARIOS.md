# Estimate evaluation specifications

Specification scenarios, not executed host tests.

| Scenario | Expected behavior |
|---|---|
| @estimate or /ESTIMATE: price a house | Select canonical Estimate once and mandatory Delegate. |
| Construction BOQ and BOM from drawings | Semantic activation, source-linked takeoff and reconciled schedules. |
| Rough cost per m² only, no BOQ | No automatic Estimate activation. |
| Convert 5 m to cm or electronics BOM | No automatic Estimate activation. |
| Review existing estimate without edits | Read-only Review; no unsolicited rebuilt estimate. |
| @max @estimate | One outer coordinator, two Delegate cycles, no duplicate dependency or extra cycle. |
| @ask @estimate with unclear scope | Ask confirmation first, reuse answers; at most two Estimate intake questions total. |
| Missing critical dimensions after two questions | Conditional subtotal/gap report; unknown not zero; no PASS. |
| PHP 10,000 net taxable plus PHP 1,000 verified pass-through | VAT PHP 1,200 and gross PHP 12,200. |
| PHP 11,200 VAT-inclusive taxable quote | Net PHP 10,000, VAT PHP 1,200; no duplicate VAT; net/gross toggle preserves liability. |
| Paid secured permit and unpaid secured permit | Paid incremental zero with evidence; unpaid remains payable; unknown fee not zero. |
| 6.60 kg gross needed, 5 kg packs, PHP 20/kg | Buy 10 kg, PHP 200; surplus premium PHP 68 allocated once; zero variance. |
| Native agents unavailable | Four sequential roles, non-independent SELF-REVIEW; explicit independence requirement blocked. |
| Web or document parsing unavailable | Dated benchmark/assumed rates or unknown; readable extracts only; disclose limitations. |
| XLSX/PDF unavailable or final variance nonzero | Disclose missing artifact or failed gate; useful partial output, never fabricated PASS. |
