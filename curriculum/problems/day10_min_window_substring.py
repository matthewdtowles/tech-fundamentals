"""
Given strings s and t, return the minimum window substring of s such that every
character in t (INCLUDING duplicates) is in the window. If none exists, return "".
The answer is unique when it exists.

Example 1: s = "ADOBECODEBANC", t = "ABC"  ->  "BANC"
Example 2: s = "a", t = "a"                ->  "a"
Example 3: s = "a", t = "aa"               ->  ""

Constraints: 1 <= len(s), len(t) <= 10^5; upper and lower case English letters.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestMinWindow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(Solution().minWindow("a", "a"), "a")
        self.assertEqual(Solution().minWindow("a", "aa"), "")

    def test_duplicates_in_t(self):
        self.assertEqual(Solution().minWindow("aaflslflsldkalskaaa", "aaa"), "aaa")

    def test_case_sensitive(self):
        self.assertEqual(Solution().minWindow("aAbB", "AB"), "AbB")

    def test_whole_string(self):
        self.assertEqual(Solution().minWindow("abc", "cba"), "abc")

    def test_performance(self):
        s = "a" * 20_000 + "b" + "a" * 20_000 + "c"
        start = time.perf_counter()
        got = Solution().minWindow(s, "bc")
        self.assertLess(time.perf_counter() - start, 1.0, "Too slow: aim for O(m + n)")
        self.assertEqual(got, "b" + "a" * 20_000 + "c")


if __name__ == "__main__":
    unittest.main(verbosity=2)
