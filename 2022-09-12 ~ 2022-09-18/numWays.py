class Solution:
    def numWays(self, n: int) -> int:
        mod_num = 10 ** 9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        p, q, r = 0, 1, 1
        for i in range(2, n + 1):
            p = q
            q = r
            r = (p + q)
        return r % mod_num


if __name__ == '__main__':
    s = Solution()
    ret = s.numWays(11)
    print(ret)
