# Independent-store experiments

The v0.4 experiment evaluated a setting in which resource and governance updates were independently committed rather than enclosed in one common resource transaction.

The research question was whether the tested constraint could be maintained while treating incomplete knowledge about outcomes conservatively.

## Why independent commits matter

A resource change and a governance record need not become visible together. An interruption can leave uncertainty about which effects occurred or which observations are current.

An executor report alone does not remove that uncertainty. Nor does the absence of a report establish that nothing happened.

Independent commits therefore create reconciliation problems: later observations may need to be considered before the experiment can characterize an outcome. Those observations need not describe every store at the same instant.

## Conservative interpretation

Under the stated assumptions, the experimental record reports preservation of the tested constraint with unresolved outcomes retained where available information did not establish a result.

Maintaining a constraint can come at the expense of progress. The appropriate experimental observation may remain unresolved rather than being treated as success or failure.

This description states the question and observed property only. It does not specify an implementation protocol.

## Limits

The result does not demonstrate a common atomic update across the stores, distributed consensus or resistance to malicious storage changes. Conservative treatment can delay progress indefinitely. Simulated interruptions do not certify behavior under physical power loss or arbitrary network conditions.
