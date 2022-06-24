
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        m = n
        while m:
            if m % 2 == 1:
                res *= x
            x *= x
            m //= 2
        return res if n > 0 else 1 / res


if __name__ == '__main__':
    s = Solution()
    r = s.myPow(2, 10)
    print(r)