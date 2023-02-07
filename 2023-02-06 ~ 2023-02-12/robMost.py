from typing import List


class Solution:
    def rob_most(self, cost: List):
        n = len(cost)
        if n <= 2:
            return max(cost)
        # dp[i]表示到i位置能偷到的最大金额之和
        dp = [0] * 2
        dp[0] = cost[0]
        dp[1] = max(cost[0], cost[1])
        for i in range(2, len(cost)):
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + cost[i])
        return dp[(n-1) % 2]


if __name__ == '__main__':
    s = Solution()
    ret = s.rob_most([2, 3, 4, 5, 3])
    print(ret)
