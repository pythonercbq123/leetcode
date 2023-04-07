
class Solution:
    def common_factors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans

    def common_factors2(self, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        c = gcd(a, b)
        ans = 0
        i = 1
        while i * i <= c:
            if c % i == 0:
                ans += 1
                if i * i != c:
                    ans += 1
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.common_factors(8, 5)
    print(ret)
    ret = s.common_factors2(8, 5)
    print(ret)


