

class Solution:
    def min_cut(self, s: str) -> int:
        n = len(s)
        is_pal = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i <= j+1 or is_pal[j+1][i-1]):
                    is_pal[j][i] = 1
        dp = [i for i in range(n)]
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                for j in range(i+1):
                    if is_pal[j][i]:
                        dp[i] = min(dp[j-1] + 1, dp[i])
        return dp[n-1]


if __name__ == '__main__':

    s = Solution()
    ret = s.min_cut('google')
    print(ret)

