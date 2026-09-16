"""Public fixture types only; no runtime validation or evaluation."""

from typing import Literal, TypedDict


# Preserve the supplied JSON fields, including missing fields and action lists.
SyntheticActionRequest = dict[str, object]

DemoExecutionStatus = Literal["EXECUTED", "NOT_EXECUTED"]
ConfirmationStatus = Literal["CONFIRMED", "PENDING", "FAILED", "NOT_REQUIRED"]


class SyntheticResult(TypedDict, total=False):
    """Only observed public dimensions; omitted fields carry no implied result.

    F12's fixture-specific demo_call expectation is outside this container.
    Type annotations do not enforce values at runtime.
    """

    decision: Literal["ADMITTED", "ADMITTED_WITH_CONTROLS", "BLOCKED", "UNRESOLVED"]
    execution: DemoExecutionStatus
    confirmation: ConfirmationStatus
