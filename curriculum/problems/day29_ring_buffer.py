"""
Implement a thread-safe, fixed-capacity ring buffer (circular queue).

  RingBuffer(capacity)
  offer(item) -> bool    add to the back; False (and no change) if full
  poll()                 remove and return the front item; None if empty
  __len__()              number of items

Rules:
  - Storage is ONE preallocated list of length capacity. It never grows or
    shrinks — use head index + count (or head + tail) with modulo arithmetic.
  - No deque, no queue.Queue.
  - Safe to call from many threads at once.

Discuss first: telling full from empty (count field vs one wasted slot),
lock-based vs lock-free (CAS, LMAX Disruptor), false sharing.
"""
import threading


class RingBuffer:
    def __init__(self, capacity: int):
        pass

    def offer(self, item) -> bool:
        raise NotImplementedError

    def poll(self):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import collections
import sys
import unittest


class TestRingBuffer(unittest.TestCase):
    def test_fifo_and_bounds(self):
        rb = RingBuffer(3)
        self.assertIsNone(rb.poll())
        self.assertTrue(all(rb.offer(x) for x in "abc"))
        self.assertFalse(rb.offer("d"))
        self.assertEqual(len(rb), 3)
        self.assertEqual([rb.poll(), rb.poll()], ["a", "b"])

    def test_wraps_around(self):
        rb, out = RingBuffer(3), []
        rb.offer(0)
        rb.offer(1)
        for i in range(2, 12):
            self.assertTrue(rb.offer(i))
            out.append(rb.poll())
        while len(rb):
            out.append(rb.poll())
        self.assertEqual(out, list(range(12)))

    def test_fixed_storage(self):
        rb = RingBuffer(4)
        for i in range(100):
            rb.offer(i)
            rb.poll()
        lists = [v for v in vars(rb).values() if isinstance(v, list)]
        self.assertTrue(lists and all(len(v) == 4 for v in lists), "one preallocated list of length capacity")
        self.assertFalse(any(isinstance(v, collections.deque) for v in vars(rb).values()))

    def test_concurrent_producers_consumers(self):
        rb, consumed, lock = RingBuffer(8), [], threading.Lock()
        n_producers, per_producer = 4, 2_000
        done = threading.Event()

        def produce(p):
            for i in range(per_producer):
                while not rb.offer((p, i)):
                    pass

        def consume():
            while not (done.is_set() and len(rb) == 0):
                item = rb.poll()
                if item is not None:
                    with lock:
                        consumed.append(item)

        old = sys.getswitchinterval()
        sys.setswitchinterval(1e-5)
        try:
            producers = [threading.Thread(target=produce, args=(p,), daemon=True) for p in range(n_producers)]
            consumers = [threading.Thread(target=consume, daemon=True) for _ in range(3)]
            for t in producers + consumers:
                t.start()
            for t in producers:
                t.join(timeout=30)
            done.set()
            for t in consumers:
                t.join(timeout=30)
        finally:
            sys.setswitchinterval(old)
        self.assertEqual(sorted(consumed), sorted((p, i) for p in range(n_producers) for i in range(per_producer)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
