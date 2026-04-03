class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        res = []
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                need = -nums[i]-nums[j]
                if need in seen:
                    temp = str(sorted([need, nums[i], nums[j]]))
                    if temp not in results:
                        results.add(temp)
                        res.append([need, nums[i], nums[j]])
                seen.add(nums[j])
        return res
        