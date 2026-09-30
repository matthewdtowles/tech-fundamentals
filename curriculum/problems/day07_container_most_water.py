"""
You are given an integer array height of length n. There are n vertical lines;
line i goes from (i, 0) to (i, height[i]). Find two lines that, together with
the x-axis, form a container holding the most water. Return that max area.

Example 1: [1, 8, 6, 2, 5, 4, 8, 3, 7]  ->  49
Example 2: [1, 1]                       ->  1

Constraints: 2 <= n <= 10^5, 0 <= height[i] <= 10^4
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestMaxArea(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(Solution().maxArea([1, 1]), 1)

    def test_zeros(self):
        self.assertEqual(Solution().maxArea([0, 0, 0]), 0)

    def test_tall_middle(self):
        self.assertEqual(Solution().maxArea([1, 100, 100, 1]), 100)

    def test_performance(self):
        height = list(range(1, 10_001))
        start = time.perf_counter()
        got = Solution().maxArea(height)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got, 25_000_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
