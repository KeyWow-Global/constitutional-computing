"""Synthetic version comparison only."""


def is_current(evaluated_version: int, current_version: int) -> bool:
    """Compare explicitly supplied integer versions.

    True means the prior synthetic result remains current, not that execution
    is authorized. False means it is invalidated and demo execution must not
    proceed. The caller supplies integers; no runtime type validation is done.
    """
    return evaluated_version == current_version
