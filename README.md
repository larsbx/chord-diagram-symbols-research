# chord-diagram-symbols-research

Connected chord enumeration, exact symbol normalizations, and prior-art reconciliation.

## First milestone

Reuse the source component-and-gap proof without creating a second theorem record. Reconcile the cited recurrence and asymptotic literature, exact position/rotation conventions, graph-product precedence, source manuscript indexing, and independent mathematical acceptance. Do not claim novelty for A000699.

The reproducible first experiment is `python3 experiments/first.py`; its exact
bounded output is recorded in [conformance/first.json](conformance/first.json).
See [REPRODUCING.md](REPRODUCING.md) for setup and comparison commands, and
[the roadmap](docs/roadmap.md) for remaining proof obligations.

## Initial result

See [the bootstrap results](docs/first-results.md) for exact scope and next gates.

## Mathematical conventions and authority

Finite simple undirected graphs; embeddings are injective edge-preserving maps,
not necessarily induced. An ordinary cycle is unoriented and unrooted, with its
selected edges: divide labeled traversals by 2m for a length-m cycle. Coordinate
support means nonconstant vertex projection. Centered defects use
u_G=G-|V(G)|K1, with no factorial division in the symbol.

[The claim registry](proof/claims.toml) separates source references, local finite
computations, proof obligations, conjectures, and falsified candidates.
The shared graph-ring foundations retain a single authority in
[28d0224](https://github.com/larsbx/graph-product-ring-research/tree/28d022402037274a9fe85c1fd64ecda2532dceb9); source claims labeled **working** remain working.
Lean kernel verification of a specified component, bounded computational evidence,
and independent mathematical acceptance are distinct fields. This bootstrap adds
no Lean proof and makes no independent-acceptance or novelty claim.

Non-goals: changing publication/manuscript bytes; silently upgrading inherited
claims; treating finite search or a language port as a theorem.

## Source and related programs

- [Pinned ordinary-cycle support/order proof](https://github.com/larsbx/graph-product-ring-research/blob/28d022402037274a9fe85c1fd64ecda2532dceb9/proof/even-cycle-order-symbol.md).
- [Pinned component-and-gap proof candidate](https://github.com/larsbx/graph-product-ring-research/blob/28d022402037274a9fe85c1fd64ecda2532dceb9/docs/research/c2k-chord-symbol-all-k-proof-2026-10-22.md).
- [Pinned source claim registry](https://github.com/larsbx/graph-product-ring-research/blob/28d022402037274a9fe85c1fd64ecda2532dceb9/proof/claims.toml).
- [Central bridge map](https://github.com/larsbx/graph-product-ring-research/blob/main/docs/research/bridge-repositories.md).
- [Provenance and acceptance boundaries](docs/provenance.md).
- [Sibling repositories](docs/bridges.md).

The [existing Vizing program](https://github.com/larsbx/vizing-domination-conjecture-research)
remains independent. Literature and novelty review remain coordinated with
[novelty-lab](https://github.com/larsbx/novelty-lab).
