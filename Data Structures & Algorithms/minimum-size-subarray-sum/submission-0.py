class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = float('inf')
        L = 0
        for R in range(L, len(nums)):
            while sum(nums[L:R+1]) >= target:
                m = min(R-L+1, m)
                L += 1
        if m == float('inf'):
            return 0
        return m
