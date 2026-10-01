"""
You are given non-overlapping intervals sorted by start, and a newInterval.
Insert newInterval so the result is still sorted and non-overlapping (merge
where necessary). Return the new list. Touching intervals merge.

Example 1: intervals = [[1,3],[6,9]], newInterval = [2,5]  ->  [[1,5],[6,9]]
Example 2: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
           ->  [[1,2],[3,10],[12,16]]

Constraints: 0 <= n <= 10^4. Goal: O(n) — the input is already sorted, don't re-sort.
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestInsertInterval(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])

    def test_empty(self):
        self.assertEqual(Solution().insert([], [5, 7]), [[5, 7]])

    def test_before_all_and_after_all(self):
        self.assertEqual(Solution().insert([[3, 4]], [0, 1]), [[0, 1], [3, 4]])
        self.assertEqual(Solution().insert([[3, 4]], [6, 8]), [[3, 4], [6, 8]])

    def test_swallows_everything(self):
        self.assertEqual(Solution().insert([[2, 3], [5, 6]], [1, 10]), [[1, 10]])

    def test_touching(self):
        self.assertEqual(Solution().insert([[1, 2], [5, 6]], [2, 5]), [[1, 6]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
