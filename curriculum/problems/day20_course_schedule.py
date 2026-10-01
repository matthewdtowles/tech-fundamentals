"""
There are numCourses courses labeled 0..numCourses-1. prerequisites[i] = [a, b]
means you must take b BEFORE a. Return True if you can finish all courses
(i.e. the dependency graph has no cycle).

Example 1: numCourses = 2, prerequisites = [[1,0]]        ->  True
Example 2: numCourses = 2, prerequisites = [[1,0],[0,1]]  ->  False

Constraints: 1 <= numCourses <= 2000 (a test uses a 5000-long chain),
0 <= len(prerequisites) <= 5000. Use Kahn's algorithm (no recursion needed).
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestCanFinish(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(Solution().canFinish(2, [[1, 0]]))
        self.assertFalse(Solution().canFinish(2, [[1, 0], [0, 1]]))

    def test_no_prerequisites(self):
        self.assertTrue(Solution().canFinish(3, []))

    def test_diamond(self):
        self.assertTrue(Solution().canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    def test_cycle_in_disconnected_part(self):
        self.assertFalse(Solution().canFinish(5, [[1, 0], [3, 2], [4, 3], [2, 4]]))

    def test_self_loop(self):
        self.assertFalse(Solution().canFinish(1, [[0, 0]]))

    def test_long_chain(self):
        n = 5_000
        self.assertTrue(Solution().canFinish(n, [[i + 1, i] for i in range(n - 1)]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
