"""
Build a log analyzer that streams a (potentially multi-GB) log file.

Line format:
    <YYYY-MM-DDTHH:MM:SS> [<LEVEL>] <service>: <message>
ERROR lines start their message with an error code like E503:
    2026-09-28T19:42:57 [ERROR] payments: E503 upstream timeout
    2026-09-28T19:42:58 [INFO] search: query ok
Lines that do not match the format (blank lines included) are MALFORMED: count
them and skip them.

analyze(path, top_n=5) returns a dict:
    "error_rate": {minute -> errors / valid lines in that minute}
                  minute is the timestamp truncated to "YYYY-MM-DDTHH:MM"
    "top_errors": [(code, count), ...] the top_n error codes, highest count
                  first, ties broken by code ascending
    "malformed":  number of malformed lines

Requirements: memory must NOT grow with file size (the test measures peak
memory on a ~15 MB file). Stream line by line; never read() or readlines().
"""


def analyze(path: str, top_n: int = 5) -> dict:
    raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import os
import tempfile
import tracemalloc
import unittest

SAMPLE = """2026-09-28T19:42:01 [INFO] search: query ok
2026-09-28T19:42:05 [ERROR] payments: E503 upstream timeout
2026-09-28T19:42:09 [WARN] search: slow query
2026-09-28T19:42:30 [ERROR] auth: E401 bad token
this line is garbage
2026-09-28T19:43:00 [ERROR] payments: E503 upstream timeout
2026-09-28T19:43:10 [INFO] payments: charge ok

2026-09-28T19:43:20 [ERROR] payments: E500 null pointer
"""


class TestAnalyze(unittest.TestCase):
    def write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".log", delete=False)
        f.write(text)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def test_sample(self):
        report = analyze(self.write(SAMPLE))
        self.assertEqual(report["malformed"], 2)
        self.assertAlmostEqual(report["error_rate"]["2026-09-28T19:42"], 0.5)
        self.assertAlmostEqual(report["error_rate"]["2026-09-28T19:43"], 2 / 3)
        self.assertEqual(report["top_errors"], [("E503", 2), ("E401", 1), ("E500", 1)])

    def test_top_n_limit(self):
        lines = [f"2026-01-01T00:00:{i:02d} [ERROR] svc: E{100 + i % 7} boom" for i in range(49)]
        report = analyze(self.write("\n".join(lines) + "\n"), top_n=3)
        self.assertEqual(len(report["top_errors"]), 3)
        self.assertEqual(report["top_errors"][0][1], 7)

    def test_no_errors(self):
        report = analyze(self.write("2026-01-01T00:00:00 [INFO] a: fine\n"))
        self.assertEqual(report["error_rate"], {"2026-01-01T00:00": 0.0})
        self.assertEqual(report["top_errors"], [])

    def test_streams_big_file(self):
        path = self.write("")
        with open(path, "w") as f:
            for i in range(250_000):
                level = "ERROR" if i % 10 == 0 else "INFO"
                msg = f"E{500 + i % 4} failure" if level == "ERROR" else "all good here"
                f.write(f"2026-02-03T04:{(i // 5000) % 60:02d}:{i % 60:02d} [{level}] service{i % 20}: {msg}\n")
        tracemalloc.start()
        report = analyze(path)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        self.assertLess(peak, 2_000_000, f"peak {peak / 1e6:.1f} MB: you are holding the file in memory")
        self.assertEqual(sum(c for _, c in report["top_errors"]), 25_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
