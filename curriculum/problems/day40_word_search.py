"""
Given an m x n grid of characters and a word, return True if the word can be
built from sequentially adjacent cells (up/down/left/right). A cell may not be
used more than once in the same word.

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
  word = "ABCCED"  ->  True
  word = "SEE"     ->  True
  word = "ABCB"    ->  False

Constraints: 1 <= m, n <= 6, 1 <= len(word) <= 15.
If you mark cells visited in-place, restore them — the board must be unchanged afterwards.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import copy
import unittest

BOARD = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


class TestWordSearch(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(Solution().exist(copy.deepcopy(BOARD), "ABCCED"))
        self.assertTrue(Solution().exist(copy.deepcopy(BOARD), "SEE"))
        self.assertFalse(Solution().exist(copy.deepcopy(BOARD), "ABCB"))

    def test_single_cell(self):
        self.assertTrue(Solution().exist([["a"]], "a"))
        self.assertFalse(Solution().exist([["a"]], "aa"))

    def test_board_restored(self):
        board = copy.deepcopy(BOARD)
        Solution().exist(board, "ABCCED")
        Solution().exist(board, "ABCB")
        self.assertEqual(board, BOARD)


if __name__ == "__main__":
    unittest.main(verbosity=2)
