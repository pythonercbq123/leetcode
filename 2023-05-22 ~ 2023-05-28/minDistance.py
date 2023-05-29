class Solution:
    def editDistance(self, str1: str, str2: str) -> int:
        # write code here
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for j in range(m + 1):
            dp[j][0] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    ret = s.editDistance("nowcoder","new")
    print(ret)
