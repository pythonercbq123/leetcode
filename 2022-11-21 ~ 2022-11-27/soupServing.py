from collections import defaultdict
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        val = defaultdict(int)
        for i, x in enumerate(order):
            val[x] += 1
        return ''.join(sorted(s, key=lambda c: val[c]))

    # 计数排序
    def customSortString2(self, order: str, s: str) -> str:
        freq = Counter(s)
        ret = []
        for c in order:
            if c in freq:
                ret.append(c * freq[c])
                freq[c] = 0
        for c, v in freq.items():
            if v != 0:
                ret.append(c * v)
        return ''.join(ret)


if __name__ == '__main__':
    s = Solution()
    ret = s.customSortString2(order="cba", s="abcd")
    print(ret)
