from typing import List


class Solution:
    def generate_parenthesis(self, n: int):
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, left: int, right: int, parenthesis: str, result: List):
        if left == 0 and right == 0:
            result.append(parenthesis)
        if left > 0:
            self.helper(left - 1, right, parenthesis + '(', result)
        if left < right:
            self.helper(left, right - 1, parenthesis + ')', result)


if __name__ == '__main__':
    s = Solution()
    ret = s.generate_parenthesis(2)
    print(ret)
