"""Authorized adversarial probes; no runtime behavior is added.

All numerical values are synthetic test values, not production-derived.
"""

import copy
from pathlib import Path
import tempfile
import unittest

from test_harness import fixture, reproduction_args
from cc_harness import cli
from cc_harness.composition import compose
from cc_harness.confirmation import confirm
from cc_harness.demo_executor import execute
from cc_harness.evaluator import evaluate
from cc_harness.reproduction import write_reproduction
from cc_harness.version_check import is_current


class AdversarialTests(unittest.TestCase):
    def test_01_missing_fields(self):
        request = fixture("F01")
        del request["context"]
        self.assertEqual(evaluate(request), {"decision": "UNRESOLVED"})
        request = fixture("F01")
        del request["action"]
        self.assertEqual(evaluate(request), {"decision": "UNRESOLVED"})
        request = fixture("F01")
        del request["action"]["type"]
        self.assertEqual(evaluate(request), {"decision": "UNRESOLVED"})

    def test_02_unknown_action_must_not_silently_admit(self):
        request = fixture("F01")
        request["action"]["type"] = "synthetic-unknown-action"
        result = evaluate(request)
        self.assertEqual(result, {"decision": "UNRESOLVED"})

    def test_02_unrestricted_transfer_is_unresolved(self):
        request = fixture("F13")
        request["context"]["restricted"] = False
        self.assertEqual(evaluate(request), {"decision": "UNRESOLVED"})
        del request["context"]["restricted"]
        self.assertEqual(evaluate(request), {"decision": "UNRESOLVED"})

    def test_03_malformed_rules_are_pass_through_only(self):
        # The writer does not validate YAML or establish decisions from it.
        args = reproduction_args()
        args["demo_rules_text"] = "synthetic: [\r\n"
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "package"
            write_reproduction(target, **args)
            self.assertEqual((target / "demo-rules.yaml").read_bytes(), b"synthetic: [\n")

    def test_04_changed_version(self):
        self.assertFalse(is_current(12, 13))
        self.assertEqual(cli._version_observation({"evaluated_version": 12, "current_version": 13}),
                         {"execution": "NOT_EXECUTED"})

    def test_05_duplicate_inputs(self):
        request = fixture("F08")
        before = copy.deepcopy(request)
        self.assertEqual(compose(request), compose(copy.deepcopy(request)))
        self.assertEqual(request, before)

    def test_06_exact_numeric_boundary(self):
        request = fixture("F14")
        request["state"]["replicas_remaining"] = 4
        # 4 - 2 equals the minimum; this check does not establish admission.
        self.assertEqual(compose(request), {})

    def test_07_one_above_boundary(self):
        request = fixture("F14")
        request["state"]["replicas_remaining"] = 5
        # 5 - 2 is one above the minimum; no admission is inferred.
        self.assertEqual(compose(request), {})

    def test_08_reordered_explicit_sequence(self):
        request = fixture("F09")
        request["sequence"].reverse()
        self.assertEqual(compose(request), {"decision": "BLOCKED"})

    def test_09_direct_demo_executor_invocation(self):
        self.assertEqual(execute(), {"demo_call": "REJECTED"})
        self.assertEqual(execute({}), {"demo_call": "REJECTED"})

    def test_10_missing_confirmation(self):
        request = fixture("F11")
        del request["simulated_confirmation"]
        # Missing confirmation is unsupported; no confirmation is inferred.
        with self.assertRaises(KeyError):
            confirm(request)

    def test_11_unknown_context_field(self):
        request = fixture("F02")
        request["context"]["synthetic_extra_field"] = "ignored"
        self.assertEqual(evaluate(request), {"decision": "BLOCKED"})


if __name__ == "__main__":
    unittest.main(failfast=True)
