class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        print(count)
        ops = 0
        for val in count.values():
            if val == 1:
                return -1
            ops += math.ceil(val / 3)
        return ops