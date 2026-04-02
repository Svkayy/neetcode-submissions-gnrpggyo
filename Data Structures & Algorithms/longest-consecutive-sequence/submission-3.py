class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxLength = 0
        if len(numbers) == 1:
            return 1
        for num in nums:
            length = 0
            if num - 1 in numbers:
                continue
            if num + 1 in numbers:
                x = num
                length += 1
                while x + 1 in numbers:
                    length += 1
                    x += 1
                maxLength = max(length, maxLength)
        return maxLength

        