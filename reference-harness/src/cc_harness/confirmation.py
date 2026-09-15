"""Map an explicit synthetic confirmation flag to its public observation."""

from .models import SyntheticActionRequest, SyntheticResult


def confirm(request: SyntheticActionRequest) -> SyntheticResult:
    """Require an explicitly supplied boolean simulated_confirmation field.

    No other field is read. This does not establish real-world completion.
    Arbitrary-input validation is outside this fixture-only function.
    """
    if request["simulated_confirmation"] is True:
        return {"confirmation": "CONFIRMED"}
    return {"confirmation": "PENDING"}
