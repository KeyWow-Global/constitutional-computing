"""Toy checks for the supported synthetic actions and explicit missing-field probes."""

from .models import SyntheticActionRequest, SyntheticResult


def evaluate(request: SyntheticActionRequest) -> SyntheticResult:
    """Evaluate supported fixture shapes without arbitrary-input validation.

    Missing context, action, or action type and unsupported actions are unresolved.
    """
    if "context" not in request or "action" not in request:
        return {"decision": "UNRESOLVED"}
    action_type = request["action"].get("type")
    if action_type not in ("reduce_replicas", "transfer"):
        return {"decision": "UNRESOLVED"}

    context = request["context"]
    if action_type == "transfer":
        # Only explicitly restricted synthetic transfers have an supported result.
        if context.get("restricted") is True:
            return {"decision": "BLOCKED"}
        return {"decision": "UNRESOLVED"}

    # The remaining supported action is reduce_replicas.
    if context["protected"] is True:
        return {"decision": "BLOCKED"}
    if context.get("required_control") == "demo-operator confirmation":
        return {"decision": "ADMITTED_WITH_CONTROLS"}
    return {"decision": "ADMITTED"}
