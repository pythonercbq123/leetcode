from typing import List
from collections import OrderedDict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # write code here
        n = len(prices)
        dp = [[-10000] * 5 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return max(dp[n - 1])


if __name__ == '__main__':
    s = Solution()
    ret = s.maxProfit([10000] * 30)
    print(ret)
