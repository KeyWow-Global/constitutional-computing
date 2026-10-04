# Test methodology

The experimental program used finite synthetic tests to examine specified behavior under stated assumptions. This narrative summarizes methodology without providing executable tests or operational recipes.

## Methods

- **Deterministic synthetic fixtures:** explicit inputs and expected observations make differences in repeatable cases visible.
- **Finite adversarial tests:** deliberately unsuitable or incomplete conditions challenge the model's stated boundaries.
- **Synchronized race tests:** competing operations exercise concurrency behavior in the tested setting.
- **Simulated crash/retry windows:** controlled interruptions examine how incomplete outcomes affect subsequent observations.
- **Deterministic fuzzing:** scheduled synthetic operation sequences explore combinations beyond individual examples.
- **Actor/session differential tests:** comparable scenarios vary caller labels to examine whether shared consequences depend on those labels.
- **Offline installation and reproducibility checks:** packaging and repeatability checks examine the artifact in the tested environment.

The methods address different questions. Successful installation is not evidence of invariant preservation. Repeatable output is not evidence that every possible input is handled correctly.

## Reading the evidence

Finite testing is evidence about the tested model; it is not a formal proof of all possible executions.

A reported pass means the expected observation was obtained for the specified test. It does not expand the threat model or remove assumptions about trusted storage, revisions, clocks and writers.

A simulated interruption examines a selected condition. It does not reproduce every physical failure, operating-system behavior or network condition.

## Historical record

The totals in [Aggregate results](AGGREGATE_RESULTS.md) are historical reports from the frozen experimental record. Preparing this publication candidate did not rerun those experiments. This narrative alone is not an executable reproduction package.
