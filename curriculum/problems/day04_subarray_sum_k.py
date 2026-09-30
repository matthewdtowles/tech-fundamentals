"""
Given an array of integers nums and an integer k, return the total number of
contiguous, non-empty subarrays whose sum equals k.

Example 1: nums = [1, 1, 1], k = 2  ->  2
Example 2: nums = [1, 2, 3], k = 3  ->  2

Constraints: 1 <= len(nums) <= 2 * 10^4, -1000 <= nums[i] <= 1000 (negatives allowed!)
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestSubarraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().subarraySum([1, 1, 1], 2), 2)
        self.assertEqual(Solution().subarraySum([1, 2, 3], 3), 2)

    def test_negatives(self):
        self.assertEqual(Solution().subarraySum([1, -1, 0], 0), 3)

    def test_zero_sum_run(self):
        self.assertEqual(Solution().subarraySum([0, 0, 0], 0), 6)

    def test_no_match(self):
        self.assertEqual(Solution().subarraySum([1, 2, 3], 7), 0)

    def test_performance(self):
        nums = [1, -1] * 5_000
        start = time.perf_counter()
        got = Solution().subarraySum(nums, 0)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got, 25_000_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
