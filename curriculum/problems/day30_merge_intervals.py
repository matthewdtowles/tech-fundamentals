"""
Given an array of intervals [start, end], merge all overlapping intervals and
return the non-overlapping intervals that cover all input ranges, sorted by start.
Intervals that touch (end == next start) count as overlapping.

Example 1: [[1,3],[2,6],[8,10],[15,18]]  ->  [[1,6],[8,10],[15,18]]
Example 2: [[1,4],[4,5]]                 ->  [[1,5]]

Constraints: 1 <= n <= 10^4; input is NOT necessarily sorted.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestMergeIntervals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(Solution().merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_contained_interval_does_not_shrink(self):
        self.assertEqual(Solution().merge([[1, 4], [2, 3]]), [[1, 4]])

    def test_unsorted(self):
        self.assertEqual(Solution().merge([[4, 7], [1, 4], [9, 9]]), [[1, 7], [9, 9]])

    def test_single(self):
        self.assertEqual(Solution().merge([[5, 5]]), [[5, 5]])

    def test_chain(self):
        self.assertEqual(Solution().merge([[1, 2], [2, 3], [3, 4], [10, 11]]), [[1, 4], [10, 11]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
