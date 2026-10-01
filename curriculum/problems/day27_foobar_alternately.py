"""
Two threads share one FooBar(n) instance. Thread A calls foo(), thread B calls
bar(). Make them output "foobar" n times, strictly alternating:
"foobarfoobar..." — foo always first.

Each method receives a callable (printFoo / printBar) to call n times total.

Rules: no busy-waiting. Try it with two Semaphores, then (follow-up) with a
single Condition — and explain why the wait must be inside a while loop.
"""
import threading
from typing import Callable


class FooBar:
    def __init__(self, n: int):
        self.n = n

    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            raise NotImplementedError

    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestFooBar(unittest.TestCase):
    def run_n(self, n, bar_first=False):
        fb, out, errors = FooBar(n), [], []

        def guarded(fn):
            try:
                fn()
            except Exception as e:
                errors.append(e)

        a = threading.Thread(target=guarded, args=(lambda: fb.foo(lambda: out.append("foo")),), daemon=True)
        b = threading.Thread(target=guarded, args=(lambda: fb.bar(lambda: out.append("bar")),), daemon=True)
        for t in ([b, a] if bar_first else [a, b]):
            t.start()
        a.join(timeout=5)
        b.join(timeout=5)
        self.assertFalse(errors, errors)
        self.assertFalse(a.is_alive() or b.is_alive(), "deadlock: a thread never finished")
        return "".join(out)

    def test_one(self):
        self.assertEqual(self.run_n(1), "foobar")

    def test_bar_thread_starts_first(self):
        self.assertEqual(self.run_n(3, bar_first=True), "foobar" * 3)

    def test_many(self):
        self.assertEqual(self.run_n(500), "foobar" * 500)


if __name__ == "__main__":
    unittest.main(verbosity=2)
