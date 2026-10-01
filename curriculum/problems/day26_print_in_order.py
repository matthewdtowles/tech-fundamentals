"""
The same Foo instance is passed to three threads. Thread A calls first(),
thread B calls second(), thread C calls third(). The threads may START in any
order. Make sure second() runs its print only after first(), and third() only
after second().

Each method receives a callable (printFirst etc.) that you must call exactly once.

Rules: use threading primitives (Event, Lock, Condition, Semaphore, Barrier).
No busy-waiting (no 'while not flag: pass' and no sleep-polling).

Discuss first: race condition, critical section, happens-before, what the GIL
does and does NOT protect you from, deadlock conditions.
"""
import threading
from typing import Callable


class Foo:
    def __init__(self):
        pass

    def first(self, printFirst: Callable[[], None]) -> None:
        raise NotImplementedError

    def second(self, printSecond: Callable[[], None]) -> None:
        raise NotImplementedError

    def third(self, printThird: Callable[[], None]) -> None:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import itertools
import random
import time
import unittest


class TestPrintInOrder(unittest.TestCase):
    def run_order(self, start_order):
        foo, out, errors = Foo(), [], []
        calls = {
            1: lambda: foo.first(lambda: out.append("first")),
            2: lambda: foo.second(lambda: out.append("second")),
            3: lambda: foo.third(lambda: out.append("third")),
        }

        def guarded(fn):
            try:
                time.sleep(random.random() / 200)
                fn()
            except Exception as e:  # surface thread errors in the test
                errors.append(e)

        threads = [threading.Thread(target=guarded, args=(calls[i],), daemon=True) for i in start_order]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=2)
        self.assertFalse(errors, errors)
        self.assertFalse(any(t.is_alive() for t in threads), "deadlock: a thread never finished")
        return "".join(out)

    def test_all_start_orders(self):
        for order in itertools.permutations([1, 2, 3]):
            for _ in range(5):
                self.assertEqual(self.run_order(order), "firstsecondthird", f"start order {order}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
