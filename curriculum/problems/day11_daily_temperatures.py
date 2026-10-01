"""
Given daily temperatures, return answer where answer[i] is the number of days
after day i until a warmer temperature. If there is none, answer[i] = 0.

Example 1: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
Example 2: [30,40,50,60]              ->  [1,1,1,0]
Example 3: [30,60,90]                 ->  [1,1,0]

Constraints: 1 <= n <= 10^5, 30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestDailyTemperatures(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(Solution().dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(Solution().dailyTemperatures([30, 60, 90]), [1, 1, 0])

    def test_equal_is_not_warmer(self):
        self.assertEqual(Solution().dailyTemperatures([50, 50, 51]), [2, 1, 0])

    def test_decreasing(self):
        self.assertEqual(Solution().dailyTemperatures([90, 80, 70]), [0, 0, 0])

    def test_performance(self):
        temps = [99 - i * 69 // 20_000 for i in range(20_000)] + [100]
        start = time.perf_counter()
        got = Solution().dailyTemperatures(temps)
        self.assertLess(time.perf_counter() - start, 0.5, "Too slow: aim for O(n)")
        self.assertEqual(got[0], 20_000)

if __name__ == "__main__":
    unittest.main(verbosity=2)
