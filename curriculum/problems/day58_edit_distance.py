"""
Given word1 and word2, return the minimum number of operations to convert word1
into word2. Operations: insert a character, delete a character, replace a character.

Example 1: "horse", "ros"            ->  3   (horse -> rorse -> rose -> ros)
Example 2: "intention", "execution"  ->  5

Constraints: 0 <= len(word1), len(word2) <= 500, lowercase letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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


class TestEditDistance(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().minDistance("horse", "ros"), 3)
        self.assertEqual(Solution().minDistance("intention", "execution"), 5)

    def test_empty(self):
        self.assertEqual(Solution().minDistance("", "abc"), 3)
        self.assertEqual(Solution().minDistance("abc", ""), 3)
        self.assertEqual(Solution().minDistance("", ""), 0)

    def test_equal(self):
        self.assertEqual(Solution().minDistance("same", "same"), 0)

    def test_performance(self):
        with Deadline(3, "2-D DP, O(m * n)"):
            self.assertEqual(Solution().minDistance("a" * 500, "b" * 500), 500)


if __name__ == "__main__":
    unittest.main(verbosity=2)
