from typing import List


# 后缀表达式是一种算术表达式，它的操作符在操作数的后面。
# 输入一个用字符串数组表示的后缀表达式，请输出该后缀表达式的计算结果。
# 假设输入的一定是有效的后缀表达式。例如，后缀表达式["2"，"1"，"3"，"*"，"+"]对应的算术表达式是“2+1*3”，因此输出它的计算结果5。
class Solution:
    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     for i in tokens:
    #         if i not in "+-*/":
    #             stack.append(int(i))
    #         else:
    #             a = stack.pop()
    #             b = stack.pop()
    #             stack.append(self.helper(b, a, i))
    #     return stack.pop()

    # def helper(self, a, b, op):
    #     if op == "+":
    #         return a + b
    #     elif op == "-":
    #         return a - b
    #     elif op == "*":
    #         return a * b
    #     elif op == "/":
    #         return int(a / b)
    #     else:
    #         return 0
    def evalRpn(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                # 注意顺序
                stack.append(self.helper(token, num2, num1))
        return stack[0]

    def helper(self, opr, num1, num2):
        if opr == '+':
            return num1 + num2
        elif opr == '-':
            return num1 - num2
        elif opr == '*':
            return num1 * num2
        elif opr == '/':
            return int(num1 // num2)
        else:
            return 0

