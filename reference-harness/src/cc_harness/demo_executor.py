"""Return synthetic observations only; no action is performed."""

from .models import SyntheticResult


def execute(prior_result: SyntheticResult | None = None) -> dict[str, str]:
    """Read only the supplied decision; do not establish or verify it.

    The local demo_call rejection is not a SyntheticResult status.
    """
    decision = prior_result.get("decision") if prior_result is not None else None
    if decision in ("ADMITTED", "ADMITTED_WITH_CONTROLS"):
        return {"execution": "EXECUTED"}
    if decision in ("BLOCKED", "UNRESOLVED"):
        return {"execution": "NOT_EXECUTED"}
    return {"demo_call": "REJECTED"}
