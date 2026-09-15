"""Public synthetic tests only. Numerical values are synthetic test values,
not derived from production systems. No private tests or data are used.
"""

import copy
from contextlib import redirect_stdout, redirect_stderr
import hashlib
from io import StringIO
import json
from pathlib import Path
import shutil
import struct
import sys
import tempfile
import typing
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cc_harness import cli
from cc_harness.baseline import baseline
from cc_harness.composition import compose
from cc_harness.confirmation import confirm
from cc_harness.demo_executor import execute
from cc_harness.evaluator import evaluate
from cc_harness.metrics import calculate_metrics, RUNTIME_DISCLAIMER
from cc_harness.models import SyntheticResult, DemoExecutionStatus, ConfirmationStatus
from cc_harness.reproduction import write_reproduction
from cc_harness.version_check import is_current


def fixture(case_id):
    stem = next(s for s in cli.FIXTURES if s.startswith(case_id + "-"))
    return json.loads((ROOT / "fixtures" / (stem + ".json")).read_text())


def invoke(args):
    output = StringIO()
    with redirect_stdout(output):
        code = cli.main(args)
    return code, json.loads(output.getvalue())


def reproduction_args():
    return dict(input_data={"z": 1, "a": "é"},
                expected_result={"expected": {"decision": "ADMITTED"}},
                actual_result={"decision": "ADMITTED"},
                evaluation_log=["RESULT_RECORDED"],
                demo_rules_text="b: 2\r\na: 1\r", harness_version="0.1.0")


class ScenarioTests(unittest.TestCase):
    def check_case(self, case_id):
        request = fixture(case_id)
        actual = cli._actual(request)
        stem = next(s for s in cli.FIXTURES if s.startswith(case_id + "-"))
        expected = cli._read_expected(ROOT / "expected" / (stem + ".yaml"), case_id)
        self.assertEqual(actual, expected)

    def test_f01(self): self.check_case("F01")
    def test_f02(self): self.check_case("F02")
    def test_f03(self): self.check_case("F03")
    def test_f04(self): self.check_case("F04")
    def test_f05(self): self.check_case("F05")
    def test_f06(self): self.check_case("F06")
    def test_f07(self): self.check_case("F07")
    def test_f08(self): self.check_case("F08")
    def test_f09(self): self.check_case("F09")
    def test_f10(self): self.check_case("F10")
    def test_f11(self): self.check_case("F11")
    def test_f12(self): self.check_case("F12")
    def test_f13(self): self.check_case("F13")
    def test_f14(self): self.check_case("F14")


class UnitTests(unittest.TestCase):
    def test_status_domains(self):
        self.assertEqual(set(typing.get_args(DemoExecutionStatus)), {"EXECUTED", "NOT_EXECUTED"})
        self.assertEqual(set(typing.get_args(ConfirmationStatus)), {"CONFIRMED", "PENDING", "FAILED", "NOT_REQUIRED"})
        hints = typing.get_type_hints(SyntheticResult)
        self.assertEqual(set(hints), {"decision", "execution", "confirmation"})
        self.assertEqual(set(typing.get_args(hints["decision"])), {"ADMITTED", "ADMITTED_WITH_CONTROLS", "BLOCKED", "UNRESOLVED"})
        self.assertFalse(SyntheticResult.__required_keys__)

    def test_version_equality_and_adapter(self):
        self.assertTrue(is_current(12, 12))
        self.assertFalse(is_current(12, 13))
        self.assertFalse(is_current(13, 12))
        self.assertEqual(cli._version_observation({"evaluated_version": 12, "current_version": 12}), {})

    def test_confirmation_both_values(self):
        self.assertEqual(confirm({"simulated_confirmation": True}), {"confirmation": "CONFIRMED"})
        self.assertEqual(confirm({"simulated_confirmation": False}), {"confirmation": "PENDING"})

    def test_execution_four_decisions_and_absence(self):
        for decision in ("ADMITTED", "ADMITTED_WITH_CONTROLS"):
            self.assertEqual(execute({"decision": decision}), {"execution": "EXECUTED"})
        for decision in ("BLOCKED", "UNRESOLVED"):
            self.assertEqual(execute({"decision": decision}), {"execution": "NOT_EXECUTED"})
        self.assertEqual(execute(), {"demo_call": "REJECTED"})
        self.assertEqual(execute({}), {"demo_call": "REJECTED"})

    def test_baseline_boolean(self):
        self.assertEqual(baseline(True), {"execution": "EXECUTED"})
        self.assertEqual(baseline(False), {"execution": "NOT_EXECUTED"})

    def test_all_cli_commands(self):
        f = str(ROOT / "fixtures/F02-protected-target.json")
        self.assertEqual(invoke(["evaluate", f]), (0, {"decision": "BLOCKED"}))
        self.assertEqual(invoke(["compose", str(ROOT / "fixtures/F08-aggregate-limit.json")]), (0, {"decision": "BLOCKED"}))
        for flag, value in (("true", "EXECUTED"), ("false", "NOT_EXECUTED")):
            self.assertEqual(invoke(["baseline", "--baseline-authorized", flag]), (0, {"execution": value}))
            self.assertEqual(invoke(["compare", f, "--baseline-authorized", flag]),
                             (0, {"baseline": {"execution": value}, "harness": {"decision": "BLOCKED"}}))
        code, report = invoke(["test-suite"])
        self.assertEqual(code, 0)
        self.assertEqual(len(report["cases"]), 14)
        self.assertTrue(all(r["matched"] for r in report["cases"]))
        self.assertEqual(report["runtime_disclaimer"], RUNTIME_DISCLAIMER)

    def test_cli_requires_explicit_baseline(self):
        for args in (["baseline"], ["compare", str(ROOT / "fixtures/F01-low-impact-development.json")]):
            with redirect_stderr(StringIO()), self.assertRaises(SystemExit) as error:
                cli.main(args)
            self.assertEqual(error.exception.code, 2)

    def test_reproduction_framing_and_artifacts(self):
        args = reproduction_args()
        parts = (b'{"a":"\xc3\xa9","z":1}', b'b: 2\na: 1\n', b'{"decision":"ADMITTED"}')
        expected = hashlib.sha256(b"".join(struct.pack(">Q", len(p)) + p for p in parts)).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "package"
            self.assertEqual(write_reproduction(target, **args), expected)
            for name, value in zip(("input.json", "demo-rules.yaml", "actual.json"), parts):
                self.assertEqual((target / name).read_bytes(), value)
            self.assertEqual(json.loads((target / "expected.yaml").read_text()), args["expected_result"])
            self.assertEqual(json.loads((target / "evaluation-log.json").read_text()), args["evaluation_log"])
            self.assertEqual(json.loads((target / "manifest.json").read_text()),
                             {"harness_version": "0.1.0", "reproduction_checksum": expected})
            self.assertEqual(len(list(target.iterdir())), 6)
            other = Path(directory) / "with-metrics"
            self.assertEqual(write_reproduction(other, **args, metrics={}, fixture_identifier="F01"), expected)
            self.assertEqual(json.loads((other / "metrics.json").read_text()), {})
            self.assertEqual(len(list(other.iterdir())), 7)

    def test_reproduction_component_boundaries(self):
        args = reproduction_args()
        with tempfile.TemporaryDirectory() as directory:
            a = write_reproduction(Path(directory) / "a", **dict(args, input_data=1, demo_rules_text="23", actual_result=4))
            b = write_reproduction(Path(directory) / "b", **dict(args, input_data=12, demo_rules_text="3", actual_result=4))
            self.assertNotEqual(a, b)


class MetricTests(unittest.TestCase):
    def test_approved_suite_rates(self):
        metrics = calculate_metrics(cli.run_test_suite(ROOT))
        expected = {"false_admission_rate": (0, 7), "false_blocking_rate": (0, 4),
                    "unresolved_rate": (2, 11), "demo_bypass_rate": (0, 1),
                    "state_invalidation_failure_rate": (0, 1),
                    "simple_composition_failure_rate": (0, 4), "confirmation_rate": (0, 1)}
        for name, (n, d) in expected.items():
            self.assertEqual(metrics[name], {"numerator": n, "denominator": d, "value": n / d})

    def test_zero_denominators_and_unavailable(self):
        self.assertTrue(all(m["value"] is None for m in calculate_metrics([]).values()))
        metrics = calculate_metrics(cli.run_test_suite(ROOT))
        for name in ("task_completion_rate", "baseline_divergence_rate"):
            self.assertEqual(metrics[name], {"numerator": None, "denominator": None, "value": None})

    def test_nonzero_failure_numerators(self):
        rows = cli.run_test_suite(ROOT)
        changes = {"F01": {"decision": "UNRESOLVED"}, "F02": {"decision": "ADMITTED_WITH_CONTROLS"},
                   "F05": {}, "F08": {"decision": "ADMITTED"}, "F11": {"confirmation": "CONFIRMED"},
                   "F12": {"demo_call": "REJECTED", "execution": "EXECUTED"}}
        for row in rows:
            if row["case_id"] in changes: row["actual"] = changes[row["case_id"]]
        metrics = calculate_metrics(rows)
        for name, n in (("false_admission_rate", 2), ("false_blocking_rate", 1),
                        ("unresolved_rate", 3), ("demo_bypass_rate", 1),
                        ("state_invalidation_failure_rate", 1),
                        ("simple_composition_failure_rate", 1), ("confirmation_rate", 1)):
            self.assertEqual(metrics[name]["numerator"], n)

    def test_controls_are_not_false_blocking(self):
        rows = [{"case_id": "F04", "expected": {"decision": "ADMITTED_WITH_CONTROLS"},
                 "actual": {"decision": "ADMITTED"}}]
        self.assertEqual(calculate_metrics(rows)["false_blocking_rate"]["value"], 0)

    def test_missing_observations_are_not_inferred(self):
        rows = [{"case_id": "F02", "expected": {"decision": "BLOCKED"}, "actual": {}}]
        metrics = calculate_metrics(rows)
        self.assertEqual(metrics["false_admission_rate"]["denominator"], 1)
        self.assertEqual(metrics["false_admission_rate"]["numerator"], 0)
        self.assertIsNone(metrics["unresolved_rate"]["value"])
        self.assertIsNone(metrics["confirmation_rate"]["value"])

    def test_runtime_clock_boundary_and_conversion(self):
        events = []
        read = cli._read_fixture
        expected = cli._read_expected
        def clock():
            events.append("clock")
            return 10.0 if events.count("clock") == 1 else 10.25
        def read_fixture(path):
            events.append(Path(path).stem[:3])
            return read(path)
        def read_expected(path, case_id):
            events.append("expected-" + case_id)
            return expected(path, case_id)
        with patch.object(cli, "perf_counter", side_effect=clock), \
             patch.object(cli, "_read_fixture", side_effect=read_fixture), \
             patch.object(cli, "_read_expected", side_effect=read_expected):
            code, report = invoke(["test-suite"])
        self.assertEqual(code, 0)
        self.assertEqual(events[:2], ["clock", "F01"])
        self.assertEqual(events[-2:], ["expected-F14", "clock"])
        self.assertEqual(report["metrics"]["local_runtime_ms"]["value"], 250)


class InvariantTests(unittest.TestCase):
    def test_expected_changes_cannot_change_actual(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "fixtures", root / "fixtures")
            shutil.copytree(ROOT / "expected", root / "expected")
            (root / "expected/F01-low-impact-development.yaml").write_text(
                "case_id: F01\nexpected:\n  decision: BLOCKED\n")
            code, report = invoke(["test-suite", "--root", str(root)])
            self.assertEqual(code, 1)
            self.assertEqual(report["cases"][0]["actual"], {"decision": "ADMITTED"})
            self.assertFalse(report["cases"][0]["matched"])

    def test_modules_and_metrics_preserve_inputs(self):
        for stem in cli.FIXTURES:
            request = fixture(stem[:3])
            before = copy.deepcopy(request)
            cli._actual(request)
            self.assertEqual(request, before)
        rows = cli.run_test_suite(ROOT)
        before = copy.deepcopy(rows)
        calculate_metrics(rows)
        self.assertEqual(rows, before)

    def test_behavior_modules_ignore_case_identifier(self):
        for stem in cli.FIXTURES:
            request = fixture(stem[:3])
            handler = cli.DISPATCH[request["case_id"]]
            before = handler(request)
            request["case_id"] = "synthetic-renamed-case"
            self.assertEqual(handler(request), before)

    def test_confirmation_ignores_invocation_completion(self):
        request = fixture("F11")
        request["invocation_completed"] = False
        self.assertEqual(confirm(request), {"confirmation": "PENDING"})

    def test_runtime_does_not_control_match_or_exit(self):
        with patch.object(cli, "perf_counter", side_effect=[0, 1]):
            first_code, first = invoke(["test-suite"])
        with patch.object(cli, "perf_counter", side_effect=[0, 100]):
            second_code, second = invoke(["test-suite"])
        self.assertEqual(first_code, second_code)
        self.assertEqual(first["cases"], second["cases"])
        first["metrics"].pop("local_runtime_ms")
        second["metrics"].pop("local_runtime_ms")
        self.assertEqual(first["metrics"], second["metrics"])

    def test_runtime_metrics_do_not_enter_checksum(self):
        with tempfile.TemporaryDirectory() as directory:
            args = reproduction_args()
            a = write_reproduction(Path(directory) / "a", **args, metrics={"local_runtime_ms": 1})
            b = write_reproduction(Path(directory) / "b", **args, metrics={"local_runtime_ms": 100})
            self.assertEqual(a, b)


class DeterminismTests(unittest.TestCase):
    def test_repeated_suite_and_metrics(self):
        first = cli.run_test_suite(ROOT)
        second = cli.run_test_suite(ROOT)
        self.assertEqual(first, second)
        self.assertEqual(calculate_metrics(first), calculate_metrics(second))

    def test_json_order_and_line_endings(self):
        with tempfile.TemporaryDirectory() as directory:
            args = reproduction_args()
            a = write_reproduction(Path(directory) / "a", **args)
            args["input_data"] = {"a": "é", "z": 1}
            args["demo_rules_text"] = "b: 2\na: 1\n"
            b = write_reproduction(Path(directory) / "b", **args)
            self.assertEqual(a, b)
            for p in (Path(directory) / "a").iterdir():
                self.assertEqual(p.read_bytes(), (Path(directory) / "b" / p.name).read_bytes())

    def test_changed_checksum_components(self):
        with tempfile.TemporaryDirectory() as directory:
            args = reproduction_args()
            original = write_reproduction(Path(directory) / "original", **args)
            for key, value in (("input_data", {}), ("actual_result", {"decision": "BLOCKED"}),
                               ("demo_rules_text", "a: 1\nb: 2\n")):
                changed = write_reproduction(Path(directory) / key, **dict(args, **{key: value}))
                self.assertNotEqual(original, changed)


if __name__ == "__main__":
    unittest.main()
