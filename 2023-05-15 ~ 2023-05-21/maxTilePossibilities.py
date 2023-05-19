class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        count = [0] * 26
        for i in tiles:
            count[ord(i) - ord('A')] += 1

        def dfs(count):
            res = 0
            for i in range(26):
                if count[i] == 0:
                    continue
                res += 1
                count[i] -= 1
                res += dfs(count)
                count[i] += 1
            return res

        res = dfs(count)
        return res
