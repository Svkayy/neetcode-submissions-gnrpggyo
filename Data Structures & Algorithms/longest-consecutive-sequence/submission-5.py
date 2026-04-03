class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        seen = set(nums)
        maxCount = 1
        for num in nums:
            if num - 1 in seen:
                continue

            count = 1
            while num + 1 in seen:
                count += 1
                num += 1

            maxCount = max(maxCount, count)
        
        return maxCount