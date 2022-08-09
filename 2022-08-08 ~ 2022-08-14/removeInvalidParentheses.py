from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l_remove = 0
        r_remove = 0
        ret = []
        for c in s:
            if c == '(':
                l_remove += 1
            elif c == ')':
                if l_remove == 0:
                    r_remove += 1
                else:
                    l_remove -= 1

        def is_valid(s: str):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, l_remove, r_remove):
            if l_remove == 0 and r_remove == 0:
                if is_valid(s):
                    ret.append(s)
            for i in range(start, len(s)):
                if i > 0 and s[i] == s[i-1]:
                    # 剪枝处理
                    continue
                if l_remove + r_remove > len(s) - i:
                    break
                if l_remove > 0 and s[i] == '(':
                    # 尝试删除左边括号
                    helper(s[:i]+s[i+1:], i, l_remove - 1, r_remove)
                if r_remove > 0 and s[i] == ')':
                    # 尝试删除右边括号
                    helper(s[:i]+s[i+1:], i, l_remove, r_remove -1)
        helper(s, 0, l_remove, r_remove)
        return ret

