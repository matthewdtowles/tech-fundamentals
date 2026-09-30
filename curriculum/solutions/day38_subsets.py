from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []

        def backtrack(i):
            if i == len(nums):
                result.append(path[:])
                return
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
            backtrack(i + 1)

        backtrack(0)
        return result
