"""
You have CPU tasks labeled 'A'-'Z' and a cooldown n. Each unit of time the CPU
runs one task or idles. Two runs of the SAME task must be at least n units apart.
Return the minimum number of time units to finish all tasks (any order).

Example 1: tasks = ["A","A","A","B","B","B"], n = 2  ->  8   (A B idle A B idle A B)
Example 2: tasks = ["A","C","A","B","D","B"], n = 1  ->  6
Example 3: tasks = ["A","A","A","B","B","B"], n = 3  ->  10

Constraints: 1 <= len(tasks) <= 10^4, 0 <= n <= 100
"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestLeastInterval(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().leastInterval(list("AAABBB"), 2), 8)
        self.assertEqual(Solution().leastInterval(list("ACABDB"), 1), 6)
        self.assertEqual(Solution().leastInterval(list("AAABBB"), 3), 10)

    def test_no_cooldown(self):
        self.assertEqual(Solution().leastInterval(list("AAABBB"), 0), 6)

    def test_one_dominant_task(self):
        self.assertEqual(Solution().leastInterval(list("AAAAAABCDEFG"), 2), 16)

    def test_no_idle_needed(self):
        self.assertEqual(Solution().leastInterval(list("ABCDEABCDE"), 2), 10)

    def test_single(self):
        self.assertEqual(Solution().leastInterval(["A"], 100), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
