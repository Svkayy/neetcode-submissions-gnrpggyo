class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sol = set()
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s > 0:
                    need = -s
                elif s == 0:
                    need = 0
                else:
                    need = abs(s)
                res = str(sorted([need, nums[i], nums[j]]))
                if need in seen and res not in sol:
                    sol.add(res)
                    result.append([need, nums[i], nums[j]])
            seen.add(nums[i])
        return result
        