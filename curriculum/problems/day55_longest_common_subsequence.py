"""
Given two strings, return the length of their longest common subsequence
(characters in the same relative order, not necessarily contiguous). 0 if none.

Example 1: "abcde", "ace"  ->  3   ("ace")
Example 2: "abc", "abc"    ->  3
Example 3: "abc", "def"    ->  0

Constraints: 1 <= len(text1), len(text2) <= 1000, lowercase letters.
Follow-up: O(min(m, n)) space with rolling rows.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import signal
import unittest


class Deadline:
    """Fails the test instead of hanging when an exponential solution runs too long."""

    def __init__(self, seconds, hint):
        self.seconds, self.hint = seconds, hint

    def __enter__(self):
        signal.signal(signal.SIGALRM, self._fail)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)

    def __exit__(self, *exc):
        signal.setitimer(signal.ITIMER_REAL, 0)

    def _fail(self, *_):
        raise TimeoutError(f"Too slow (> {self.seconds}s): {self.hint}")


class TestLCS(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "def"), 0)

    def test_order_matters(self):
        self.assertEqual(Solution().longestCommonSubsequence("abc", "cba"), 1)

    def test_repeats(self):
        self.assertEqual(Solution().longestCommonSubsequence("aaaa", "aa"), 2)
        self.assertEqual(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"), 1)

    def test_performance(self):
        with Deadline(3, "2-D DP, O(m * n)"):
            got = Solution().longestCommonSubsequence("abcde" * 160, "aebdc" * 160)
        self.assertEqual(got, 480)


if __name__ == "__main__":
    unittest.main(verbosity=2)
