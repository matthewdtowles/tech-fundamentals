"""Pure state machine for daily progress. Each day moves: learn -> discuss -> solve -> done."""

QUIZ_PASS_RATIO = 0.8


class StageError(Exception):
    pass


def new_state():
    return {"version": 1, "current_day": 1, "days": {}}


def current(state):
    return state["days"].setdefault(str(state["current_day"]), {"stage": "learn", "quiz_attempts": 0})


def stage(state):
    return current(state)["stage"]


def is_done(state, n):
    return state["days"].get(str(n), {}).get("stage") == "done"


def is_finished(state, total_days):
    return state["current_day"] > total_days


def _require(state, expected):
    actual = stage(state)
    if actual != expected:
        raise StageError(f"Day {state['current_day']} is in stage '{actual}', expected '{expected}'.")


def record_quiz(state, correct, total, now):
    if total <= 0 or not 0 <= correct <= total:
        raise ValueError(f"Invalid score {correct}/{total}.")
    _require(state, "learn")
    record = current(state)
    record["quiz_attempts"] += 1
    passed = correct / total >= QUIZ_PASS_RATIO
    if passed:
        record.update(stage="discuss", quiz_score=f"{correct}/{total}", quiz_passed_at=now)
    return passed


def record_discussion(state, notes, now):
    _require(state, "discuss")
    current(state).update(stage="solve", discussion_notes=notes, started_at=now)


def record_completion(state, now, total_days):
    _require(state, "solve")
    current(state).update(stage="done", completed_at=now)
    state["current_day"] += 1
    if not is_finished(state, total_days):
        current(state)
