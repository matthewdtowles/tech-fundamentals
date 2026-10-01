"""
Implement a thread-safe bounded blocking queue (FIFO).

  BoundedBlockingQueue(capacity)
  enqueue(element)   add to the back; if full, BLOCK until there is room
  dequeue() -> int   remove from the front; if empty, BLOCK until an element arrives
  size() -> int      current number of elements

Rules: do not use queue.Queue (that's the answer key). Use threading.Lock +
threading.Condition. collections.deque is fine for storage.

Discuss first: producer-consumer, why two conditions (not_full, not_empty) can
share one lock, why 'while' and not 'if' around wait(), backpressure.
"""
import threading


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        pass

    def enqueue(self, element: int) -> None:
        raise NotImplementedError

    def dequeue(self) -> int:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import queue
import time
import unittest


def start(fn, *args):
    t = threading.Thread(target=fn, args=args, daemon=True)
    t.start()
    return t


class TestBoundedBlockingQueue(unittest.TestCase):
    def test_fifo_single_thread(self):
        q = BoundedBlockingQueue(3)
        for x in (1, 2, 3):
            q.enqueue(x)
        self.assertEqual(q.size(), 3)
        self.assertEqual([q.dequeue() for _ in range(3)], [1, 2, 3])
        self.assertEqual(q.size(), 0)

    def test_not_queue_queue(self):
        q = BoundedBlockingQueue(1)
        self.assertFalse(any(isinstance(v, queue.Queue) for v in vars(q).values()), "build it yourself")

    def test_enqueue_blocks_when_full(self):
        q = BoundedBlockingQueue(1)
        q.enqueue(1)
        t = start(q.enqueue, 2)
        time.sleep(0.1)
        self.assertTrue(t.is_alive(), "enqueue should block while full")
        self.assertEqual(q.dequeue(), 1)
        t.join(timeout=1)
        self.assertFalse(t.is_alive())
        self.assertEqual(q.dequeue(), 2)

    def test_dequeue_blocks_when_empty(self):
        q, got = BoundedBlockingQueue(2), []
        t = start(lambda: got.append(q.dequeue()))
        time.sleep(0.1)
        self.assertTrue(t.is_alive(), "dequeue should block while empty")
        q.enqueue(42)
        t.join(timeout=1)
        self.assertEqual(got, [42])

    def test_many_producers_and_consumers(self):
        q, consumed, lock = BoundedBlockingQueue(5), [], threading.Lock()
        producers = [start(lambda base=p: [q.enqueue(base * 1000 + i) for i in range(500)]) for p in range(4)]

        def consume():
            for _ in range(500):
                x = q.dequeue()
                with lock:
                    consumed.append(x)

        consumers = [start(consume) for _ in range(4)]
        for t in producers + consumers:
            t.join(timeout=10)
        self.assertEqual(sorted(consumed), sorted(p * 1000 + i for p in range(4) for i in range(500)))
        self.assertEqual(q.size(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
