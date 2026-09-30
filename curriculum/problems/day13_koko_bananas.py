"""
Koko has n piles of bananas; piles[i] bananas in pile i. Guards return in h hours.
Each hour she picks one pile and eats k bananas from it (if the pile has fewer
than k, she eats them all and waits out the rest of that hour).
Return the minimum integer k such that she eats everything within h hours.

Example 1: piles = [3, 6, 7, 11], h = 8        ->  4
Example 2: piles = [30, 11, 23, 4, 20], h = 5  ->  30
Example 3: piles = [30, 11, 23, 4, 20], h = 6  ->  23

Constraints: 1 <= len(piles) <= h <= 10^9, 1 <= piles[i] <= 10^9
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestKoko(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().minEatingSpeed([3, 6, 7, 11], 8), 4)
        self.assertEqual(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6), 23)

    def test_lots_of_time(self):
        self.assertEqual(Solution().minEatingSpeed([1_000_000_000], 1_000_000_000), 1)

    def test_one_pile_ceiling(self):
        self.assertEqual(Solution().minEatingSpeed([10], 3), 4)

    def test_performance(self):
        piles = [1_000_000] * 100
        start = time.perf_counter()
        got = Solution().minEatingSpeed(piles, 200)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: binary search the answer")
        self.assertEqual(got, 500_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
