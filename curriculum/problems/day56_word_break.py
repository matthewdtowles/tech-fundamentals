"""
Given a string s and a dictionary wordDict, return True if s can be split into
a space-separated sequence of one or more dictionary words (words may be reused).

Example 1: s = "leetcode", wordDict = ["leet","code"]                        ->  True
Example 2: s = "applepenapple", wordDict = ["apple","pen"]                   ->  True
Example 3: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]      ->  False

Constraints: 1 <= len(s) <= 300, 1 <= len(wordDict) <= 1000, 1 <= len(word) <= 20
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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


class TestWordBreak(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(Solution().wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(Solution().wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_needs_backtracking(self):
        self.assertTrue(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))

    def test_performance(self):
        words = ["a" * i for i in range(1, 11)]
        with Deadline(1, "memoize / DP over prefixes"):
            self.assertFalse(Solution().wordBreak("a" * 150 + "b", words))


if __name__ == "__main__":
    unittest.main(verbosity=2)
