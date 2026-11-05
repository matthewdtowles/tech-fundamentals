import os
import unittest
from pathlib import Path
from unittest import mock

from fundamentals.paths import ROOT, Paths


class PathsTest(unittest.TestCase):
    def test_progress_lives_in_repo_by_default(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(Paths.default().progress_file, ROOT / "progress.json")

    def test_env_var_overrides_progress_dir(self):
        with mock.patch.dict(os.environ, {"TECH_FUNDAMENTALS_HOME": "/tmp/tf"}):
            self.assertEqual(Paths.default().progress_file, Path("/tmp/tf/progress.json"))


if __name__ == "__main__":
    unittest.main()
