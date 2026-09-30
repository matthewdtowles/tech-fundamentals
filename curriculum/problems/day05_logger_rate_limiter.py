"""
Design a logger that receives a stream of messages with timestamps (seconds).
Each UNIQUE message should be printed at most once every 10 seconds: if a
message is printed at time t, identical messages before t + 10 are dropped.

Timestamps arrive in non-decreasing order. Several messages may share a timestamp.

  Logger()                                   initializes the logger
  shouldPrintMessage(timestamp, message)     True if the message should print now

Example:
  shouldPrintMessage(1, "foo")  -> True   (next allowed "foo" at 11)
  shouldPrintMessage(2, "bar")  -> True
  shouldPrintMessage(3, "foo")  -> False
  shouldPrintMessage(11, "foo") -> True

Follow-up (discuss, and bonus points if you implement it): memory must not grow
forever in a long-running service. The extra test below checks that stale
messages are eventually forgotten; make it pass without breaking O(1) amortized.
"""


class Logger:
    def __init__(self):
        pass

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestLogger(unittest.TestCase):
    def test_example(self):
        log = Logger()
        self.assertTrue(log.shouldPrintMessage(1, "foo"))
        self.assertTrue(log.shouldPrintMessage(2, "bar"))
        self.assertFalse(log.shouldPrintMessage(3, "foo"))
        self.assertFalse(log.shouldPrintMessage(8, "bar"))
        self.assertFalse(log.shouldPrintMessage(10, "foo"))
        self.assertTrue(log.shouldPrintMessage(11, "foo"))

    def test_same_timestamp(self):
        log = Logger()
        self.assertTrue(log.shouldPrintMessage(0, "a"))
        self.assertFalse(log.shouldPrintMessage(0, "a"))
        self.assertTrue(log.shouldPrintMessage(0, "b"))

    def test_dropped_message_does_not_reset_window(self):
        log = Logger()
        self.assertTrue(log.shouldPrintMessage(0, "a"))
        self.assertFalse(log.shouldPrintMessage(9, "a"))
        self.assertTrue(log.shouldPrintMessage(10, "a"))

    def test_memory_is_bounded(self):
        log = Logger()
        for t in range(100_000):
            log.shouldPrintMessage(t, f"unique-{t}")
        size = sum(len(v) for v in vars(log).values() if hasattr(v, "__len__"))
        self.assertLess(size, 1_000, "Stale messages are never evicted (memory leak)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
