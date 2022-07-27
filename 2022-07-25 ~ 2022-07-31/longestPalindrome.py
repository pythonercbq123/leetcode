class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        start = 0
        end = 0
        max_len = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n, 1):
                if s[j] == s[i]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if max_len < dp[i][j]:
                        start = i
                        end = j
                        max_len = dp[i][j]
                else:
                    if dp[i + 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i + 1][j]
                        if max_len < dp[i][j]:
                            start = i + 1
                            end = j
                            max_len = dp[i][j]

                    else:
                        dp[i][j] = dp[i][j - 1]
                        if max_len < dp[i][j - 1]:
                            start = i
                            end = j - 1
                            max_len = dp[i][j]

        return s[start:end+1]


if __name__ == '__main__':
    s = Solution()
    t = s.longestPalindrome("aacabdkacaa")
    print(t)