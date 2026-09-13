# Beyond Policy-as-Code: Admissibility as a Runtime Primitive for Autonomous Systems

*How Constitutional Computing builds on reference monitors, capability security, policy enforcement and least privilege for systems that generate their own execution paths.*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22738519.svg)](https://doi.org/10.5281/zenodo.22738519)

DOI: https://doi.org/10.5281/zenodo.22738519

**Publication type:** Technical paper  
**Publisher:** KeyWow  
**Domain:** Execution governance for autonomous AI  
**Objective:** Governed Autonomy

## Overview

Autonomous systems increasingly generate their own execution paths: they can form intermediate goals, select tools dynamically, compose actions and adapt strategies at runtime.

This paper examines the execution-governance problem created by that shift.

Constitutional Computing does not replace established security mechanisms such as least privilege, capability security, reference monitors, Zero Trust or policy-as-code. It builds on these foundations and examines how their enforcement requirements apply when autonomous systems generate execution paths dynamically:

> **Should this specific consequential action be allowed to become execution under the conditions that apply now?**

The paper develops the distinction between capability, permission, authorization and admissibility, and examines the architectural requirements that follow from treating admissibility as an explicit runtime concern.

## Core thesis

> **We do not require deterministic reasoning. We require deterministic consequence boundaries.**

Autonomous reasoning may remain probabilistic and open-ended. Consequential effects should cross execution boundaries that are inspectable, enforceable and subject to current governance conditions.

## Research themes

- Constitutional Computing
- Governed Autonomy
- Runtime admissibility
- Reference monitors and complete mediation
- Capability security
- Policy-as-code and policy enforcement
- Least privilege
- Non-bypassable execution governance
- Time-of-check vs. time-of-use
- Compositional execution risk
- Trusted computing base
- Independent verification
- Safety, liveness and governance latency

## Paper

[Download the technical paper (PDF)](beyond-policy-as-code.pdf)

## References

See:

[`../../references/beyond-policy-as-code.md`](../../references/beyond-policy-as-code.md)

## Citation

KeyWow. (2026). *Beyond Policy-as-Code: Admissibility as a Runtime Primitive for Autonomous Systems* (Version 1.0.0). KeyWow. https://doi.org/10.5281/zenodo.22738519

The repository-level [`CITATION.cff`](../../CITATION.cff) describes the broader **Constitutional Computing: Public Research** collection.

## About KeyWow

KeyWow develops architecture for **Governed Autonomy**: enabling increasingly capable autonomous systems while keeping consequential execution subject to independent, enforceable and verifiable governance.

Website: https://keywowglobal.com

## License

This publication is covered by the repository documentation license. See:

[`../../LICENSE.md`](../../LICENSE.md)
