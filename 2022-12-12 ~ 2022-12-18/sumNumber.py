class Solution:
    def sumOfAlpha(self, s: str, k: int) -> int:
        digits = ''.join([str(ord(c) - ord('a') + 1) for c in s])

        for i in range(k):
            if len(digits) == 1:
                break
            total = sum(int(ch) for ch in digits)
            digits = str(total)
        return int(digits)
