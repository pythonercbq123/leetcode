from typing import List


class Solution:
    def partition(self, s: str) -> List[List[int]]:
        n = len(s)
        ret = list()
        ans = list()
        f = [[True] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and (f[i+1][j-1])

        def backtrack(i):
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    backtrack(j + 1)
                    ans.pop()
        backtrack(0)
        return ret

