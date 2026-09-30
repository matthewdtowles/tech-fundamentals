"""
Given an m x n board of characters and a list of words, return all words that
can be formed on the board (same adjacency rules as Word Search: up/down/left/
right, a cell used at most once per word). Any order, no duplicates.

board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]  ->  ["eat","oath"]

Constraints: 1 <= m, n <= 12, 1 <= len(words) <= 3 * 10^4, 1 <= len(word) <= 10.
Running Word Search once per word is too slow — build a trie of the words.
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestFindWords(unittest.TestCase):
    def test_example(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        self.assertEqual(sorted(Solution().findWords(board, ["oath", "pea", "eat", "rain"])), ["eat", "oath"])

    def test_no_cell_reuse(self):
        self.assertEqual(Solution().findWords([["a", "b"], ["c", "d"]], ["abcb"]), [])

    def test_no_duplicates(self):
        self.assertEqual(Solution().findWords([["a", "a"]], ["a", "aa", "a"]).count("a"), 1)

    def test_prefix_words(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertEqual(sorted(Solution().findWords(board, ["ab", "abd", "acdb", "abc"])), ["ab", "abd", "acdb"])

    def test_performance(self):
        board = [["a"] * 10 for _ in range(10)]
        words = ["a" * i for i in range(1, 9)] + ["a" * i + "b" for i in range(1, 9)] + [f"x{i}" for i in range(5_000)]
        start = time.perf_counter()
        got = Solution().findWords(board, words)
        self.assertLess(time.perf_counter() - start, 5.0, "Too slow: trie + pruning")
        self.assertEqual(sorted(got), sorted("a" * i for i in range(1, 9)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
