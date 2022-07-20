from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        # 因为矩阵是对称的 随意行列一致 无需另外求解
        cols = len(matrix[0])
        # 上下对换
        for row in range(rows//2):
            for col in range(cols):
                # 两个行的和为row - 1而不是 row
                matrix[row][col], matrix[rows - row - 1][col] = matrix[rows - row - 1][col],  matrix[row][col]
        # 对角对换
        for row in range(rows):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
