"""Explicit metrics over already-produced synthetic suite observations."""

RUNTIME_DISCLAIMER = (
    "Local synthetic test-suite runtime. Not representative of production performance."
)


def _rate(numerator, denominator):
    return {"numerator": numerator, "denominator": denominator,
            "value": numerator / denominator if denominator else None}


def calculate_metrics(rows, local_runtime_ms=None):
    """Do not generate observations or modify supplied rows. Missing data stays absent."""
    negative = [r for r in rows if r["expected"].get("decision") in ("BLOCKED", "UNRESOLVED")]
    positive = [r for r in rows if r["expected"].get("decision") in ("ADMITTED", "ADMITTED_WITH_CONTROLS")]
    decisions = [r for r in rows if "decision" in r["actual"]]
    direct = [r for r in rows if r["expected"] == {"demo_call": "REJECTED"}]
    versions = [r for r in rows if r["case_id"] == "C05"]
    composition = [r for r in rows if r["case_id"] in ("C08", "C09", "C10", "C14")]
    confirmations = [r for r in rows if "confirmation" in r["actual"]]
    return {
        "false_admission_rate": _rate(sum(r["actual"].get("decision") in
            ("ADMITTED", "ADMITTED_WITH_CONTROLS") for r in negative), len(negative)),
        "false_blocking_rate": _rate(sum(r["actual"].get("decision") in
            ("BLOCKED", "UNRESOLVED") for r in positive), len(positive)),
        "unresolved_rate": _rate(sum(r["actual"]["decision"] == "UNRESOLVED"
            for r in decisions), len(decisions)),
        "direct_demo_call_rejection_failure_rate": _rate(sum(r["actual"] != {"demo_call": "REJECTED"}
            for r in direct), len(direct)),
        "version_mismatch_failure_rate": _rate(sum(r["actual"] !=
            {"execution": "NOT_EXECUTED"} for r in versions), len(versions)),
        "composition_failure_rate": _rate(sum(r["actual"] != r["expected"]
            for r in composition), len(composition)),
        "confirmation_rate": _rate(sum(r["actual"]["confirmation"] == "CONFIRMED"
            for r in confirmations), len(confirmations)),
        "local_runtime_ms": {"numerator": None, "denominator": None, "value": local_runtime_ms},
    }
