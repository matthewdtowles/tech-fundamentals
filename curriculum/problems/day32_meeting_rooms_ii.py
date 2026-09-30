"""
Given meeting time intervals [start, end), return the minimum number of
conference rooms required. A meeting ending at t frees its room for one starting at t.

Example 1: [[0,30],[5,10],[15,20]]  ->  2
Example 2: [[7,10],[2,4]]           ->  1

Constraints: 1 <= n <= 10^4, 0 <= start < end <= 10^6
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestMeetingRooms(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(Solution().minMeetingRooms([[7, 10], [2, 4]]), 1)

    def test_back_to_back_reuses_room(self):
        self.assertEqual(Solution().minMeetingRooms([[1, 5], [5, 10], [10, 15]]), 1)

    def test_all_overlap(self):
        self.assertEqual(Solution().minMeetingRooms([[1, 10], [2, 9], [3, 8]]), 3)

    def test_unsorted(self):
        self.assertEqual(Solution().minMeetingRooms([[9, 12], [1, 3], [2, 10], [11, 13]]), 2)

    def test_performance(self):
        intervals = [[i, i + 5_000] for i in range(10_000)]
        start = time.perf_counter()
        got = Solution().minMeetingRooms(intervals)
        self.assertLess(time.perf_counter() - start, 1.0, "Too slow: aim for O(n log n)")
        self.assertEqual(got, 5_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
