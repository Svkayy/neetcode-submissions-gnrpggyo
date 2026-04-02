class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        startLeft = 1
        result = []
        for num in nums:
            result.append(startLeft)
            startLeft *= num
        
        endLeft = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= endLeft
            endLeft *= nums[i]
        
        return result
            
        