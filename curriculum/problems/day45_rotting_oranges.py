"""
In an m x n grid each cell is 0 (empty), 1 (fresh orange), or 2 (rotten orange).
Every minute, any fresh orange 4-directionally adjacent to a rotten one rots.
Return the minimum minutes until no fresh orange remains, or -1 if impossible.

Example 1: [[2,1,1],[1,1,0],[0,1,1]]  ->  4
Example 2: [[2,1,1],[0,1,1],[1,0,1]]  ->  -1  (bottom-left never rots)
Example 3: [[0,2]]                    ->  0

Constraints: 1 <= m, n <= 10
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestOrangesRotting(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
        self.assertEqual(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
        self.assertEqual(Solution().orangesRotting([[0, 2]]), 0)

    def test_no_oranges(self):
        self.assertEqual(Solution().orangesRotting([[0]]), 0)

    def test_fresh_but_no_rotten(self):
        self.assertEqual(Solution().orangesRotting([[1]]), -1)

    def test_multiple_sources_spread_simultaneously(self):
        self.assertEqual(Solution().orangesRotting([[2, 1, 1, 1, 2]]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
