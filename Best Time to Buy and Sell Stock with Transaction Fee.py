class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        posi = -prices[0]
        n = len(prices)

        for i in range(1, n):
            posi = max(posi, profit-prices[i])
            profit = max(profit, posi + prices[i]-fee)

        return profit
