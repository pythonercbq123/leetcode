from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])
        for i in range(length):
            s = strs[0][i]
            for index in range(1, len(strs)):
                # if i == len(strs[index]) or strs[index][i] != s:
                if len(strs[index]) - 1 < i or strs[index][i] != s:
                    return strs[0][:i]
        return strs[0]


