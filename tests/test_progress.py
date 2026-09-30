import unittest

from fundamentals import progress
from fundamentals.progress import StageError


class ProgressTest(unittest.TestCase):
    def setUp(self):
        self.state = progress.new_state()

    def test_new_state_starts_at_day_one_learning(self):
        self.assertEqual(self.state["current_day"], 1)
        self.assertEqual(progress.stage(self.state), "learn")

    def test_failing_quiz_stays_in_learn_and_counts_attempt(self):
        passed = progress.record_quiz(self.state, 3, 5, "t0")
        self.assertFalse(passed)
        self.assertEqual(progress.stage(self.state), "learn")
        self.assertEqual(progress.current(self.state)["quiz_attempts"], 1)

    def test_passing_quiz_moves_to_discuss(self):
        self.assertTrue(progress.record_quiz(self.state, 4, 5, "t0"))
        self.assertEqual(progress.stage(self.state), "discuss")
        self.assertEqual(progress.current(self.state)["quiz_score"], "4/5")

    def test_quiz_rejects_bad_scores(self):
        with self.assertRaises(ValueError):
            progress.record_quiz(self.state, 6, 5, "t0")
        with self.assertRaises(ValueError):
            progress.record_quiz(self.state, 1, 0, "t0")

    def test_cannot_discuss_before_quiz(self):
        with self.assertRaises(StageError):
            progress.record_discussion(self.state, "notes", "t0")

    def test_discussion_moves_to_solve(self):
        progress.record_quiz(self.state, 5, 5, "t0")
        progress.record_discussion(self.state, "hash map of complements", "t1")
        record = progress.current(self.state)
        self.assertEqual(record["stage"], "solve")
        self.assertEqual(record["discussion_notes"], "hash map of complements")
        self.assertEqual(record["started_at"], "t1")

    def test_cannot_complete_before_solve(self):
        progress.record_quiz(self.state, 5, 5, "t0")
        with self.assertRaises(StageError):
            progress.record_completion(self.state, "t2", total_days=3)

    def test_completion_advances_to_next_day(self):
        progress.record_quiz(self.state, 5, 5, "t0")
        progress.record_discussion(self.state, "", "t1")
        progress.record_completion(self.state, "t2", total_days=3)
        self.assertEqual(self.state["days"]["1"]["stage"], "done")
        self.assertEqual(self.state["days"]["1"]["completed_at"], "t2")
        self.assertEqual(self.state["current_day"], 2)
        self.assertEqual(progress.stage(self.state), "learn")

    def test_completing_last_day_finishes_plan(self):
        self.state["current_day"] = 3
        progress.record_quiz(self.state, 5, 5, "t0")
        progress.record_discussion(self.state, "", "t1")
        progress.record_completion(self.state, "t2", total_days=3)
        self.assertTrue(progress.is_finished(self.state, total_days=3))

    def test_is_done(self):
        self.assertFalse(progress.is_done(self.state, 1))
        progress.record_quiz(self.state, 5, 5, "t0")
        progress.record_discussion(self.state, "", "t1")
        progress.record_completion(self.state, "t2", total_days=3)
        self.assertTrue(progress.is_done(self.state, 1))


if __name__ == "__main__":
    unittest.main()
