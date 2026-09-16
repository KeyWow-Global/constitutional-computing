"""Standard-library wheel builder for this fixed public harness only."""

import base64
import csv
import hashlib
import io
from pathlib import Path
import zipfile


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    root = Path(__file__).resolve().parent
    modules = (
        "__init__", "baseline", "cli", "composition", "confirmation",
        "demo_executor", "evaluator", "metrics", "models", "reproduction",
        "version_check",
    )
    cases = (
        "C01-low-impact-development", "C02-protected-target",
        "C03-missing-context", "C04-synthetic-control", "C05-version-change",
        "C06-simple-action-a", "C07-simple-action-b", "C08-aggregate-limit",
        "C09-explicit-prohibited-state", "C10-incomplete-aggregate-state",
        "C11-confirmation-pending", "C12-direct-demo-execution",
        "C13-restricted-synthetic-transfer", "C14-explicit-combined-reduction",
    )
    files = {f"cc_harness/{name}.py":
             (root / "src" / "cc_harness" / f"{name}.py").read_bytes()
             for name in modules}
    for directory, extension in (("fixtures", "json"), ("expected", "yaml")):
        for case in cases:
            name = f"{directory}/{case}.{extension}"
            files[f"cc_harness/_data/{name}"] = (root / name).read_bytes()
    info = "cc_harness-0.1.0.dist-info"
    files[f"{info}/METADATA"] = (
        "Metadata-Version: 2.1\nName: cc-harness\nVersion: 0.1.0\n"
        "Summary: Synthetic public reference harness scaffold\n"
        "License: BSD-3-Clause\n\n"
    ).encode("utf-8")
    files[f"{info}/LICENSE"] = (root / "LICENSE").read_bytes()
    files[f"{info}/WHEEL"] = (
        "Wheel-Version: 1.0\nGenerator: cc-harness\n"
        "Root-Is-Purelib: true\nTag: py3-none-any\n"
    ).encode("utf-8")
    files[f"{info}/entry_points.txt"] = (
        "[console_scripts]\ncc-harness = cc_harness.cli:main\n"
    ).encode("utf-8")
    record = io.StringIO(newline="")
    writer = csv.writer(record, lineterminator="\n")
    for name, data in sorted(files.items()):
        digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=")
        writer.writerow((name, "sha256=" + digest.decode("ascii"), len(data)))
    writer.writerow((f"{info}/RECORD", "", ""))
    files[f"{info}/RECORD"] = record.getvalue().encode("utf-8")
    filename = "cc_harness-0.1.0-py3-none-any.whl"
    with zipfile.ZipFile(Path(wheel_directory) / filename, "w") as wheel:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.external_attr = 0o644 << 16
            wheel.writestr(entry, data)
    return filename
