"""Intentionally minimal synthetic experimental comparator."""

from .models import SyntheticResult


def baseline(technically_authorized: bool) -> SyntheticResult:
    """Map a caller-supplied boolean to a synthetic execution observation.

    No authorization is determined and no action is performed.
    The caller supplies a boolean; no runtime type validation is done.
    """
    if technically_authorized is True:
        return {"execution": "EXECUTED"}
    return {"execution": "NOT_EXECUTED"}
