class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre_sign = '+'
        for i in range(len(s)):
            c = s[i]
            if c != ' ' and  c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            if i == len(s) - 1 or c in '+-*/':
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                pre_sign = s[i]
                num = 0
        return sum(stack)


if __name__ == '__main__':
    s = Solution()
    r = s.calculate(' 3/2 ')
    print(r)