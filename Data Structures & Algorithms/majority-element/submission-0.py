class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        majority = len(nums) // 2
        m = -1
        for key in count:
            if count[key] > majority:
                m = key
        return m
