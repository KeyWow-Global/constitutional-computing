# References — Beyond Policy-as-Code

This bibliography supports the technical foundations discussed in:

**Beyond Policy-as-Code: Admissibility as a Runtime Primitive for Autonomous Systems**

The sources below document established security concepts that Constitutional Computing builds upon. They should not be interpreted as claiming that the cited authors endorse KeyWow's architectural interpretation.

## Reference monitors and protection principles

### James P. Anderson
**Computer Security Technology Planning Study, Volume II**  
ESD-TR-73-51, Vol. II  
Electronic Systems Division, Air Force Systems Command  
October 1972.

Foundational work associated with the reference-monitor concept and complete mediation of security-relevant operations.

Reference:
https://seclab.cs.ucdavis.edu/projects/history/papers/ande72.pdf

---

### Jerome H. Saltzer and Michael D. Schroeder
**The Protection of Information in Computer Systems**  
*Proceedings of the IEEE*, 63(9), 1278–1308, September 1975.

Foundational articulation of security design principles including least privilege, complete mediation and economy of mechanism.

DOI:
https://doi.org/10.1109/PROC.1975.9939

## Capability security

### seL4 documentation contributors
**Capabilities**

Documentation of capability-based access control in the seL4 microkernel, where capabilities represent explicit authority over kernel-managed objects and resources.

Reference:
https://docs.sel4.systems/Tutorials/capabilities.html

Accessed September 13, 2026

## Zero Trust

### National Institute of Standards and Technology
**NIST SP 800-207 — Zero Trust Architecture**  
Scott Rose, Oliver Borchert, Stu Mitchell, and Sean Connelly  
August 2020.

Defines Zero Trust architecture, including the separation of policy decision and policy enforcement functions and contextual access decisions.

Reference:
https://csrc.nist.gov/pubs/sp/800/207/final

DOI:
https://doi.org/10.6028/NIST.SP.800-207

PDF:
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf

## Policy-as-code

### Open Policy Agent contributors
**Open Policy Agent (OPA)**

Open Policy Agent is a general-purpose policy engine that separates policy decision-making from policy enforcement and evaluates structured input against declarative policy.

Reference:
https://www.openpolicyagent.org/docs

Accessed September 13, 2026

### Open Policy Agent contributors
**How to Deploy OPA**

Documents OPA deployment models, including placement close to enforcement where latency and availability matter.

Reference:
https://www.openpolicyagent.org/docs/deploy

Accessed September 13, 2026

## Citation note

These references establish prior work in access control, capability security, reference monitors, Zero Trust and policy enforcement.

KeyWow's Constitutional Computing thesis does **not** claim to replace or originate those mechanisms.

The architectural interpretation advanced in the paper is KeyWow's own: that autonomous systems which generate their own execution paths benefit from treating the admissibility of consequential actions as an explicit runtime concern.
