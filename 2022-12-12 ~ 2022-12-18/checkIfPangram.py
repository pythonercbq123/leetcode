class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        state = 0
        for c in sentence:
            state |= 1 << (ord(c) - ord('a'))
        return state == (1 << 26) - 1


if __name__ == '__main__':
    s = Solution()
    ret = s.checkIfPangram('abcdefghijklmnopqrstuvwxyz')
    print(ret)