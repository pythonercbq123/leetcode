# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = self.r_serialize(root, "")
        return s

    def r_serialize(self, root, p: str):
        if root is None:
            p += 'null,'
        else:
            p += str(root.val) + ','
            p = self.r_serialize(root.left, p)
            p = self.r_serialize(root.right, p)
        return p

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        tree = self.r_deserialize(data_list)
        return tree

    def r_deserialize(self, data_list):
        if data_list:
            val = data_list.pop(0)
            if val == 'null':
                return None
            root = TreeNode(val)
            root.left = self.r_deserialize(data_list)
            root.right = self.r_deserialize(data_list)
            return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
if __name__ == '__main__':
    s = Codec()
    from collections import deque

    r = s.r_deserialize([1, 2, 3, 'null', 'null', 4, 5])
    print(r)
    d = s.serialize(r)
    print(d)
