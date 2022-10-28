from typing import List


class Solution:
    def minCostClimbStairs(self, cost: List) -> int:
        """
        迭代法求解 自下向上
        dp保存中间记录
        :param cost:
        :return:
        """
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0] = cost[0], dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[n - 1], dp[n - 2])

    def minCostClimbStairs2(self, cost: List) -> int:
        """
        空间复杂度优化
        :param cost:
        :return:
        """
        n = len(cost)
        dp = [cost[0], cost[1]]
        for i in range(2, n):
            dp[i % 2] = min(dp[0], dp[1]) + cost[i]
        return min(dp[0], dp[1])

    def minCostClimbStairs3(self, cost: List) -> int:
        """
        递归求解 自上而下
        """
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        self.helper(cost, n-1, dp)
        return min(dp[n-2], dp[n-1])

    def helper(self, cost, i, dp):
        if i < 2:
            return cost[i]
        else:
            if dp[i] != 0:
                self.helper(cost, i-1, dp)
                self.helper(cost, i-2, dp)
                dp[i] = min(dp[i-1], dp[i-2]) + cost[1]


