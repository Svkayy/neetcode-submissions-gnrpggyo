class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = float('inf')
        curr = 0
        L = 0
        for R in range(L, len(nums)):
            curr += nums[R]
            while curr >= target:
                m = min(R-L+1, m)
                curr -= nums[L]
                L += 1
        
        if m == float('inf'):
            return 0
        return m
