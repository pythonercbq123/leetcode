from typing import List


# 第一个要素是访问相邻结点。二叉树的相邻结点非常简单，只有左子结点和右子结点两个。二叉树本身就是一个递归定义的结构
# ：一棵二叉树，它的左子树和右子树也是一棵二叉树。那么我们的 DFS 遍历只需要递归调用左子树和右子树即可。
#
# 第二个要素是 判断 base case。一般来说，二叉树遍历的 base case 是 root == null。这样一个条件判断其实有两个含义：
# 一方面，这表示 root 指向的子树为空，不需要再往下遍历了。另一方面，在 root == null 的时候及时返回，可以让后面的 root.left
# 和 root.right 操作不会出现空指针异常。
#
# 对于网格上的 DFS，我们完全可以参考二叉树的 DFS，写出网格 DFS 的两个要素：
#
# 首先，网格结构中的格子有多少相邻结点？答案是上下左右四个。对于格子 (r, c) 来说（r 和 c 分别代表行坐标和列坐标），
# 四个相邻的格子分别是 (r-1, c)、(r+1, c)、(r, c-1)、(r, c+1)。换句话说，网格结构是「四叉」的。

# 避免重复遍历
# 网格结构的 DFS 与二叉树的 DFS 最大的不同之处在于，遍历中可能遇到遍历过的结点。这是因为，
# 网格结构本质上是一个「图」，我们可以把每个格子看成图中的结点，每个结点有向上下左右的四条边。
# 在图中遍历时，自然可能遇到重复遍历结点。
#
# 这时候，DFS 可能会不停地「兜圈子」，永远停不下来，如下图所示：


# 如何避免这样的重复遍历呢？答案是标记已经遍历过的格子。
# 以岛屿问题为例，我们需要在所有值为 1 的陆地格子上做 DFS 遍历。每走过一个陆地格子，就把格子的值改为 2，
# 这样当我们遇到 2 的时候，就知道这是遍历过的格子了。也就是说，每个格子可能取三个值：

# 0 —— 海洋格子
# 1 —— 陆地格子（未遍历过）
# 2 —— 陆地格子（已遍历过）


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        count = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(grid, r, c)
        return count

    def dfs(self, grid, r, c):
        # for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        #     if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
        #         self.dfs(grid, x, y)
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '2'
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)


if __name__ == '__main__':
    s = Solution()
    ret = s.numIslands(grid=[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                             ["0", "0", "0", "0", "0"]])
    print(ret)
