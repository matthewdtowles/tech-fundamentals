# Day 01 — Two Sum (LeetCode 1, Easy)
# https://leetcode.com/problems/two-sum/
# Pattern: Hash map (complement lookup)
# GOAL: O(n) time, O(n) space
# Run tests: ./tf check

"""
Given an array of integers nums and an integer target, return the indices of the
two numbers that add up to target. Exactly one solution exists, and you may not
use the same element twice. Return the two indices in any order.

Example 1: nums = [2, 7, 11, 15], target = 9  ->  [0, 1]
Example 2: nums = [3, 2, 4], target = 6       ->  [1, 2]

Constraints: 2 <= len(nums) <= 10^4, -10^9 <= nums[i], target <= 10^9
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}
        for i, num in enumerate(nums):
            index_of[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_of and index_of[diff] != i:
                return [index_of[diff], i]


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestTwoSum(unittest.TestCase):
    def check(self, nums, target):
        i, j = Solution().twoSum(nums, target)
        self.assertNotEqual(i, j)
        self.assertEqual(nums[i] + nums[j], target)

    def test_example(self):
        self.check([2, 7, 11, 15], 9)

    def test_unsorted(self):
        self.check([3, 2, 4], 6)

    def test_duplicate_values(self):
        self.check([3, 3], 6)

    def test_negatives_and_zero(self):
        self.check([-3, 4, 3, 90], 0)

    def test_performance(self):
        nums = list(range(10_000))
        start = time.perf_counter()
        self.check(nums, 9_998 + 9_999)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
