from typing import List


class Solution:
    def workBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] 表示s的前i字符能够被wordDict中单词拆分
        word_dict_set = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(n + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in word_dict_set:
                    dp[i] = True

        return dp[n]
