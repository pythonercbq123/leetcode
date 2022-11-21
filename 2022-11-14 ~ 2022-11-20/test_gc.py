class Solution:

    def soupServings(self, n: int) -> float:
        """
        分汤问题 动态规划
        dp[i][j]
        边界条件
            j = 0 i>0  0
            j=0, i=0, 0.5
            j>0 i=0, 1
        :param n:
        :return:
        """
        n = (n + 24) // 25
        if n >= 179:
            return 1
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0] = [0.5] + [1] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(i - 4, 0)][j] + dp[max(i - 3, 0)][max(j - 1, 0)] + dp[max(i - 2, 0)][max(j - 2, 0)] + dp[max(i-1, 0)][max(j-3, 0)]) / 4
        return dp[n][n]


if __name__ == '__main__':

    s = Solution()
    ret = s.soupServings(100)
    print(ret)
