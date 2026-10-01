"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1: "abcabcbb" -> 3  ("abc")
Example 2: "bbbbb"    -> 1
Example 3: "pwwkew"   -> 3  ("wke"; "pwke" is a subsequence, not a substring)

Constraints: 0 <= len(s) <= 5 * 10^4; letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import string
import time
import unittest


class TestLongestSubstring(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_and_space(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)
        self.assertEqual(Solution().lengthOfLongestSubstring(" "), 1)

    def test_left_pointer_never_moves_back(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abba"), 2)

    def test_repeat_far_back(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("dvdf"), 3)

    def test_performance(self):
        s = string.printable * 500
        start = time.perf_counter()
        got = Solution().lengthOfLongestSubstring(s)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got, len(string.printable))


if __name__ == "__main__":
    unittest.main(verbosity=2)
