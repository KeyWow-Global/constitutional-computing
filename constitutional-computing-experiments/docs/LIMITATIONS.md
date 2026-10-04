# Limitations

The experiments evaluate narrow synthetic models. Their observations depend on assumptions about the components that maintain and report state.

## Trust assumptions

- Storage is trusted to preserve the relevant records.
- Writers are assumed to conform to the model's rules.
- Revision discipline is trusted: relevant changes must be represented consistently.
- Logical clocks, where applicable, are trusted.
- Local and central authorities remain trusted within the tested architecture.

Changing actor or session labels does not reset shared state in the tested cases. This does not establish that a caller's asserted identity is authentic.

## Properties not demonstrated

The experiments do not demonstrate:

- Caller authentication.
- Cryptographic authenticity.
- Byzantine protection.
- Distributed consensus.
- General distributed atomic commit.
- Resistance to malicious storage modification or malicious rollback.

An ABA situation occurs when state changes and later returns to an earlier-looking value. Restored versions can conceal intervening history. The experiments do not establish protection against malicious restoration of state and versions.

## Observation and closure

Observed agreement with an expected result does not establish causation. A separate observer path is not necessarily an independent trust domain.

An observation describes state when observed. It does not establish that the state will remain unchanged or that later changes satisfy the same constraint.

Across independently committed stores, observations need not form a simultaneous view. Uncertainty may remain unresolved, and progress may be delayed.

## Scope of testing

Finite tests examine specified cases, generated sequences and selected concurrent conditions. They do not establish behavior for arbitrary actions, resource relationships or environments.

Simulated crashes are not physical power-loss certification. Offline installation and reproducibility checks do not establish deployment suitability.

Synthetic results do not establish production security. The narrative and aggregate counts should be read together with these limitations.
