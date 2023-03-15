from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connect = [[0] * n for _ in range(n)]
        for road in roads:
            connect[road[0]][road[1]] = 1
            connect[road[1]][road[0]] = 1
            degree[road[0]] += 1
            degree[road[1]] += 1
        max_res = 0
        for i in range(n):
            # 从i + 1开始
            for j in range(i + 1, n):
                max_res = max(max_res, degree[i] + degree[j] - connect[i][j])
        return max_res


if __name__ == '__main__':
    s = Solution()
    ret = s.maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]])
    print(ret)

    ret = s.maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]])
    print(ret)
