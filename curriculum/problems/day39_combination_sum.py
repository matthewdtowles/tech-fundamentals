"""
Given an array of DISTINCT positive integers candidates and a target, return all
unique combinations whose sum is target. The same number may be used unlimited
times. Two combinations are the same if they use the same numbers with the same
counts (order doesn't matter). Any output order.

Example 1: candidates = [2,3,6,7], target = 7  ->  [[2,2,3],[7]]
Example 2: candidates = [2,3,5],   target = 8  ->  [[2,2,2,2],[2,3,3],[3,5]]
Example 3: candidates = [2],       target = 1  ->  []

Constraints: 1 <= len(candidates) <= 30, 2 <= candidates[i] <= 40, 1 <= target <= 40
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


def normalize(combos):
    return sorted(sorted(c) for c in combos)


class TestCombinationSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(normalize(Solution().combinationSum([2, 3, 6, 7], 7)), [[2, 2, 3], [7]])
        self.assertEqual(normalize(Solution().combinationSum([2, 3, 5], 8)), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        self.assertEqual(Solution().combinationSum([2], 1), [])

    def test_no_permutation_duplicates(self):
        got = Solution().combinationSum([3, 2], 5)
        self.assertEqual(normalize(got), [[2, 3]])

    def test_bigger(self):
        got = normalize(Solution().combinationSum([2, 3, 5, 7], 12))
        self.assertEqual(len(got), len({tuple(c) for c in got}))
        self.assertTrue(all(sum(c) == 12 for c in got))
        self.assertEqual(len(got), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
