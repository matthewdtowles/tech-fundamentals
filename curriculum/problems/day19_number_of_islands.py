"""
Given an m x n grid of "1" (land) and "0" (water), return the number of islands.
An island is land connected horizontally or vertically, surrounded by water.
Everything outside the grid is water.

Example 1:
  [["1","1","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","0","0","0"]]   ->  1
Example 2:
  [["1","1","0","0","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]]   ->  3

Constraints: 1 <= m, n <= 300.
Heads-up: one test is a single 150 x 150 island. Python's default recursion
limit is 1000 — a recursive flood fill will crash. Use an explicit stack/queue.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestNumIslands(unittest.TestCase):
    def test_examples(self):
        g1 = [list("11110"), list("11010"), list("11000"), list("00000")]
        g2 = [list("11000"), list("11000"), list("00100"), list("00011")]
        self.assertEqual(Solution().numIslands(g1), 1)
        self.assertEqual(Solution().numIslands(g2), 3)

    def test_all_water(self):
        self.assertEqual(Solution().numIslands([list("000")]), 0)

    def test_diagonal_is_not_connected(self):
        self.assertEqual(Solution().numIslands([list("101"), list("010"), list("101")]), 5)

    def test_snake(self):
        grid = [list("11111"), list("00001"), list("11111"), list("10000"), list("11111")]
        self.assertEqual(Solution().numIslands(grid), 1)

    def test_huge_island_no_recursion_crash(self):
        self.assertEqual(Solution().numIslands([["1"] * 150 for _ in range(150)]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
