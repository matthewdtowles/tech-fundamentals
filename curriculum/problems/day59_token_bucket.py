"""
Implement a token bucket rate limiter.

  TokenBucket(capacity, refill_rate, clock=time.monotonic)
      capacity     max tokens the bucket holds (also the max burst)
      refill_rate  tokens added per second (can be fractional)
      clock        function returning current time in seconds — injected so
                   tests can control time (time is a port, not a global)
  allow(tokens=1) -> bool
      If at least 'tokens' are available, consume them and return True.
      Otherwise consume nothing and return False.

The bucket starts FULL. Tokens refill continuously (fractions accumulate) but
never exceed capacity. Do not use a background thread — refill lazily on each call.

Example (capacity 3, rate 1/s, time frozen at 0):
  allow() True, allow() True, allow() True, allow() False
  ...time advances 1.0s...
  allow() True, allow() False

Discuss before coding: fixed window vs sliding log vs sliding window counter vs
token bucket vs leaky bucket — memory, burst behavior, accuracy.
"""
import time


class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float, clock=time.monotonic):
        pass

    def allow(self, tokens: int = 1) -> bool:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class FakeClock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self):
        return self.now


class TestTokenBucket(unittest.TestCase):
    def setUp(self):
        self.clock = FakeClock()

    def test_burst_then_deny(self):
        b = TokenBucket(3, 1, self.clock)
        self.assertEqual([b.allow() for _ in range(4)], [True, True, True, False])

    def test_refill(self):
        b = TokenBucket(3, 1, self.clock)
        for _ in range(3):
            b.allow()
        self.clock.now += 1.0
        self.assertTrue(b.allow())
        self.assertFalse(b.allow())

    def test_fractional_refill_accumulates(self):
        b = TokenBucket(1, 2, self.clock)
        self.assertTrue(b.allow())
        self.clock.now += 0.25
        self.assertFalse(b.allow())
        self.clock.now += 0.25
        self.assertTrue(b.allow())

    def test_never_exceeds_capacity(self):
        b = TokenBucket(2, 10, self.clock)
        self.clock.now += 3600
        self.assertEqual([b.allow() for _ in range(3)], [True, True, False])

    def test_multi_token_requests(self):
        b = TokenBucket(5, 1, self.clock)
        self.assertTrue(b.allow(4))
        self.assertFalse(b.allow(2), "denied requests consume nothing")
        self.assertTrue(b.allow(1))
        self.assertFalse(b.allow(6), "more than capacity can never pass")

    def test_uses_injected_clock(self):
        b = TokenBucket(1, 1, self.clock)
        b.allow()
        self.assertFalse(b.allow())
        self.clock.now += 1
        self.assertTrue(b.allow())


if __name__ == "__main__":
    unittest.main(verbosity=2)
