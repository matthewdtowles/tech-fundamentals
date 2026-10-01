"""
Design a Least Recently Used (LRU) cache.

  LRUCache(capacity)   positive capacity
  get(key)             value if present else -1; counts as a USE
  put(key, value)      insert or update (update counts as a USE). If inserting
                       exceeds capacity, evict the least recently used key first.

get and put must each run in O(1) average time.
Do NOT use collections.OrderedDict or functools.lru_cache — build the
hash map + doubly linked list yourself.

Example (capacity 2):
  put(1, 1); put(2, 2)
  get(1)    -> 1      (order now: 2 is LRU)
  put(3, 3)           (evicts 2)
  get(2)    -> -1
  put(4, 4)           (evicts 1)
  get(1)    -> -1
  get(3)    -> 3
  get(4)    -> 4

Constraints: 1 <= capacity <= 3000, up to 2 * 10^5 calls.
"""


class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestLRUCache(unittest.TestCase):
    def test_example(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), 1)
        c.put(3, 3)
        self.assertEqual(c.get(2), -1)
        c.put(4, 4)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(3), 3)
        self.assertEqual(c.get(4), 4)

    def test_update_refreshes_recency(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        c.put(1, 10)
        c.put(3, 3)
        self.assertEqual(c.get(1), 10)
        self.assertEqual(c.get(2), -1)

    def test_capacity_one(self):
        c = LRUCache(1)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(2), 2)

    def test_get_miss_does_not_change_order(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(9), -1)
        c.put(3, 3)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(2), 2)

    def test_no_ordered_dict(self):
        from collections import OrderedDict
        c = LRUCache(2)
        self.assertFalse(any(isinstance(v, OrderedDict) for v in vars(c).values()), "build it yourself")

    def test_performance(self):
        c = LRUCache(3000)
        start = time.perf_counter()
        for i in range(100_000):
            c.put(i, i)
            c.get(i - 1500)
        self.assertLess(time.perf_counter() - start, 2.0, "Too slow: get/put must be O(1)")
        self.assertEqual(c.get(99_999), 99_999)
        self.assertEqual(c.get(50_000), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
