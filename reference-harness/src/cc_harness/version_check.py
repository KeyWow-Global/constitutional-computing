"""Synthetic version comparison only."""


def is_current(evaluated_version: int, current_version: int) -> bool:
    """Compare explicitly supplied integer versions.

    True means the supplied versions are equal, not that execution is authorized.
    False means the supplied versions differ; C05 expects NOT_EXECUTED.
    The caller supplies integers; no runtime type validation is done.
    """
    return evaluated_version == current_version
