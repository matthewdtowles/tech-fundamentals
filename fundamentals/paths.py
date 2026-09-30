import json
import os
from dataclasses import dataclass
from pathlib import Path

from . import progress

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Paths:
    curriculum: Path
    workspace: Path
    progress_file: Path

    @classmethod
    def default(cls):
        home = Path(os.environ.get("TECH_FUNDAMENTALS_HOME", "~/.tech-fundamentals")).expanduser()
        return cls(curriculum=ROOT / "curriculum", workspace=ROOT / "workspace", progress_file=home / "progress.json")

    def template(self, day):
        return self.curriculum / "problems" / day.filename

    def solution(self, day):
        return self.curriculum / "solutions" / day.filename

    def workspace_file(self, day):
        return self.workspace / day.filename

    def load_state(self):
        if not self.progress_file.exists():
            return progress.new_state()
        return json.loads(self.progress_file.read_text())

    def save_state(self, state):
        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.progress_file.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2) + "\n")
        tmp.replace(self.progress_file)
