
class Trie:
    # 字典树

    def __init__(self):
        self.root = {}
        self.is_end = False

    def search_prefix(self, prefix: str) -> "Trie":
        node = self
        for c in prefix:
            if c not in node.root:
                return None
            else:
                node = node.root[c]
        return node

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.root:
                node.root[c] = Trie()
            node = node.root[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None


if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    t.search('apple')
    t.search('app')
    t.startsWith('app')
    t.insert('app')
    t.search('app')
    t.insert('acc')
    t.search('app')
    r = t.startsWith('apee')
    print(r)
