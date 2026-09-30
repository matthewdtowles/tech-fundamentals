"""
A tree of n nodes (labeled 1..n) had ONE extra edge added, creating exactly one
cycle. Given the edges in order, return an edge that can be removed so the
result is a tree. If there are several answers, return the one that appears
LAST in the input.

Example 1: [[1,2],[1,3],[2,3]]              ->  [2,3]
Example 2: [[1,2],[2,3],[3,4],[1,4],[1,5]]  ->  [1,4]

Constraints: 3 <= n <= 1000. Implement Union-Find (path compression + union by rank/size).
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestRedundantConnection(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3])
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])

    def test_cycle_closed_late(self):
        self.assertEqual(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]), [2, 5])

    def test_performance(self):
        n = 20_000
        edges = [[i, i + 1] for i in range(1, n)] + [[1, n]]
        start = time.perf_counter()
        got = Solution().findRedundantConnection(edges)
        self.assertLess(time.perf_counter() - start, 1.0, "Too slow: use union-find with path compression")
        self.assertEqual(got, [1, n])


if __name__ == "__main__":
    unittest.main(verbosity=2)
