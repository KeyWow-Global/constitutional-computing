# Composition boundaries

Individually acceptable actions can combine into an unacceptable consequence. A composite invariant is a condition that must continue to hold across the relevant shared scope.

For example, consider a newly invented illustration in which a demonstration must retain an accessible route through a venue. Closing either of two alternative routes may be acceptable when the other is open. Considering the closures independently misses the consequence of both being closed.

This is a qualitative explanation, not a test case from the experimental record.

## The v0.3 question

The experiment evaluated whether individually admissible actions could jointly violate a composite invariant, and whether a shared authoritative scope could prevent the tested conflict.

The relevant scope includes the resources whose combined state determines whether the condition holds. Evaluating only the targeted resource can omit a consequential change elsewhere in that scope.

In the tested architecture, v0.3 evaluated this question inside one authoritative transaction scope. The experimental record reports preservation of the tested composite condition under the stated conforming-writer assumptions.

This experiment did not demonstrate distributed atomicity.

## Boundary of the observation

The result concerns a defined synthetic scope and a defined constraint. It does not establish automatic discovery of resource relationships, interpretation of arbitrary actions or preservation of every possible cross-resource constraint.

The independently committed setting is a separate experimental question, described in [Independent-store experiments](INDEPENDENT_STORE_EXPERIMENTS.md).
