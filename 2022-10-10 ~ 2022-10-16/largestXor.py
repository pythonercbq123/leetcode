class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class LargestXor:

    @staticmethod
    def build_trie(nums):
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        return root

    def find_largest_xor(self, nums):

        max_rs = 0
        root = self.build_trie(nums)
        for num in nums:
            node = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if 1 - bit in node.children:
                    xor = (xor << 1) + 1
                    node = node.children[1 - bit]
                else:
                    xor <<= 1
                    node = node.children[bit]
            max_rs = max(max_rs, xor)
        return max_rs


if __name__ == '__main__':
    s = LargestXor()
    r = s.find_largest_xor([1, 3, 8])
    print(r)
