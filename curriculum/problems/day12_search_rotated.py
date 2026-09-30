"""
nums is an ascending array of DISTINCT integers that may have been rotated at an
unknown pivot (e.g. [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]). Given target, return
its index or -1. You must write O(log n).

Example 1: nums = [4,5,6,7,0,1,2], target = 0  ->  4
Example 2: nums = [4,5,6,7,0,1,2], target = 3  ->  -1
Example 3: nums = [1], target = 0              ->  -1

Constraints: 1 <= len(nums) <= 5000
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestSearchRotated(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(Solution().search([1], 0), -1)

    def test_every_rotation_and_target(self):
        base = list(range(0, 20, 2))
        for r in range(len(base)):
            nums = base[r:] + base[:r]
            for i, x in enumerate(nums):
                self.assertEqual(Solution().search(nums, x), i, f"nums={nums} target={x}")
            self.assertEqual(Solution().search(nums, 5), -1)

    def test_performance(self):
        nums = list(range(50_000, 100_000)) + list(range(50_000))
        start = time.perf_counter()
        for target in range(0, 100_000, 50):
            self.assertEqual(Solution().search(nums, target), (target + 50_000) % 100_000)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(log n)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
