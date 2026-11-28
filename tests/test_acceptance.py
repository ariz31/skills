"""Executable acceptance coverage for validation and packaging."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_registry import validate, deterministic_route


class AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        cls.skills = {s["id"]: s for s in cls.registry["skills"]}

    def validate_copy(self, mutation=None, registry_mutation=None):
        with tempfile.TemporaryDirectory() as td:
            copyroot = Path(td) / "repo"
            shutil.copytree(ROOT, copyroot, ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))
            data = copy.deepcopy(self.registry)
            if mutation:
                mutation(copyroot)
            if registry_mutation:
                registry_mutation(data)
            return validate(copyroot, data, trigger_file=copyroot / "evaluations/triggers.json")

    def test_positive(self):
        result = self.validate_copy()
        self.assertEqual(result["status"], "pass", result)
        self.assertEqual(result["active_skills"], 10)
        self.assertTrue(all(n <= 800 for n in result["word_counts"].values()))

    def test_word_cap(self):
        def mutate(root):
            file = root / self.skills["ask"]["path"]
            with file.open("a", encoding="utf-8") as f:
                f.write("\n" + "word " * 850)
        result = self.validate_copy(mutate)
        self.assertEqual(result["status"], "fail")
        self.assertTrue(any(x["rule"] == "V8" for x in result["errors"]), result)

    def test_escaped_link(self):
        def mutate(root):
            file = root / self.skills["max"]["path"]
            with file.open("a", encoding="utf-8") as f:
                f.write("\n[bad](../delegate/SKILL.md)\n")
        result = self.validate_copy(mutate)
        self.assertTrue(any(x["rule"] == "V12" for x in result["errors"]), result)

    def test_missing_local_link(self):
        def mutate(root):
            file = root / self.skills["count"]["path"]
            with file.open("a", encoding="utf-8") as f:
                f.write("\n[bad](references/missing.md)\n")
        result = self.validate_copy(mutate)
        self.assertTrue(any(x["rule"] == "V12" for x in result["errors"]), result)

    def test_cycle(self):
        def mutate(data):
            next(s for s in data["skills"] if s["id"] == "delegate")["required_dependencies"] = ["estimate"]
        result = self.validate_copy(registry_mutation=mutate)
        self.assertTrue(any(x["rule"] == "V11" and "cycle" in x["message"] for x in result["errors"]), result)

    def test_optional_cycle_is_advisory(self):
        def mutate(data):
            next(s for s in data["skills"] if s["id"] == "delegate")["optional_dependencies"] = ["ask"]
        result = self.validate_copy(registry_mutation=mutate)
        self.assertEqual(result["status"], "pass", result)
        self.assertTrue(any(x["rule"] == "V11" and "cycle" in x["message"] for x in result["warnings"]), result)

    def test_protected_package_output(self):
        for folder in ("docs", "scripts", "tests", ".git"):
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/package_skill.py"), "--skill", "estimate",
                 "--format", "zip", "--output-dir", str(ROOT / folder / "nested"), "--dry-run"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("unsafe output path", result.stderr)

    def test_read_only_and_install_routing(self):
        self.assertEqual(deterministic_route("Use ariz31/skills @review audit code", self.skills),
                         ("execute", ["delegate", "review"]))
        self.assertEqual(deterministic_route("install ariz31/skills estimate", self.skills),
                         ("install", ["delegate", "estimate"]))
        self.assertEqual(deterministic_route("@delegate split this task", self.skills),
                         ("execute", ["delegate"]))
        self.assertEqual(deterministic_route("@ask @estimate price a house", self.skills),
                         ("clarify_first", ["ask", "delegate", "estimate"]))

    def test_estimate_zip_determinism_and_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            args = [sys.executable, str(ROOT / "scripts/package_skill.py"), "--skill", "estimate",
                    "--platform", "gemini-task", "--format", "zip"]
            archives = []
            for dest in (out / "one", out / "two"):
                subprocess.run(args + ["--output-dir", str(dest)], cwd=ROOT, check=True, capture_output=True, text=True)
                archives.append(next(dest.glob("*.zip")))
            self.assertEqual(archives[0].read_bytes(), archives[1].read_bytes())
            with zipfile.ZipFile(archives[0]) as z:
                names = set(z.namelist())
                self.assertEqual(names, {"estimate/" + p for p in (
                    "SKILL.md", "adapters/gemini-task.md", "references/invariants.md",
                    "references/ph-compliance-and-vat.md", "references/reconciliation-and-audit.md",
                    "PACKAGE_MANIFEST.json")})
                manifest = json.loads(z.read("estimate/PACKAGE_MANIFEST.json"))
                self.assertEqual(manifest["required_dependencies"], ["delegate"])
                for p, digest in manifest["files"].items():
                    self.assertEqual(digest, "sha256:" + hashlib.sha256(z.read("estimate/" + p)).hexdigest())

    def test_rename_and_dry_run(self):
        with tempfile.TemporaryDirectory() as td:
            dest = Path(td) / "output"
            args = [sys.executable, str(ROOT / "scripts/package_skill.py"), "--skill", "threejs-modeling",
                    "--platform", "gemini-task", "--format", "dir", "--rename", "custom-model",
                    "--output-dir", str(dest)]
            subprocess.run(args + ["--dry-run"], cwd=ROOT, check=True, capture_output=True, text=True)
            self.assertFalse(dest.exists())
            subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
            package = dest / "custom-model"
            manifest = json.loads((package / "PACKAGE_MANIFEST.json").read_text())
            self.assertEqual(manifest["source_id"], "3d")
            self.assertEqual(manifest["id"], "custom-model")
            self.assertIn("\nname: custom-model\n", (package / "SKILL.md").read_text())


if __name__ == "__main__":
    unittest.main()
