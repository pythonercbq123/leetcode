from typing import List


class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j]
                if i > 0 and j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif 0 < i == j:
                    dp[i][j] += dp[i - 1][j - 1]
                elif i > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])
        ret = float('inf')
        for i in range(n):
            ret = min(ret, dp[n - 1][i])
        return ret

    def minimum_total_one_dimension(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        # 想象具体的阶梯来理解代码
        for i in range(n):
            for j in range(i, -1, -1):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif i == j:
                    dp[j] = triangle[i][j] + dp[j-1]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
        return min(dp)


if __name__ == '__main__':
    s = Solution(
    )
    ret = s.minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(ret)
    ret = s.minimum_total_one_dimension([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(ret)
