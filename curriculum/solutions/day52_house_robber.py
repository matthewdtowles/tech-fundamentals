from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, best = 0, 0  # best up to i - 2, best up to i - 1
        for x in nums:
            prev, best = best, max(best, prev + x)
        return best
