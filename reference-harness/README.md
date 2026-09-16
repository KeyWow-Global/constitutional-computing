# Constitutional Computing Public Reference Harness v0.1

## Scope and current status

> This project is a synthetic public reference harness for reproducible experimentation. It is not the KeyWow production system and should not be interpreted as describing KeyWow's internal implementation.

The harness implements narrow synthetic checks, fixed fixture dispatch, a pass-through reproduction writer, and tests for the supplied cases. Expected results remain independent requirements; the test suite compares them with actual observations. Passing these tests demonstrates only the tested synthetic behavior, not production enforcement or performance.

## Independent design

> This public reference harness was independently designed from public architectural claims and synthetic test requirements. It does not reuse KeyWow production source code, confidential implementation specifications, production datasets, internal test suites, or proprietary configuration.

The fixture inputs were independently invented from public requirements and synthetic test cases. Expected results were separately transcribed from the authorized public case requirements; they were not computed from inputs.

## Inputs and aggregate state

> Action structure and classifications are supplied by synthetic fixtures. The harness does not infer latent intent or formalize arbitrary natural-language actions.

> The harness does not infer latent intent. Aggregate constraints operate only on explicitly represented synthetic state.

All actors, resources, and environments are fictitious. JSON files are case descriptions, not an evaluator design, schema implementation, or ordered evaluation procedure. Different cases contain only the explicit data needed to describe their scenario. Missing fields in F03 and F10 are deliberate. Array order in F09 describes an explicit sequence of supplied changes.

All numerical fixture values, including amounts, replica counts, and state versions, have this designation:

> Synthetic test value. Not derived from production systems.

Each fixture repeats this designation in `numeric_values_note`. The same designation accompanies the numeric rule value. Case identifiers, phase numbers, package versions, and the license year are document or package metadata, not experimental thresholds.

## Files and expected results

- `config/demo-rules.yaml`: static human-readable case requirements; no executable expressions or evaluator ordering.
- `fixtures/`: F01–F14 inputs without expected outcomes.
- `expected/`: one matching YAML filename per fixture, containing only its case identifier and authorized expected result.
- `src/cc_harness/__init__.py`: empty package initializer.
- `tests/`: scenario, unit, metric, invariant, determinism, and adversarial tests.

Each expected file contains an `expected` object with only the relevant observation dimension: `decision` for decision cases, `execution` for F05, `confirmation` for F11, or `demo_call` for F12. `REJECTED` is only the fixture-specific expected result of the F12 direct demo-call test; it is not a general evaluation outcome, execution status, or confirmation status. These fields do not introduce a generalized state or enum.

## Implemented behavior and boundaries

The following boundaries apply to the implemented synthetic mappings and artifact writer.

> The demo executor exists solely to make test behavior observable. It is not a production execution-control mechanism.

The demo executor maps a supplied ADMITTED or ADMITTED_WITH_CONTROLS decision to EXECUTED, and BLOCKED or UNRESOLVED to NOT_EXECUTED. Without a qualifying supplied decision it returns the local demo-call observation REJECTED. These are returned values only; no real-world action is performed.

> The baseline is an intentionally minimal experimental comparator. It does not represent a complete IAM, authorization, policy-enforcement or production security system.

The baseline maps an explicitly supplied true boolean to EXECUTED and false to NOT_EXECUTED; it performs no action.

> Evaluation-log event names and order are explanatory constructs of the public harness and do not represent KeyWow production architecture.

The reproduction writer stores caller-supplied artifacts; it does not generate evaluation logs or metrics. The test-suite runtime is informational and carries this disclaimer:

> Local synthetic test-suite runtime. Not representative of production performance.

## Known limitations

The runtime functions support the approved fixture shapes, not arbitrary input validation. Missing context, action, or action type and unsupported action types are unresolved in the evaluator; an unrestricted transfer is also unresolved. Other malformed inputs may raise exceptions. Missing simulated confirmation is unsupported and raises an exception, which the adversarial test records as a limitation, not a confirmation outcome.

Composition at or above the synthetic minimum returns an empty observation, not admission. Supplied rules text is preserved with LF line endings without YAML validation. Reproduction artifacts contain caller-supplied content without redaction. The checksum covers only canonical input, rules text, and actual output, each prefixed by its unsigned 8-byte big-endian byte length. It does not certify other artifacts. CLI dispatch is fixed to the supplied case identifiers.

## License and trademarks

The public code in this directory is licensed under BSD-3-Clause; see `LICENSE`.

> KeyWow names, logos, trademarks and brand assets are not licensed under the BSD-3-Clause software license.
