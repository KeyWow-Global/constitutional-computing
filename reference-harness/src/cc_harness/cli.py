"""Fixed public fixture CLI; observations are produced before expectations load."""

import argparse
import json
from pathlib import Path
import re
from time import perf_counter

from .baseline import baseline
from .composition import compose
from .confirmation import confirm
from .demo_executor import execute
from .evaluator import evaluate
from .version_check import is_current
from .metrics import calculate_metrics, RUNTIME_DISCLAIMER


def _version_observation(request):
    if not is_current(request["evaluated_version"], request["current_version"]):
        return {"execution": "NOT_EXECUTED"}
    return {}


def _demo_call(request):
    return execute(request["supplied_result"])


DISPATCH = {
    "C01": evaluate, "C02": evaluate, "C03": evaluate, "C04": evaluate,
    "C05": _version_observation, "C06": evaluate, "C07": evaluate,
    "C08": compose, "C09": compose, "C10": compose, "C11": confirm,
    "C12": _demo_call, "C13": evaluate, "C14": compose,
}

FIXTURES = (
    "C01-low-impact-development", "C02-protected-target",
    "C03-missing-context", "C04-synthetic-control", "C05-version-change",
    "C06-simple-action-a", "C07-simple-action-b", "C08-aggregate-limit",
    "C09-explicit-prohibited-state", "C10-incomplete-aggregate-state",
    "C11-confirmation-pending", "C12-direct-demo-execution",
    "C13-restricted-synthetic-transfer", "C14-explicit-combined-reduction",
)


def _read_fixture(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _actual(request):
    return DISPATCH[request["case_id"]](request)


def _read_expected(path, case_id):
    """Read only the supported three-line expected-file format, not general YAML."""
    text = Path(path).read_text(encoding="utf-8")
    match = re.fullmatch(
        r"case_id: (C[0-9]{2})\nexpected:\n  "
        r"(decision|execution|confirmation|demo_call): ([A-Z_]+)\n?", text,
    )
    if match is None or match[1] != case_id:
        raise ValueError("Expected file must match the supported case and format")
    return {match[2]: match[3]}


def run_test_suite(root, timing=None):
    rows = []
    started = perf_counter()
    for stem in FIXTURES:
        request = _read_fixture(Path(root) / "fixtures" / (stem + ".json"))
        case_id = stem[:3]
        if request["case_id"] != case_id:
            raise ValueError("Fixture identifier does not match its filename")
        actual = _actual(request)
        expected = _read_expected(Path(root) / "expected" / (stem + ".yaml"), case_id)
        rows.append({"case_id": case_id, "expected": expected,
                     "actual": actual, "matched": actual == expected})
    elapsed_ms = (perf_counter() - started) * 1000
    if timing is not None:
        timing["local_runtime_ms"] = elapsed_ms
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description="Synthetic public fixture observations only")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("evaluate").add_argument("fixture", type=Path)
    commands.add_parser("compose").add_argument("fixture", type=Path)
    baseline_parser = commands.add_parser("baseline")
    baseline_parser.add_argument("--baseline-authorized", choices=("true", "false"), required=True)
    compare_parser = commands.add_parser("compare")
    compare_parser.add_argument("fixture", type=Path)
    compare_parser.add_argument("--baseline-authorized", choices=("true", "false"), required=True)
    suite_parser = commands.add_parser("test-suite")
    suite_parser.add_argument("--root", type=Path, default=(Path(__file__).resolve().parent / "_data"
                                      if (Path(__file__).resolve().parent / "_data").is_dir()
                                      else Path(__file__).resolve().parents[2]),
                             help="Directory containing the supported fixtures and expected files")
    args = parser.parse_args(argv)
    try:
        if args.command == "baseline":
            result = baseline(args.baseline_authorized == "true")
        elif args.command == "test-suite":
            timing = {}
            rows = run_test_suite(args.root, timing)
            result = {"cases": rows,
                      "metrics": calculate_metrics(rows, timing["local_runtime_ms"]),
                      "runtime_disclaimer": RUNTIME_DISCLAIMER}
        else:
            request = _read_fixture(args.fixture)
            if args.command == "compose":
                if request["case_id"] not in ("C08", "C09", "C10", "C14"):
                    parser.error("compose accepts only the supported composition fixtures")
                result = compose(request)
            elif args.command == "compare":
                baseline_result = baseline(args.baseline_authorized == "true")
                result = {"baseline": baseline_result, "harness": _actual(request)}
            else:
                result = _actual(request)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    print(json.dumps(result, sort_keys=True, ensure_ascii=False))
    if args.command == "test-suite" and not all(row["matched"] for row in result["cases"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
