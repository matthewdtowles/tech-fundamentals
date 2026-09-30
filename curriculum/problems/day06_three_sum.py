"""
Given an integer array nums, return all unique triplets [a, b, c] such that
a + b + c == 0 and the three come from distinct indices. The result must not
contain duplicate triplets. Order of triplets and of values inside does not matter.

Example 1: [-1, 0, 1, 2, -1, -4]  ->  [[-1, -1, 2], [-1, 0, 1]]
Example 2: [0, 1, 1]              ->  []
Example 3: [0, 0, 0]              ->  [[0, 0, 0]]

Constraints: 3 <= len(nums) <= 3000, -10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


def normalize(triplets):
    return sorted(sorted(t) for t in triplets)


class TestThreeSum(unittest.TestCase):
    def test_example(self):
        got = Solution().threeSum([-1, 0, 1, 2, -1, -4])
        self.assertEqual(normalize(got), [[-1, -1, 2], [-1, 0, 1]])

    def test_none(self):
        self.assertEqual(Solution().threeSum([0, 1, 1]), [])

    def test_all_zero_no_duplicates(self):
        self.assertEqual(normalize(Solution().threeSum([0, 0, 0, 0, 0])), [[0, 0, 0]])

    def test_many_duplicates(self):
        got = Solution().threeSum([-2, 0, 0, 2, 2, -2, 1, 1, -1])
        self.assertEqual(normalize(got), [[-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])

    def test_performance(self):
        nums = list(range(-250, 250))
        start = time.perf_counter()
        got = Solution().threeSum(nums)
        self.assertLess(time.perf_counter() - start, 1.0, "Too slow: aim for O(n^2)")
        self.assertEqual(len(got), len({tuple(sorted(t)) for t in got}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
