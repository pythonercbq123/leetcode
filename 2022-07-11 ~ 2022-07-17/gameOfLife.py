from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]):
        # neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),  (1, 1)]
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        copy = [[board[row][col] for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                live_num = 0
                self_lived = copy[row][col]
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if 0 <= r < rows and 0 <= c < cols and copy[r][c] == 1:
                        live_num += 1
                if self_lived == 1 and (live_num < 2 or live_num > 3):
                    board[row][col] = 0

                if self_lived == 0 and live_num == 3:
                    board[row][col] = 1
        return board


if __name__ == '__main__':
    s = Solution()
    r = s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
    print(r)
