from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi, best = 0, len(height) - 1, 0
        while lo < hi:
            best = max(best, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return best
