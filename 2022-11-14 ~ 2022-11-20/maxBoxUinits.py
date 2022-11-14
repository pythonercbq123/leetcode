from typing import List


class Solution:

    def max_box_units(self, box_types: List, trunk_size: int) -> int:

        ordered_box_types = sorted(box_types, key=lambda x: x[1], reverse=True)
        count = 0
        total = 0
        for i in ordered_box_types:
            if count + i[0] <= trunk_size:
                delta = i[0]
            else:
                delta = trunk_size - count
            count += delta
            total += delta * i[1]
        return total

    def new_max_box_units(self, box_types, trunk_size):
        #  通过trunk_size递减可以省去count变量
        #  通过sort而非sorted避免重新创建O(n)的空间
        box_types.sort(key=lambda x: x[1], reverse=True)
        res = 0
        for num, weight in box_types:

            if num <= trunk_size:
                res += num * weight
                trunk_size -= num
            else:
                res += trunk_size * weight
                break
        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.new_max_box_units(box_types=[[1, 3], [2, 2], [3, 1]], trunk_size=4)
    print(ret)
