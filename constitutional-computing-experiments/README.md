# Constitutional Computing Experiments

This repository section documents a sequence of synthetic research experiments exploring governed execution under changing state, composite consequences, independently committed stores, and bounded local authority.

The experiments are intentionally narrow.

They are not production security systems.

They do not demonstrate distributed consensus, Byzantine fault tolerance, cryptographic causality, malicious-store resistance, or general distributed atomicity.

The experiments evaluate specific properties under stated assumptions and finite synthetic tests.

## Research progression

1. **Deterministic governance** — v0.1 exercises explicit synthetic inputs and repeatable observations.
2. **State-bound execution** — v0.2 examines whether an earlier admission remains applicable when authoritative resource state changes.
3. **Composite consequence governance** — v0.3 examines consequences across a shared resource scope.
4. **Independent-store experiments** — v0.4 examines uncertainty when resource and governance updates commit independently.
5. **Bounded local operation** — v0.5 examines ordinary local action within previously assigned authority without consulting a root authority for every action.

An admission is a determination that a proposed action may proceed under specified conditions. Closure describes whether the required resulting state was observed. These are separate questions.

This candidate contains research descriptions and historical aggregate observations. It does not contain an executable reproduction of the later experiments. The narrative does not describe KeyWow production architecture.

## Reading guide

- [Experiment lineage](docs/EXPERIMENT_LINEAGE.md): questions, observations and boundaries by version.
- [State-bound observations](docs/STATE_BOUND_OBSERVATIONS.md): current state, stale admission and observed results.
- [Composition boundaries](docs/COMPOSITION_BOUNDARIES.md): individual and combined consequences.
- [Independent-store experiments](docs/INDEPENDENT_STORE_EXPERIMENTS.md): independent commits and unresolved outcomes.
- [Bounded local operation](docs/BOUNDED_LOCAL_OPERATION.md): previously assigned bounds and local operation.
- [Test methodology](docs/TEST_METHODOLOGY.md): synthetic testing and its evidential limits.
- [Aggregate results](docs/AGGREGATE_RESULTS.md): historical reported totals.
- [Limitations](docs/LIMITATIONS.md): assumptions and untested conditions.

## Candidate status

This is a local publication candidate. Preparing this narrative did not rerun the experiments or publish their implementations.

## License

Unless otherwise noted, this research narrative is licensed under the repository's CC BY-NC-ND 4.0 documentation/research license. The executable reference harness is separately licensed.
