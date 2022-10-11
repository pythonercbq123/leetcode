from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False


class Magic:
    root = TrieNode()
    def build_dict(self, words):

        for word in words:
            node = self.root
            for c in word:
                if c not in node.child:
                    node.child[c] = TrieNode()
                node = node.child[c]
            node.is_word = True

    def search(self, word):
        return self.dfs(self.root, word, 0, 0)

    def dfs(self, root, word, index, edit):
        if root is None:
            return False
        if root.is_word and index == len(word) and edit == 1:
            return True
        if index < len(word) and edit <= 1:
            found = False
            for i in range(ord('a'), ord('a') + 26):
                if found:
                    break

                c = chr(i)
                if c != word[index]:
                    _next = edit + 1
                else:
                    _next = edit
                found = self.dfs(root.child.get(c), word, index + 1, _next)

            return found
        return False


if __name__ == '__main__':
    s = Magic()
    s.build_dict(['happy', 'new', 'year'])
    r = s.search('now')
    print(r)