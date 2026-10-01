from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices with increasing heights
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                best = max(best, height * (i - left))
            stack.append(i)
        return best
