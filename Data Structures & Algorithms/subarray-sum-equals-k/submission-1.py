class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        count = 0
        for j in range(len(nums)):
            count += prefix_count[nums[j] - k]
            prefix_count[nums[j]] += 1
        
        return count

        