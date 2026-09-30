"""
Make an LRU cache safe to share between threads.

  ThreadSafeLRUCache(capacity)
  get(key) -> value or None     (a hit counts as a use)
  put(key, value)               insert/update; evict least recently used when over capacity
  compute(key, fn) -> new value
      ATOMICALLY: new = fn(current value or None); store new; return new.
      Like Java's ConcurrentHashMap.compute — no other thread may see or change
      the key between the read and the write.
  __len__() -> number of entries

This time you MAY use collections.OrderedDict for the LRU part — today is about
concurrency, not linked lists.

Discuss first: why an LRU get() is actually a WRITE (so a read/write lock buys
little), why check-then-act needs one lock around both steps, 'with lock:' /
try-finally release, and lock striping for less contention.
"""
import threading


class ThreadSafeLRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value) -> None:
        raise NotImplementedError

    def compute(self, key, fn):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import sys
import unittest


def hammer(n_threads, fn):
    errors = []

    def run(i):
        try:
            fn(i)
        except Exception as e:
            errors.append(e)

    threads = [threading.Thread(target=run, args=(i,), daemon=True) for i in range(n_threads)]
    old = sys.getswitchinterval()
    sys.setswitchinterval(1e-6)  # force frequent thread switches to expose races
    try:
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=30)
    finally:
        sys.setswitchinterval(old)
    return errors


class TestThreadSafeLRU(unittest.TestCase):
    def test_lru_semantics(self):
        c = ThreadSafeLRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        self.assertEqual(c.get("a"), 1)
        c.put("c", 3)
        self.assertIsNone(c.get("b"))
        self.assertEqual(len(c), 2)

    def test_compute(self):
        c = ThreadSafeLRUCache(2)
        self.assertEqual(c.compute("x", lambda v: (v or 0) + 5), 5)
        self.assertEqual(c.compute("x", lambda v: v * 2), 10)
        self.assertEqual(c.get("x"), 10)

    def test_concurrent_compute_loses_no_updates(self):
        c = ThreadSafeLRUCache(10)

        def slow_increment(v):
            current = v or 0
            for _ in range(50):  # widen the race window
                pass
            return current + 1

        errors = hammer(8, lambda i: [c.compute("hits", slow_increment) for _ in range(2_000)])
        self.assertFalse(errors, errors[:3])
        self.assertEqual(c.get("hits"), 16_000, "lost updates: compute is not atomic")

    def test_concurrent_mixed_ops_respect_capacity(self):
        c = ThreadSafeLRUCache(50)

        def work(i):
            for j in range(3_000):
                c.put((i * 7 + j) % 200, j)
                c.get((i + j) % 200)

        errors = hammer(8, work)
        self.assertFalse(errors, errors[:3])
        self.assertLessEqual(len(c), 50)
        self.assertEqual(sum(c.get(k) is not None for k in range(200)), len(c))


if __name__ == "__main__":
    unittest.main(verbosity=2)
