"""
Given a sorted (ascending) array of DISTINCT integers nums and a target, return
the index of target, or -1 if it is not present. You must write O(log n).

Example 1: nums = [-1, 0, 3, 5, 9, 12], target = 9  ->  4
Example 2: nums = [-1, 0, 3, 5, 9, 12], target = 2  ->  -1

Do not use the bisect module — write the loop yourself.
Constraints: 1 <= len(nums) <= 10^4
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_single(self):
        self.assertEqual(Solution().search([5], 5), 0)
        self.assertEqual(Solution().search([5], -5), -1)

    def test_boundaries(self):
        nums = [1, 3, 5, 7]
        self.assertEqual(Solution().search(nums, 1), 0)
        self.assertEqual(Solution().search(nums, 7), 3)
        self.assertEqual(Solution().search(nums, 0), -1)
        self.assertEqual(Solution().search(nums, 8), -1)

    def test_every_element(self):
        nums = list(range(0, 200, 2))
        for i, x in enumerate(nums):
            self.assertEqual(Solution().search(nums, x), i)
            self.assertEqual(Solution().search(nums, x + 1), -1)

    def test_performance(self):
        nums = list(range(100_000))
        start = time.perf_counter()
        for target in range(99_000, 100_000):
            Solution().search(nums, target)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(log n)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
