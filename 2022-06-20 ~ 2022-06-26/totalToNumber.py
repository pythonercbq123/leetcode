class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        multiply = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            k = ord(columnTitle[i]) - ord('A') + 1
            num += k * multiply
            multiply *= 26
        return num