# Aggregate results

The frozen experimental record reports the following historical automated-test totals:

| Experiment | Reported tests passed |
|---|---:|
| v0.2 | 86/86 |
| v0.3 | 97/97 |
| v0.4 | 168/168 |
| v0.5 | 200/200 |

For v0.5, the frozen experimental record reports additional testing at aggregate level:

- Thousands of synchronized concurrency trials.
- 225,000 scheduled fuzz operations.
- A 1,000-seed actor/session differential.
- Root-offline local operation scenarios within already assigned bounds.

These measures describe different units of testing. Scheduled operations, seeds and concurrency trials are not additional independently counted automated test cases and should not be added to the table totals.

## Interpretation

The observations concern synthetic models under stated assumptions. Counts do not measure production coverage, severity, reliability in an untested environment or behavior under all possible executions.

The versions address different questions, so their test totals are not a ranking of quality or strength.

Preparing this publication candidate did not rerun these experiments. The figures are historical reported results, not new validation outcomes from this documentation task.
