# Experiment lineage

The sequence expands the experimental question while preserving a narrow synthetic setting. Results apply to the tested model and its assumptions.

| Version | Research question | Experimental property | High-level result | Important boundary |
|---|---|---|---|---|
| v0.1 | Can explicit synthetic cases produce repeatable governance observations? | Deterministic handling of supplied inputs | The reference artifact exercises repeatable categorical observations and reproducibility checks. | A returned execution observation is not a real-world action. |
| v0.2 | Would an action admitted against one authoritative resource revision remain executable after relevant state changed? | Admission tied to evaluated state, with a separate observation of the result | The experimental record reports rejection of stale and previously used admissions in the tested cases. | Trusted state and revision discipline are assumptions; observation does not establish causation. |
| v0.3 | Could individually admissible actions jointly violate a composite invariant, and could a shared authoritative scope prevent the tested conflict? | Evaluation of combined consequences within one authoritative transaction scope | The experimental record reports preservation of the tested composite constraint under conforming writers. | This result does not extend to general distributed atomicity. |
| v0.4 | What happens when resource and governance updates commit independently rather than within one common resource transaction? | Conservative treatment of uncertain outcomes across independent stores | The experimental record reports the tested constraint being maintained while ambiguous outcomes remained unresolved where necessary. | Progress can be delayed; observations across stores need not describe one instant. |
| v0.5 | Could ordinary local actions proceed within previously assigned bounds without consulting a root authority for every action? | Bounded local operation, including root-offline scenarios | The experimental record reports ordinary local operation within existing bounds without per-action root access. | Trusted authorities remain assumed; root may still be needed for allocation or coordination outside ordinary actions. |

## What persists across sessions

The later experiments examine governed state shared beyond an individual session. Starting another session or changing an actor label does not reset the relevant resource consequences or previously assigned bounds.

This property is separate from authenticating the caller. The experiments do not demonstrate caller authentication.

## Interpreting the progression

Each version addresses a different experimental boundary. A result inside one authoritative transaction scope does not establish the same behavior across independently committed stores. Local operation without a root consultation for every action does not establish independence from root for all activities.

The historical totals are summarized in [Aggregate results](AGGREGATE_RESULTS.md). They are not measurements from preparing this document.
