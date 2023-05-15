from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 关键是找到翻转后一样的行 这个理解是解题关键
        m, n = len(matrix), len(matrix[0])
        count = Counter()
        for i in range(m):
            value = 0
            for j in range(n):
                value += 10 * value + matrix[i][j] ^ matrix[i][0]
            count[value] += 1
        res = 0
        for k, v in count.items():
            res = max(res, v)
        return res