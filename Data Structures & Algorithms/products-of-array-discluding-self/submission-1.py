class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [nums[0]]
        p1 = nums[0]
        for i in range(1, len(nums)):
            p1 *= nums[i]
            r.append(p1)
        print(r)
        
        l = [nums[-1]]
        p2 = nums[-1]
        for j in range(len(nums)-2, -1, -1):
            p2 *= nums[j]
            l.append(p2)
        l = l[::-1]
        print(l)

        res = []
        for k in range(len(nums)):
            if k == 0:
                res.append(l[1])
            elif k == len(nums) - 1:
                res.append(r[k-1])
            else:
                res.append(r[k-1] * l[k+1])
        return res



        