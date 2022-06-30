from operator import add, sub, mul
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        opr_map = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda x, y: int(x / y)
        }
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                opr = opr_map.get(token)
                num2 = stack.pop()
                num1 = stack.pop()
                num = opr(num1, num2)
            finally:
                stack.append(num)
        return stack[0]
