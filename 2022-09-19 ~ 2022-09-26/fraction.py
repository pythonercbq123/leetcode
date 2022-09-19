import numpy as np
from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if len(cont) == 1:
            return [cont[0], 1]
        cont = cont[::-1]
        dividend, divisor = cont[0] * cont[1] + 1, cont[0]
        for i in cont[2:]:
            dividend, divisor = dividend * i + divisor, dividend
        g = int(np.gcd(dividend, divisor))
        return [dividend // g, divisor // g]


if __name__ == '__main__':
    s = Solution()
    ret = s.fraction([3, 2, 0, 2])
    print(ret)
