import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from fundamentals import cli
from fundamentals.curriculum import DAYS
from fundamentals.paths import Paths


class CliFlowTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        real = Paths.default()
        tmp = Path(self.tmp.name)
        self.paths = Paths(curriculum=real.curriculum, workspace=tmp / "workspace", progress_file=tmp / "home" / "progress.json")

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = cli.main(list(args), self.paths)
        return code, out.getvalue()

    def test_status_on_fresh_install(self):
        code, out = self.run_cli("status")
        self.assertEqual(code, 0)
        self.assertIn("Day 1", out)
        self.assertIn("learn", out)

    def test_full_day_one_flow(self):
        self.assertEqual(self.run_cli("discussed")[0], 1, "gate: quiz first")
        self.assertEqual(self.run_cli("quiz", "3/5")[0], 1)
        self.assertEqual(self.run_cli("quiz", "4/5")[0], 0)
        self.assertEqual(self.run_cli("solution")[0], 1, "solution locked until done")

        code, out = self.run_cli("discussed", "--notes", "hash map")
        self.assertEqual(code, 0)
        file = self.paths.workspace_file(DAYS[0])
        self.assertTrue(file.exists())
        self.assertIn("GOAL:", file.read_text())

        self.assertEqual(self.run_cli("check")[0], 1, "stub fails")

        solution = self.paths.solution(DAYS[0]).read_text()
        text = file.read_text()
        tests = text[text.index(cli.TESTS_MARKER):]
        file.write_text(solution + "\n\n" + tests)
        code, out = self.run_cli("check")
        self.assertEqual(code, 0, out)
        self.assertIn("Day 2", self.run_cli("status")[1])
        self.assertEqual(self.run_cli("solution", "1")[0], 0)

    def test_scaffold_does_not_overwrite(self):
        self.run_cli("quiz", "5/5")
        self.run_cli("discussed")
        file = self.paths.workspace_file(DAYS[0])
        file.write_text("my work")
        self.run_cli("scaffold")
        self.assertEqual(file.read_text(), "my work")

    def test_complete_rejected_on_code_day(self):
        self.run_cli("quiz", "5/5")
        self.run_cli("discussed")
        self.assertEqual(self.run_cli("complete")[0], 1)


if __name__ == "__main__":
    unittest.main()
