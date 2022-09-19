from functools import lru_cache


class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        mod_num = 10 ** 9 + 7
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.fib(n - 1) + self.fib(n - 2)) % mod_num

    def fib2(self, n: int) -> int:
        # 防止递归引起的栈溢出问题
        mod_num = 10 ** 9 + 7
        if n <= 1:
            return n
        p, q, r = 0, 0, 1
        for i in range(2, n+1):
            p = q
            q = r
            r = (p + q) % mod_num
        return r


