"""
A network has n nodes labeled 1..n. times[i] = (u, v, w) is a directed edge
from u to v taking w time. A signal is sent from node k. Return the minimum time
for ALL nodes to receive it, or -1 if some node never does.

Example 1: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2  ->  2
Example 2: times = [[1,2,1]], n = 2, k = 1                  ->  1
Example 3: times = [[1,2,1]], n = 2, k = 2                  ->  -1

Constraints: 1 <= n <= 100 (perf test: 10^4), 1 <= len(times) <= 6000, 0 <= w <= 100
"""
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestNetworkDelay(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
        self.assertEqual(Solution().networkDelayTime([[1, 2, 1]], 2, 1), 1)
        self.assertEqual(Solution().networkDelayTime([[1, 2, 1]], 2, 2), -1)

    def test_more_hops_can_be_faster(self):
        self.assertEqual(Solution().networkDelayTime([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1), 2)

    def test_single_node(self):
        self.assertEqual(Solution().networkDelayTime([], 1, 1), 0)

    def test_zero_weight(self):
        self.assertEqual(Solution().networkDelayTime([[1, 2, 0], [2, 3, 0]], 3, 1), 0)

    def test_performance(self):
        n = 10_000
        times = [[i, i + 1, 1] for i in range(1, n)] + [[1, i, 100_000] for i in range(2, n + 1)]
        start = time.perf_counter()
        got = Solution().networkDelayTime(times, n, 1)
        self.assertLess(time.perf_counter() - start, 1.5, "Too slow: use a heap (Dijkstra)")
        self.assertEqual(got, n - 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
