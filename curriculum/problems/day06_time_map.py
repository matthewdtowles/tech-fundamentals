"""
Design a time-based key-value store that keeps multiple values for the same key
at different timestamps and retrieves the value as of a given time.

  TimeMap()                        initialize
  set(key, value, timestamp)       store value for key at timestamp
  get(key, timestamp)              return the value with the LARGEST stored
                                   timestamp_prev <= timestamp, or "" if none

All set() timestamps for a key are strictly increasing.

Example:
  set("foo", "bar", 1)
  get("foo", 1) -> "bar"
  get("foo", 3) -> "bar"
  set("foo", "bar2", 4)
  get("foo", 4) -> "bar2"
  get("foo", 5) -> "bar2"
  get("foo", 0) -> ""

Constraints: up to 2 * 10^5 calls total. Do not use bisect — write the search.
"""


class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        raise NotImplementedError

    def get(self, key: str, timestamp: int) -> str:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestTimeMap(unittest.TestCase):
    def test_example(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        self.assertEqual(tm.get("foo", 1), "bar")
        self.assertEqual(tm.get("foo", 3), "bar")
        tm.set("foo", "bar2", 4)
        self.assertEqual(tm.get("foo", 4), "bar2")
        self.assertEqual(tm.get("foo", 5), "bar2")
        self.assertEqual(tm.get("foo", 0), "")

    def test_missing_key(self):
        self.assertEqual(TimeMap().get("nope", 10), "")

    def test_many_versions(self):
        tm = TimeMap()
        for t in range(10, 100, 10):
            tm.set("k", f"v{t}", t)
        self.assertEqual(tm.get("k", 9), "")
        self.assertEqual(tm.get("k", 10), "v10")
        self.assertEqual(tm.get("k", 55), "v50")
        self.assertEqual(tm.get("k", 1000), "v90")

    def test_keys_are_independent(self):
        tm = TimeMap()
        tm.set("a", "a1", 1)
        tm.set("b", "b5", 5)
        self.assertEqual(tm.get("a", 5), "a1")
        self.assertEqual(tm.get("b", 4), "")

    def test_performance(self):
        tm = TimeMap()
        for t in range(10_000):
            tm.set("k", str(t), t * 2)
        start = time.perf_counter()
        for t in range(0, 20_000, 4):
            self.assertEqual(tm.get("k", t + 1), str(t // 2))
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: get should be O(log n)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
