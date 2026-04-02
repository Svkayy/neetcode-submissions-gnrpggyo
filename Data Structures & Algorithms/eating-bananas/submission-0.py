class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        def isCorrect(piles, h, k):
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            if count > h:
                return 1
            else:
                return -1
        
        res = hi
        while lo <= hi:
            mid = (lo + hi)//2
            if isCorrect(piles, h, mid) <= 0:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res