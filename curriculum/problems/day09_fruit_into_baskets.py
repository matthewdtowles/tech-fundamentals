"""
You walk a row of fruit trees; fruits[i] is the type of fruit tree i produces.
You have two baskets, each holds unlimited fruit of a SINGLE type. Starting at any
tree, pick exactly one fruit from every tree moving right, and stop when a fruit
won't fit in either basket. Return the maximum number of fruits you can pick.

(Equivalent: longest contiguous subarray with at most 2 distinct values.)

Example 1: [1, 2, 1]           -> 3
Example 2: [0, 1, 2, 2]        -> 3
Example 3: [1, 2, 3, 2, 2]     -> 4

Constraints: 1 <= len(fruits) <= 10^5, 0 <= fruits[i] < len(fruits)
"""
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestTotalFruit(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().totalFruit([1, 2, 1]), 3)
        self.assertEqual(Solution().totalFruit([0, 1, 2, 2]), 3)
        self.assertEqual(Solution().totalFruit([1, 2, 3, 2, 2]), 4)

    def test_single_type(self):
        self.assertEqual(Solution().totalFruit([7, 7, 7]), 3)

    def test_longer(self):
        self.assertEqual(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

    def test_performance(self):
        fruits = [i % 3 for i in range(30_000)] + [1, 2] * 5_000
        start = time.perf_counter()
        got = Solution().totalFruit(fruits)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got, 10_002)


if __name__ == "__main__":
    unittest.main(verbosity=2)
