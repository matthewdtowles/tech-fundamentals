"""
Given an array of strings strs, group the anagrams together. Return the groups
in any order (words inside a group in any order).

Example: ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]]

Constraints: 1 <= len(strs) <= 10^4, 0 <= len(strs[i]) <= 100, lowercase English letters.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


def normalize(groups):
    return sorted(sorted(g) for g in groups)


class TestGroupAnagrams(unittest.TestCase):
    def test_example(self):
        got = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(normalize(got), normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]))

    def test_empty_string(self):
        self.assertEqual(normalize(Solution().groupAnagrams([""])), [[""]])

    def test_single(self):
        self.assertEqual(normalize(Solution().groupAnagrams(["a"])), [["a"]])

    def test_same_letters_different_counts(self):
        got = Solution().groupAnagrams(["aab", "abb", "bab", "aba"])
        self.assertEqual(normalize(got), normalize([["aab", "aba"], ["abb", "bab"]]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
