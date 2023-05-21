from typing import List


class Solution:
    def splitPalindrome(self, s: str) -> List:

        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(s, index, subset, res):
            if index == len(s):
                res.append(list(subset))

            for i in range(index, len(s)):
                if is_palindrome(s[index: i + 1]):
                    subset.append(s[index: i + 1])
                    dfs(s, i + 1, subset, res)
                    subset.pop()
        res = []
        subset = []
        dfs(s, 0, subset, res)
        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.splitPalindrome('google')
    print(ret)