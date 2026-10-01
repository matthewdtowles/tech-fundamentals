"""
Given bar heights of a histogram where each bar has width 1, return the area of
the largest rectangle that fits inside the histogram.

Example 1: [2, 1, 5, 6, 2, 3]  ->  10   (bars 5 and 6, height 5, width 2)
Example 2: [2, 4]              ->  4

Constraints: 1 <= n <= 10^5, 0 <= heights[i] <= 10^4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestLargestRectangle(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(Solution().largestRectangleArea([2, 4]), 4)

    def test_single_and_zero(self):
        self.assertEqual(Solution().largestRectangleArea([0]), 0)
        self.assertEqual(Solution().largestRectangleArea([7]), 7)

    def test_all_equal(self):
        self.assertEqual(Solution().largestRectangleArea([3, 3, 3, 3]), 12)

    def test_valley(self):
        self.assertEqual(Solution().largestRectangleArea([4, 2, 0, 3, 2, 5]), 6)

    def test_performance(self):
        heights = list(range(1, 10_001))
        start = time.perf_counter()
        got = Solution().largestRectangleArea(heights)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got, 25_005_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
