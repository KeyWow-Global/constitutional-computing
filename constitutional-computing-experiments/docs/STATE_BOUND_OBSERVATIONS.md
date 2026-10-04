# State-bound observations

Permission alone is not sufficient to establish that an action remains appropriate for the current relevant state. An admission can depend on the resource state and policy version considered during evaluation.

A resource revision identifies the state considered by an evaluation. When a relevant revision or bound policy version changes, an earlier admission can become stale. Re-evaluation may be needed before proceeding.

The experiment distinguishes a previously admitted action from a currently applicable admission. In the tested cases, an admission that had already been used did not provide another execution opportunity.

## Illustrative examples

The following qualitative examples are newly invented explanations. They are not experiment fixtures, recorded runs or implementation recipes.

### A changed destination

A proposed action places a sample into a cabinet compartment. At evaluation, the compartment is available. Before the action proceeds, an external operator marks that compartment unavailable.

The earlier permission does not establish that the current destination remains appropriate. The relevant current state must inform a new determination.

### A changed policy

A proposal to display a synthetic notice is evaluated under the current publication policy. Before it proceeds, the applicable policy changes to require an additional review.

The prior determination refers to the policy considered at evaluation. It is not an indefinite permission under later conditions.

### A report and an observation

An executor reports that a synthetic indicator changed to its requested setting. A separate observation still shows the previous setting.

The report establishes what the executor said. It does not, by itself, establish that the requested result was observed. Missing observation also leaves a different question from an observed mismatch.

## Observation boundary

Closure concerns the observed resulting state in relation to the expected consequence. It is distinct from the executor's success report.

A separate observation path does not necessarily belong to an independent trust domain. In these experiments, trusted storage remains an assumption. A matching observation does not establish which actor caused the state or how long the state will persist.
