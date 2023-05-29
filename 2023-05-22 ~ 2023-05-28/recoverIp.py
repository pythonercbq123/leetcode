from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # write code here
        res = []
        n = len(s)

        def dfs(s, index, subset, res):
            if index == n and len(subset) == 4:
                res.append('.'.join(list(subset)))
            elif index < n and len(subset) < 4:

                subset.append(s[index])
                dfs(s, index + 1, subset, res)
                subset.pop()
                if int(s[index] != 0):
                    subset.append(s[index:index + 2])
                    dfs(s, index + 2, subset, res)
                    subset.pop()
                if 100 < int(s[index:index + 3]) <= 255:
                    subset.append(s[index:index + 3])
                    dfs(s, index + 3, subset, res)
                    subset.pop()

        dfs(s, 0, [], res)
        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.restoreIpAddresses("010010")
    print(ret)