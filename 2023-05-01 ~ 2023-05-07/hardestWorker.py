from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans, max_cost = logs[0]
        for i in range(1, len(logs)):
            idi, cost = logs[i][0], logs[i][1] - logs[i - 1][1]
            if cost > max_cost or (cost == max_cost and idi < ans):
                ans, max_cost = idi, cost
        return ans


if __name__ == '__main__':
    # test for hardestWorker
    n = 5
    logs = [[1, 3], [2, 5], [3, 7]]
    s = Solution()
    ret = s.hardestWorker(n, logs)
    print(ret)
