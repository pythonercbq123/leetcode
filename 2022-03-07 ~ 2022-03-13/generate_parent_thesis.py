# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#  
#
# 提示：
#
# 1 <= n <= 8
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def back_track(s, left, right):
            if len(s) == 2 * n:
                ret.append(''.join(s))
            else:
                if left < n:
                    s.append('(')
                    back_track(s, left + 1, right)
                    s.pop()
                if right < left:
                    s.append(')')
                    back_track(s, left, right + 1)
                    s.pop()

        back_track([], 0, 0)
        return ret


if __name__ == '__main__':
    s = Solution()
    ret = s.generateParenthesis(4)
    print(ret)