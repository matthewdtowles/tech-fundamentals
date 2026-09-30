from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
