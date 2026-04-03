class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [nums.index(need), i]
            seen.add(num)
        return []