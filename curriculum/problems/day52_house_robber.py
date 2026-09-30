"""
Houses along a street hold nums[i] money. Adjacent houses have linked alarms:
robbing two adjacent houses the same night calls the police. Return the most
money you can rob tonight without alerting the police.

Example 1: [1, 2, 3, 1]     ->  4    (1 + 3)
Example 2: [2, 7, 9, 3, 1]  ->  12   (2 + 9 + 1)

Constraints: 1 <= len(nums) <= 100 (perf test: 10^4), 0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import signal
import unittest


class Deadline:
    """Fails the test instead of hanging when an exponential solution runs too long."""

    def __init__(self, seconds, hint):
        self.seconds, self.hint = seconds, hint

    def __enter__(self):
        signal.signal(signal.SIGALRM, self._fail)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)

    def __exit__(self, *exc):
        signal.setitimer(signal.ITIMER_REAL, 0)

    def _fail(self, *_):
        raise TimeoutError(f"Too slow (> {self.seconds}s): {self.hint}")


class TestRob(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)
        self.assertEqual(Solution().rob([2, 7, 9, 3, 1]), 12)

    def test_skip_two(self):
        self.assertEqual(Solution().rob([2, 1, 1, 2]), 4)

    def test_single_and_pair(self):
        self.assertEqual(Solution().rob([5]), 5)
        self.assertEqual(Solution().rob([1, 9]), 9)

    def test_performance(self):
        with Deadline(1, "O(n) DP"):
            self.assertEqual(Solution().rob([1, 2] * 5_000), 10_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
