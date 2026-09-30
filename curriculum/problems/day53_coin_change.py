"""
Given coin denominations and an amount, return the FEWEST coins that make up
that amount (unlimited coins of each kind). Return -1 if impossible.

Example 1: coins = [1, 2, 5], amount = 11  ->  3   (5 + 5 + 1)
Example 2: coins = [2], amount = 3         ->  -1
Example 3: coins = [1], amount = 0         ->  0

Constraints: 1 <= len(coins) <= 12, 1 <= coins[i] <= 2^31 - 1, 0 <= amount <= 10^4
Note: greedy (largest coin first) is wrong — find the counterexample in the tests.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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


class TestCoinChange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().coinChange([1, 2, 5], 11), 3)
        self.assertEqual(Solution().coinChange([2], 3), -1)
        self.assertEqual(Solution().coinChange([1], 0), 0)

    def test_greedy_fails(self):
        self.assertEqual(Solution().coinChange([1, 3, 4], 6), 2)

    def test_huge_coin(self):
        self.assertEqual(Solution().coinChange([2 ** 31 - 1, 3], 9), 3)

    def test_performance(self):
        with Deadline(2, "DP over amounts, O(amount * coins)"):
            self.assertEqual(Solution().coinChange([7, 11, 13, 29], 10_000), 346)


if __name__ == "__main__":
    unittest.main(verbosity=2)
