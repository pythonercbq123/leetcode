from collections import defaultdict
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        res = 0
        s_values = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)
        count = defaultdict(int)
        for i in s_values:
            count[i[1]] += 1
            if count[i[1]] <= useLimit:
                res += i[0]
                numWanted -= 1
                if numWanted == 0:
                    break

        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.largestValsFromLabels([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1)
    print(ret)
