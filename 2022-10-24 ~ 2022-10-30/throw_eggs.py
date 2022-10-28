def throw_eggs(K: int, N: int):
    memo = {}

    def dp(k: int, n: int):
        """
        :param k:k个鸡蛋
        :param n:n层楼
        :return:
        """
        if (k, n) in memo:
            return memo[(k, n)]
        if k == 1:
            return n
        if k == 0:
            return 0
        res = n
        for i in range(1, n + 1):
            res = min(res,
                      max(dp(k, n - i), dp(k - 1, i - 1)) + 1)
        memo[(k, n)] = res
        return res

    return dp(K, N)


if __name__ == '__main__':
    c = throw_eggs(2, 100)
    print(c)
