"""
Design a Least Frequently Used (LFU) cache.

  LFUCache(capacity)   capacity >= 1
  get(key)             value if present else -1. A hit increments the key's use count.
  put(key, value)      update (increments use count) or insert (use count = 1).
                       When inserting into a full cache, first evict the key with
                       the LOWEST use count; break ties by evicting the least
                       recently used among them.

get and put must each run in O(1) average time.

Example (capacity 2):
  put(1, 1); put(2, 2)
  get(1)   -> 1        counts: 1->2, 2->1
  put(3, 3)            evicts 2 (lowest count)
  get(2)   -> -1
  get(3)   -> 3        counts: 1->2, 3->2
  put(4, 4)            tie at count 2: key 1 is least recent -> evict 1
  get(1)   -> -1
  get(3)   -> 3
  get(4)   -> 4

Constraints: 1 <= capacity <= 10^4, up to 2 * 10^5 calls.
"""


class LFUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestLFUCache(unittest.TestCase):
    def test_example(self):
        c = LFUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), 1)
        c.put(3, 3)
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(3), 3)
        c.put(4, 4)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(3), 3)
        self.assertEqual(c.get(4), 4)

    def test_update_counts_as_use(self):
        c = LFUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        c.put(1, 10)
        c.put(3, 3)
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(1), 10)

    def test_new_key_resets_min_frequency(self):
        c = LFUCache(2)
        c.put(1, 1)
        for _ in range(5):
            c.get(1)
        c.put(2, 2)
        c.put(3, 3)
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(1), 1)
        self.assertEqual(c.get(3), 3)

    def test_capacity_one(self):
        c = LFUCache(1)
        c.put(1, 1)
        c.get(1)
        c.put(2, 2)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(2), 2)

    def test_performance(self):
        c = LFUCache(5_000)
        start = time.perf_counter()
        for i in range(100_000):
            c.put(i, i)
            c.get(i // 2)
        self.assertLess(time.perf_counter() - start, 2.0, "Too slow: get/put must be O(1)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
