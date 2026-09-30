class Solution:
    def climbStairs(self, n: int) -> int:
        one_back, two_back = 1, 1  # ways(i - 1), ways(i - 2)
        for _ in range(n - 1):
            one_back, two_back = one_back + two_back, one_back
        return one_back
