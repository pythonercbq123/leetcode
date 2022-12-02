class Solution:
    def nthMagic(self, n: int, a: int, b: int) -> int:
        if a == b:
            return (n - 1) * a
        if a > b:
            a, b = b, a
        ptr_a = 0
        ptr_b = 0
        dp = [0 for _ in range(n)]
        for i in range(0, n):
            ptr_a = ptr_a + a
            ptr_b = ptr_b + b
            if ptr_a < ptr_b:
                dp[i] = ptr_a
                ptr_b -= b
            elif ptr_a > ptr_b:
                dp[i] = ptr_b
                ptr_a -= a
            else:
                dp[i] = ptr_a
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    ret = s.nthMagic(1, 2, 3)
    print(ret)