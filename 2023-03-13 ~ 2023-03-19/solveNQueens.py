from typing import List


class Solution:
    def solveNQueen(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        result = []

        def is_valid(row, col, board):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def dfs(board, row, n):
            if row == n:
                temp_list = []
                for row_content in board:
                    temp_str = ''.join(row_content)
                    temp_list.append(temp_str)
                result.append(temp_list)
            for col in range(n):
                if is_valid(row, col, board):
                    board[row][col] = 'Q'
                    dfs(board, row + 1, n)
                    board[row][col] = '.'

        dfs(board, 0, n)

        return result


if __name__ == '__main__':
    s = Solution()
    ret = s.solveNQueen(4)
    print(ret)
    ret = s.solveNQueen(1)
    print(ret)