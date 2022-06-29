from typing import List


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator % denominator) == 0:
            return str(numerator // denominator)
        ans = []
        # get the symbol
        if (numerator < 0) != (denominator < 0):
            ans.append('-')
        # integer
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_part = str(numerator // denominator)
        ans.append(int_part)
        ans.append('.')

        # remainder  长除法 余数 * 10 再除
        index_map = {}
        mod = numerator % denominator
        while mod and mod not in index_map:
            index_map[mod] = len(ans)
            mod = mod * 10
            ans.append(str(mod // denominator))
            mod %= denominator
        if mod:
            index = index_map.get(mod)
            ans.insert(index, '(')
            ans.append(')')
        return ''.join(ans)



