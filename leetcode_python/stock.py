class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = -1
        b, s = 0, 1
        while b < n and s < n:
            if prices[s] > prices[b]:
                profit = prices[s]-prices[b]
                maxProfit = max(profit, maxProfit)
                s += 1
            else:
                b = s
                s += 1
        return 0 if maxProfit == -1 else maxProfit
        