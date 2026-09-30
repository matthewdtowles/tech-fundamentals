"""
Given an integer array nums and an integer k, return the k most frequent
elements, in any order. The answer is guaranteed to be unique.

Example 1: nums = [1, 1, 1, 2, 2, 3], k = 2  ->  [1, 2]
Example 2: nums = [1], k = 1                 ->  [1]

Constraints: 1 <= len(nums) <= 10^5, k in [1, number of distinct elements]
Goal: better than O(n log n). Heap gives O(n log k); bucket sort gives O(n).
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestTopKFrequent(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])
        self.assertEqual(Solution().topKFrequent([1], 1), [1])

    def test_negatives(self):
        self.assertEqual(sorted(Solution().topKFrequent([-1, -1, 4, 4, 4, 7], 2)), [-1, 4])

    def test_all_distinct_frequencies(self):
        nums = [5] * 5 + [4] * 4 + [3] * 3 + [2] * 2 + [1]
        self.assertEqual(sorted(Solution().topKFrequent(nums, 3)), [3, 4, 5])

    def test_k_is_all(self):
        self.assertEqual(sorted(Solution().topKFrequent([1, 2, 2], 2)), [1, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
