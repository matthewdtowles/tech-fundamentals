"""
You are climbing a staircase with n steps. Each move you climb 1 or 2 steps.
In how many distinct ways can you reach the top?

Example 1: n = 2  ->  2   (1+1, 2)
Example 2: n = 3  ->  3   (1+1+1, 1+2, 2+1)

Constraints: 1 <= n <= 45
Write it three ways if you have time: plain recursion (watch it die), memoized,
bottom-up with O(1) space. Only the last two pass the performance test.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
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


class TestClimbStairs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().climbStairs(2), 2)
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_small(self):
        self.assertEqual([Solution().climbStairs(n) for n in range(1, 8)], [1, 2, 3, 5, 8, 13, 21])

    def test_performance(self):
        with Deadline(1, "memoize or go bottom-up"):
            self.assertEqual(Solution().climbStairs(45), 1_836_311_903)


if __name__ == "__main__":
    unittest.main(verbosity=2)
