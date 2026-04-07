class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = sorted(nums)
        for i in range(len(s)):
            if s[i] > 0:
                break
            if i > 0 and s[i] == s[i-1]:
                continue
            
            L = i + 1
            R = len(s) - 1
            while L < R:
                total = s[i] + s[L] + s[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([s[i], s[L], s[R]])
                    L += 1
                    R -= 1
                
                    while L < R and s[L] == s[L-1]:
                        L += 1
                    while L < R and s[R] == s[R+1]:
                        R -= 1
        return res
