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
    "F01": evaluate, "F02": evaluate, "F03": evaluate, "F04": evaluate,
    "F05": _version_observation, "F06": evaluate, "F07": evaluate,
    "F08": compose, "F09": compose, "F10": compose, "F11": confirm,
    "F12": _demo_call, "F13": evaluate, "F14": compose,
}

FIXTURES = (
    "F01-low-impact-development", "F02-protected-target",
    "F03-missing-context", "F04-synthetic-control", "F05-version-change",
    "F06-simple-action-a", "F07-simple-action-b", "F08-aggregate-limit",
    "F09-explicit-prohibited-state", "F10-incomplete-aggregate-state",
    "F11-confirmation-pending", "F12-direct-demo-execution",
    "F13-restricted-synthetic-transfer", "F14-reformulated-aggregate-effect",
)


def _read_fixture(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _actual(request):
    return DISPATCH[request["case_id"]](request)


def _read_expected(path, case_id):
    """Read only the approved three-line expected-file format, not general YAML."""
    text = Path(path).read_text(encoding="utf-8")
    match = re.fullmatch(
        r"case_id: (F[0-9]{2})\nexpected:\n  "
        r"(decision|execution|confirmation|demo_call): ([A-Z_]+)\n?", text,
    )
    if match is None or match[1] != case_id:
        raise ValueError("Expected file must match the approved case and format")
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
                             help="Directory containing the approved fixtures and expected files")
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
                if request["case_id"] not in ("F08", "F09", "F10", "F14"):
                    parser.error("compose accepts only the approved composition fixtures")
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
