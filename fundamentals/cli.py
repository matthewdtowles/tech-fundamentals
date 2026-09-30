import argparse
import subprocess
import sys
from datetime import datetime

from . import curriculum, progress
from .curriculum import DAYS, TESTS_MARKER
from .progress import StageError

MINUTES = {"Easy": 45, "Medium": 75, "Hard": 120}
NEXT_STEP = {
    "learn": "Learn the topic, then pass the quiz (>= 80%).",
    "discuss": "Explain your approach before coding.",
    "solve": "Solve it in the workspace file, then run: ./tf check",
    "done": "Done.",
}


def now():
    return datetime.now().isoformat(timespec="seconds")


def elapsed(start, end):
    minutes = int((datetime.fromisoformat(end) - datetime.fromisoformat(start)).total_seconds() // 60)
    return f"{minutes // 60}h {minutes % 60}m" if minutes >= 60 else f"{minutes}m"


def header(day):
    source = f"LeetCode {day.lc}, {day.difficulty}" if day.lc else day.difficulty
    lines = [f"Day {day.n:02d} — {day.title} ({source})"]
    if day.url:
        lines.append(day.url)
    lines += [f"Pattern: {day.pattern}", f"GOAL: {day.target}"]
    if day.kind == "code":
        return "".join(f"# {line}\n" for line in lines + ["Run tests: ./tf check"]) + "\n"
    return "".join(f"> {line}  \n" for line in lines) + "\n"


def describe(day, state, paths):
    record = state["days"].get(str(day.n), {})
    source = f"LeetCode {day.lc} · {day.difficulty}" if day.lc else day.difficulty
    out = [
        f"Day {day.n}/{len(DAYS)} — {day.title}  [{source}]",
        f"Module:   {day.module}",
        f"Pattern:  {day.pattern}",
        f"Goal:     {day.target}",
        f"Type:     {'Python file with tests' if day.kind == 'code' else 'Written (markdown), reviewed by Claude'}",
        f"Estimate: ~{MINUTES[day.difficulty]} min total",
    ]
    if day.url:
        out.append(f"Link:     {day.url}")
    out.append(f"Stage:    {record.get('stage', 'learn')}")
    out.append("Concepts to teach:")
    out += [f"  - {c}" for c in day.concepts]
    out.append(f"Workspace file: {paths.workspace_file(day)}")
    if record.get("discussion_notes"):
        out.append(f"Discussion notes: {record['discussion_notes']}")
    return "\n".join(out)


def cmd_status(args, state, paths):
    done = sum(progress.is_done(state, d.n) for d in DAYS)
    filled = round(20 * done / len(DAYS))
    print(f"Progress: [{'#' * filled}{'.' * (20 - filled)}] {done}/{len(DAYS)} days")
    if progress.is_finished(state, len(DAYS)):
        print("All days complete.")
        return 0
    day = curriculum.get(state["current_day"])
    stage = progress.stage(state)
    print(f"Current:  Day {day.n} — {day.title} ({day.module})")
    print(f"Stage:    {stage} -> {NEXT_STEP[stage]}")
    return 0


def cmd_list(args, state, paths):
    module = None
    for day in DAYS:
        if day.module != module:
            module = day.module
            print(f"\n{module}")
        mark = "x" if progress.is_done(state, day.n) else (">" if day.n == state["current_day"] else " ")
        print(f"  [{mark}] {day.n:2d}. {day.title}")
    return 0


def cmd_show(args, state, paths):
    print(describe(curriculum.get(args.day or state["current_day"]), state, paths))
    return 0


def cmd_quiz(args, state, paths):
    correct, total = (int(x) for x in args.score.split("/"))
    passed = progress.record_quiz(state, correct, total, now())
    paths.save_state(state)
    if passed:
        print(f"Quiz passed ({correct}/{total}). Next: {NEXT_STEP['discuss']}")
        return 0
    print(f"Quiz not passed ({correct}/{total}, need {progress.QUIZ_PASS_RATIO:.0%}). Review and retake.")
    return 1


def scaffold(day, paths):
    target = paths.workspace_file(day)
    if target.exists():
        return target, False
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(header(day) + paths.template(day).read_text())
    return target, True


def cmd_discussed(args, state, paths):
    progress.record_discussion(state, args.notes, now())
    paths.save_state(state)
    target, _ = scaffold(curriculum.get(state["current_day"]), paths)
    print(f"Ready to solve: {target}")
    return 0


def cmd_scaffold(args, state, paths):
    if progress.stage(state) != "solve":
        raise StageError("Scaffold is only available in the 'solve' stage.")
    target, created = scaffold(curriculum.get(state["current_day"]), paths)
    print(f"{'Created' if created else 'Already exists (not overwritten)'}: {target}")
    return 0


def finish(state, paths):
    day = curriculum.get(state["current_day"])
    started = progress.current(state).get("started_at")
    finished_at = now()
    progress.record_completion(state, finished_at, len(DAYS))
    paths.save_state(state)
    took = f" Solve time: {elapsed(started, finished_at)}." if started else ""
    print(f"Day {day.n} complete: {day.title}.{took}")
    if not progress.is_finished(state, len(DAYS)):
        print(f"Next: Day {state['current_day']} — {curriculum.get(state['current_day']).title}")


def cmd_check(args, state, paths):
    day = curriculum.get(state["current_day"])
    if day.kind != "code":
        raise StageError("This is a written day. Claude reviews it, then runs: ./tf complete")
    if progress.stage(state) != "solve":
        raise StageError(f"Day {day.n} is in stage '{progress.stage(state)}'. {NEXT_STEP[progress.stage(state)]}")
    target = paths.workspace_file(day)
    if not target.exists():
        raise StageError(f"Missing {target}. Run: ./tf scaffold")
    result = subprocess.run([sys.executable, str(target)], capture_output=True, text=True)
    print(result.stdout + result.stderr)
    if result.returncode != 0:
        print("Tests failing. Keep going.")
        return 1
    finish(state, paths)
    return 0


def cmd_complete(args, state, paths):
    day = curriculum.get(state["current_day"])
    if day.kind == "code":
        raise StageError("Code days complete by passing tests: ./tf check")
    finish(state, paths)
    return 0


def cmd_solution(args, state, paths):
    day = curriculum.get(args.day or state["current_day"])
    if not progress.is_done(state, day.n):
        raise StageError(f"Day {day.n} is not done yet. Solve it first.")
    if day.kind != "code":
        raise StageError("Written days have no reference solution.")
    print(paths.solution(day).read_text())
    return 0


def parser():
    p = argparse.ArgumentParser(prog="tf", description="Tech fundamentals: one problem per day.")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="Progress and current stage").set_defaults(fn=cmd_status)
    sub.add_parser("list", help="All days with completion marks").set_defaults(fn=cmd_list)
    show = sub.add_parser("show", help="Day brief: goal, concepts, file")
    show.add_argument("day", nargs="?", type=int)
    show.set_defaults(fn=cmd_show)
    quiz = sub.add_parser("quiz", help="Record a quiz score, e.g. 4/5")
    quiz.add_argument("score")
    quiz.set_defaults(fn=cmd_quiz)
    discussed = sub.add_parser("discussed", help="Record approach discussion and create the workspace file")
    discussed.add_argument("--notes", default="")
    discussed.set_defaults(fn=cmd_discussed)
    sub.add_parser("scaffold", help="Recreate a missing workspace file").set_defaults(fn=cmd_scaffold)
    sub.add_parser("check", help="Run tests; passing completes the day").set_defaults(fn=cmd_check)
    sub.add_parser("complete", help="Complete a written day after review").set_defaults(fn=cmd_complete)
    solution = sub.add_parser("solution", help="Show the reference solution (only after completing)")
    solution.add_argument("day", nargs="?", type=int)
    solution.set_defaults(fn=cmd_solution)
    return p


def main(argv, paths):
    args = parser().parse_args(argv)
    state = paths.load_state()
    try:
        return args.fn(args, state, paths)
    except (StageError, ValueError) as e:
        print(f"Error: {e}")
        return 1
