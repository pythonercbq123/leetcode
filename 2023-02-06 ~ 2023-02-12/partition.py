from typing import List


class Solution:
    def partition(self, s: str):
        result = []
        self.helper(s, 0, [], result)
        return result

    def helper(self, s: str, index: int, substrings: List[str], result: List):
        if index == len(s):
            result.append(list(substrings))
        else:
            for i in range(index, len(s)):
                add_str = s[index:i + 1]
                if self.ispalindrome(add_str):
                    substrings.append(add_str)
                    # 注意这里下一个开始的index为i+1
                    self.helper(s, i + 1, substrings, result)
                    substrings.pop()

    def ispalindrome(self, substrings: str):
        left, right = 0, len(substrings) - 1
        while left < right:
            if substrings[left] != substrings[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    ret = s.partition('google')
    print(ret)