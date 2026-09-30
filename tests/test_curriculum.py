"""Validates every day's content: files exist, stubs fail, reference solutions pass."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from fundamentals.curriculum import DAYS, TESTS_MARKER
from fundamentals.paths import Paths

PATHS = Paths.default()


def run_python(source):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(source)
    try:
        return subprocess.run([sys.executable, f.name], capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return None
    finally:
        Path(f.name).unlink()


class CurriculumTest(unittest.TestCase):
    def test_days_are_numbered_consecutively(self):
        self.assertEqual([d.n for d in DAYS], list(range(1, len(DAYS) + 1)))

    def test_slugs_are_unique(self):
        slugs = [d.slug for d in DAYS]
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_every_day_has_template(self):
        for day in DAYS:
            with self.subTest(day=day.n):
                self.assertTrue(PATHS.template(day).exists(), PATHS.template(day))
                self.assertTrue(day.concepts, "concepts drive the lesson")
                self.assertTrue(day.target, "every day needs a goal")

    def test_code_templates_have_tests_marker_and_solution(self):
        for day in DAYS:
            if day.kind != "code":
                continue
            with self.subTest(day=day.n):
                self.assertIn(TESTS_MARKER, PATHS.template(day).read_text())
                self.assertTrue(PATHS.solution(day).exists(), PATHS.solution(day))

    def test_stubs_fail_and_solutions_pass(self):
        for day in DAYS:
            if day.kind != "code":
                continue
            with self.subTest(day=day.n, slug=day.slug):
                template = PATHS.template(day).read_text()
                tests = template[template.index(TESTS_MARKER):]
                solved = run_python(PATHS.solution(day).read_text() + "\n\n" + tests)
                self.assertIsNotNone(solved, "solution timed out")
                self.assertEqual(solved.returncode, 0, solved.stderr[-3000:])
                stub = run_python(template)
                if stub is not None:
                    self.assertNotEqual(stub.returncode, 0, "stub should fail its tests")


if __name__ == "__main__":
    unittest.main()
