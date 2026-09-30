"""
MOCK INTERVIEW — cold problem, 40-minute timer. Use the 4-step drill:
clarify (5) -> brute force vs optimal (5) -> code (20) -> dry-run and edge cases (10).

Implement RandomizedSet:
  insert(val) -> bool    insert if absent; True if inserted
  remove(val) -> bool    remove if present; True if removed
  getRandom() -> int     a random element; each element equally likely
                         (called only when the set is non-empty)

Every operation must be O(1) average.

Example:
  insert(1) -> True, remove(2) -> False, insert(2) -> True,
  getRandom() -> 1 or 2, remove(1) -> True, insert(2) -> False, getRandom() -> 2
"""
import random


class RandomizedSet:
    def __init__(self):
        pass

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def getRandom(self) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import collections
import time
import unittest


class TestRandomizedSet(unittest.TestCase):
    def test_example(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        self.assertIn(rs.getRandom(), (1, 2))
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        self.assertEqual(rs.getRandom(), 2)

    def test_remove_last_and_middle(self):
        rs = RandomizedSet()
        for x in (10, 20, 30):
            rs.insert(x)
        self.assertTrue(rs.remove(30))
        self.assertTrue(rs.remove(10))
        self.assertEqual({rs.getRandom() for _ in range(20)}, {20})
        self.assertTrue(rs.insert(10))
        self.assertEqual({rs.getRandom() for _ in range(200)}, {10, 20})

    def test_uniform(self):
        rs = RandomizedSet()
        for x in range(5):
            rs.insert(x)
        counts = collections.Counter(rs.getRandom() for _ in range(20_000))
        self.assertTrue(all(3_400 < counts[x] < 4_600 for x in range(5)), counts)

    def test_performance(self):
        rs = RandomizedSet()
        values = list(range(60_000))
        for v in values:
            rs.insert(v)
        random.Random(5).shuffle(values)
        start = time.perf_counter()
        for v in values:
            rs.remove(v)
        self.assertLess(time.perf_counter() - start, 1.0, "remove must be O(1): swap with last, then pop")


if __name__ == "__main__":
    unittest.main(verbosity=2)
