class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            min_num = float('inf')
            j = 1
            while j >= 1 and j * j <= i:
                min_num = min(min_num, dp[i - j * j])
                j += 1
            dp[i] = min_num + 1
        return int(dp[n])
