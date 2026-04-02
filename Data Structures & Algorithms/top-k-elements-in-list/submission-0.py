from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        for val in Counter(nums).most_common(k):
            result.append(val[0])
        return result