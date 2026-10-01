"""
An alien language uses lowercase English letters in an unknown order. You get a
list of words from its dictionary, sorted lexicographically by the alien rules.
Return a string of all UNIQUE letters in the words, in an order consistent with
the rules. If no valid order exists, return "". Any valid order is accepted.

Example 1: ["wrt","wrf","er","ett","rftt"]  ->  "wertf"
Example 2: ["z","x"]                        ->  "zx"
Example 3: ["z","x","z"]                    ->  ""   (z < x and x < z: cycle)
Example 4: ["abc","ab"]                     ->  ""   (a word can't come before its own prefix)

Constraints: 1 <= len(words) <= 100, 1 <= len(word) <= 100
"""
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestAlienOrder(unittest.TestCase):
    def assertValid(self, words, order):
        letters = {ch for w in words for ch in w}
        self.assertEqual(len(order), len(letters), "each letter exactly once")
        self.assertEqual(set(order), letters)
        rank = {ch: i for i, ch in enumerate(order)}
        keys = [[rank[ch] for ch in w] for w in words]
        self.assertEqual(keys, sorted(keys), f"order {order!r} does not sort the words")

    def test_examples(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertValid(words, Solution().alienOrder(words))
        self.assertValid(["z", "x"], Solution().alienOrder(["z", "x"]))

    def test_cycle(self):
        self.assertEqual(Solution().alienOrder(["z", "x", "z"]), "")

    def test_prefix_after_word_invalid(self):
        self.assertEqual(Solution().alienOrder(["abc", "ab"]), "")

    def test_letters_without_edges_included(self):
        words = ["ab", "adc"]
        self.assertValid(words, Solution().alienOrder(words))

    def test_single_word(self):
        self.assertValid(["zyx"], Solution().alienOrder(["zyx"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
