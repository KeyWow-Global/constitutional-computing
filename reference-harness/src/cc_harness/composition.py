"""Explicit replica arithmetic for the supplied synthetic composition cases."""

from .models import SyntheticActionRequest, SyntheticResult


# Synthetic test value. Not derived from production systems.
# Matches minimum_replicas_remaining in config/demo-rules.yaml.
MINIMUM_REPLICAS = 2


def compose(request: SyntheticActionRequest) -> SyntheticResult:
    """Handle the supplied C08, C09, C10, and C14 shapes only.

    No arbitrary-input validation or admission decision is provided. An empty
    result means no below-minimum violation was established by this check.
    """
    state = request["state"]
    if "action" in request:
        # C14 supplies its starting count as replicas_remaining.
        remaining = state["replicas_remaining"] - request["action"]["amount"]
    else:
        # C10 omits initial_replicas; do not supply a default.
        if "initial_replicas" not in state:
            return {"decision": "UNRESOLVED"}
        remaining = state["initial_replicas"]
        if "sequence" in request:
            # C09: preserve the explicitly supplied sequence order.
            for reduction in request["sequence"]:
                remaining -= reduction["amount"]
        else:
            # C08: subtract only the explicitly supplied reductions.
            remaining -= sum(reduction["amount"] for reduction in request["actions"])

    if remaining < MINIMUM_REPLICAS:
        return {"decision": "BLOCKED"}
    return {}
