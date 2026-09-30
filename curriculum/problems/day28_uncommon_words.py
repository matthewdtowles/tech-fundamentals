"""
A sentence is a string of single-space separated lowercase words. A word is
UNCOMMON if it appears exactly once in one sentence and not at all in the other.
Given two sentences, return all uncommon words in any order.

Example 1: "this apple is sweet", "this apple is sour"  ->  ["sweet", "sour"]
Example 2: "apple apple", "banana"                      ->  ["banana"]

Constraints: 1 <= len(s1), len(s2) <= 200, no leading/trailing spaces.
"""
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestUncommonWords(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sorted(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour")), ["sour", "sweet"])
        self.assertEqual(Solution().uncommonFromSentences("apple apple", "banana"), ["banana"])

    def test_none(self):
        self.assertEqual(Solution().uncommonFromSentences("a b", "b a"), [])

    def test_repeat_within_one(self):
        self.assertEqual(sorted(Solution().uncommonFromSentences("x x y", "z")), ["y", "z"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
