class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = -1
        b = -1
        seen = set()
        for num in nums:
            need = target - num
            if need in seen:
                a = need
                b = num
            else:
                seen.add(num)
        idx1 = -1
        idx2 = -1
        for i in range(len(nums)):
            if nums[i] == a:
                idx1 = i
                break

        for i in range(len(nums)):
            if nums[i] == b and i != idx1:
                idx2 = i
                break
        return [idx1, idx2]


        