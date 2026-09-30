"""
Given an integer array nums, return an array answer such that answer[i] is the
product of all elements of nums except nums[i].
You must run in O(n) time and WITHOUT using division.

Example 1: [1, 2, 3, 4]       -> [24, 12, 8, 6]
Example 2: [-1, 1, 0, -3, 3]  -> [0, 0, 9, 0, 0]

Constraints: 2 <= len(nums) <= 10^5
Follow-up: O(1) extra space (the output array does not count).
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestProductExceptSelf(unittest.TestCase):
    def test_example(self):
        self.assertEqual(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_with_zero(self):
        self.assertEqual(Solution().productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_two_zeros(self):
        self.assertEqual(Solution().productExceptSelf([0, 2, 0]), [0, 0, 0])

    def test_two_elements(self):
        self.assertEqual(Solution().productExceptSelf([5, 7]), [7, 5])

    def test_performance(self):
        nums = [1, -1] * 5_000
        start = time.perf_counter()
        got = Solution().productExceptSelf(nums)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got[0], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
