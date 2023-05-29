from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # write code here
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if is_valid(board, i, j, str(num)):
                                board[i][j] = str(num)
                                if dfs(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
                if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num:
                    return False
            return True

        dfs(board)