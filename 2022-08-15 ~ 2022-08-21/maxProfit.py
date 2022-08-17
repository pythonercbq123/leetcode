from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #  dp[i][0] 手中持有股票的最大收益
        #  dp[i][1] 手中不持有股票 但是在冷冻期的最大收益
        #  dp[i][2]  手中不持有股票， 但不是在冷冻期的最大收益
        dp = [[-prices[0], 0, 0]] + [[0, 0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[n-1][1], dp[n-1][2])