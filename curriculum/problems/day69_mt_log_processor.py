"""
Build a multithreaded log-processing pipeline:

    reader (1 thread)  --bounded queue-->  N parser workers  -->  merged totals

process_logs(lines, parse, num_workers=4, queue_size=1000) -> Counter
    lines   an iterable (possibly a huge generator — never materialize it)
    parse   parse(line) -> key or None. Slow (think: regex + enrichment lookup).
            Count each non-None key.
    returns collections.Counter of key -> count

Requirements:
  - Parsing runs on num_workers threads concurrently.
  - The reader must never get more than queue_size lines ahead of the parsers
    (bounded queue = backpressure = bounded memory).
  - Each worker keeps its OWN Counter; merge at the end (no shared locked
    counter on the hot path).
  - Signal end-of-stream with one sentinel per worker.
"""
import queue
import threading
from collections import Counter


def process_logs(lines, parse, num_workers=4, queue_size=1000) -> Counter:
    raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


def level_of(line):
    parts = line.split(" ")
    return parts[1] if len(parts) > 2 and parts[1].startswith("[") else None


def make_lines(n):
    levels = ["[INFO]", "[WARN]", "[ERROR]"]
    for i in range(n):
        yield "garbage" if i % 100 == 0 else f"2026-01-01T00:00:00 {levels[i % 3]} svc: msg {i}"


class TestProcessLogs(unittest.TestCase):
    def test_counts_match_sequential(self):
        got = process_logs(make_lines(30_000), level_of)
        expected = Counter(k for k in map(level_of, make_lines(30_000)) if k)
        self.assertEqual(got, expected)

    def test_parsing_is_concurrent(self):
        def slow(line):
            time.sleep(0.01)
            return "x"

        start = time.perf_counter()
        got = process_logs((str(i) for i in range(80)), slow, num_workers=8)
        self.assertEqual(got["x"], 80)
        self.assertLess(time.perf_counter() - start, 0.5, "80 x 10ms parses on 8 workers should take ~0.1s")

    def test_backpressure(self):
        state = {"produced": 0, "parsed": 0, "max_ahead": 0}
        lock = threading.Lock()

        def source():
            for i in range(20_000):
                with lock:
                    state["produced"] += 1
                    state["max_ahead"] = max(state["max_ahead"], state["produced"] - state["parsed"])
                yield "line"

        def parse(line):
            with lock:
                state["parsed"] += 1
            return "k"

        got = process_logs(source(), parse, num_workers=4, queue_size=100)
        self.assertEqual(got["k"], 20_000)
        self.assertLess(state["max_ahead"], 200, "reader ran ahead: use a bounded queue")

    def test_empty_input(self):
        self.assertEqual(process_logs([], level_of), Counter())


if __name__ == "__main__":
    unittest.main(verbosity=2)
