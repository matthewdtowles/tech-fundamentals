"""
Given an integer array nums, return the length of the longest STRICTLY
increasing subsequence (not necessarily contiguous).

Example 1: [10, 9, 2, 5, 3, 7, 101, 18]  ->  4   ([2, 3, 7, 101])
Example 2: [0, 1, 0, 3, 2, 3]            ->  4
Example 3: [7, 7, 7, 7]                  ->  1

Constraints: 1 <= len(nums) <= 2500 (perf test: 20,000)
Start with the O(n^2) DP, then get to O(n log n) — the perf test requires it.
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import random
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


class TestLIS(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(Solution().lengthOfLIS([7, 7, 7, 7]), 1)

    def test_single(self):
        self.assertEqual(Solution().lengthOfLIS([5]), 1)

    def test_decreasing(self):
        self.assertEqual(Solution().lengthOfLIS([5, 4, 3, 2, 1]), 1)

    def test_performance(self):
        rng = random.Random(1)
        nums = [rng.randint(-10 ** 6, 10 ** 6) for _ in range(20_000)] + list(range(10 ** 6 + 1, 10 ** 6 + 501))
        with Deadline(1, "aim for O(n log n) with binary search"):
            got = Solution().lengthOfLIS(nums)
        self.assertGreater(got, 500)


if __name__ == "__main__":
    unittest.main(verbosity=2)
