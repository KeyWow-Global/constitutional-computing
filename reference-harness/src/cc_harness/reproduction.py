"""Write caller-supplied reproduction artifacts without computing behavior."""

import hashlib
import json
from pathlib import Path


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def write_reproduction(
    directory: str | Path,
    *,
    input_data: object,
    expected_result: object,
    actual_result: object,
    evaluation_log: object,
    demo_rules_text: str,
    harness_version: str,
    fixture_identifier: str | None = None,
    metrics: object = None,
) -> str:
    """Write into a new directory and return its reproduction checksum.

    Values must be JSON-serializable. None means metrics were not supplied.
    expected.yaml uses JSON syntax, which is valid YAML, without YAML parsing.
    Version and optional fixture identifier are supplied by the caller.
    No timestamps or additional observations are generated.
    """
    canonical_input = _canonical_json(input_data)
    canonical_output = _canonical_json(actual_result)
    canonical_rules = demo_rules_text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    checksum = hashlib.sha256(
        len(canonical_input).to_bytes(8, "big", signed=False) + canonical_input
        + len(canonical_rules).to_bytes(8, "big", signed=False) + canonical_rules
        + len(canonical_output).to_bytes(8, "big", signed=False) + canonical_output
    ).hexdigest()
    manifest = {
        "harness_version": harness_version,
        "reproduction_checksum": checksum,
    }
    if fixture_identifier is not None:
        manifest["fixture_identifier"] = fixture_identifier
    artifacts = {
        "input.json": canonical_input,
        "demo-rules.yaml": canonical_rules,
        "expected.yaml": _canonical_json(expected_result),
        "actual.json": canonical_output,
        "evaluation-log.json": _canonical_json(evaluation_log),
        "manifest.json": _canonical_json(manifest),
    }
    if metrics is not None:
        artifacts["metrics.json"] = _canonical_json(metrics)
    destination = Path(directory)
    destination.mkdir(parents=True, exist_ok=False)
    for name, content in artifacts.items():
        (destination / name).write_bytes(content)
    return checksum
