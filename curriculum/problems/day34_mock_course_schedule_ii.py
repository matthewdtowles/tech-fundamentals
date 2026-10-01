"""
MOCK INTERVIEW — 35-minute timer, narrated. Say out loud:
  - which algorithm (Kahn vs DFS) and why; O(V + E) time and space
  - your assumptions about input (duplicates? self-loops?)
  - test cases you will dry-run: a cycle, a disconnected graph, zero prerequisites

There are numCourses courses labeled 0..numCourses-1. prerequisites[i] = [a, b]
means you must take b BEFORE a. Return an ordering of courses that satisfies
all prerequisites. Any valid order is accepted. If impossible, return [].

Example 1: numCourses = 2, prerequisites = [[1,0]]                    ->  [0,1]
Example 2: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]  ->  [0,1,2,3] or [0,2,1,3]
Example 3: numCourses = 1, prerequisites = []                         ->  [0]

Constraints: 1 <= numCourses <= 2000, 0 <= len(prerequisites) <= numCourses * (numCourses - 1)
"""
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestFindOrder(unittest.TestCase):
    def assertValidOrder(self, n, prereqs, order):
        self.assertEqual(sorted(order), list(range(n)), "must contain every course exactly once")
        position = {course: i for i, course in enumerate(order)}
        for course, before in prereqs:
            self.assertLess(position[before], position[course], f"{before} must come before {course}")

    def test_examples(self):
        self.assertValidOrder(2, [[1, 0]], Solution().findOrder(2, [[1, 0]]))
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assertValidOrder(4, prereqs, Solution().findOrder(4, prereqs))
        self.assertEqual(Solution().findOrder(1, []), [0])

    def test_cycle(self):
        self.assertEqual(Solution().findOrder(3, [[0, 1], [1, 2], [2, 0]]), [])

    def test_disconnected(self):
        prereqs = [[1, 0], [3, 2]]
        self.assertValidOrder(5, prereqs, Solution().findOrder(5, prereqs))

    def test_long_chain(self):
        n = 3_000
        prereqs = [[i, i + 1] for i in range(n - 1)]
        self.assertEqual(Solution().findOrder(n, prereqs), list(range(n - 1, -1, -1)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
