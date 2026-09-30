"""
You start at index 0 of nums. nums[i] is your MAXIMUM jump length from index i.
Return True if you can reach the last index.

Example 1: [2, 3, 1, 1, 4]  ->  True
Example 2: [3, 2, 1, 0, 4]  ->  False  (always land on the 0 at index 3)

Constraints: 1 <= len(nums) <= 10^4 (a test uses 5 * 10^4), 0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
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


class TestCanJump(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(Solution().canJump([2, 3, 1, 1, 4]))
        self.assertFalse(Solution().canJump([3, 2, 1, 0, 4]))

    def test_single(self):
        self.assertTrue(Solution().canJump([0]))

    def test_zero_at_end_is_fine(self):
        self.assertTrue(Solution().canJump([2, 0, 0]))

    def test_stuck_at_start(self):
        self.assertFalse(Solution().canJump([0, 1]))

    def test_performance(self):
        with Deadline(1, "greedy O(n)"):
            self.assertTrue(Solution().canJump([1] * 50_000))
            self.assertFalse(Solution().canJump(list(range(25_000, 0, -1)) + [0, 0]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
