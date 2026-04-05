class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        sol = []
        s = sorted(nums)
        def twoSum(nums, k):
            seen = set()
            res = []
            for val in nums:
                need = k - val
                if need in seen:
                    res.append([need, val])
                seen.add(val)
            return res

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                need = target - s[i] - s[j]
                l = twoSum(s[j+1:], need)
                for val in l:
                    k = sorted(val + [s[i], s[j]])
                    if str(k) not in seen:
                        sol.append(k)
                    seen.add(str(k))
        return sol




            