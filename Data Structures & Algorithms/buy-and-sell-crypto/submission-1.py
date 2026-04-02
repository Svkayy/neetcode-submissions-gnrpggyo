class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(L+1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            profit = max(profit, prices[R] - prices[L])
        if profit <= 0:
            return 0
        return profit
        