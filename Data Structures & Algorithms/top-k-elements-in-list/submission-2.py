from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        kList = count.most_common(k)
        res = []
        for i,j in kList:
            res.append(i)
        return res