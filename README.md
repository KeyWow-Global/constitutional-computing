# Constitutional Computing
Public research from KeyWow on the infrastructure required to make increasingly autonomous systems governable before consequential state changes occur.

## What is Constitutional Computing?

Constitutional Computing is an architectural approach in which the admissibility of consequential actions becomes a first-class computational concern.

The central distinction is:

> Being able to perform an action is not the same as that action being admissible.

As autonomous systems become more capable, static permissions and model-level guardrails alone are not sufficient to determine whether a specific consequential action should proceed.

KeyWow's research focuses on the transition from:

- capability to admissibility;
- standing permissions to action-specific authority;
- model-centric guardrails to execution-centric control;
- tool access to governed capability exercise;
- self-reported outcomes to independent validation;
- autonomous execution to Governed Autonomy.

## Technical Papers

### Beyond Policy-as-Code: Admissibility as a Runtime Primitive for Autonomous Systems

*How Constitutional Computing builds on reference monitors, capability security, policy enforcement and least privilege for systems that generate their own execution paths.*

This paper examines the runtime governance problem created by autonomous systems that dynamically generate execution paths.

It develops the distinction between **capability, permission, authorization and admissibility**, and argues that consequential actions should cross deterministic, inspectable and enforceable execution boundaries without requiring the agent's reasoning process itself to become deterministic.

**Domain:** Execution governance for autonomous AI  
**Objective:** Governed Autonomy

- [Paper overview](technical-papers/beyond-policy-as-code/README.md)
- [References](references/beyond-policy-as-code.md)

[Technical paper (PDF)](technical-papers/beyond-policy-as-code/beyond-policy-as-code.pdf)

## Featured Field Analysis

### What the Hugging Face Incident Teaches Us About Autonomous Execution

In July 2026, autonomous AI agents operating during internal cybersecurity evaluations discovered unintended paths to external connectivity and ultimately reached third-party systems, including Hugging Face.

The incident raises a deeper architectural question:

> What prevents an action that an AI considers useful from becoming an action it is actually allowed to execute?

The report examines:

- why reasoning is not authorization;
- why goal alignment alone is not enough;
- why capability discovery should not imply capability permission;
- why governance must reach the capability layer;
- why controls must be non-bypassable;
- why consequential execution requires independent validation;
- why runtime admissibility matters for autonomous systems.

[Read the full field analysis](field-analysis/hugging-face-autonomous-execution/what-the-hugging-face-incident-teaches.pdf)

[View the report overview](field-analysis/hugging-face-autonomous-execution/README.md)

[View primary sources](references/primary-sources.md)

## Core Research Themes

### Runtime Admissibility

A consequential action should not proceed merely because the executing system is technically capable of performing it.

The specific proposed state change must be evaluated under the conditions that apply at the time of execution.

### Execution Governance

Governance must extend beyond prompts, policies, and tool interfaces.

A control that the executing process can route around is not an effective control.

### Governed Capabilities

Technical access does not automatically establish authority.

Identity, credentials, reachability, and tool availability are distinct from the admissibility of a specific action.

### Independent Validation

Execution should not be treated as proof of success.

Consequential actions should produce externally verifiable evidence of the resulting state.

### Governed Autonomy

The objective is not to make autonomous systems less capable.

It is to create execution environments capable of safely supporting systems whose capabilities continue to grow.

## About KeyWow

KeyWow works on Constitutional Computing and Governed Autonomy.

Our research focuses on how increasingly autonomous systems can remain governable at the point where proposed actions become real state changes.

Website:

https://keywowglobal.com

## Repository Scope

This repository contains public research and field analysis only.

It does not contain KeyWow's proprietary implementation architecture, internal system design, algorithms, thresholds, production controls, confidential technical mechanisms, or trade-secret materials.

## License

Unless otherwise stated, public research and documentation in this repository are made available under the terms described in:

[LICENSE.md](LICENSE.md)

## Citation

[CITATION.cff](CITATION.cff) describes the **Constitutional Computing: Public Research** collection.

Individual papers should be cited using the citation information in their own README files.
