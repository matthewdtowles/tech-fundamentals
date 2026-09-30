"""
Given an integer array nums and an integer k, return the kth largest element
(kth largest in sorted order, not kth distinct).

Challenge: do it without fully sorting — use a size-k min-heap (heapq), then
try quickselect as a follow-up.

Example 1: nums = [3, 2, 1, 5, 6, 4], k = 2           ->  5
Example 2: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4  ->  4

Constraints: 1 <= k <= len(nums) <= 10^5
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import random
import unittest


class TestKthLargest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_single(self):
        self.assertEqual(Solution().findKthLargest([1], 1), 1)

    def test_k_equals_n(self):
        self.assertEqual(Solution().findKthLargest([5, -1, 3], 3), -1)

    def test_two_elements(self):
        nums = [2, 1]
        self.assertEqual(Solution().findKthLargest(nums, 1), 2)

    def test_random_against_sort(self):
        rng = random.Random(7)
        for _ in range(50):
            nums = [rng.randint(-50, 50) for _ in range(rng.randint(1, 60))]
            k = rng.randint(1, len(nums))
            self.assertEqual(Solution().findKthLargest(list(nums), k), sorted(nums, reverse=True)[k - 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
