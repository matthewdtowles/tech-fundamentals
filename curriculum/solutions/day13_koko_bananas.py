from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            return sum((p + k - 1) // k for p in piles) <= h

        lo, hi = 1, max(piles)  # answer is in [lo, hi]
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
