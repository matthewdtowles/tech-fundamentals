"""
Design a structure that receives a stream of integers and returns the median
of everything seen so far. With an even count, the median is the mean of the
two middle values.

  MedianFinder()
  addNum(num)       add an integer
  findMedian()      median as float (answers within 1e-5 are accepted)

Example:
  addNum(1); addNum(2); findMedian() -> 1.5
  addNum(3);            findMedian() -> 2.0

Constraints: up to 5 * 10^4 calls; findMedian only called after at least one add.
Goal: addNum O(log n), findMedian O(1).
"""


class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        raise NotImplementedError

    def findMedian(self) -> float:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import random
import statistics
import time
import unittest


class TestMedianFinder(unittest.TestCase):
    def test_example(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0)

    def test_single_and_negatives(self):
        mf = MedianFinder()
        mf.addNum(-5)
        self.assertAlmostEqual(mf.findMedian(), -5.0)
        mf.addNum(-1)
        self.assertAlmostEqual(mf.findMedian(), -3.0)

    def test_random_against_statistics(self):
        rng = random.Random(3)
        mf, seen = MedianFinder(), []
        for _ in range(300):
            x = rng.randint(-100, 100)
            mf.addNum(x)
            seen.append(x)
            self.assertAlmostEqual(mf.findMedian(), statistics.median(seen))

    def test_performance(self):
        mf = MedianFinder()
        start = time.perf_counter()
        for i in range(50_000):
            mf.addNum((i * 7919) % 50_000)
            mf.findMedian()
        self.assertLess(time.perf_counter() - start, 1.0, "Too slow: aim for O(log n) add")


if __name__ == "__main__":
    unittest.main(verbosity=2)
