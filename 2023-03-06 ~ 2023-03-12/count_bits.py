class Solution:
    def count_bits(self, num: int):
        """
        求一个数二进制中1的个数
        count[num] = count[num & num -1] + 1
        :param num:
        :return:
        """
        counts = [0] * (num + 1)
        for i in range(1, num+1):
            counts[i] = counts[i & (i - 1)] + 1
        return counts[num]


if __name__ == '__main__':
    s = Solution()
    ret = s.count_bits(8)
    print(ret)
    ret = s.count_bits(7)
    print(ret)
