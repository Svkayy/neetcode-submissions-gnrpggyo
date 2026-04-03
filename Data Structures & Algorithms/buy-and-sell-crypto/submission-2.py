class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        L = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            m = max(prices[R] - prices[L], m)
        return m