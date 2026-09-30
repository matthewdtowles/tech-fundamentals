"""
Given an array of UNIQUE integers, return all possible subsets (the power set).
No duplicate subsets. Any order (of subsets and of values inside).

Example 1: [1, 2, 3]  ->  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2: [0]        ->  [[],[0]]

Constraints: 1 <= len(nums) <= 10
Do it with backtracking (choose / explore / un-choose). Bitmasks are the follow-up.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


def normalize(subsets):
    return sorted(sorted(s) for s in subsets)


class TestSubsets(unittest.TestCase):
    def test_examples(self):
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(normalize(Solution().subsets([1, 2, 3])), normalize(expected))
        self.assertEqual(normalize(Solution().subsets([0])), [[], [0]])

    def test_count_and_uniqueness(self):
        got = Solution().subsets(list(range(10)))
        self.assertEqual(len(got), 1024)
        self.assertEqual(len({tuple(sorted(s)) for s in got}), 1024)

    def test_subsets_are_independent_lists(self):
        got = Solution().subsets([1, 2])
        self.assertEqual(len({id(s) for s in got}), len(got), "copy the path when recording it")


if __name__ == "__main__":
    unittest.main(verbosity=2)
