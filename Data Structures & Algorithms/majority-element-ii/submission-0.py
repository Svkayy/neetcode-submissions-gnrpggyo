from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        threshold = len(nums) // 3
        for val in counter:
            if counter[val] > threshold:
                res.append(val)
        return res
        