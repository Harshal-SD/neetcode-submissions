class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices) - 1):

            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > maxP:
                    maxP = max(prices[j] - prices[i], maxP)
        return maxP