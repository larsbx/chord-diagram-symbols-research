# Replay of the existing chord bridge

The source component-and-gap proof is cited, not rewritten. The original C++
oracle compares chord-intersection connectivity and distinct parity-prefix
vertices on every matching through k=8: all 2,027,025 eight-chord pairings have
zero predicate mismatches; 593,859 pass both predicates. The original Python
recurrence oracle also replays its exact normalization and historical correction.

These are fresh executions of the existing source implementations, not a new
independent implementation or proof of the all-k theorem. The original oracle's
two predicates provide its independent checks. The k=9,10 coefficients remain
recurrence-derived predictions; this bootstrap performs no Q8 cycle enumeration.
Exact stdout is in `conformance/first.json`.

Read `docs/prior-art-ledger.md` before advancing any novelty or acceptance claim.
