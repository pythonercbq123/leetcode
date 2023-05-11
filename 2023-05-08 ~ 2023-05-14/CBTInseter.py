class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = [root]
        while self.queue:
            node = self.queue[0]
            if node.left and node.right:
                self.queue.append(node.left)
                self.queue.append(node.right)
                self.queue.pop(0)
            else:
                break

    def insert(self, v):
        node = TreeNode(v)
        parent = self.queue[0]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.queue.pop(0)
            self.queue.append(parent.left)
            self.queue.append(parent.right)
        return parent.val

    def get_root(self):
        return self.root
