from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0] * n for _ in range(m)]
        i, j = 0, 0
        while i < m and j < n:
            v = min(rowSum[i], colSum[j])
            matrix[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:  # 第i行其他都是0，直接跳转到i+1
                i += 1
            if colSum[j] == 0:
                j += 1
        return matrix
