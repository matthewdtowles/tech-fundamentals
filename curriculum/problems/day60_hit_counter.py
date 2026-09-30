"""
Design a hit counter that counts hits received in the past 5 minutes (300 s).

  HitCounter()
  hit(timestamp)        record a hit at timestamp (seconds)
  getHits(timestamp)    number of hits in (timestamp - 300, timestamp]

Calls arrive in chronological order (timestamps never decrease). Several hits
can share a timestamp.

Example:
  hit(1); hit(2); hit(3)
  getHits(4)    -> 3
  hit(300)
  getHits(300)  -> 4
  getHits(301)  -> 3   (the hit at 1 expired)

Follow-up (tested): what if there's a burst of 100,000 hits in one second?
Memory must stay bounded by the window, not by the number of hits.
"""


class HitCounter:
    def __init__(self):
        pass

    def hit(self, timestamp: int) -> None:
        raise NotImplementedError

    def getHits(self, timestamp: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


def footprint(obj):
    return sum(len(v) for v in vars(obj).values() if hasattr(v, "__len__"))


class TestHitCounter(unittest.TestCase):
    def test_example(self):
        c = HitCounter()
        c.hit(1)
        c.hit(2)
        c.hit(3)
        self.assertEqual(c.getHits(4), 3)
        c.hit(300)
        self.assertEqual(c.getHits(300), 4)
        self.assertEqual(c.getHits(301), 3)

    def test_same_second(self):
        c = HitCounter()
        for _ in range(5):
            c.hit(10)
        self.assertEqual(c.getHits(10), 5)
        self.assertEqual(c.getHits(309), 5)
        self.assertEqual(c.getHits(310), 0)

    def test_long_gap(self):
        c = HitCounter()
        c.hit(1)
        self.assertEqual(c.getHits(10_000), 0)
        c.hit(10_000)
        self.assertEqual(c.getHits(10_000), 1)

    def test_burst_memory_bounded(self):
        c = HitCounter()
        for _ in range(100_000):
            c.hit(42)
        self.assertEqual(c.getHits(42), 100_000)
        self.assertLessEqual(footprint(c), 1_000, "store counts per second, not one entry per hit")


if __name__ == "__main__":
    unittest.main(verbosity=2)
